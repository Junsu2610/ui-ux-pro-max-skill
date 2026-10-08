---
name: ui-ux-pro-max
description: >-
  High-throughput UI/UX design intelligence engine and style recommendation system.
  Provides searchable local knowledge base containing 88 design styles, 192 product
  color palettes, 74 typography pairings, 119 UX guidelines, 105 curated icons,
  and 22 frontend framework stacks (React, Next.js, Vue, Tailwind, SwiftUI, Flutter,
  WPF, Avalonia, Three.js, etc.). Use whenever designing, prototyping, reviewing,
  or fixing interfaces to cure generic AI dark-purple gradients and enforce WCAG AA.
---

# UI/UX Pro Max — Design Intelligence Skill

Expert design system generator and UI/UX reasoning engine. Prevents generic AI design patterns (dark mode default, generic purple-pink gradients, oversized border radii) by selecting domain-specific styles, WCAG AA compliant colors, accessible typography pairings, and framework-specific best practices.

---

## 🚀 Quick Execution via Python or CLI

### 1. Generate Complete Design System
```bash
# Via global CLI
uipro "Luxury spa booking" --stack react

# Via Python module
python -m ui_ux_pro_max "Fintech banking dashboard" --stack nextjs
```

### 2. Search Specific Design Domains
```bash
# Search industry palettes
uipro palette "fintech"
uipro palette "healthcare"

# Search typography pairings
uipro font "luxury"
uipro font "editorial"

# Search design styles
uipro search "minimalism" -d style

# Framework stack best practices
uipro search "hooks" -s react
uipro search "animation" -s flutter
```

### 3. Pre-Delivery Quality Checklist
```bash
uipro checklist
```

---

## 🐍 Python Library Usage

Any Python script or agent in the workspace can import and use `ui_ux_pro_max` directly:

```python
from ui_ux_pro_max import get_design_system, search_colors, search_styles

# 1. Generate full design system
ds = get_design_system("Luxury spa booking", stack="react")
print("Style:", ds.style_name)
print("Primary color:", ds.primary_color)
print("Avoid:", ds.anti_patterns)

# 2. Export design tokens
css_vars = ds.to_css_variables()
tailwind_config = ds.to_tailwind_theme()
markdown_spec = ds.to_markdown()

# 3. Search palettes
palettes = search_colors("cyberpunk")
for item in palettes.items:
    print(item["Product Type"], item["Primary"], item["Accent"])
```

---

## 🛡️ Anti-Patterns & Quality Rules (Do NOTs)

- **CẤM tím gradient mặc định**: Không áp dụng dark-mode tím/hồng cho sản phẩm ngân hàng, y tế, giáo dục, hoặc thương mại điện tử sang trọng.
- **CẤM Emoji làm Icon**: Luôn sử dụng icon SVG chuẩn (Lucide, Phosphor, Heroicons).
- **Chuẩn tương phản WCAG AA**: Độ tương phản chữ trên nền tối thiểu **4.5:1** (hoặc 3:1 cho tiêu đề lớn).
- **Hỗ trợ Motion Accessibility**: Bắt buộc tôn trọng `@media (prefers-reduced-motion: reduce)`.
- **Phản hồi tương tác**: Bắt buộc `cursor-pointer` cho mọi thành phần click được, hover state mượt mà (150–300ms).
