# Building Custom Chatbots with LLMs

One of the most exciting capabilities of Large Language Models is:
> Building custom conversational agents with relatively little effort.

Examples:
- AI customer support agents
- Restaurant order bots
- Internal assistants
- Workflow copilots
- Conversational interfaces

The discussion emphasizes:
> ChatGPT itself is just one example of a conversational interface powered by an LLM.

Developers can build their own domain-specific chatbots using the same underlying concepts.

---

# Chat Models Work Using Messages

Chat models are designed around:
> A sequence of messages as input.

The model then generates:
> A message as output.

This message-based structure supports:
- Multi-turn conversations
- Context retention
- Persona control
- Stateful interactions

---

# Single-Turn vs Multi-Turn Usage

Although chat models are optimized for conversations:
> They also work well for single-turn tasks.

Previous examples in the course:
- Summarization
- Classification
- Transformation

were actually still using the chat format internally.

---

# Chat Message Structure

The message system uses different roles.

Core roles:
- system
- user
- assistant

---

# System Message

The system message:
> Defines high-level assistant behavior.

Examples:
- Personality
- Tone
- Rules
- Instructions
- Workflow constraints

Important analogy introduced:
> The system message is like whispering instructions into the assistant’s ear.

The user typically does not see:
- System instructions
- Hidden behavioral constraints

---

# Purpose of the System Message

The system message allows developers to:
- Shape assistant behavior
- Define conversation framing
- Control persona
- Add operational instructions

without making these instructions part of the visible conversation.

---

# User Message

The user message:
> Represents the human input.

This is equivalent to:
- Messages typed into ChatGPT

---

# Assistant Message

The assistant message:
> Represents the model-generated response.

This allows conversations to accumulate as:
- alternating user/assistant exchanges

---

# Example — Shakespearean Assistant

System message:

    You are an assistant that speaks like Shakespeare.

User messages:
- Tell me a joke
- Why did the chicken cross the road?
- I don't know

The assistant responds:
> In Shakespearean style.

This demonstrates:
> The system message strongly influences assistant personality and behavior.

---

# Understanding the Assistant Response Object

The assistant response contains:
- role
- content

Example:
- role = assistant
- content = generated text

This reflects the underlying message-based architecture of chat systems.

---

# Example — Friendly Chatbot

System message:

    You are a friendly chatbot.

User says:

    Hi, my name is Isa.

Assistant responds appropriately and conversationally.

---

# Important Concept — Context Is Not Persistent

A crucial limitation is introduced:

> Each API call is stateless unless prior messages are explicitly included.

Example:
If the user later asks:

    What is my name?

without providing earlier messages:
> The model does not know.

---

# Context Window

To make the model “remember”:
> Previous conversation messages must be included in the current request.

This accumulated message history is called:
> Context

---

# Context as Conversation Memory

Conversation memory is simulated by:
- Appending earlier user messages
- Appending earlier assistant responses
- Sending full conversation history repeatedly

Important understanding:
> The model itself does not maintain hidden long-term conversational memory between API calls.

---

# Example — Providing Prior Context

When earlier messages include:

    My name is Isa.

the assistant can correctly answer:

    Your name is Isa.

because the necessary context is present in the message list.

---

# Building a Real Chatbot — OrderBot

The main practical example:
> A pizza-ordering chatbot called OrderBot.

Goal:
- Automate restaurant ordering interactions

---

# Conversation State Management

A helper function is introduced to:
- Collect user messages
- Append messages to context
- Send updated context to model
- Append assistant responses back into context

This creates:
> A growing conversation history.

---

# Important Chatbot Architecture Pattern

Core loop:

1. User sends message
2. Add to context
3. Call model
4. Receive assistant response
5. Add response to context
6. Repeat

This is the foundational architecture of many chatbot systems.

---

# System Prompt for OrderBot

The system message defines detailed operational behavior.

Instructions include:

- Greet customer
- Collect order
- Ask pickup or delivery
- Clarify sizes/options
- Confirm order
- Collect payment
- Remain conversational and friendly

The system message also contains:
> Full menu information.

---

# Prompt Engineering as Workflow Programming

The system prompt effectively encodes:
- Business logic
- Operational flow
- Interaction rules

This demonstrates an important idea:
> Prompt engineering can function like lightweight conversational programming.

---

# Conversational Clarification Behavior

The assistant asks follow-up questions such as:
- Pizza size
- Toppings
- Side size

because the system prompt explicitly instructed it to:
> Clarify all options and extras.

---

# Important Chatbot Design Principle

Good conversational systems should:
- Reduce ambiguity
- Confirm details
- Gather structured information incrementally

The assistant demonstrates this naturally through prompting.

---

# Structured Output from Conversation

After the conversation:
> The chatbot generates a JSON summary of the order.

Requested fields:
- Pizza
- Toppings
- Drinks
- Sides
- Total price

---

# Conversation → Structured Data

A major architectural pattern appears here:

Natural language conversation →
Structured machine-readable output

This is extremely important for real applications because it enables:
- Backend integration
- Order processing
- Databases
- APIs
- Automation systems

---

# Using Additional Instructions Mid-Conversation

A new system message is appended later asking for:
> JSON order summarization.

Important insight:
> System instructions can be added dynamically during workflows.

---

# Temperature Usage in Chatbots

Temperature is discussed again in chatbot context.

Recommendation:
> Lower temperature is generally preferable for operational chatbots.

Reason:
- Predictability
- Reliability
- Consistency

Higher temperatures may be useful for:
- Creative agents
- Entertainment bots
- Brainstorming assistants

---

# Predictability vs Creativity Tradeoff

For production assistants like OrderBot:
> Predictable behavior is usually more important than creativity.

This is especially true for:
- Orders
- Customer support
- Transactional systems

---

# Major Architectural Concepts Demonstrated

The OrderBot example demonstrates several foundational chatbot concepts.

## Persona Control
- Via system prompts

## Stateful Conversations
- Via accumulated context

## Workflow Guidance
- Via explicit instructions

## Clarification Handling
- Via conversational follow-up questions

## Structured Output Generation
- JSON summaries from dialogue

## Backend Integration Readiness
- Machine-readable outputs

---

# Chatbots as Prompt-Orchestrated Systems

A major conceptual shift throughout the discussion:

> Chatbots are not magic conversational entities.

They are:
- Carefully structured message histories
- Prompt-driven workflows
- Context-managed systems

---

# Core Prompt Engineering Patterns Reinforced

Recurring patterns throughout the chatbot examples:

- System role instructions
- Structured conversational flow
- Context accumulation
- Explicit operational guidance
- Controlled output formatting
- Predictable low-temperature behavior

---

# Overall Philosophy of Custom Chatbots with LLMs

Strong recurring themes throughout the discussion:

- LLMs make custom chatbot development highly accessible
- System messages strongly shape assistant behavior
- Context management is essential for conversational continuity
- Conversations can be converted into structured operational data
- Prompt engineering can encode workflow logic
- Reliable production chatbots generally favor lower temperature settings
- Chatbots are fundamentally message-driven systems with accumulated conversational context