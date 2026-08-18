# Day 9 - Chunk & Embed a Document

This project implements the document ingestion and retrieval part of a Retrieval-Augmented Generation (RAG) pipeline.

## Files

- `document.txt` - Source document used for the RAG experiment.
- `ingest.py` - Reads the document, creates chunks, generates embeddings, and saves them to `chunks.json`.
- `query.py` - Searches the document using semantic similarity and displays the top 3 matching chunks.
- `chunks.json` - Stores the document chunks and their embeddings.
- `requirements.txt` - Lists the required Python packages.

## Install Dependencies

Activate the existing project virtual environment and run:

```bash
pip install -r requirements.txt