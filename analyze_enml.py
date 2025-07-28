#!/usr/bin/env python3
"""Quick analysis of ENML content complexity."""

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path.cwd() / "src"))

import enote


def analyze_enml_complexity():
    print("=== ENML Content Analysis ===")

    corpus = enote.Corpus()
    corpus.load(max_notes=10)  # Sample analysis

    tag_counts = {}
    total_content_length = 0
    total_markup_length = 0

    for note_id, note in corpus.notes.items():
        content = note.get("content", "")
        if not content:
            continue

        # Count total length
        total_content_length += len(content)

        # Find all HTML/XML tags
        tags = re.findall(r"<[^>]+>", content)
        for tag in tags:
            tag_name = re.findall(r"</?(\w+)", tag)
            if tag_name:
                tag_counts[tag_name[0]] = tag_counts.get(tag_name[0], 0) + 1

        # Calculate markup vs content ratio
        markup_chars = sum(len(tag) for tag in tags)
        total_markup_length += markup_chars

        # Show first note as example
        if note_id == list(corpus.notes.keys())[0]:
            print(f"\nFirst note content preview:")
            print(f"Title: {note.get('title', 'No title')}")
            print(f"Content length: {len(content)} chars")
            print(f"Content preview:")
            print(content[:500] + "..." if len(content) > 500 else content)

    print(f"\n=== MARKUP ANALYSIS ===")
    print(f"Total content: {total_content_length:,} characters")
    print(f"Total markup: {total_markup_length:,} characters")

    if total_content_length > 0:
        markup_percentage = (total_markup_length / total_content_length) * 100
        print(f"Markup overhead: {markup_percentage:.1f}%")

    print(f"\nMost common tags:")
    for tag, count in sorted(
        tag_counts.items(), key=lambda x: x[1], reverse=True
    )[:10]:
        print(f"  {tag}: {count} occurrences")


if __name__ == "__main__":
    analyze_enml_complexity()
