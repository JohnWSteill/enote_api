"""
Test stubs for the Corpus class.

These tests define the expected behavior of the Corpus API
and will be implemented as we develop the SDK integration.
"""

import pytest
import enote


class TestCorpusInit:
    """Test Corpus initialization and basic setup."""

    @pytest.mark.parametrize(
        "credentials",
        [
            {"dev_token": "fake_token", "sandbox": True},
            {"api_key": "test_key"},
            {"oauth_token": "oauth123", "sandbox": False},
        ],
    )
    def test_corpus_init_stores_credentials(self, credentials):
        """Test that Corpus initializes and stores credential formats."""
        corpus = enote.Corpus(credentials)
        assert corpus.credentials == credentials
        assert corpus._client is None  # Not initialized until SDK chosen


class TestCorpusReadOperations:
    """Test reading notes from Evernote."""

    @pytest.fixture
    def mock_corpus(self):
        """Create a Corpus instance for testing."""
        return enote.Corpus({"dev_token": "fake_token"})

    def test_get_all_notes_not_implemented(self, mock_corpus):
        """Test that get_all_notes raises NotImplementedError."""
        with pytest.raises(
            NotImplementedError, match="SDK implementation required"
        ):
            mock_corpus.get_all_notes()

    def test_get_note_not_implemented(self, mock_corpus):
        """Test that get_note raises NotImplementedError."""
        with pytest.raises(
            NotImplementedError, match="SDK implementation required"
        ):
            mock_corpus.get_note("fake_id")

    # Future test when implemented
    @pytest.mark.skip("TODO: Implement when SDK is chosen")
    def test_get_all_notes_returns_dict(self, mock_corpus):
        """Test that get_all_notes returns expected format."""
        # Will mock SDK response and test return format
        pass

    @pytest.mark.skip("TODO: Implement when SDK is chosen")
    def test_get_note_returns_note_dict(self, mock_corpus):
        """Test that get_note returns proper note structure."""
        # Will test: {title, body, tags, created, updated, links}
        pass

    @pytest.mark.skip("TODO: Implement when SDK is chosen")
    def test_get_note_nonexistent_returns_none(self, mock_corpus):
        """Test that get_note returns None for missing notes."""
        pass


class TestCorpusWriteOperations:
    """Test writing and updating notes."""

    @pytest.fixture
    def mock_corpus(self):
        """Create a Corpus instance for testing."""
        return enote.Corpus({"dev_token": "fake_token"})

    def test_write_new_note_not_implemented(self, mock_corpus):
        """Test that write_new_note raises NotImplementedError."""
        with pytest.raises(
            NotImplementedError, match="SDK implementation required"
        ):
            mock_corpus.write_new_note("Test Title", "Test content")

    def test_overwrite_note_not_implemented(self, mock_corpus):
        """Test that overwrite_note raises NotImplementedError."""
        with pytest.raises(
            NotImplementedError, match="SDK implementation required"
        ):
            mock_corpus.overwrite_note("fake_id", "New content")

    def test_delete_note_not_implemented(self, mock_corpus):
        """Test that delete_note raises NotImplementedError."""
        with pytest.raises(
            NotImplementedError, match="SDK implementation required"
        ):
            mock_corpus.delete_note("fake_id")

    # Future tests when implemented
    @pytest.mark.skip("TODO: Implement when SDK is chosen")
    def test_write_new_note_returns_id(self, mock_corpus):
        """Test that write_new_note returns note ID."""
        pass

    @pytest.mark.skip("TODO: Implement when SDK is chosen")
    def test_write_new_note_with_tags(self, mock_corpus):
        """Test creating note with tags."""
        pass

    @pytest.mark.skip("TODO: Implement when SDK is chosen")
    def test_overwrite_note_success(self, mock_corpus):
        """Test successful note update."""
        pass


class TestCorpusGraphOperations:
    """Test graph-like operations (future implementation)."""

    @pytest.fixture
    def mock_corpus(self):
        """Create a Corpus instance for testing."""
        return enote.Corpus({"dev_token": "fake_token"})

    def test_get_linked_notes_not_implemented(self, mock_corpus):
        """Test that get_linked_notes raises NotImplementedError."""
        with pytest.raises(NotImplementedError, match="Future implementation"):
            mock_corpus.get_linked_notes("fake_id")

    def test_get_backlinks_not_implemented(self, mock_corpus):
        """Test that get_backlinks raises NotImplementedError."""
        with pytest.raises(NotImplementedError, match="Future implementation"):
            mock_corpus.get_backlinks("fake_id")

    def test_query_not_implemented(self, mock_corpus):
        """Test that query raises NotImplementedError."""
        with pytest.raises(NotImplementedError, match="Future implementation"):
            mock_corpus.query("search text")


class TestCorpusIntegration:
    """Integration tests for complete workflows."""

    @pytest.mark.skip("TODO: Implement when SDK is chosen")
    def test_create_read_update_delete_workflow(self):
        """Test complete CRUD workflow."""
        # Will test: create note -> read it -> update it -> delete it
        pass

    @pytest.mark.skip("TODO: Implement when SDK is chosen")
    def test_tag_management_workflow(self):
        """Test tag operations across multiple notes."""
        pass
