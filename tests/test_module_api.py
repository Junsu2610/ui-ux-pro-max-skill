"""
Tests for ui_ux_pro_max Python package API and CLI
"""

import unittest
from ui_ux_pro_max import (
    __version__,
    get_design_system,
    list_stacks,
    list_styles,
    search,
    search_colors,
    search_stack,
    search_styles,
    search_typography,
)
from ui_ux_pro_max.api import DesignSystemResult, SearchResult


class TestModuleAPI(unittest.TestCase):
    def test_version_present(self):
        self.assertTrue(len(__version__) > 0)
        self.assertEqual(__version__, "2.6.0")

    def test_list_stacks(self):
        stacks = list_stacks()
        self.assertGreaterEqual(len(stacks), 20)
        self.assertIn("react", stacks)
        self.assertIn("html-tailwind", stacks)
        self.assertIn("wpf", stacks)

    def test_list_styles(self):
        styles = list_styles()
        self.assertGreater(len(styles), 10)

    def test_search_styles(self):
        res = search_styles("minimalism", max_results=2)
        self.assertIsInstance(res, SearchResult)
        self.assertGreater(res.count, 0)
        self.assertEqual(res.domain, "style")

    def test_search_colors(self):
        res = search_colors("fintech", max_results=1)
        self.assertIsInstance(res, SearchResult)
        self.assertGreater(res.count, 0)
        self.assertEqual(res.domain, "color")

    def test_search_typography(self):
        res = search_typography("luxury", max_results=2)
        self.assertIsInstance(res, SearchResult)
        self.assertGreater(res.count, 0)
        self.assertEqual(res.domain, "typography")

    def test_search_stack(self):
        res = search_stack(stack="react", query="hooks", max_results=3)
        self.assertIsInstance(res, SearchResult)
        self.assertEqual(res.stack, "react")
        self.assertGreater(res.count, 0)

    def test_get_design_system_structure(self):
        ds = get_design_system("Luxury spa booking", stack="react")
        self.assertIsInstance(ds, DesignSystemResult)
        self.assertTrue(len(ds.style_name) > 0)
        self.assertTrue(len(ds.primary_color) > 0)
        self.assertIsInstance(ds.colors, dict)
        self.assertIsInstance(ds.anti_patterns, list)
        self.assertIsInstance(ds.pre_delivery_checklist, list)
        self.assertGreater(len(ds.pre_delivery_checklist), 0)

        # Check export methods
        css = ds.to_css_variables()
        self.assertIn(":root", css)
        self.assertIn("--color-primary", css)

        theme = ds.to_tailwind_theme()
        self.assertIn("theme", theme)
        self.assertIn("extend", theme["theme"])

        markdown = ds.to_markdown()
        self.assertIn("Design System", markdown)

        d = ds.to_dict()
        self.assertIn("colors", d)
        self.assertIn("style", d)


if __name__ == "__main__":
    unittest.main()
