# Iterative Prompt Development

## Why This Matters

Good prompts are rarely written perfectly on the first attempt.

Prompt engineering is closer to software debugging than memorizing “perfect prompts.” You start with an intent, write a prompt, inspect the output, identify what failed, and refine the prompt.

The core lesson:

```text
Prompt quality improves through iteration, not guessing.
````

For real applications, this matters because the first prompt usually reveals hidden requirements:

* the output is too long,
* the tone is wrong,
* the model focuses on the wrong details,
* the format is hard to parse,
* key fields are missing,
* the result works for one example but fails on others.

The skill is not knowing a universal prompt. The skill is having a repeatable process for improving prompts for a specific task.

---

## Core Idea

Iterative prompt development follows a loop:

```text
Idea → Prompt → Output → Error Analysis → Refined Prompt → Better Output
```

This mirrors traditional machine learning development:

```text
Idea → Implementation → Experiment → Error Analysis → Iteration
```

The important shift is that the “implementation” is often the prompt itself.

---

## Mental Model

Treat a prompt like a small program.

A prompt has:

* inputs,
* instructions,
* constraints,
* expected outputs,
* failure modes.

When the output is wrong, do not simply blame the model. Ask:

```text
What did I fail to specify?
What ambiguity did I leave open?
What constraint did the model not know?
What output contract did I forget to define?
```

Prompt refinement is specification refinement.

---

## Running Example: Product Fact Sheet to Marketing Copy

The notebook uses a technical fact sheet for a chair and asks the model to generate a retail product description.

The fact sheet includes:

* overview,
* construction details,
* dimensions,
* options,
* materials,
* country of origin,
* product IDs.

The task seems simple:

```text
Turn technical specifications into marketing copy.
```

But the iterations reveal that this task contains several hidden requirements.

---

## First Prompt: Basic Task Description

A first attempt looks like this:

````python
prompt = f"""
Your task is to help a marketing team create a
description for a retail website of a product based
on a technical fact sheet.

Write a product description based on the information
provided in the technical specifications delimited by
triple backticks.

Technical specifications: ```{fact_sheet_chair}```
"""
````

This prompt is clear enough to produce a reasonable product description.

But it is incomplete.

The model does not know:

* desired length,
* intended audience,
* important details,
* output format,
* whether product IDs matter,
* whether dimensions should be extracted.

The result may be fluent but not yet useful.

---

## Iteration 1: The Output Is Too Long

The first issue is length.

The model writes a good description, but it is too verbose for a retail website.

Refinement:

````python
prompt = f"""
Your task is to help a marketing team create a
description for a retail website of a product based
on a technical fact sheet.

Write a product description based on the information
provided in the technical specifications delimited by
triple backticks.

Use at most 50 words.

Technical specifications: ```{fact_sheet_chair}```
"""
````

This shows a key prompting pattern:

```text
When the output violates an unstated expectation, make the expectation explicit.
```

---

## Length Constraints Are Approximate

Models are not perfect counters.

A prompt like:

```text
Use at most 50 words.
```

may produce 52, 58, or 63 words.

This happens because models generate text token by token. They do not naturally “count words” with perfect reliability while generating.

Better alternatives:

```text
Use at most 3 sentences.
```

or:

```text
Write a concise paragraph suitable for a product listing.
```

For strict limits, enforce them in code after generation.

```python
words = response.split()
shortened = " ".join(words[:50])
```

For production systems, prompt constraints should be combined with validation.

---

## Iteration 2: The Output Focuses on the Wrong Details

The next issue is audience mismatch.

A consumer-facing product description may emphasize style and comfort.

A retailer-facing description may need materials, construction, product variants, and commercial suitability.

Refinement:

````python
prompt = f"""
Your task is to help a marketing team create a
description for a retail website of a product based
on a technical fact sheet.

Write a product description based on the information
provided in the technical specifications delimited by
triple backticks.

The description is intended for furniture retailers,
so should be technical in nature and focus on the
materials the product is constructed from.

Use at most 50 words.

Technical specifications: ```{fact_sheet_chair}```
"""
````

This illustrates an important rule:

```text
Audience determines relevance.
```

The same source material can produce very different outputs depending on who the output is for.

---

## Audience Is a Control Surface

Specifying the audience helps control:

* vocabulary,
* tone,
* detail level,
* what information is emphasized,
* what information is omitted.

Examples:

```text
For consumers:
Focus on comfort, style, and home office use.

