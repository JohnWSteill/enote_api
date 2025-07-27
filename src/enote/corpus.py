"""
Corpus class for collections of Evernote notes, designed as a knowledge
management abstraction over note collections.
"""

from typing import Dict, List, Optional, Any
import logging
import xml.etree.ElementTree as ET
from pathlib import Path

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

        # Extract and store the ENEX path for later use
        self.enex_path = enex_config.get("enex_path", DEFAULT_ENEX_PATH)

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
        enex_path = Path(self.enex_path).expanduser()

        # Clear any existing notes
        self.notes = {}
        note_count = 0

        # Process each ENEX file in the directory
        for enex_file in enex_path.glob("*.enex"):
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
                        # Use a simple counter as note ID for now
                        note_id = f"note_{note_count:06d}"
                        self.notes[note_id] = note_data
                        note_count += 1

            except ET.ParseError as e:
                logger.warning(f"Failed to parse {enex_file}: {e}")
                continue

        logger.info(f"Loaded {len(self.notes)} notes into corpus")

    def _parse_note_element(self, note_elem) -> Optional[Dict[str, Any]]:
        """Parse a single note element from ENEX."""
        try:
            title = note_elem.find("title")
            title_text = title.text if title is not None else "Untitled"

            created = note_elem.find("created")
            created_text = created.text if created is not None else ""

            updated = note_elem.find("updated")
            updated_text = updated.text if updated is not None else ""

            # Extract tags
            tags = []
            for tag_elem in note_elem.findall("tag"):
                if tag_elem.text:
                    tags.append(tag_elem.text)

            # Extract content (simplified for now)
            content_elem = note_elem.find("content")
            content = content_elem.text if content_elem is not None else ""

            return {
                "title": title_text,
                "body": content,
                "tags": tags,
                "created": created_text,
                "updated": updated_text,
            }

        except Exception as e:
            logger.error(f"Error parsing note: {e}")
            return None

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
