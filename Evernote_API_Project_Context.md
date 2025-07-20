# 📚 Evernote API Project: Developer Context

## 🎯 Ultimate Goal

Build a robust, testable Python module that can:
- ✅ **Read notes** from my Evernote account, including:
  - Title, body, tags
  - Internal note-to-note hyperlinks and backlinks
- ✅ **Write or update notes**, with:
  - Markdown or ENML support
  - Tag management
  - Internal links to other notes (by GUID or title)
- ✅ Eventually support lightweight syncing and automation tasks

---

## 🛤️ High-Level Roadmap

### 🔧 Phase 1: Developer Environment Setup ✅ _(complete)_
- Installed Python 3.13 via Homebrew on macOS (Apple Silicon)
- Created a `VS_Code` virtual environment
- Configured VS Code to use it as the **global default interpreter**
- Verified Jupyter, Black, and Flake8 are working
- Cleaned up old Anaconda/brew clutter
- Modularized and version-controlled bash profile

➡️ All dev work will occur in this environment

---

### 📁 Phase 2: Project Bootstrap
- [ ] Create a repo: `evernote-api-sandbox`
- [ ] Add basic structure: `README.md`, `requirements.txt`, `notebooks/`, `src/`, `tests/`
- [ ] Document use cases and desired capabilities

---

### 🔍 Phase 3: Evaluate Evernote SDKs and APIs
- [ ] Explore options:
  - [ ] [evernote-sdk-python3](https://github.com/evernote/evernote-sdk-python3)
  - [ ] [g-e-o/evernote-backup](https://github.com/vzh/evernote-backup)
  - [ ] Evernote public API documentation
- [ ] Test read-only API access using a personal dev token
- [ ] Evaluate Markdown vs. ENML parsing/serialization
- [ ] Inventory Evernote's support for backlinks/internal references

---

### 🧪 Phase 4: Build Minimal Read Library
- [ ] Authenticate and list notebooks
- [ ] Read notes and extract title/body/tags
- [ ] Parse note content (ENML → HTML/Markdown)
- [ ] Parse and catalog note links + backlinks

---

### ✍️ Phase 5: Write Support
- [ ] Create new notes with tags + links
- [ ] Update existing notes
- [ ] (Optional) Attach images or files
- [ ] Ensure idempotency/safety

---

### 🧠 Phase 6: Memory Graph / Automation Layer _(future goal)_
- [ ] Cross-reference notes by tag and backlink
- [ ] Auto-generate project dashboards or index notes
- [ ] Trigger note creation or editing from terminal scripts

---

## 📌 Miscellaneous Details

- Platform: macOS (Apple M2)
- Python: 3.13.5, managed via Homebrew
- Environment: `~/venvs/VS_Code`
- Editor: Visual Studio Code (with GitHub Copilot)
- Shell: Bash, configured with long history, custom PS1, etc.
- GitHub repo(s): Bash profile in version control, Evernote API repo coming next

---

## 🤖 Notes for Copilot or Claude Use
- You may suggest architectural improvements
- Prioritize composability and readability
- I prefer CLI-friendly utilities and Jupyter for prototyping
- Please annotate generated code clearly
