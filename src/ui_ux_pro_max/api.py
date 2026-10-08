"""
UI/UX Pro Max - High-Level Python API
Provides typed, elegant, and pythonic interfaces for UI/UX reasoning,
design system generation, and multi-domain style retrieval.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Union

try:
    from .core import (
        AVAILABLE_STACKS,
        CSV_CONFIG,
        DATA_DIR,
        STACK_CONFIG,
        search as _core_search,
        search_stack as _core_search_stack,
    )
    from .design_system import generate_design_system as _core_generate_design_system
except ImportError:
    from core import (
        AVAILABLE_STACKS,
        CSV_CONFIG,
        DATA_DIR,
        STACK_CONFIG,
        search as _core_search,
        search_stack as _core_search_stack,
    )
    from design_system import generate_design_system as _core_generate_design_system


@dataclass
class SearchResult:
    """Represents the results of a domain or stack search."""
    domain: str
    query: str
    count: int
    items: List[Dict[str, Any]]
    stack: Optional[str] = None
    suggestions: List[str] = field(default_factory=list)
    raw: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "domain": self.domain,
            "query": self.query,
            "count": self.count,
            "items": self.items,
            "stack": self.stack,
            "suggestions": self.suggestions,
        }

    def to_json(self, indent: int = 2) -> str:
        return json.dumps(self.to_dict(), indent=indent, ensure_ascii=False)


@dataclass
class DesignSystemResult:
    """Rich structured result of a design system generation query."""
    project_name: str
    category: str
    style_name: str
    style_category: str
    pattern_name: str
    primary_color: str
    colors: Dict[str, str]
    typography: Dict[str, Any]
    anti_patterns: List[str]
    pre_delivery_checklist: List[str]
    key_effects: List[str]
    spacing_scale: Dict[str, str]
    raw_text: str
    raw: Dict[str, Any]
    persistence: Optional[Dict[str, Any]] = None
    stack_guidelines: List[Dict[str, Any]] = field(default_factory=list)

    def to_markdown(self) -> str:
        """Returns the full formatted design system specification."""
        return self.raw_text

    def to_dict(self) -> Dict[str, Any]:
        """Returns structured dictionary representing the design system."""
        return {
            "project_name": self.project_name,
            "category": self.category,
            "style": {
                "name": self.style_name,
                "category": self.style_category,
            },
            "pattern": self.pattern_name,
            "colors": self.colors,
            "typography": self.typography,
            "anti_patterns": self.anti_patterns,
            "pre_delivery_checklist": self.pre_delivery_checklist,
            "key_effects": self.key_effects,
            "spacing_scale": self.spacing_scale,
            "persistence": self.persistence,
        }

    def to_json(self, indent: int = 2) -> str:
        """Returns JSON serialized design system."""
        return json.dumps(self.to_dict(), indent=indent, ensure_ascii=False)

    def to_css_variables(self) -> str:
        """Generates standard CSS custom properties (:root block) from colors and spacing."""
        lines = [":root {", "  /* Semantic Colors */"]
        for name, value in self.colors.items():
            if name == "notes" or not str(value).startswith("#"):
                continue
            var_name = name.lower().replace("/", "-").replace(" ", "-").replace("_", "-")
            lines.append(f"  --color-{var_name}: {value};")

        if self.spacing_scale:
            lines.append("\n  /* Spacing Scale */")
            for size, val in self.spacing_scale.items():
                lines.append(f"  --spacing-{size}: {val};")

        lines.append("}")
        return "\n".join(lines)

    def to_tailwind_theme(self) -> Dict[str, Any]:
        """Generates a Tailwind CSS v3/v4 color theme extension dictionary."""
        theme_colors: Dict[str, str] = {}
        for name, value in self.colors.items():
            if name == "notes" or not str(value).startswith("#"):
                continue
            key = name.lower().replace("/", "-").replace(" ", "-").replace("_", "-")
            theme_colors[key] = value
        return {
            "theme": {
                "extend": {
                    "colors": theme_colors,
                    "spacing": self.spacing_scale or {},
                }
            }
        }


def get_design_system(
    query: str,
    project_name: Optional[str] = None,
    stack: Optional[str] = None,
    variance: Optional[int] = None,
    motion: Optional[int] = None,
    density: Optional[int] = None,
    page: Optional[str] = None,
    format: str = "markdown",
    persist: bool = False,
    output_dir: Optional[str] = None,
    force: bool = False,
) -> DesignSystemResult:
    """
    Generate a complete, cohesive design system recommendation based on a query.

    Args:
        query: Description of product or interface (e.g. 'Fintech mobile banking', 'Luxury spa booking')
        project_name: Display name of project (defaults to query title)
        stack: Target frontend framework (e.g. 'react', 'nextjs', 'tailwind', 'flutter', 'wpf')
        variance: Design variance dial 1-10 (1=minimal/symmetric, 10=bold/asymmetric)
        motion: Motion intensity dial 1-10 (1=subtle, 10=complex GSAP)
        density: Visual density dial 1-10 (1=spacious, 10=dense dashboard)
        page: Optional specific page override to generate
        format: Output text format ('markdown' or 'ascii')
        persist: Save to design-system/<project>/MASTER.md
        output_dir: Output directory when persisting
        force: Overwrite existing MASTER.md if True

    Returns:
        DesignSystemResult instance with both formatted text and structured attributes.
    """
    raw_res = _core_generate_design_system(
        query=query,
        project_name=project_name,
        output_format=format,
        persist=persist,
        page=page,
        output_dir=output_dir,
        force=force,
        variance=variance,
        motion=motion,
        density=density,
    )

    stack_guidelines: List[Dict[str, Any]] = []
    if stack:
        stack_res = _core_search_stack(query=query, stack=stack, max_results=5)
        stack_guidelines = stack_res.get("results", [])

    ds = raw_res.get("design_system", {})
    style = ds.get("style", {})
    pattern = ds.get("pattern", {})
    colors_raw = ds.get("colors", {})
    typography = ds.get("typography", {})

    # Extract semantic color mapping
    colors_dict: Dict[str, str] = {}
    if isinstance(colors_raw, dict):
        for k, v in colors_raw.items():
            if isinstance(v, str) and v.startswith("#"):
                colors_dict[k] = v
            elif k == "notes" and isinstance(v, str):
                colors_dict["notes"] = v

    # Extract anti-patterns (Avoid items)
    anti_patterns = ds.get("anti_patterns", [])
    if isinstance(anti_patterns, str):
        anti_patterns = [p.strip() for p in anti_patterns.split("+") if p.strip()]

    # Extract checklist
    checklist = [
        "No emojis as icons (use SVG: Lucide / Phosphor)",
        "cursor-pointer on all clickable interactive elements",
        "Hover states with smooth transitions (150-300ms)",
        "Light/Dark mode: text contrast 4.5:1 minimum (WCAG AA)",
        "Visible focus rings for keyboard navigation",
        "prefers-reduced-motion respected for all animations",
        "Responsive breakpoints: 375px, 768px, 1024px, 1440px",
    ]

    return DesignSystemResult(
        project_name=ds.get("project_name", query),
        category=ds.get("category", ""),
        style_name=style.get("Style ID", "") or style.get("name", "Modern Clean"),
        style_category=style.get("Style Category", ""),
        pattern_name=pattern.get("Pattern Name", "") or pattern.get("name", "Standard Layout"),
        primary_color=colors_dict.get("Primary", "#3B82F6"),
        colors=colors_dict,
        typography=typography,
        anti_patterns=anti_patterns,
        pre_delivery_checklist=checklist,
        key_effects=ds.get("key_effects", []),
        spacing_scale=ds.get("spacing_scale", {}),
        raw_text=raw_res.get("text", ""),
        raw=raw_res,
        persistence=raw_res.get("persistence"),
        stack_guidelines=stack_guidelines,
    )


def search(
    query: str,
    domain: Optional[str] = None,
    stack: Optional[str] = None,
    max_results: int = 3,
) -> SearchResult:
    """
    Search the UI/UX Pro Max knowledge base across any domain or framework stack.
    """
    if stack:
        raw = _core_search_stack(query=query, stack=stack, max_results=max_results)
        return SearchResult(
            domain="stack",
            query=query,
            count=raw.get("count", 0),
            items=raw.get("results", []),
            stack=stack,
            suggestions=raw.get("suggestions", []),
            raw=raw,
        )

    raw = _core_search(query=query, domain=domain, max_results=max_results)
    return SearchResult(
        domain=raw.get("domain", domain or "auto"),
        query=query,
        count=raw.get("count", 0),
        items=raw.get("results", []),
        raw=raw,
    )


def search_styles(query: str, max_results: int = 3) -> SearchResult:
    """Search design styles (e.g. 'minimalism', 'glassmorphism', 'bento grid')."""
    return search(query, domain="style", max_results=max_results)


def search_colors(query: str, max_results: int = 3) -> SearchResult:
    """Search color palettes for industries/products (e.g. 'fintech', 'healthcare', 'crypto')."""
    return search(query, domain="color", max_results=max_results)


def search_typography(query: str, max_results: int = 3) -> SearchResult:
    """Search font pairings and mood typography (e.g. 'luxury', 'editorial', 'tech')."""
    return search(query, domain="typography", max_results=max_results)


def search_landing(query: str, max_results: int = 3) -> SearchResult:
    """Search landing page high-converting section patterns."""
    return search(query, domain="landing", max_results=max_results)


def search_ux(query: str, max_results: int = 3) -> SearchResult:
    """Search UX guidelines, common antipatterns and solutions."""
    return search(query, domain="ux", max_results=max_results)


def search_icons(query: str, max_results: int = 5) -> SearchResult:
    """Search curated icon names and import code."""
    return search(query, domain="icons", max_results=max_results)


def search_charts(query: str, max_results: int = 3) -> SearchResult:
    """Search chart types and data visualization guidelines."""
    return search(query, domain="chart", max_results=max_results)


def search_google_fonts(query: str, max_results: int = 5) -> SearchResult:
    """Search Google Fonts library and licenses."""
    return search(query, domain="google-fonts", max_results=max_results)


def search_stack(
    stack: str,
    query: str = "",
    max_results: int = 5,
) -> SearchResult:
    """
    Search framework-specific UI best practices.
    Available stacks: react, nextjs, vue, svelte, astro, swiftui, react-native,
    flutter, nuxtjs, nuxt-ui, html-tailwind, shadcn, jetpack-compose, threejs,
    angular, laravel, javafx, wpf, winui, avalonia, uno, uwp.
    """
    return search(query=query, stack=stack, max_results=max_results)


def list_stacks() -> List[str]:
    """Return all 22 supported UI framework stacks."""
    return list(AVAILABLE_STACKS)


def list_styles() -> List[Dict[str, Any]]:
    """Return all cataloged design styles from styles.csv."""
    styles_file = DATA_DIR / "styles.csv"
    if not styles_file.exists():
        return []
    import csv
    with open(styles_file, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)
