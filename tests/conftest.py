"""
Test configuration and fixtures for the Evernote API Sandbox.

This module sets up common test fixtures and configuration
that can be shared across all test modules.
"""

import pytest
import sys
from pathlib import Path

# Set up import path at module level so imports work
src_path = Path(__file__).parent.parent / "src"
if str(src_path) not in sys.path:
    sys.path.insert(0, str(src_path))


@pytest.fixture
def project_root():
    """Return the project root directory."""
    return Path(__file__).parent.parent
