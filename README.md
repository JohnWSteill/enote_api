# Evernote Corpus Extractor

A Python utility for extracting and structuring Evernote note collections into GenAI-ready datasets. Designed to transform years of personal knowledge into structured corpora for AI applications, RAG systems, and intelligent agents.

## 🎯 Project Goals

- **Extract** notes from Evernote ENEX exports with full metadata preservation
- **Structure** large note collections into AI-consumable formats
- **Preserve** semantic relationships (tags, timestamps, note connections)
- **Enable** GenAI application development with personal knowledge bases
- **Support** Future AI agent development

## 💡 **Current Usage**

```python
import enote

# Initialize with ENEX backup path
corpus = enote.Corpus({"enex_path": "~/tmp/evernote_backup"})

# Extract structured notes (respects memory limits)
notes = corpus.get_all_notes(max_notes=100)

# Each note contains: title, body, tags, created, updated
for note_id, note_data in notes.items():
    print(f"Title: {note_data['title']}")
    print(f"Tags: {note_data['tags']}")
    print(f"Content: {note_data['body'][:200]}...")
```

## 🎯 Use Cases

- **RAG Systems**: Structure personal knowledge for retrieval-augmented generation
- **AI Training Data**: Prepare curated datasets from personal note collections  
- **Knowledge Graphs**: Extract semantic relationships between notes and concepts
- **Executive AI Agents**: Build assistants with deep personal context

## 🏗️ Project Structure

```
├── src/enote/         # Core extraction library
├── notebooks/         # Data analysis and development examples
├── tests/             # Unit and integration tests  
├── requirements.txt   # Core dependencies
└── README.md         # This file
```

## 🛠️ Development Environment

- Python 3.13.5 (Homebrew on macOS Apple Silicon)
- Virtual Environment: `~/venvs/VS_Code`
- Tools: Jupyter, Black, Flake8, pytest
- Data Source: ENEX exports from evernote-backup

## 📊 Current Capabilities

✅ **ENEX File Parsing** - Processes multiple notebook exports  
✅ **Metadata Extraction** - Titles, tags, timestamps preserved  
✅ **Memory Management** - Configurable note limits for large datasets  
✅ **Test Coverage** - Verified with real note collection  
🔄 **Content Cleaning** - ENML to plain text (in development)  
🔄 **Export Formats** - JSON, Markdown, vector-ready (planned)

---

*This tool enables GenAI development with personal knowledge bases. See `notebooks/` for examples and `tests/` for usage patterns.*

## � Data Setup

1. **Export your Evernote data using evernote-backup:**
   ```bash
   # Install evernote-backup
   brew install evernote-backup
   
   # Initialize and sync your account  
   evernote-backup init-db
   evernote-backup sync
   
   # Export to ENEX files
   evernote-backup export ~/tmp/evernote_backup
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Test the extraction:**
   ```bash
   pytest tests/
   ```

## 📋 Development Status

- [x] Phase 1: Environment Setup
- [x] Phase 2: Project Bootstrap  
- [x] Phase 3: ENEX Parsing Implementation
- [x] Phase 4: Core Read Operations (4,874 notes successfully parsed)
- [ ] Phase 5: ENML Content Extraction & Cleaning
- [ ] Phase 6: GenAI Export Formats (JSON, Markdown, Vector-ready)
- [ ] Phase 7: BabyCoach MVP Integration

## 🛠️ Development Environment

- Python 3.13.5 (Homebrew on macOS Apple Silicon)
- Virtual Environment: `~/venvs/VS_Code`
- Tools: Jupyter, Black, Flake8, pytest

---

*See `Evernote_API_Project_Context.md` for detailed project roadmap and context.*
