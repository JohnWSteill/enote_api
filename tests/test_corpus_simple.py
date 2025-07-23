"""Simple test to verify Corpus can be imported."""

import enote


def test_corpus_can_be_imported():
    """Test that we can import and create a Corpus."""
    corpus = enote.Corpus({"test": "credentials"})
    assert corpus is not None
    assert hasattr(corpus, "get_all_notes")