For furniture retailers:
Focus on construction, materials, options, and contract suitability.

For procurement teams:
Focus on durability, dimensions, country of origin, and product IDs.
```

Prompt quality improves when the model understands the reader.

---

## Iteration 3: Missing Required Details

The next issue is that the description should include product IDs.

The fact sheet contains:

```text
SWC-100
SWC-110
```

Refinement:

````python
prompt = f"""
Your task is to help a marketing team create a
description for a retail website of a product based
on a technical fact sheet.

Write a product description based on the information
provided in the technical specifications delimited by
triple backticks.

The description is intended for furniture retailers,
so should be technical in nature and focus on the
materials the product is constructed from.

At the end of the description, include every 7-character
Product ID in the technical specification.

Use at most 50 words.

Technical specifications: ```{fact_sheet_chair}```
"""
````

This is a critical engineering pattern:

```text
If a field is mandatory, explicitly require it.
```

Do not assume the model will preserve every important detail from the source.

---

## Extraction vs Generation

This example mixes two tasks:

1. Generate marketing copy.
2. Extract product IDs.

These are different operations.

Generation is flexible.

Extraction should be precise.

For robust systems, separate them when correctness matters:

```text
Step 1: Extract product IDs.
Step 2: Generate description.
Step 3: Append extracted product IDs.
```

This reduces the risk that the model forgets, mutates, or invents identifiers.

---

## Iteration 4: Add Structured Output

The final notebook iteration asks for:

* a product description,
* a dimensions table,
* HTML formatting,
* inches-only measurements,
* a specific table title,
* the description inside a `<div>`.

Prompt:

````python
prompt = f"""
Your task is to help a marketing team create a
description for a retail website of a product based
on a technical fact sheet.

Write a product description based on the information
provided in the technical specifications delimited by
triple backticks.

The description is intended for furniture retailers,
so should be technical in nature and focus on the
materials the product is constructed from.

At the end of the description, include every 7-character
Product ID in the technical specification.

After the description, include a table that gives the
product's dimensions. The table should have two columns.
In the first column include the name of the dimension.
In the second column include the measurements in inches only.

Give the table the title 'Product Dimensions'.

Format everything as HTML that can be used in a website.
Place the description in a <div> element.

Technical specifications: ```{fact_sheet_chair}```
"""
````

This is no longer just “write copy.”

It is a mini content-transformation pipeline:

```text
Technical fact sheet
→ audience-specific summary
→ required ID extraction
→ dimension extraction
→ unit filtering
→ HTML formatting
```

A prompt can orchestrate this, but every added requirement increases the need for validation.

---

## Why the Final Prompt Works Better

The final prompt works better because it defines:

| Requirement          | Prompt Control               |
| -------------------- | ---------------------------- |
| Source boundary      | Triple backticks             |
| Task                 | Product description          |
| Audience             | Furniture retailers          |
| Focus                | Materials and construction   |
| Required identifiers | Every 7-character product ID |
| Additional structure | Dimensions table             |
| Unit constraint      | Inches only                  |
| Output medium        | HTML                         |
| HTML placement       | Description inside `<div>`   |

The model no longer has to guess the product manager’s intent.

---

## Prompt Development as Error Analysis

The lecture’s strongest engineering lesson is that prompt improvement should be driven by observed failures.

Example process:

```text
Output too long
→ add length constraint

Wrong emphasis
→ specify audience and focus

Missing product IDs
→ explicitly require product IDs

