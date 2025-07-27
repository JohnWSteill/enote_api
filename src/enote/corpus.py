"""
Corpus class for managing collections of Evernote notes.

This module provides the main interface for interacting with Evernote APIs,
designed as a knowledge management abstraction over note collections.
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

        # Extract notes with metadata
        note_dict = my_notes.read_notes(max_notes=100)
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
        logger.info(f"Initialized Corpus with ENEX path: {self.enex_path}")

    def read_notes(
        self, max_notes: Optional[int] = None
    ) -> Dict[str, Dict[str, Any]]:
        """
        Read and parse notes from ENEX files.

        Args:
            max_notes: Optional limit on number of notes to return
                      (useful for testing with large datasets)

        Returns:
            Dict mapping note_id -> {title, body, tags, metadata}

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

        notes = {}
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
                        return notes

                    # Extract note data
                    note_data = self._parse_note_element(note_elem)
                    if note_data:
                        # Use a simple counter as note ID for now
                        note_id = f"note_{note_count:06d}"
                        notes[note_id] = note_data
                        note_count += 1

            except ET.ParseError as e:
                logger.warning(f"Failed to parse {enex_file}: {e}")
                continue

        return notes

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

    def write_new_note(
        self,
        title: str,
        body: str,
        tags: Optional[List[str]] = None,
    ) -> str:
        """
        Create a new note.

        Args:
            title: Note title
            body: Note content (Markdown or ENML)
            tags: List of tag strings

        Returns:
            note_id: Unique identifier of created note
        """
        raise NotImplementedError("SDK implementation required")

    def overwrite_note(
        self, note_id: str, body: str, tags: Optional[List[str]] = None
    ) -> bool:
        """
        Replace the content of an existing note.

        Args:
            note_id: Note to update
            body: New content
            tags: New tags (None to keep existing)

        Returns:
            True if successful, False otherwise
        """
        raise NotImplementedError("SDK implementation required")

    def delete_note(self, note_id: str) -> bool:
        """
        Delete a note permanently.

        Args:
            note_id: Note to delete

        Returns:
            True if successful, False otherwise
        """
        raise NotImplementedError("SDK implementation required")

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
