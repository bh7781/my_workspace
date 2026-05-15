# LLMs as a Developer Tool

A large amount of prompting content available online focuses mainly on:
- Chat interfaces
- One-off prompts
- Individual productivity tasks

However, the real power of Large Language Models (LLMs) comes from using them programmatically through APIs to build software applications quickly.

Key idea:
> LLMs are not just chat tools. They are development platforms.

Examples of applications developers can build using LLM APIs:
- Summarization systems
- Information extraction tools
- Chatbots
- AI assistants
- Transformation pipelines
- Automated workflows

The discussion emphasizes that this developer-oriented usage of LLMs is still significantly underappreciated.

---

# Why LLM APIs Matter for Developers

The ability to call LLMs through APIs enables developers to rapidly prototype and build applications that previously required substantial engineering effort.

A major observation:
> Developers can now build useful AI-powered applications extremely quickly.

The focus is not just on interacting with a chatbot manually, but on integrating LLMs directly into software systems and workflows.

---

# Course Direction and Main Use Cases

The discussion outlines several practical categories of LLM applications that will be explored:

- Summarization
- Inferring information
- Transforming text
- Expanding content
- Building chatbots

The overall goal is to spark ideas for new AI-powered applications.

---

# Two Broad Types of LLMs

The discussion separates LLMs into two major categories:

1. Base LLMs
2. Instruction-Tuned LLMs

---

# Base LLMs

A base LLM is trained primarily to:
> Predict the next word in a sequence.

Training data usually comes from:
- Internet text
- Articles
- Large-scale text corpora

The model learns statistical patterns about what words are likely to come next.

---

## Example: Story Completion

Prompt:

    Once upon a time there was a unicorn

Possible continuation:

    that lived in a magical forest with all unicorn friends

The model is simply continuing text based on learned patterns.

---

## Example: Why Base LLMs Can Behave Unexpectedly

Prompt:

    What is the capital of France?

A base LLM might continue with:

- What is France's largest city?
- What is France's population?
- Other quiz-style questions

Reason:
> The model is predicting likely text continuations, not necessarily answering the question directly.

Since internet text often contains lists of quiz questions, the model may continue the pattern rather than provide an answer.

This is a very important mental model:
> Base LLMs are text completion systems.

They are not inherently optimized for instruction-following.

---

# Instruction-Tuned LLMs

Instruction-tuned LLMs are trained specifically to:
> Follow instructions and produce useful responses.

For the same prompt:

    What is the capital of France?

An instruction-tuned model is much more likely to answer:

    The capital of France is Paris.

---

# How Instruction-Tuned LLMs Are Created

The process generally works like this:

1. Start with a base LLM trained on massive text data
2. Fine-tune it using:
   - Instructions
   - High-quality example responses
3. Further improve it using RLHF

---

# RLHF — Reinforcement Learning from Human Feedback

RLHF is used to improve:
- Helpfulness
- Instruction-following ability
- Alignment with human expectations

The goal is to make the system:
- Helpful
- Honest
- Harmless

---

# Why Instruction-Tuned Models Became Dominant

Instruction-tuned models are generally:
- Easier to use
- Better at following intent
- Safer for practical applications

Compared to base LLMs, they are less likely to generate:
- Toxic outputs
- Problematic text
- Unhelpful completions

Important practical takeaway:
> Most real-world applications today should focus on instruction-tuned LLMs rather than base LLMs.

---

# Prompting Mindset for Instruction-Tuned LLMs

A key analogy is introduced:

> Think of prompting an instruction-tuned LLM like giving instructions to a smart person who lacks context about your task.

This framing is extremely important.

When an LLM gives poor output, the issue is often:
> The instructions were not sufficiently clear.

---

# Example: Poorly Specified Prompt

Prompt:

    Please write me something about Alan Turing.

Problem:
- The request is too vague.

The model does not know whether to focus on:
- Scientific contributions
- Personal life
- Historical role
- Writing style
- Tone

---

# Better Prompting Through Specificity

Good prompting involves clarifying:
- Desired focus
- Tone
- Style
- Context
- Expected format

Examples of useful clarifications:
- Should the tone sound professional?
- Should it read like a journalist wrote it?
- Should it feel casual and conversational?
- Which aspects of Alan Turing should be emphasized?

---

# Important Prompting Philosophy

Another strong mental model from the discussion:

> Give the model the same context you would give a smart new graduate assigned to the task.

If a human would need:
- Background information
- Reference material
- Examples
- Constraints

then the LLM often benefits from the same guidance.

Example:
> Providing reference text snippets before asking for generated content can significantly improve results.

---

# Core Prompting Principles Introduced

Two major prompting principles are introduced:

1. Be clear and specific
2. Give the model time to think

The first principle is emphasized heavily in this section:
> Better instructions usually produce better outputs.

The second principle is introduced briefly and explored later:
> Prompting techniques can encourage more deliberate reasoning from the model.