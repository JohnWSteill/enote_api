"""
Basic tests to verify project structure and imports.

These tests ensure the core package is properly configured
and can be imported without errors.
"""


def test_project_structure(project_root):
    """Test that all required directories and files exist."""
    assert (project_root / "src").exists()
    assert (project_root / "tests").exists()
    assert (project_root / "notebooks").exists()
    assert (project_root / "requirements.txt").exists()
    assert (project_root / "README.md").exists()


def test_version_defined():
    """Test that package version is defined."""
    # Import path is automatically set up by conftest.py
    import enote

    assert hasattr(enote, "__version__")
    assert isinstance(enote.__version__, str)
    assert len(enote.__version__) > 0
