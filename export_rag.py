#!/usr/bin/env python3
"""Export all notes to RAG format JSON."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path.cwd() / "src"))

import enote


def export_all_notes():
    print("=== Exporting Notes to RAG Format ===")

    corpus = enote.Corpus()
    print(f"Loading notes from: {corpus.enex_path}")

    # Load all notes (remove max_notes limit)
    corpus.load()
    print(f"Loaded {len(corpus.notes)} notes")

    # Export to JSON file
    output_file = "evernote_rag_export.json"
    corpus.export_for_rag(output_file)

    print(f"✅ Exported to {output_file}")
    print(f"📊 File size: {Path(output_file).stat().st_size / 1024:.1f} KB")

    # Show sample of what was exported
    print("\nSample note IDs:")
    for i, note_id in enumerate(list(corpus.notes.keys())[:5]):
        print(f"  {i+1}. {note_id}")

    if len(corpus.notes) > 5:
        print(f"  ... and {len(corpus.notes) - 5} more")


if __name__ == "__main__":
    export_all_notes()
