# Runnables in LangChain and the Evolution from Chains

Another important thing is to understand **why LangChain introduced Runnables and how they improve over traditional Chains** when building LLM-based applications.

Earlier versions of LangChain primarily relied on **Chains** to connect prompts, models, and output parsers. However, as applications became more complex, Chains started showing limitations. Runnables were introduced as a more flexible and composable abstraction for building AI pipelines.

---

# Why Runnables Exist

Traditional LangChain workflows were built using **chains**, where different components were connected sequentially.

A typical chain looked like this:

```
User Input
     ↓
Prompt Template
     ↓
Language Model
     ↓
Output Parser
     ↓
Final Output
```

While chains worked well for simple workflows, they had several limitations when building more advanced systems.

Some common issues included:

- difficulty composing multiple chains
- limited flexibility when building parallel or branching workflows
- inconsistent interfaces across different components
- complicated debugging and tracing
- harder integration with async execution

To solve these problems, LangChain introduced **Runnables**, which provide a unified way to represent executable steps in an AI pipeline.

---

# Chains vs Runnables

Understanding the difference between chains and runnables is important when working with modern LangChain versions.

### Chains

Chains represent **predefined workflows** where components are connected in a specific order.

Example:

```
Prompt → Model → Output Parser
```

Characteristics of chains:

- designed for simple sequential pipelines
- less flexible for complex workflows
- harder to compose dynamically
- limited support for parallel execution
- each chain type had its own interface

Chains were useful for simple applications but became restrictive for more advanced pipelines.

---

### Runnables

Runnables provide a **general abstraction for executable units in a pipeline**.

Every component in the workflow (prompts, models, retrievers, parsers) can be treated as a runnable.

Example pipeline:

```
Prompt | Model | Output Parser
```

Key advantages of runnables:

- unified interface for all components
- easy composition using operators
- support for sequential, parallel, and conditional workflows
- better debugging and tracing
- native async support
- more modular and reusable pipelines

Runnables make it easier to build **complex AI systems with minimal code complexity**.

---

# Simple LLM Application using Runnables

A basic LLM application can be expressed as a runnable pipeline.

Conceptual flow:

```
User Input
    ↓
Prompt Template
    ↓
Language Model
    ↓
Output Parser
```

Using runnables, these components can be combined into a single pipeline where each step automatically passes its output to the next.

This greatly simplifies the process of building LLM applications.

---

# Different Types of Chains

Before runnables were introduced, LangChain provided multiple chain types such as:

- LLMChain
- SequentialChain
- RouterChain
- SimpleSequentialChain

Each chain served a specific purpose, but this design created fragmentation.

Developers often had to learn **multiple chain classes**, which made the framework harder to use.

This was one of the reasons LangChain moved toward the **Runnable-based architecture**.

---

# Problems with the Old Chain Approach

Some limitations of traditional chains included:

- rigid workflow definitions
- difficulty composing multiple chains together
- limited support for parallel execution
- separate implementations for similar workflows
- reduced flexibility when designing complex pipelines

As applications evolved toward **RAG systems, agents, and multi-step reasoning pipelines**, these limitations became more apparent.

---

# What are Runnables?

A **Runnable** represents any component that can be executed within a LangChain pipeline.

Examples of runnables include:

- prompt templates
- language models
- retrievers
- output parsers
- custom functions

All runnables follow a consistent interface, which allows them to be composed easily.

Example concept:

```
Prompt | Model | Parser
```

Each step is treated as a runnable, and the output flows automatically to the next step.

---

# Runnable Categories

Runnables can be categorized based on how they process and route data through the pipeline.

The main runnable types include:

- RunnableSequence
- RunnableParallel
- RunnablePassthrough
- RunnableLambda
- RunnableBranch

Each type enables a different type of workflow behavior.

---

# RunnableSequence

RunnableSequence represents a **sequential pipeline** where operations occur one after another.

Example flow:

```
User Input
     ↓
Prompt Template
     ↓
Language Model
     ↓
Output Parser
```

Each component receives the output of the previous component.

This is the most common runnable pattern when building standard LLM pipelines.

---

# RunnableParallel

RunnableParallel executes multiple runnables **at the same time**.

Example structure:

```
User Input
   ↓
 ┌─────────────┬─────────────┐
 ↓             ↓             ↓
Task A        Task B        Task C
 ↓             ↓             ↓
        Combined Output
```

This approach is useful when:

- multiple independent tasks must be executed
- information must be gathered from several sources
- faster response times are required

Parallel execution improves efficiency in many AI pipelines.

---

# RunnablePassthrough

RunnablePassthrough allows the input to pass through the pipeline **without modification** while still enabling other operations to run.

This is useful when:

- the original input must be preserved
- additional transformations are applied in parallel
- context needs to be forwarded unchanged

It helps maintain data flow across different pipeline branches.

---

# RunnableLambda

RunnableLambda allows custom Python functions to be inserted into a runnable pipeline.

Example use cases include:

- preprocessing input data
- formatting prompts
- transforming model outputs
- filtering retrieved documents

This makes the pipeline highly customizable.

---

# RunnableBranch

RunnableBranch enables **conditional execution**.

Instead of a fixed pipeline, the system decides which runnable to execute based on certain conditions.

Example concept:

```
User Query
     ↓
Condition Check
     ↓
 ┌─────────────┬─────────────┐
 ↓             ↓             ↓
Task A       Task B        Task C
```

For example:

- math questions → calculator tool
- knowledge queries → retrieval system
- general questions → language model

This allows AI systems to become more adaptive.

---

# LCEL (LangChain Expression Language)

LCEL is a concise syntax used to compose runnable pipelines.

It allows components to be connected using simple operators.

Example idea:

```
prompt | model | parser
```

This syntax makes it easy to define complex workflows in a clear and readable way.

LCEL significantly reduces the amount of code required to build LLM pipelines.

---

# Key Takeaways

- Chains were the original mechanism for building LLM workflows in LangChain.
- Chains were limited when building complex pipelines.
- Runnables were introduced to provide a unified and flexible execution model.
- Runnables support sequential, parallel, and conditional workflows.
- Different runnable types allow developers to design modular AI pipelines.
- LCEL simplifies runnable composition using a clean syntax.

Understanding runnables is essential for building modern LangChain applications such as:

- Retrieval-Augmented Generation systems
- AI assistants
- multi-step reasoning pipelines
- agent-based AI systems
