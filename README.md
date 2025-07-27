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

## ⚡ Performance Considerations

**File Processing Order**: Currently processes ENEX files in filesystem order (typically alphabetical). For large datasets with mixed file sizes, this may not be optimal.

**TODO**: Consider implementing smart file ordering:
- Process smaller files first for faster feedback during development
- Sort by file size for predictable memory usage patterns  
- Add progress indicators for large file processing (430MB+ files)
- Consider implementing `ET.iterparse()` for truly lazy loading of massive files

**Current Behavior**: Full DOM parsing via `ET.parse()` loads entire ENEX files into memory before processing. This works well for typical sizes but may need optimization for very large exports.

## 🏗️ Architectural Considerations

**Key Design Questions Identified**:

1. **Hardcoded vs. Dynamic Attribute Extraction**
   - *Current*: Manually extract `title`, `created`, `updated`, `tags`, `content`
   - *Concern*: Brittle and may miss ENEX fields across different export formats
   - *Recommendation*: Implement dynamic extraction that discovers all available attributes

2. **Note ID Strategy & Linking**
   - *Current*: Manual counter-based IDs (`note_000000`)
   - *Concern*: Cannot resolve Evernote's internal note links and references
   - *Recommendation*: Use ENEX GUID fields for note identification to preserve linking

3. **Long-term RAG Architecture**
   - *Current*: Simple dictionary storage in memory
   - *Concern*: Scalability for vector search, metadata indexing, and graph traversal
   - *Recommendation*: Plan for vector embeddings, link graphs, and hybrid search capabilities

**Next Phase Priorities**:
- [ ] Dynamic ENEX attribute discovery
- [ ] GUID-based note identification
- [ ] Link relationship extraction
- [ ] Vector search foundation

## 📋 Development TODOs

### Environment Setup
- [ ] Set up project-specific virtual environment (.venv in project root)
- [ ] Document workspace environment setup best practices  
- [ ] Move project-specific packages out of global VS_Code venv
- [ ] Code workspace settings for Python interpreter
- [ ] Modify workspace environment so src is in path
- [ ] Add environment setup to README.md

### Performance & Scalability
- [ ] Smart ENEX file processing order (size-based)
- [ ] Progress indicators for large file processing (430MB+ files)
- [ ] Consider `ET.iterparse()` for lazy loading of massive files
- [ ] Memory usage profiling and optimization

### Core Functionality
- [ ] Dynamic attribute extraction from ENEX elements
- [ ] GUID-based note identification system
- [ ] Note linking and relationship discovery
- [ ] ENML content cleaning and conversion
- [ ] Vector embedding preparation for RAG

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
   
   # Export to ENEX files (this path becomes the default for enote)
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
