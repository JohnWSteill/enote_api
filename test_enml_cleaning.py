#!/usr/bin/env python3
"""Test ENML cleaning functionality."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path.cwd() / "src"))

import enote


def test_enml_cleaning():
    print("=== Testing ENML Cleaning ===")
    
    corpus = enote.Corpus()
    corpus.load(max_notes=3)  # Test with just a few notes
    
    for note_id, note in corpus.notes.items():
        print(f"\n--- {note_id} ---")
        print(f"Title: {note.get('title', 'No title')}")
        
        original = note.get('content', '')
        cleaned = note.get('cleaned_text', '')
        
        print(f"\nOriginal length: {len(original)} chars")
        print(f"Cleaned length: {len(cleaned)} chars")
        
        if len(original) > 0:
            reduction = ((len(original) - len(cleaned)) / len(original)) * 100
            print(f"Size reduction: {reduction:.1f}%")
        
        print(f"\nOriginal preview:")
        print(original[:300] + "..." if len(original) > 300 else original)
        
        print(f"\nCleaned text:")
        print(cleaned[:500] + "..." if len(cleaned) > 500 else cleaned)
        
        print(f"\n" + "="*60)


if __name__ == "__main__":
    test_enml_cleaning()