Need web-ready format
→ request HTML and table structure
```

Each refinement responds to a concrete defect.

This is much better than randomly adding prompt tricks.

---

## Practical Iteration Loop

Use this loop when developing prompts:

```text
1. Start with a simple, clear prompt.
2. Run it on a representative input.
3. Inspect the output.
4. Identify the biggest mismatch.
5. Modify the prompt to address that mismatch.
6. Repeat.
7. Test on more examples.
```

The goal is not to write the longest prompt.

The goal is to remove ambiguity that causes bad outputs.

---

## From One Example to Evaluation Sets

Early prompt development often starts with one example.

That is useful for fast exploration.

But mature applications need multiple test cases.

For example, if building a product-description generator, test against:

* short fact sheets,
* long fact sheets,
* missing dimensions,
* multiple product IDs,
* no product IDs,
* different product categories,
* conflicting units,
* unusual materials,
* multilingual inputs.

A prompt that works for one chair may fail for a sofa, lamp, or industrial part.

---

## Average Case vs Worst Case

When testing prompts, look at both:

```text
Average performance:
How good is the output across many examples?

Worst-case performance:
Where does the prompt fail badly?
```

Worst-case failures often matter more in production.

Examples:

* hallucinated product IDs,
* missing safety information,
* invalid HTML,
* wrong units,
* unsupported claims,
* malformed JSON.

A good prompt is not merely impressive on one demo. It is stable across realistic variation.

---

## Modern Context: Prompt Evaluation

The lecture focuses on manual iteration.

Modern LLM development often adds systematic evaluation:

* golden test sets,
* automated checks,
* schema validation,
* factual consistency checks,
* human review,
* regression tests,
* A/B comparisons,
* LLM-as-judge evaluation for subjective criteria.

Prompt changes should be treated like code changes.

When you update a prompt, ask:

```text
Did this improve the target case?
Did it break other cases?
Did it increase cost or latency?
Did it make the output harder to parse?
```

---

## Modern Context: API and Model Changes

The notebook uses the older `gpt-3.5-turbo` chat completions style.

The durable lesson is not the exact API call. It is the workflow:

```text
Define task → call model → inspect output → refine prompt → evaluate
```

Modern applications may use:

* newer model families,
* structured outputs,
* tool calling,
* function schemas,
* retrieval-augmented generation,
* multimodal inputs,
* eval frameworks.

But iterative development remains essential because model behavior is still shaped by instructions, context, examples, and constraints.

---

## Key Code Pattern: Deterministic Prompt Testing

The notebook uses `temperature=0`:

```python
def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]
```

The important idea:

```text
Lower temperature reduces randomness.
```

For prompt development, this is useful because it makes changes easier to compare.

If outputs vary too much, it becomes harder to know whether a prompt edit actually helped.

---

## Key Code Pattern: Measuring Output Length

The notebook checks word count:

```python
len(response.split())
```

This is simple but important.

It shows that prompt evaluation should not rely only on visual inspection.

Even lightweight checks help:

```python
assert len(response.split()) <= 60
assert "SWC-100" in response
assert "SWC-110" in response
```

These checks turn vague quality goals into testable requirements.

---

## Key Code Pattern: Rendering Generated HTML

The notebook displays the model-generated HTML:

```python
from IPython.display import display, HTML

