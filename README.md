# GraphRAG-Knowledge-Graph-Vector-Retrieval-QA-System
GraphRAG is an advanced Retrieval-Augmented Generation (RAG) system that combines knowledge graphs with vector similarity search to improve multi-hop question answering. Unlike traditional RAG pipelines that retrieve isolated text chunks
Traditional RAG pipelines retrieve independent text chunks based only on semantic similarity. This project extends the approach by building a knowledge graph of entities and relationships extracted from documents, enabling the system to understand connections between concepts and perform multi-hop reasoning.

## The system retrieves context through two complementary paths:

1.Graph Retrieval: Traverses relationships between entities stored in a knowledge graph.

2.Vector Retrieval: Retrieves semantically similar document chunks from a vector database.

3.Both contexts are merged and passed to a language model to generate accurate, relationship-aware answers.

# Architecture

        Documents (PDF / Text)
                │
                ▼
        Entity Extraction (NER)
                │
                ▼
        Relation Extraction
                │
                ▼
        Knowledge Graph (Neo4j)
                │
                ▼
        Dual Retrieval
         ├── Graph Traversal
         └── Vector Search (FAISS)
                │
                ▼
        Context Aggregation
                │
                ▼
        LLM Response Generation
                │
                ▼
        FastAPI Backend
                │
                ▼
        Docker Deployment


# Key Features

Entity extraction using NLP models

Relationship extraction between entities

Knowledge graph construction and traversal

Dual retrieval pipeline (graph + vector search)

Natural language question answering




# Project Workflow
## 1. Document Processing

Documents such as PDFs or text files are ingested and split into smaller chunks for processing.

## 2. Entity Extraction

Named Entity Recognition (NER) models identify entities such as:
People
Organizations
Locations
Dates
Concepts

## 3. Relationship Extraction

A relation extraction model identifies relationships between entities, for example:

Elon Musk → CEO of → Tesla
Tesla → produces → Electric Vehicles
## 4. Knowledge Graph Construction

Entities are stored as nodes and relationships as edges in a Neo4j graph database.

## 5. Vector Indexing

Document chunks are converted into embeddings and stored in FAISS for semantic retrieval.

## 6. Query Processing

When a user submits a question:

Entities are extracted from the query

Graph traversal retrieves related nodes

Vector search retrieves relevant document chunks

Context is merged and passed to the LLM

## 7. Response Generation

The LLM generates a final answer using the combined context.

Source-aware answer generation

API-based deployment for production use
