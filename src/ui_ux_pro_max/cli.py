"""
UI/UX Pro Max - Unified Command Line Interface
"""

from __future__ import annotations

import argparse
import io
import json
import sys

# Ensure UTF-8 output on Windows consoles
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
if sys.stderr.encoding and sys.stderr.encoding.lower() != "utf-8":
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")

from .api import (
    get_design_system,
    list_stacks,
    search,
    search_colors,
    search_styles,
    search_typography,
)
from .core import AVAILABLE_STACKS

__version__ = "2.6.0"


def print_banner():
    banner = """
╔═══════════════════════════════════════════════════════════════════════════╗
║                      UI/UX PRO MAX - DESIGN ENGINE                        ║
║                 Intelligence Engine for AI Agents & Devs                  ║
╚═══════════════════════════════════════════════════════════════════════════╝
"""
    print(banner.strip())


def main():
    # Auto-route bare queries to "design" sub-command
    KNOWN_COMMANDS = {
        "stacks", "styles", "checklist", "palette", "font", "search", "design",
        "--version", "-v", "--help", "-h"
    }
    if len(sys.argv) > 1 and sys.argv[1] not in KNOWN_COMMANDS and not sys.argv[1].startswith("-"):
        sys.argv.insert(1, "design")

    parser = argparse.ArgumentParser(
        prog="uipro",
        description="UI/UX Pro Max - Design Intelligence Engine & Style Generator",
    )
    parser.add_argument(
        "--version", "-v",
        action="version",
        version=f"%(prog)s {__version__}",
    )

    subparsers = parser.add_subparsers(dest="subcommand", help="Sub-commands")

    # Command: stacks
    subparsers.add_parser("stacks", help="List all 22 supported UI framework stacks")

    # Command: styles
    subparsers.add_parser("styles", help="List all cataloged UI design styles")

    # Command: checklist
    subparsers.add_parser("checklist", help="Print WCAG & UI Pre-delivery QA Checklist")

    # Command: palette
    palette_parser = subparsers.add_parser("palette", help="Search industry color palettes")
    palette_parser.add_argument("target", help="Industry or vibe (e.g. 'fintech', 'wellness', 'cyberpunk')")
    palette_parser.add_argument("--json", action="store_true", help="Output as JSON")

    # Command: font
    font_parser = subparsers.add_parser("font", help="Search Google Font pairings")
    font_parser.add_argument("target", help="Style or mood (e.g. 'luxury', 'modern saas', 'editorial')")
    font_parser.add_argument("--json", action="store_true", help="Output as JSON")

    # Command: search
    search_parser = subparsers.add_parser("search", help="Search design knowledge base")
    search_parser.add_argument("target", help="Search keywords")
    search_parser.add_argument(
        "--domain", "-d",
        choices=["style", "color", "chart", "landing", "product", "ux", "typography", "icons", "gsap", "react", "web", "google-fonts"],
        help="Search specific domain",
    )
    search_parser.add_argument(
        "--stack", "-s",
        choices=AVAILABLE_STACKS,
        help="Search specific framework stack",
    )
    search_parser.add_argument("--max-results", "-n", type=int, default=3, help="Max results (default: 3)")
    search_parser.add_argument("--json", action="store_true", help="Output as JSON")

    # Command: design (or bare query)
    design_parser = subparsers.add_parser("design", help="Generate full design system recommendation")
    design_parser.add_argument("query", help="Product or UI prompt (e.g. 'SaaS Analytics Dashboard')")
    design_parser.add_argument("--stack", "-s", choices=AVAILABLE_STACKS, help="Target framework stack")
    design_parser.add_argument("--project-name", "-p", help="Custom project title")
    design_parser.add_argument("--format", "-f", choices=["markdown", "ascii"], default="markdown", help="Output format")
    design_parser.add_argument("--persist", action="store_true", help="Save MASTER.md to design-system/")
    design_parser.add_argument("--page", help="Specific page override file to generate")
    design_parser.add_argument("--output-dir", "-o", help="Root directory for saving files")
    design_parser.add_argument("--variance", type=int, choices=range(1, 11), help="Design variance dial (1-10)")
    design_parser.add_argument("--motion", type=int, choices=range(1, 11), help="Motion intensity dial (1-10)")
    design_parser.add_argument("--density", type=int, choices=range(1, 11), help="Visual density dial (1-10)")
    design_parser.add_argument("--json", action="store_true", help="Output result as JSON")
    design_parser.add_argument("--css", action="store_true", help="Output generated CSS variables")

    args = parser.parse_args()

    # Handle subcommands
    if args.subcommand == "stacks":
        print_banner()
        print("\n📦 SUPPORTED FRAMEWORK STACKS (22):")
        for i, s in enumerate(list_stacks(), 1):
            print(f"  {i:2d}. {s}")
        return

    if args.subcommand == "styles":
        print_banner()
        res = search_styles("", max_results=100)
        print(f"\n🎨 CATALOGED DESIGN STYLES ({res.count}):")
        for item in res.items:
            style_id = item.get("Style ID", "Unknown")
            cat = item.get("Style Category", "")
            mode = item.get("Preferred Mode", "Both")
            print(f"  • {style_id:25s} [{cat}] (Mode: {mode})")
        return

    if args.subcommand == "checklist":
        print_banner()
        checklist = [
            "[ ] No emojis as icons (use SVG: Lucide / Phosphor / Heroicons)",
            "[ ] cursor-pointer explicitly set on all clickable elements",
            "[ ] Smooth hover & focus transitions (150-300ms)",
            "[ ] Text contrast minimum 4.5:1 (WCAG AA) on all backgrounds",
            "[ ] Visible keyboard focus rings (focus-visible / outline)",
            "[ ] Respect prefers-reduced-motion CSS media query",
            "[ ] Responsive layout tested at 375px, 768px, 1024px, 1440px",
            "[ ] No generic dark-purple gradient for non-crypto/non-gaming apps",
            "[ ] Semantic HTML (header, main, nav, section, footer, button)",
        ]
        print("\n✅ PRE-DELIVERY QUALITY CHECKLIST:")
        for item in checklist:
            print(f"  {item}")
        return

    if args.subcommand == "palette":
        res = search_colors(args.target)
        if args.json:
            print(res.to_json())
        else:
            print_banner()
            print(f"\n🎨 COLOR PALETTE RECOMMENDATION FOR: '{args.target}'\n")
            for item in res.items:
                for k, v in item.items():
                    if v:
                        print(f"  {k:20s}: {v}")
                print("  " + "-" * 50)
        return

    if args.subcommand == "font":
        res = search_typography(args.target)
        if args.json:
            print(res.to_json())
        else:
            print_banner()
            print(f"\n🔤 TYPOGRAPHY PAIRINGS FOR: '{args.target}'\n")
            for item in res.items:
                name = item.get("Font Pairing Name", "")
                head = item.get("Heading Font", "")
                body = item.get("Body Font", "")
                url = item.get("Google Fonts URL", "")
                print(f"  • {name} -> Heading: {head} | Body: {body}")
                if url:
                    print(f"    Google Fonts: {url}")
                print()
        return

    if args.subcommand == "search":
        res = search(
            query=args.target,
            domain=args.domain,
            stack=args.stack,
            max_results=args.max_results,
        )
        if args.json:
            print(res.to_json())
        else:
            print_banner()
            print(f"\n🔍 SEARCH RESULTS ({res.count} items) for '{args.target}' in domain '{res.domain}':\n")
            for i, item in enumerate(res.items, 1):
                print(f"[{i}] " + " | ".join(f"{k}: {v}" for k, v in list(item.items())[:3]))
                for k, v in list(item.items())[3:]:
                    if v and len(str(v).strip()) > 0:
                        print(f"    {k}: {v}")
                print()
        return

    if args.subcommand == "design":
        ds_res = get_design_system(
            query=args.query,
            project_name=args.project_name,
            stack=args.stack,
            variance=args.variance,
            motion=args.motion,
            density=args.density,
            page=args.page,
            format=args.format,
            persist=args.persist,
            output_dir=args.output_dir,
        )

        if args.json:
            print(ds_res.to_json())
        elif args.css:
            print(ds_res.to_css_variables())
        else:
            print(ds_res.to_markdown())
        return

    parser.print_help()


if __name__ == "__main__":
    main()
