import argparse
import json
from pathlib import Path

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


def load_chunks(file_path):
    """Load chunks and embeddings from the JSON file."""
    data = json.loads(
        Path(file_path).read_text(encoding="utf-8")
    )

    return data["chunks"]


def find_top_chunks(question, chunks, model, top_k=3):
    """Find the most similar document chunks."""
    question_embedding = model.encode(
        [question],
        normalize_embeddings=True
    )

    similarities = []

    for chunk in chunks:
        score = cosine_similarity(
            question_embedding,
            [chunk["embedding"]]
        )[0][0]

        similarities.append(
            {
                "id": chunk["id"],
                "text": chunk["text"],
                "score": float(score)
            }
        )

    similarities.sort(
        key=lambda item: item["score"],
        reverse=True
    )

    return similarities[:top_k]


def main():
    parser = argparse.ArgumentParser(
        description="Search document chunks using semantic similarity."
    )

    parser.add_argument(
        "question",
        help="Question to search for."
    )

    parser.add_argument(
        "--input",
        default="chunks.json",
        help="JSON file containing chunks and embeddings."
    )

    parser.add_argument(
        "--top-k",
        type=int,
        default=3,
        help="Number of results to display."
    )

    args = parser.parse_args()

    print("Loading embedding model...")
    model = SentenceTransformer("all-MiniLM-L6-v2")

    chunks = load_chunks(args.input)

    results = find_top_chunks(
        args.question,
        chunks,
        model,
        args.top_k
    )

    print("\nTop matching chunks:\n")

    for position, result in enumerate(results, start=1):
        print("=" * 70)
        print(f"Result #{position}")
        print(f"Chunk ID: {result['id']}")
        print(f"Similarity score: {result['score']:.4f}")
        print("-" * 70)
        print(result["text"])
        print()


if __name__ == "__main__":
    main()