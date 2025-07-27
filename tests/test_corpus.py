"""
Tests for the Corpus class - Evernote ENEX parsing and extraction.

These tests validate the ENEX parsing functionality that extracts
structured note data from Evernote exports for GenAI applications.
"""

import pytest
import enote


class TestCorpusInit:
    """Test Corpus initialization and ENEX directory validation."""

    def test_corpus_init_with_valid_enex_path(self):
        """Test that Corpus initializes with valid ENEX directory."""
        # Use the actual backup directory that exists
        corpus = enote.Corpus({"enex_path": enote.DEFAULT_ENEX_PATH})
        assert corpus.enex_path == enote.DEFAULT_ENEX_PATH

    def test_corpus_init_with_default_enex_path(self):
        """Test that Corpus uses default ENEX path when none provided."""
        corpus = enote.Corpus()
        assert corpus.enex_path == enote.DEFAULT_ENEX_PATH
        # The default path logic is now in __init__, not get_all_notes()

    def test_corpus_init_with_custom_enex_path(self):
        """Test that Corpus accepts custom ENEX directory paths."""
        custom_path = "/some/custom/path"
        corpus = enote.Corpus({"enex_path": custom_path})
        assert corpus.enex_path == custom_path

    @pytest.mark.parametrize(
        "config,expected_path",
        [
            ({"enex_path": enote.DEFAULT_ENEX_PATH}, enote.DEFAULT_ENEX_PATH),
            (
                {"enex_path": "/absolute/path/to/backup"},
                "/absolute/path/to/backup",
            ),
            ({"enex_path": "./relative/path"}, "./relative/path"),
            ({}, enote.DEFAULT_ENEX_PATH),  # Test empty config (uses default)
            (None, enote.DEFAULT_ENEX_PATH),  # Test None config (uses default)
        ],
    )
    def test_corpus_init_stores_enex_path(self, config, expected_path):
        """Test that Corpus initializes and stores the ENEX path correctly."""
        corpus = enote.Corpus(config)
        assert corpus.enex_path == expected_path


class TestCorpusReadOperations:
    """Test reading notes from ENEX files."""

    @pytest.fixture
    def corpus(self):
        """Create a Corpus instance for testing."""
        return enote.Corpus({"enex_path": enote.DEFAULT_ENEX_PATH})

    def test_read_notes_with_max_limit(self, corpus):
        """Test that read_notes respects max_notes parameter."""
        notes = corpus.read_notes(max_notes=5)
        assert isinstance(notes, dict)
        assert len(notes) <= 5

    # These tests validate expected data structure from ENEX parsing
    @pytest.mark.skip("TODO: Validate complete ENEX data structure")
    def test_read_notes_returns_expected_format(self, corpus):
        """Test that read_notes returns expected ENEX-parsed format."""
        # Will validate: {note_id: {title, body, tags, created, updated}}
        pass


class TestCorpusGraphOperations:
    """Test graph-like operations (future implementation)."""

    @pytest.fixture
    def corpus(self):
        """Create a Corpus instance for testing error handling."""
        return enote.Corpus()

    def test_get_linked_notes_not_implemented(self, corpus):
        """Test that get_linked_notes raises NotImplementedError."""
        with pytest.raises(NotImplementedError, match="Future implementation"):
            corpus.get_linked_notes("fake_id")

    def test_get_backlinks_not_implemented(self, corpus):
        """Test that get_backlinks raises NotImplementedError."""
        with pytest.raises(NotImplementedError, match="Future implementation"):
            corpus.get_backlinks("fake_id")

    def test_query_not_implemented(self, corpus):
        """Test that query raises NotImplementedError."""
        with pytest.raises(NotImplementedError, match="Future implementation"):
            corpus.query("search text")


class TestCorpusIntegration:
    """Integration tests for ENEX parsing workflows."""

    @pytest.mark.skip("TODO: Implement ENEX file validation")
    def test_enex_file_discovery_workflow(self):
        """Test complete ENEX discovery workflow."""
        # Will test: initialize corpus -> discover ENEX -> validate structure
        pass

    @pytest.mark.skip("TODO: Implement content extraction workflow")
    def test_content_extraction_workflow(self):
        """Test full content extraction across multiple ENEX files."""
        # Will test: parse all ENEX -> extract content -> validate metadata
        pass