display(HTML(response))
```

This reinforces another important principle:

```text
Evaluate outputs in the environment where they will be used.
```

If the model generates HTML, render it.

If it generates JSON, parse it.

If it generates SQL, inspect and sandbox it.

If it generates code, run tests.

---

## Practical Engineering Perspective

Iterative prompt development is not just “try prompts until one looks good.”

It is a disciplined process of converting product requirements into model instructions.

A production-ready prompt should answer:

* Who is the audience?
* What source content should be used?
* What should be ignored?
* What output format is required?
* What fields are mandatory?
* What constraints must be followed?
* What should happen when information is missing?
* How will correctness be checked?

The best prompts often look obvious after they are written because they encode requirements clearly.

---

## Common Failure Modes

### Output Too Long

Fix with:

```text
Use at most 3 sentences.
Use at most 50 words.
Write a concise product listing paragraph.
```

Then validate length in code.

---

### Wrong Focus

Fix by specifying:

```text
The audience is furniture retailers.
Focus on materials and construction.
Do not emphasize lifestyle or decorative language.
```

---

### Missing Required Fields

Fix by explicitly requiring them:

```text
Include every product ID found in the source.
If no product ID is present, write "No product ID provided."
```

---

### Unparseable Output

Fix by defining format:

```text
Return valid JSON with keys:
description, product_ids, dimensions
```

For modern systems, prefer schema-enforced structured outputs where available.

---

### Hallucinated Details

Fix by grounding:

```text
Use only information from the technical specifications.
Do not add claims not present in the source.
```

Then verify against source fields.

---

### Works on One Example, Fails on Others

Fix by creating a small evaluation set.

Do not overfit to a single example.

---

## Prompt Refinement Patterns

### Add Constraints

```text
Use at most 50 words.
Use inches only.
Do not mention country of origin.
```

### Add Audience

```text
Write for furniture retailers.
Write for procurement managers.
Write for consumers furnishing a home office.
```

### Add Required Fields

```text
Include all product IDs.
Include dimensions.
Include available finish options.
```

### Add Format

```text
Return HTML.
Return JSON.
Return a Markdown table.
```

### Add Fallbacks

```text
If dimensions are missing, write "Dimensions not provided."
```

### Add Grounding

```text
Use only the provided fact sheet.
Do not infer unsupported claims.
```

---

## Common Misunderstandings

### “The First Prompt Should Work”

It usually will not.

The first prompt is a probe. It reveals what the model inferred and what the developer forgot to specify.

---

### “Better Prompting Means More Complicated Prompting”

Not always.

Better prompting means clearer prompting.

Sometimes the best refinement is removing unnecessary instructions.

---

### “If the Output Looks Good, the Prompt Is Done”

A single good output is not enough.

You need to test across representative cases.

---

### “The Model Ignored Me”

Sometimes the model ignored the instruction.

Often the instruction was ambiguous, conflicting, buried, or difficult to verify.

---

### “Prompt Engineering Is Separate From Software Engineering”

In LLM applications, prompts are part of the software.

They should be versioned, tested, reviewed, and monitored.

---

## A Production-Oriented Prompt Template

For tasks like fact-sheet transformation, a stronger template is:

````text
You are generating product content from a technical fact sheet.

Audience:
Furniture retailers.

Task:
Write a concise product description using only the provided fact sheet.

Requirements:
- Focus on materials and construction.
- Include all product IDs exactly as written.
- Do not invent claims.
- If a required field is missing, say so explicitly.

Output:
Return valid JSON:
{
  "description": "...",
  "product_ids": ["..."],
  "dimensions": [
    {"name": "...", "inches": "..."}
  ]
}

Technical fact sheet:
```...```
````

This is more robust because it separates:

* role,
* audience,
* task,
* constraints,
* output schema,
* source data.

---

## Revision Summary

Iterative prompt development is the process of improving prompts through observed output failures.

The main loop:

```text
Write prompt
Run prompt
Inspect output
Identify mismatch
Refine prompt
Test again
```

The lecture demonstrates four increasingly specific versions:

| Iteration        | Problem Observed                       | Prompt Refinement                             |
| ---------------- | -------------------------------------- | --------------------------------------------- |
| Initial prompt   | Output generally works but is too long | Add length constraint                         |
| Shorter prompt   | Focus is too consumer-oriented         | Specify retailer audience and technical focus |
| Technical prompt | Product IDs missing                    | Require all 7-character product IDs           |
| Final prompt     | Need structured web output             | Add dimensions table and HTML formatting      |

The broader principle:

```text
Every prompt improvement should correspond to a real failure mode.
```

---

## Practical Takeaways

Do not search for a perfect prompt.

Build one.

Start simple, inspect carefully, and refine based on what the model actually does.

For serious applications:

* test prompts on realistic examples,
* define success criteria,
* add constraints only when needed,
* specify audience and format,
* validate outputs with code,
* evaluate across multiple cases,
* treat prompts as versioned software artifacts.

The best prompt engineers are not people who memorize prompt recipes.

They are people who can diagnose model behavior and turn vague requirements into precise, testable instructions.