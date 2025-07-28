#!/usr/bin/env python3
"""Quick test of dynamic attribute extraction."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path.cwd() / "src"))

import enote


def test_dynamic_extraction():
    print("=== Testing Dynamic Attribute Extraction ===")

    corpus = enote.Corpus()
    print(f"Corpus initialized with path: {corpus.enex_path}")

    corpus.load(max_notes=1)
    print(f"Loaded {len(corpus.notes)} notes")

    if corpus.notes:
        note_id = list(corpus.notes.keys())[0]
        note = corpus.notes[note_id]

        print(f"\nNote {note_id} discovered attributes:")
        for key, value in note.items():
            if isinstance(value, list):
                print(f"  {key}: list with {len(value)} items - {value}")
            else:
                value_preview = (
                    str(value)[:50] + "..."
                    if len(str(value)) > 50
                    else str(value)
                )
                print(f"  {key}: {type(value).__name__} - {value_preview}")
    else:
        print("No notes were loaded!")


if __name__ == "__main__":
    test_dynamic_extraction()
