# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository overview

This is a personal learning/portfolio workspace, not a single deployable product. It contains several unrelated areas at the top level:

- `ai/certifications/cca_f/uigen/` — a full Next.js/TypeScript application (AI-powered React component generator). This is the only substantial codebase here; see the dedicated section below.
- `practise/` — Python practice code: `leetcode/dsa/` (LeetCode solutions), `udemy/100_days_of_code/` (course exercises, mix of `.py` scripts and `.ipynb` notebooks), `deeplearning_ai/` (notebooks).
- `notes/` — markdown notes from courses (e.g. deeplearning.ai prompt engineering lessons). Reference material, not code to run.
- `common/` and `utils/` — small shared Python helpers (`common/utility.py` has `get_valid_input`; `utils/performance_analyzer.py` has a `PerformanceAnalyzer.measure` timing/memory decorator) used by the practice scripts.

Because these areas are independent, always check which subtree a task belongs to before assuming build/test commands — root-level Python conventions do not apply inside `uigen/`, and vice versa.

## Python practice code (`practise/`, `common/`, `utils/`)

- Uses a dedicated virtualenv/conda env named `mwspace` (interpreter pinned in `.vscode/settings.json` at `C:\PyEnvs\mwspace`). Activate it before running scripts if the venv isn't already active.
- `requirements.txt` at the repo root is currently empty — there's no formal dependency list to install from yet.
- No test runner or lint config is set up for the Python code; these are standalone learning scripts/notebooks, run directly (`python practise/leetcode/dsa/lc_0001_two_sum.py`) or via Jupyter.

## uigen app (`ai/certifications/cca_f/uigen/`)

All commands below must be run from inside this directory, not the repo root.

### Commands

```bash
npm run setup       # install deps + prisma generate + prisma migrate dev (first-time setup)
npm run dev         # start dev server (Next.js + Turbopack) on localhost:3000
npm run build       # production build
npm run start       # run production build
npm run lint        # next lint
npm test            # run vitest test suite
npx vitest run path/to/file.test.ts        # run a single test file
npx vitest run -t "test name substring"    # run tests matching a name
npm run db:reset    # prisma migrate reset --force (drops and recreates the SQLite db)
```

- **Do not run `npm audit fix`.** Dependency versions are pinned deliberately for compatibility; `audit fix` can bump packages past compatible versions and break the app. Security fixes are applied by updating specific pinned versions directly. If a scanner flags something, raise it rather than auto-fixing.
- `ANTHROPIC_API_KEY` must live in a `.env` file inside `uigen/` itself (Next.js only loads `.env` from the directory the dev server runs in, not from parent directories). Without a real key (or with the placeholder value), the app transparently falls back to a mock language model that returns canned components — see `src/lib/provider.ts`.

### Architecture

This is an AI chat app that generates React components into a **virtual, in-memory file system** — nothing is written to disk, and there's no bundler/dev-server round trip for the generated code. The pieces:

1. **Chat endpoint** (`src/app/api/chat/route.ts`): receives `{ messages, files, projectId }`, prepends a system prompt (`src/lib/prompts/generation.tsx`), rehydrates a `VirtualFileSystem` from the serialized `files`, and calls `streamText` (Vercel AI SDK) with two tools exposed to the model:
   - `str_replace_editor` (`src/lib/tools/str-replace.ts`) — edit file contents by string replacement.
   - `file_manager` (`src/lib/tools/file-manager.ts`) — create/rename/delete files and directories.
   Both tools operate directly on the shared `VirtualFileSystem` instance for that request. On finish, if a `projectId` and authenticated session exist, the conversation and serialized file system are persisted to the `Project` row (Prisma).

2. **Model selection** (`src/lib/provider.ts`): `getLanguageModel()` returns the real Anthropic model, or a hand-rolled `MockLanguageModel` (implements the AI SDK's `LanguageModelV1` interface) that plays back a scripted multi-step tool-call sequence when no API key is configured — this keeps the app fully usable for local development/demoing without a key. The mock path also uses fewer `maxSteps` (4 vs 40) to avoid repetition since it can't reason about when to stop.

3. **Virtual file system** (`src/lib/file-system.ts`): an in-memory tree (`Map<path, FileNode>`) with create/read/update/delete/rename operations and path normalization; supports serialize/deserialize so it can round-trip through the chat API request/response and Prisma storage. Exposed to the frontend via `src/lib/contexts/file-system-context.tsx`.

4. **In-browser JSX transform + preview** (`src/lib/transform/jsx-transformer.ts`, `src/components/preview/PreviewFrame.tsx`): generated files never touch a real bundler. Instead, Babel standalone transpiles JSX/TSX on the fly, an import map is constructed from the virtual files, and the result is rendered inside a sandboxed `iframe` for live preview. The transformer auto-detects an entry point (`App.jsx`/`App.tsx`/`index.jsx`/etc.) and generates placeholder modules for missing imports so partial/in-progress generations don't hard-crash the preview.

5. **Auth** (`src/lib/auth.ts`, `src/middleware.ts`): session-based auth (bcrypt + jose for JWT-like sessions). Middleware protects `/api/projects` and `/api/filesystem`; anonymous usage is otherwise allowed (see `src/lib/anon-work-tracker.ts` for tracking anonymous sessions before sign-up, and `create-project.ts`/`get-project(s).ts` server actions for persistence).

6. **Persistence** (`prisma/schema.prisma`): SQLite via Prisma. Two models: `User` (email/password) and `Project` (`messages` and `data` stored as JSON strings — the chat history and serialized virtual file system respectively). Prisma client is generated into `src/generated/prisma` (a checked-in generated directory, not `node_modules`) — re-run `npx prisma generate` after schema changes.

Tests (Vitest + jsdom + Testing Library, config in `vitest.config.mts`) live alongside source in `__tests__/` directories and cover the file system, JSX transformer, tool-using chat contexts, and key components.
