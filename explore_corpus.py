# %% [markdown]
# Interactive exploration of the Corpus class
# Use Shift+Enter to run each cell

# %%
import sys
from pathlib import Path
sys.path.insert(0, str(Path.cwd() / "src"))

import enote

# %%
# Explore the Corpus class
corpus = enote.Corpus()
print("Corpus attributes:")
print(dir(corpus))

# %%
# Look at the documentation
help(corpus.load)

# %%
# Load some notes and explore
corpus.load(max_notes=2)
print(f"Loaded {len(corpus.notes)} notes")

# %%
# Explore the notes structure
for note_id, note_data in corpus.notes.items():
    print(f"\n=== {note_id} ===")
    print(f"Title: {note_data['title']}")
    print(f"Tags: {note_data['tags']}")
    print(f"Keys: {list(note_data.keys())}")
    break  # Just show first one

# %%
# Try some operations
first_note = list(corpus.notes.values())[0]
print("First note structure:")
for key, value in first_note.items():
    print(f"{key}: {type(value)} - {str(value)[:50]}...")
