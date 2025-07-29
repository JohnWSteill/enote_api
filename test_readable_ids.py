#!/usr/bin/env python3
"""Test human-readable note IDs."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path.cwd() / "src"))

import enote


def test_readable_ids():
    print("=== Testing Human-Readable Note IDs ===")

    corpus = enote.Corpus()
    corpus.load(max_notes=5)

    print(f"\nLoaded {len(corpus.notes)} notes with IDs:")

    for note_id, note_data in corpus.notes.items():
        title = note_data.get("title", "No title")
        print(f"  {note_id} -> {title}")

    print("\nSample note structure:")
    if corpus.notes:
        first_id = list(corpus.notes.keys())[0]
        first_note = corpus.notes[first_id]

        print(f"ID: {first_id}")
        print(f"Title: {first_note.get('title', 'No title')}")
        print(f"Has cleaned_text: {'cleaned_text' in first_note}")

        cleaned = first_note.get("cleaned_text", "")
        print(f"Cleaned text preview: {cleaned[:100]}...")


if __name__ == "__main__":
    test_readable_ids()
