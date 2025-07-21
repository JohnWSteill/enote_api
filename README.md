# Evernote API Sandbox

A Python library providing a clean, SDK-agnostic interface to Evernote APIs, designed for building knowledge management applications that work with large note collections.

## 🎯 Project Goals

- **Read** notes from Evernote (title, body, tags, links, backlinks)
- **Write/Update** notes with Markdown/ENML support  
- **Manage** tags and internal note references
- **Index and search** large note collections efficiently
- **Provide clean abstractions** for knowledge management applications

## 💡 **Intended Usage**

```python
import enote_api

# Initialize with credentials
my_notes = enote_api.Corpus(credentials)

# Core operations
note_dict = my_notes.get_all_notes()  # {id: title, body, tags}
note = my_notes.get_note(note_id)
new_id = my_notes.write_new_note(body, tags)
my_notes.overwrite_note(note_id, body, tags)
my_notes.delete_note(note_id)

# Query and search (future)
results = my_notes.query("notes about project management")
```

## 🎯 Use Cases

- **Knowledge Management**: Work with large collections of interconnected notes
- **Content Analysis**: Extract insights from years of accumulated notes  
- **Automation**: Programmatically organize and cross-reference content
- **AI Integration**: Build intelligent agents that leverage personal knowledge bases

## 🏗️ Project Structure

```
├── src/               # Core library code
├── notebooks/         # Jupyter notebooks for exploration and prototyping  
├── tests/            # Unit and integration tests
├── requirements.txt  # Core dependencies (SDK-agnostic)
└── docs/            # Documentation and examples
```

## 🚀 Getting Started

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Explore APIs** 
   Check out `notebooks/` for SDK evaluation and prototyping

3. **Run Tests**
   ```bash
   pytest tests/
   ```

## 📋 Development Status

- [x] Phase 1: Environment Setup
- [x] Phase 2: Project Bootstrap  
- [ ] Phase 3: SDK Evaluation & Selection (XYZ → Concrete SDK)
- [ ] Phase 4: Core Corpus API (read operations)
- [ ] Phase 5: Write Operations & Note Management
- [ ] Phase 6: Search & Indexing Layer
- [ ] Phase 7: Advanced Knowledge Management Features

## 🛠️ Development Environment

- Python 3.13.5 (Homebrew on macOS Apple Silicon)
- Virtual Environment: `~/venvs/VS_Code`
- Tools: Jupyter, Black, Flake8, pytest

---

*See `Evernote_API_Project_Context.md` for detailed project roadmap and context.*
