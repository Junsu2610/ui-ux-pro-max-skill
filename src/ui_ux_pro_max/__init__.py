"""
UI/UX Pro Max - Design Intelligence Engine for AI Coding Agents and Developers
"""

from .api import (
    DesignSystemResult,
    SearchResult,
    get_design_system,
    list_stacks,
    list_styles,
    search,
    search_charts,
    search_colors,
    search_google_fonts,
    search_icons,
    search_landing,
    search_stack,
    search_styles,
    search_typography,
    search_ux,
)
from .core import AVAILABLE_STACKS, CSV_CONFIG, DATA_DIR, STACK_CONFIG, BM25
from .design_system import generate_design_system, persist_design_system

__version__ = "2.6.0"
__all__ = [
    "DesignSystemResult",
    "SearchResult",
    "get_design_system",
    "generate_design_system",
    "persist_design_system",
    "search",
    "search_styles",
    "search_colors",
    "search_typography",
    "search_landing",
    "search_ux",
    "search_icons",
    "search_charts",
    "search_stack",
    "search_google_fonts",
    "list_stacks",
    "list_styles",
    "BM25",
    "CSV_CONFIG",
    "STACK_CONFIG",
    "AVAILABLE_STACKS",
    "DATA_DIR",
]
