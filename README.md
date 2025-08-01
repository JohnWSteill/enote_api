# Evernote Corpus Extractor

A Python utility for extracting and structuring Evernote note collections into GenAI-ready datasets. Designed to transform years of personal knowledge into structured corpora for AI applications, RAG systems, and intelligent agents.

## 🎯 Project Goals

- **Extract** notes from Evernote ENEX exports with full metadata preservation
- **Structure** large note collections into GenAI-ready JSON datasets
- **Preserve** semantic relationships (tags, timestamps, human-readable IDs)
- **Enable** downstream AI applications (RAG systems, knowledge graphs, intelligent agents)

## 💡 **Current Usage**

```python
import enote

# Initialize with default ENEX path
corpus = enote.Corpus()
# Or specify custom path:
# corpus = enote.Corpus({"enex_path": "/path/to/backups"})

# Load notes into corpus (respects memory limits)
corpus.load(max_notes=100)

# Access the loaded notes
for note_id, note_data in corpus.notes.items():
    print(f"Title: {note_data['title']}")
    print(f"Tags: {note_data['tags']}")
    print(f"Content: {note_data['content'][:200]}...")
    print(f"Clean text: {note_data['cleaned_text'][:200]}...")
```


## 🏗️ Project Structure

```
├── src/enote/              # Core extraction library  
│   ├── corpus.py          # Main Corpus class with ENML cleaning
│   ├── constants.py       # Configuration constants
│   └── __init__.py        # Package initialization
├── notebooks/             # Interactive development and analysis
├── tests/                 # Unit and integration tests  
│   ├── test_corpus.py     # Core functionality tests
│   ├── test_basic.py      # Project structure validation
│   └── conftest.py        # Test configuration
├── .vscode/               # VS Code workspace configuration
├── requirements.txt       # Core dependencies
└── README.md             # This file
```

## 🛠️ Development Environment

- Python 3.13.5 (Homebrew on macOS Apple Silicon)
- Virtual Environment: `~/venvs/VS_Code`
- Tools: Jupyter, Black, Flake8, pytest
- Data Source: ENEX exports from evernote-backup

## 📊 Current Capabilities

✅ **ENEX File Parsing** - Processes multiple notebook exports  
✅ **Metadata Extraction** - Titles, tags, timestamps preserved  
✅ **Content Cleaning** - ENML to clean text with 76-90% size reduction
✅ **JSON Export** - Production-ready format for downstream AI applications
✅ **Human-readable IDs** - `band_practice_checklist` vs `note_000001`

## ⚡ Performance Notes

Full DOM parsing loads entire ENEX files into memory before processing. Works well for typical sizes but larger exports (430MB+) may benefit from streaming approaches in future versions.

## 🚧 ENEX Format Limitations

**Known Constraints** of the ENEX export format:
- **Note Links**: Internal Evernote links are unrecoverable from ENEX
- **Notebook Structure**: Notes exported as flat list, original organization lost
- **Tag Hierarchy**: Hierarchical relationships flattened to simple tag lists
- **Embedded Files**: Images, PDFs, attachments not processed (XML base64 data)

**Future Work**: Resource extraction from `<resource>` elements would enable processing of embedded images, PDFs, and other attachments stored as base64-encoded data within the ENEX XML structure.

## 📋 Setup & Usage

### Quick Start
```bash
# Install dependencies
pip install -r requirements.txt

# Export your Evernote data
brew install evernote-backup
evernote-backup init-db && evernote-backup sync
evernote-backup export ~/tmp/evernote_backup

# Test the extraction
pytest tests/
```

### VS Code Workspace
The project includes optimized VS Code settings for Python development with automatic environment activation and import path configuration.

## � Output Format

**Production-Ready JSON Structure:**
```python
# Clean, structured data ready for downstream AI applications
{
    "id": "band_practice_checklist",  # Human-readable identifier
    "text": "Musician AOF\n\nTASCAM\n2AA Batteries...",  # 76-90% size reduction
    "metadata": {
        "title": "Band Practice checklist",
        "tags": ["music", "band"],
        "created": "2021-02-12",
        "source": "evernote"
    }
}
```

Export files are saved to `~/Desktop` and excluded from git to protect personal data.

---

*Python 3.13.5 • VS Code optimized • See `notebooks/` for examples*
