"""
Evernote API Sandbox - Core Package

A robust Python module for Evernote API integration supporting:
- Reading notes (title, body, tags, links, backlinks)
- Writing/updating notes with Markdown/ENML support
- Tag management and internal note references
- Automation and cross-referencing capabilities

This package is designed to be SDK-agnostic, allowing for easy
swapping between different Evernote API implementations.
"""

from .corpus import Corpus
from .constants import DEFAULT_ENEX_PATH

__version__ = "0.1.0"
__author__ = "John Steill"

# Core module exports
__all__ = ["Corpus", "DEFAULT_ENEX_PATH"]
