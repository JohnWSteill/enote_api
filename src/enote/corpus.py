"""
Corpus class for collections of Evernote notes, designed as a knowledge
management abstraction over note collections.
"""

from typing import Dict, List, Optional, Any
import logging
import xml.etree.ElementTree as ET
from pathlib import Path
import re

# Import the default path constant
from .constants import DEFAULT_ENEX_PATH

logger = logging.getLogger(__name__)


class Corpus:
    """
    A collection of Evernote notes extracted from ENEX files.

    Provides a clean interface for reading and extracting structured data
    from Evernote ENEX exports, designed for GenAI and knowledge management.

    Example:
        ```python
        import enote

        # Use default ENEX path
        my_notes = enote.Corpus()

        # Or specify custom path
        my_notes = enote.Corpus({"enex_path": "/path/to/backups"})

        # Load notes into the corpus
        my_notes.load(max_notes=100)

        # Access the loaded notes
        print(f"Loaded {len(my_notes.notes)} notes")
        ```
    """

    def __init__(self, enex_config: Optional[Dict[str, Any]] = None):
        """
        Initialize the Corpus with ENEX path configuration.

        Args:
            enex_config: Optional dictionary containing ENEX path configuration
                        Format: {"enex_path": "/path/to/enex/files"}
                        If None or enex_path missing, uses default path
        """
        if enex_config is None:
            enex_config = {}

        # Extract and store the ENEX path for later use (expanded)
        raw_path = enex_config.get("enex_path", DEFAULT_ENEX_PATH)
        self.enex_path = Path(raw_path).expanduser()

        # Initialize empty notes collection
        self.notes: Dict[str, Dict[str, Any]] = {}

        logger.info(f"Initialized Corpus with ENEX path: {self.enex_path}")

    def load(self, max_notes: Optional[int] = None) -> None:
        """
        Load and parse notes from ENEX files into the corpus.

        Args:
            max_notes: Optional limit on number of notes to load
                      (useful for testing with large datasets)

        Note:
            Populates self.notes with the parsed note data.
            Each note is stored as: note_id -> {title, body, tags, metadata}

        Example:
            {
                "note_123": {
                    "title": "Project Ideas",
                    "body": "...",
                    "tags": ["projects", "brainstorm"],
                    "created": datetime(...),
                    "updated": datetime(...)
                }
            }
        """
        # Use the ENEX path configured during initialization
        # Clear any existing notes
        self.notes = {}
        note_count = 0

        # Process each ENEX file in the directory
        for enex_file in self.enex_path.glob("*.enex"):
            logger.info(f"Processing {enex_file.name}")

            # Parse the ENEX file
            try:
                tree = ET.parse(enex_file)
                root = tree.getroot()

                # Find all note elements
                for note_elem in root.findall("note"):
                    if max_notes and note_count >= max_notes:
                        return

                    # Extract note data
                    note_data = self._parse_note_element(note_elem)
                    if note_data:
                        # Add cleaned text version for RAG
                        if 'content' in note_data:
                            cleaned = self._clean_enml(note_data['content'])
                            note_data['cleaned_text'] = cleaned
                        
                        # Use a simple counter as note ID for now
                        note_id = f"note_{note_count:06d}"
                        self.notes[note_id] = note_data
                        note_count += 1

            except ET.ParseError as e:
                logger.warning(f"Failed to parse {enex_file}: {e}")
                continue

        logger.info(f"Loaded {len(self.notes)} notes into corpus")

    def _parse_note_element(self, note_elem) -> Optional[Dict[str, Any]]:
        """Parse all available attributes from ENEX note element."""
        try:
            note_data = {}

            # Extract all child elements dynamically
            for child in note_elem:
                element_name = child.tag

                # Handle multiple elements with same tag (like <tag> elements)
                if element_name in note_data:
                    # Convert to list if not already
                    if not isinstance(note_data[element_name], list):
                        note_data[element_name] = [note_data[element_name]]
                    note_data[element_name].append(child.text or "")
                else:
                    # First occurrence of this element
                    note_data[element_name] = child.text or ""

            # Ensure we have at least a title (fallback for malformed notes)
            if "title" not in note_data:
                note_data["title"] = "Untitled"

            return note_data

        except Exception as e:
            logger.error(f"Error parsing note: {e}")
            return None

    def _clean_enml(self, enml_content: str) -> str:
        """
        Clean ENML content for RAG-ready text extraction.
        
        Removes XML overhead while preserving semantic structure.
        
        Args:
            enml_content: Raw ENML content from Evernote export
            
        Returns:
            Clean text suitable for embeddings and RAG systems
        """
        if not enml_content or not enml_content.strip():
            return ""
            
        try:
            # Remove XML declaration and DOCTYPE
            content = re.sub(r'<\?xml[^>]*\?>', '', enml_content)
            content = re.sub(r'<!DOCTYPE[^>]*>', '', content)
            
            # Remove en-note wrapper
            content = re.sub(r'</?en-note[^>]*>', '', content)
            
            # Convert structural elements to readable text
            # Lists: preserve structure with bullets/numbers
            content = re.sub(r'<ul[^>]*>', '', content)
            content = re.sub(r'</ul>', '\n', content)
            content = re.sub(r'<ol[^>]*>', '', content)
            content = re.sub(r'</ol>', '\n', content)
            content = re.sub(r'<li[^>]*>', '• ', content)
            content = re.sub(r'</li>', '\n', content)
            
            # Paragraphs and line breaks
            content = re.sub(r'<div[^>]*>', '\n', content)
            content = re.sub(r'</div>', '', content)
            content = re.sub(r'<br[^>]*/?>', '\n', content)
            content = re.sub(r'<p[^>]*>', '\n', content)
            content = re.sub(r'</p>', '\n', content)
            
            # Preserve emphasis (convert to markdown-style)
            content = re.sub(r'<b[^>]*>(.*?)</b>', r'**\1**', content)
            content = re.sub(r'<i[^>]*>(.*?)</i>', r'*\1*', content)
            strong_pattern = r'<strong[^>]*>(.*?)</strong>'
            content = re.sub(strong_pattern, r'**\1**', content)
            content = re.sub(r'<em[^>]*>(.*?)</em>', r'*\1*', content)
            
            # Links: extract just the text (URLs are often broken anyway)
            content = re.sub(r'<a[^>]*>(.*?)</a>', r'\1', content)
            
            # Remove all other HTML/XML tags
            content = re.sub(r'<[^>]+>', '', content)
            
            # Decode HTML entities
            content = content.replace('&lt;', '<')
            content = content.replace('&gt;', '>')
            content = content.replace('&amp;', '&')
            content = content.replace('&quot;', '"')
            content = content.replace('&#39;', "'")
            
            # Clean up whitespace
            # Max 2 newlines
            content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)
            content = re.sub(r'[ \t]+', ' ', content)  # Normalize spaces
            content = content.strip()
            
            return content
            
        except Exception as e:
            logger.warning(f"Failed to clean ENML content: {e}")
            # Fallback: at least strip basic tags
            fallback = re.sub(r'<[^>]+>', '', enml_content)
            return fallback.strip()

    # Future methods for graph operations
    def get_linked_notes(self, note_id: str) -> List[str]:
        """Get note IDs that this note links to (outbound edges)."""
        raise NotImplementedError("Future implementation")

    def get_backlinks(self, note_id: str) -> List[str]:
        """Get note IDs that link to this note (inbound edges)."""
        raise NotImplementedError("Future implementation")

    def query(self, search_text: str) -> Dict[str, Dict[str, Any]]:
        """Search notes by content (future implementation)."""
        raise NotImplementedError("Future implementation")
