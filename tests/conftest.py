"""
Test configuration and fixtures for the Evernote API Sandbox.

This module sets up common test fixtures and configuration
that can be shared across all test modules.
"""

import pytest
import sys
from pathlib import Path


@pytest.fixture(autouse=True)
def setup_import_path():
    """Automatically add src to Python path for all tests."""
    src_path = Path(__file__).parent.parent / "src"
    if str(src_path) not in sys.path:
        sys.path.insert(0, str(src_path))


@pytest.fixture
def project_root():
    """Return the project root directory."""
    return Path(__file__).parent.parent


@pytest.fixture
def sample_enml():
    """Return sample ENML content for testing."""
    return """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE en-note SYSTEM "http://xml.evernote.com/pub/enml2.dtd">
<en-note>
    <div>This is a test note with <b>bold</b> text.</div>
    <div><br/></div>
    <div>And a <a href="https://example.com">link</a>.</div>
</en-note>"""


@pytest.fixture
def sample_markdown():
    """Return sample Markdown content for testing."""
    return """# Test Note

This is a test note with **bold** text.

And a [link](https://example.com)."""
