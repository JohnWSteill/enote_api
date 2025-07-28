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
    print(f"Content: {note_data['content'][:200]}...")
    print(f"Clean text: {note_data['cleaned_text'][:200]}...")
```

## 🎯 Use Cases

- **RAG Systems**: Structure personal knowledge for retrieval-augmented generation
- **AI Training Data**: Prepare curated datasets from personal note collections  
- **Knowledge Graphs**: Extract semantic relationships between notes and concepts
- **Executive AI Agents**: Build assistants with deep personal context

## 🏗️ Project Structure

```
├── src/enote/              # Core extraction library  
│   ├── corpus.py          # Main Corpus class with ENML cleaning
│   ├── constants.py       # Configuration constants
│   └── __init__.py        # Package initialization
├── notebooks/             # Interactive development and analysis
│   ├── corpus_exploration.ipynb    # Development playground
│   ├── performance_analysis.ipynb  # Timing and optimization
│   └── test_enex_parsing.ipynb     # ENEX format exploration
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
✅ **Memory Management** - Configurable note limits for large datasets  
✅ **Test Coverage** - Verified with real note collection  
✅ **Content Cleaning** - ENML to clean text with 76-90% size reduction
🔄 **Export Formats** - JSON, Markdown, vector-ready (planned)

## ⚡ Performance Considerations

**File Processing Order**: Currently processes ENEX files in filesystem order (typically alphabetical). For large datasets with mixed file sizes, this may not be optimal.

**TODO**: Consider implementing smart file ordering:
- Process smaller files first for faster feedback during development
- Sort by file size for predictable memory usage patterns  
- Add progress indicators for large file processing (430MB+ files)
- Consider implementing `ET.iterparse()` for truly lazy loading of massive files

**Current Behavior**: Full DOM parsing via `ET.parse()` loads entire ENEX files into memory before processing. This works well for typical sizes but may need optimization for very large exports.

## 🚧 ENEX Format Limitations

**Known Constraints** of the ENEX export format that affect migration capabilities:

### **Data Loss During Export**
- **Note Links**: Internal Evernote note links (`evernote:///view/...`) are **unrecoverable** from ENEX
- **Notebook Structure**: All notes exported as flat list, original notebook organization lost
- **Tag Hierarchy**: Hierarchical tag relationships flattened to simple tag lists
- **Note History**: Version history and revision data not included in exports

### **Resource Handling (Future Work)**
- **Nested Elements**: Current implementation extracts flat attributes only
- **Embedded Files**: `<resource>` elements (images, PDFs, attachments) not processed
- **Base64 Content**: Binary data encoded in XML requires special handling
- **MIME Types**: File type detection and extraction not implemented

### **BabyCoach MVP Scope**
**Current Focus**: Text content extraction for RAG implementation
- ✅ **Title, content, tags, timestamps** - Core text data for knowledge base
- ⏸️ **Images and attachments** - Nice-to-have for enhanced RAG, not blocking
- ⏸️ **Note linking** - Potential future feature, not essential for MVP
- ⏸️ **Notebook organization** - Can be reconstructed via tags and metadata

**Design Philosophy**: Extract maximum value from available text content rather than attempting perfect Evernote recreation.

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
- [x] Document workspace environment setup best practices  
- [ ] Move project-specific packages out of global VS_Code venv
- [x] Code workspace settings for Python interpreter
- [x] Modify workspace environment so src is in path
- [x] Add environment setup to README.md

### Performance & Scalability
- [ ] Smart ENEX file processing order (size-based)
- [ ] Progress indicators for large file processing (430MB+ files)
- [ ] Consider `ET.iterparse()` for lazy loading of massive files
- [ ] Memory usage profiling and optimization

### Core Functionality
- [x] Dynamic attribute extraction from ENEX elements
- [x] ENML content cleaning and conversion (76-90% size reduction)
- [ ] GUID-based note identification system
- [ ] Vector embedding preparation for RAG

### Future Enhancements (Post-MVP)
- [ ] Nested element parsing for `<resource>` elements
- [ ] Image and attachment extraction from base64 data
- [ ] Broken link detection and reporting
- [ ] Note relationship discovery via content analysis
- [ ] Advanced ENML to Markdown conversion
- [ ] Notebook structure reconstruction via metadata

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

