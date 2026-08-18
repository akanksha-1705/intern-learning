import argparse
import json
from pathlib import Path

from sentence_transformers import SentenceTransformer


def read_document(file_path):
    """Read the document and return its paragraphs."""
    text = Path(file_path).read_text(encoding="utf-8")
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
    return paragraphs


def create_chunks(paragraphs, chunk_size, overlap):
    """Create overlapping text chunks."""
    text = "\n\n".join(paragraphs)

    chunks = []
    start = 0

    while start < len(text):
        end = min(start + chunk_size, len(text))
        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        if end == len(text):
            break

        start = end - overlap

    return chunks


def generate_embeddings(chunks, model):
    """Generate an embedding for every chunk."""
    embeddings = model.encode(chunks, normalize_embeddings=True)
    return embeddings.tolist()


def main():
    parser = argparse.ArgumentParser(
        description="Chunk a document and generate embeddings."
    )

    parser.add_argument(
        "--input",
        default="document.txt",
        help="Path to the input document."
    )

    parser.add_argument(
        "--output",
        default="chunks.json",
        help="Path for the output JSON file."
    )

    parser.add_argument(
        "--chunk-size",
        type=int,
        default=500,
        help="Number of characters in each chunk."
    )

    parser.add_argument(
        "--overlap",
        type=int,
        default=100,
        help="Number of overlapping characters."
    )

    args = parser.parse_args()

    if args.chunk_size <= 0:
        raise ValueError("Chunk size must be greater than 0.")

    if args.overlap < 0:
        raise ValueError("Overlap cannot be negative.")

    if args.overlap >= args.chunk_size:
        raise ValueError("Overlap must be smaller than chunk size.")

    paragraphs = read_document(args.input)

    if len(paragraphs) < 10:
        raise ValueError(
            "The document must contain at least 10 paragraphs."
        )

    chunks = create_chunks(
        paragraphs,
        args.chunk_size,
        args.overlap
    )

    print(f"Document paragraphs: {len(paragraphs)}")
    print(f"Chunk size: {args.chunk_size}")
    print(f"Overlap: {args.overlap}")
    print(f"Number of chunks: {len(chunks)}")

    print("\nLoading embedding model...")
    model = SentenceTransformer("all-MiniLM-L6-v2")

    print("Generating embeddings...")
    embeddings = generate_embeddings(chunks, model)

    records = []

    for index, (chunk, embedding) in enumerate(
        zip(chunks, embeddings)
    ):
        records.append(
            {
                "id": index,
                "text": chunk,
                "embedding": embedding
            }
        )

    output = {
        "chunk_size": args.chunk_size,
        "overlap": args.overlap,
        "chunks": records
    }

    Path(args.output).write_text(
        json.dumps(output, indent=2),
        encoding="utf-8"
    )

    print(f"\nSaved {len(records)} chunks to {args.output}")


if __name__ == "__main__":
    main()