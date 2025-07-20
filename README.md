# Evernote API Sandbox

A robust Python module for Evernote API integration, supporting read/write operations with internal linking and automation capabilities.

## 🎯 Project Goals

- **Read** notes from Evernote (title, body, tags, links, backlinks)
- **Write/Update** notes with Markdown/ENML support  
- **Manage** tags and internal note references
- **Automate** note creation and cross-referencing

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
- [ ] Phase 3: SDK Evaluation
- [ ] Phase 4: Read Library
- [ ] Phase 5: Write Support
- [ ] Phase 6: Automation Layer

## 🛠️ Development Environment

- Python 3.13.5 (Homebrew on macOS Apple Silicon)
- Virtual Environment: `~/venvs/VS_Code`
- Tools: Jupyter, Black, Flake8, pytest

---

*See `Evernote_API_Project_Context.md` for detailed project roadmap and context.*