## � Development Environment Setup

### **VS Code Workspace Configuration**

The project includes optimized VS Code settings in `.vscode/settings.json`:

- **Python Interpreter**: Auto-configured to use `~/venvs/VS_Code`
- **Auto-activation**: Terminal automatically sources the virtual environment
- **PYTHONPATH**: Automatically includes `src/` for imports
- **Default Terminal**: Custom profile with venv pre-activated

### **Quick Setup Checklist**

1. **Virtual Environment**: Use existing `~/venvs/VS_Code` or create project-specific
2. **Dependencies**: `pip install -r requirements.txt`
3. **ENEX Data**: Export to `~/tmp/evernote_backup` (or configure custom path)
4. **VS Code**: Open workspace folder - environment auto-activates
5. **Test**: Run `pytest tests/` to verify setup

### **Import Path Configuration**

With the workspace settings, you can import directly:
```python
import enote  # Works automatically
corpus = enote.Corpus()  # No PYTHONPATH needed
```

### **Terminal Auto-Activation**

New terminal windows automatically:
- Activate the virtual environment
- Set working directory to project root  
- Configure PYTHONPATH for development

## �📋 Development Status

- [x] Phase 1: Environment Setup
- [x] Phase 2: Project Bootstrap  
- [x] Phase 3: ENEX Parsing Implementation
- [x] Phase 4: Core Read Operations (4,874 notes successfully parsed)
- [x] Phase 5: ENML Content Extraction & Cleaning (76-90% size reduction)
- [ ] Phase 6: GenAI Export Formats (JSON, Markdown, Vector-ready)
- [ ] Phase 7: BabyCoach MVP Integration

## 🔖 Phase 6 Bookmark: RAG Export Formats

**Status**: Ready to implement when GenAI learning progresses (Week 3-4 of bootcamp)

### **Current RAG-Ready Data Structure:**
```python
# Your notes are already perfectly structured for RAG:
{
    "band_practice_checklist": {
        "title": "Band Practice checklist",
        "cleaned_text": "Musician AOF\n\nTASCAM\n2AA Batteries...",  # 76-90% smaller
        "tags": ["music", "band"], 
        "created": "2021-02-12",
        "content": "<?xml...>"  # Original ENML preserved
    }
}
```

### **Standard RAG Export Formats:**

**JSON Lines (.jsonl) - Most Common:**
```python
def export_for_rag(self) -> str:
    """Export corpus in standard RAG format."""
    rag_data = []
    for note_id, note in self.notes.items():
        rag_data.append({
            "id": note_id,  # Human-readable: "band_practice_checklist" 
            "text": note.get('cleaned_text', ''),
            "metadata": {
                "title": note.get('title', ''),
                "tags": note.get('tag', []),
                "created": note.get('created', ''),
                "source": "evernote"
            }
        })
    return '\n'.join(json.dumps(item) for item in rag_data)
```

**Vector Database Integration (Learn in Week 4-6):**
```python
def export_to_vectordb(self, collection_name: str):
    """Export to Chroma/Pinecone/FAISS when you learn vector databases."""
    # Implementation depends on your bootcamp's vector DB choice
    pass
```

### **Why This Architecture Works:**
- ✅ **Human-readable IDs**: Easy debugging (`band_practice_checklist` vs `note_000001`)
- ✅ **Clean text**: 76-90% smaller embeddings, better semantic search
- ✅ **Rich metadata**: Tags, dates, titles for filtering and context
- ✅ **Original preserved**: ENML content available for special processing
- ✅ **Standard format**: Works with any RAG system you'll learn

**Next Steps**: Return here after learning vector embeddings and databases in bootcamp!

## 🛠️ Development Environment

- Python 3.13.5 (Homebrew on macOS Apple Silicon)
- Virtual Environment: `~/venvs/VS_Code`
- Tools: Jupyter, Black, Flake8, pytest

---

*See `Evernote_API_Project_Context.md` for detailed project roadmap and context.*
