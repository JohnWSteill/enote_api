#!/usr/bin/env python3
"""
Demo script for VS Code debugging tutorial.
This simulates the kind of debugging you'd do on the Corpus class.
"""

import enote


def main():
    print("=== VS Code Debugging Demo ===")

    # Create a corpus instance
    corpus = enote.Corpus()
    print(f"Created corpus with path: {corpus.enex_path}")

    # This is where you'd set a breakpoint in VS Code
    # (Instead of adding pdb.set_trace() here)
    corpus.load(max_notes=2)

    # Inspect the loaded data
    print(f"Loaded {len(corpus.notes)} notes")

    # Let's examine the first note
    if corpus.notes:
        first_note_id = list(corpus.notes.keys())[0]
        first_note = corpus.notes[first_note_id]

        print(f"First note ID: {first_note_id}")
        print(f"First note title: {first_note['title']}")
        print(f"First note tags: {first_note['tags']}")

        # This would be a good place for another breakpoint
        # to inspect the note data structure

    print("Demo complete!")


if __name__ == "__main__":
    main()
