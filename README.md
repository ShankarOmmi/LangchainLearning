# Generative AI & LangChain Learning Repository

This repository contains my structured learning notes and code implementations while exploring **Generative AI, LangChain, and Retrieval-Augmented Generation (RAG)**.

The goal of this repository is to document important concepts involved in building modern AI applications powered by **Large Language Models (LLMs)**. Each folder focuses on a specific concept and includes both conceptual notes and practical code examples.

The repository acts as both:

- a **personal knowledge base about GenAI, LangChain and RAG**
- a **collection of working code implementations for GenAI systems**

---

# Repository Overview

The repository is organized into multiple folders, where each folder focuses on a specific concept in the Generative AI ecosystem.

```
LangChainLearning
│
├── 01_Models
├── 02_Prompts
├── 03_Structured_Output
├── 04_OutputParsers
├── 05_Chains
├── 06_Runnables
├── 07_DocumentLoaders
├── 08_TextSplitters
├── 09_VectorStores
├── 10_Retrievers
│
├── requirements.txt
├── .gitignore
└── README.md
```

Each folder contains:

- a **README file explaining the concept**
- **code implementations demonstrating the concept**
- examples using **LangChain and LLM pipelines**

---

# Topics Covered

This repository explores several important concepts involved in building LLM-based applications.

### ▪ Generative AI Fundamentals
Basic understanding of Generative AI, its applications, limitations, and impact areas.

### ▪ LangChain Core Components
Understanding how LangChain structures AI applications using models, prompts, chains, memory, and agents.

### ▪ Models
Exploring language models, open-source models, and embedding models used in modern AI systems.

### ▪ Prompts and Prompt Templates
Designing prompts, dynamic prompt templates, chat prompts, and message structures.

### ▪ Structured Output
Generating predictable responses using JSON schemas, TypedDict, and Pydantic models.

### ▪ Output Parsers
Transforming model outputs into structured formats such as strings, JSON objects, or validated schemas.

### ▪ Chains
Connecting components into sequential or conditional pipelines.

### ▪ Runnables
Modern LangChain architecture for composing pipelines using LCEL and modular execution units.

### ▪ Retrieval-Augmented Generation (RAG)
Building AI systems that retrieve external knowledge before generating responses.

### ▪ Document Loaders
Loading knowledge sources from different formats such as text files, PDFs, websites, and CSV files.

### ▪ Text Splitting
Chunking documents efficiently for better retrieval performance.

### ▪ Vector Stores
Storing and searching embeddings using vector similarity.

### ▪ Retrievers
Retrieving relevant information using vector search, MMR, multi-query retrieval, and contextual compression.

---

# What This Repository Demonstrates

The repository contains practical examples showing how to build AI pipelines involving:

- prompt engineering
- embedding models
- vector search
- document retrieval
- LLM pipelines
- structured outputs
- RAG architectures

Each concept is supported by code examples that demonstrate how the theory translates into working implementations.

---

# How to Use This Repository

### 1. Clone the Repository

```
git clone https://github.com/ShankarOmmi/LangchainLearning.git
```

---

### 2. Create a Virtual Environment (Optional)

If you want to create your own environment:

```
python -m venv .venv
```

Activate it:

**Windows**

```
.venv\Scripts\activate
```

**Mac/Linux**

```
source .venv/bin/activate
```

---

### 3. Install Dependencies

All folders share a single dependency file.

```
pip install -r requirements.txt
```

This installs everything needed to run any example in the repository.

---

### 4. Configure API Keys

Some examples require access to external model providers.

Create a `.env` file and add your API key:

```
HUGGINGFACEHUB_API_TOKEN=your_api_key
```

The `.env` file is ignored by Git through the `.gitignore` configuration to prevent exposing sensitive information.

---

### 5. Run the Code Examples

Each folder contains code examples demonstrating the concept discussed in its README.

You can run them directly using Python or inside Jupyter notebooks depending on the file format.

Example:

```
python example_script.py
```

---

# Learning Approach

The repository follows a progressive learning approach:

1. Understanding Generative AI fundamentals  
2. Learning LangChain components  
3. Working with models and prompts  
4. Structuring outputs and parsing responses  
5. Building pipelines using chains and runnables  
6. Implementing Retrieval-Augmented Generation systems  

This structure helps build a strong foundation before moving toward more advanced AI architectures.

---

# Purpose of This Repository

The main goals of this repository are:

- building a solid conceptual understanding of LLM applications
- experimenting with LangChain components
- implementing RAG pipelines
- documenting important concepts for quick revision

It also serves as a reference for designing real-world AI applications involving external knowledge sources.

---

# Future Improvements

Possible future additions include:

- advanced RAG architectures
- hybrid search systems
- reranking models
- evaluation frameworks for LLM responses

---

# Final Note

The repository represents a continuous learning process while exploring the rapidly evolving ecosystem of **Generative AI and LLM-powered systems**.
