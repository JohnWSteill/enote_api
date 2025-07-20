"""
Basic tests to verify project structure and imports.

These tests ensure the core package is properly configured
and can be imported without errors.
"""

import sys
from pathlib import Path


def test_project_structure(project_root):
    """Test that all required directories and files exist."""
    assert (project_root / "src").exists()
    assert (project_root / "tests").exists()
    assert (project_root / "notebooks").exists()
    assert (project_root / "requirements.txt").exists()
    assert (project_root / "README.md").exists()


def test_src_package_import():
    """Test that the src package can be imported."""
    # Add src to Python path for testing
    src_path = Path(__file__).parent.parent / "src"
    if str(src_path) not in sys.path:
        sys.path.insert(0, str(src_path))
    
    # This should not raise an ImportError
    import evernote_api  # noqa: F401


def test_version_defined():
    """Test that package version is defined."""
    src_path = Path(__file__).parent.parent / "src"
    if str(src_path) not in sys.path:
        sys.path.insert(0, str(src_path))
    
    import evernote_api
    assert hasattr(evernote_api, '__version__')
    assert isinstance(evernote_api.__version__, str)
    assert len(evernote_api.__version__) > 0
