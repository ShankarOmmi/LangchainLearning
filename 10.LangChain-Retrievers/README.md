# Retrievers in RAG Systems

Retrievers are a key component of **Retrieval-Augmented Generation (RAG)** systems. Their main role is to identify and return the most relevant pieces of information from a knowledge source before the language model generates a response.

Instead of sending entire documents to a language model, retrievers select only the **most relevant chunks**, which improves response quality and reduces unnecessary context.

---

# What are Retrievers?

A retriever is responsible for **searching through a collection of documents and returning the most relevant pieces of information for a given query**.

In a typical RAG workflow:

```
User Question
      ↓
Retriever
      ↓
Relevant Documents
      ↓
Language Model
      ↓
Generated Answer
```

The retriever ensures that the language model receives **useful and focused context**, which helps reduce hallucinations and improve factual accuracy.

---

# Types of Retrievers

Different retrieval strategies can be used depending on the problem and the type of data.

Common retriever types include:

- knowledge base retrievers
- vector store retrievers
- multi-query retrievers
- contextual compression retrievers
- hybrid retrievers

Each approach focuses on improving how relevant information is selected before passing it to the model.

---

# Wikipedia Retriever

A Wikipedia retriever fetches relevant information directly from Wikipedia based on the user query.

Example workflow:

```
User Question
      ↓
Wikipedia Search
      ↓
Relevant Articles
      ↓
Extracted Content
```

This approach is useful for answering general knowledge questions without maintaining a local document database.

However, it depends on external sources and internet connectivity.

---

# Vector Store Retriever

A vector store retriever works with **embedding-based similarity search**.

The process typically looks like this:

```
Documents
      ↓
Text Splitting
      ↓
Embedding Model
      ↓
Vector Store
      ↓
Retriever
```

When a user asks a question:

1. The question is converted into an embedding.
2. The vector store searches for document vectors with the closest similarity.
3. The most relevant chunks are returned.

This is the most common retrieval approach used in RAG systems.

---

# Maximum Marginal Relevance (MMR)

Maximum Marginal Relevance is a retrieval strategy that balances **relevance and diversity**.

Standard similarity search may return many chunks that are very similar to each other. MMR helps avoid redundancy by selecting documents that are both:

- relevant to the query
- different from previously selected results

Conceptually:

```
Retrieve relevant documents
        ↓
Remove redundant results
        ↓
Return diverse information
```

This improves the quality of retrieved context.

---

# Multi Query Retriever

Sometimes a single query does not capture the full intent of the user's question.

A multi-query retriever solves this by generating **multiple variations of the original query** using a language model.

Example:

Original query:

```
How can confidence be improved?
```

Generated variations:

```
Ways to build confidence
Techniques for improving self-belief
Methods to increase confidence
```

Each query retrieves documents independently, and the results are combined.

This improves retrieval coverage and helps capture different perspectives from the dataset.

---

# Contextual Compression Retriever

Sometimes the retriever returns large chunks of text that contain useful information along with irrelevant details.

A contextual compression retriever solves this by **filtering or summarizing retrieved documents before sending them to the language model**.

Workflow:

```
Retriever
      ↓
Large Document Chunks
      ↓
Compression / Filtering
      ↓
Relevant Extracted Context
      ↓
Language Model
```

This approach reduces noise and ensures that only the most important information is used.

---

# Additional Retriever Techniques

Several other retrieval approaches exist depending on the application.

Examples include:

- hybrid retrieval (combining keyword search with vector search)
- metadata-based retrieval
- reranking models
- semantic search with advanced embeddings

These techniques aim to improve the quality of information retrieved before generation.

---

# Key Takeaways

- Retrievers identify relevant information for a given query.
- They are essential for building effective RAG systems.
- Vector store retrievers are the most commonly used approach.
- MMR improves diversity in retrieved documents.
- Multi-query retrieval expands the search space using multiple queries.
- Contextual compression removes irrelevant information from retrieved results.

Effective retrieval is one of the most important factors influencing the performance of **LLM-based question answering systems**.
