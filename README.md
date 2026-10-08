# UI/UX Pro Max — Modularized Design Intelligence Engine

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Tests Passing](https://img.shields.io/badge/tests-172%20passed-brightgreen.svg)]()
[![Zero External Dependencies](https://img.shields.io/badge/dependencies-0%20(stdlib%20only)-success.svg)]()

Phiên bản **Module hóa toàn diện (Modularized Edition)** của `ui-ux-pro-max-skill`. Đóng gói thành Python package chuẩn (`ui_ux_pro_max`), CLI tool tốc độ cao (`uipro`), và Native Agent Skill cho Antigravity, Claude Code, Cursor, và Codex.

Giải quyết triệt để **"Hội chứng giao diện tím của AI"** (AI mặc định luôn sinh web nền tối dark-mode, viền gradient tím/hồng, bo tròn quá mức) bằng kho tri thức thiết kế cục bộ chuẩn xác, hoàn toàn offline.

---

## ⚡ Cài Đặt 1 Dòng Lệnh (Quick Install)

Tại thư mục repo này:
```bash
pip install -e .
```

Sau khi cài đặt, bạn có thể:
1. Gọi CLI từ bất kỳ đâu: `uipro "spa booking"`
2. Import trực tiếp trong Python: `from ui_ux_pro_max import get_design_system`
3. Kích hoạt tự động qua Antigravity Skill: `ui-ux-pro-max`

---

## 🐍 1. Sử Dụng Như Python Library

Bất kỳ dự án hay agent nào trong hệ sinh thái đều có thể import trực tiếp:

```python
from ui_ux_pro_max import get_design_system, search_colors, search_styles, search_stack

# 1. Sinh trọn bộ Design System cho ý tưởng sản phẩm
ds = get_design_system("Fintech mobile banking app", stack="react")

print("Style đề xuất:", ds.style_name)          # e.g. Minimal Corporate / Clean Light
print("Màu chủ đạo:", ds.primary_color)          # e.g. #0F172A
print("Các điều CẤM (Anti-patterns):", ds.anti_patterns) # e.g. ['Purple AI Gradients', 'Emoji Icons']
print("Checklist trước bàn giao:", len(ds.pre_delivery_checklist))

# 2. Xuất mã CSS Custom Properties (:root) hoặc Tailwind Config
css_code = ds.to_css_variables()
tailwind_cfg = ds.to_tailwind_theme()
full_spec = ds.to_markdown()

# 3. Tra cứu nhanh bảng màu ngành nghề
palette = search_colors("luxury cosmetics")
for item in palette.items:
    print(item["Product Type"], "->", item["Primary"], item["Accent"])

# 4. Tra cứu quy chuẩn tối ưu hóa theo framework
react_rules = search_stack(stack="react", query="hooks")
for rule in react_rules.items:
    print(rule["Guideline"], ":", rule["Do"], "vs", rule["Don't"])
```

---

## 💻 2. Sử Dụng Qua CLI (`uipro`)

### A. Sinh Design System Đầy Đủ
```bash
# Sinh thiết kế chuẩn Markdown
uipro "Luxury spa booking"

# Kèm stack cụ thể (React, Next.js, Tailwind, Flutter, SwiftUI, WPF...)
uipro "Fintech trading dashboard" --stack nextjs

# Xuất thẳng mã CSS Variables
uipro "Healthcare appointment system" --css

# Xuất dạng JSON cho pipeline tự động
uipro "Cyberpunk gaming portal" --json
```

### B. Tra Cứu Nhanh Theo Chuyên Mục
```bash
# 1. Tra cứu bảng màu theo ngành
uipro palette "fintech"
uipro palette "health wellness"

# 2. Tra cứu cặp font Google Fonts tối ưu
uipro font "luxury"
uipro font "modern saas"

# 3. Tra cứu danh sách 88 phong cách thiết kế
uipro styles

# 4. Tra cứu danh sách 22 Framework Stacks
uipro stacks

# 5. In bảng kiểm chất lượng giao diện (WCAG AA & UX QA)
uipro checklist
```

---

## 🧠 3. Tích Hợp Antigravity / Agent Skill

Repo đã được cấu hình sẵn `SKILL.md` và tạo directory junction vào hệ thống skill toàn cục:
- **Shared Skills**: `D:\01_PROJECT_CODE\00_Manager\shared-skills\ui-ux-pro-max`
- **Config Skills**: `C:\Users\ptd26\.gemini\config\skills\ui-ux-pro-max`
- **Module Repo**: `D:\01_PROJECT_CODE\02_MODULE_REPO\ui-ux-pro-max`

Khi giao tiếp với Antigravity, chỉ cần yêu cầu:
> *"Thiết kế giao diện cho app đặt lịch spa"* hoặc *"Tạo design system cho hệ thống ERP"*
Agent sẽ tự động gọi skill `ui-ux-pro-max` để tra cứu màu sắc, font chữ và các điều cấm kỵ trước khi sinh code.

---

## 📊 4. Cấu Trúc Kho Tri Thức Cục Bộ (Zero Cloud / 100% Offline)

Tất cả dữ liệu được lưu trữ dưới dạng CSV tối ưu hóa, tìm kiếm bằng thuật toán **BM25 TF-IDF** không cần GPU hay mạng internet:

- `styles.csv`: 88 phong cách UI (Bento Grid, Neumorphism, Glassmorphism, Brutalism, Clean Light...)
- `colors.csv`: 192 bảng màu ngành nghề chuẩn độ tương phản
- `typography.csv`: 74 cặp font Google Fonts được giám tuyển kỹ lưỡng
- `ux-guidelines.csv`: 119 quy tắc trải nghiệm người dùng & phòng tránh bẫy giao diện
- `icons.csv`: 105 bộ icon SVG chuẩn mực (Lucide / Phosphor)
- `motion.csv`: 17 hiệu ứng chuyển động GSAP mượt mà
- `charts.csv`: 25 hướng dẫn biểu đồ trực quan hóa dữ liệu
- `stacks/`: 22 framework phổ biến:
  - Web: `react`, `nextjs`, `vue`, `svelte`, `astro`, `angular`, `html-tailwind`, `nuxtjs`, `nuxt-ui`, `shadcn`, `laravel`
  - Mobile: `react-native`, `flutter`, `swiftui`, `jetpack-compose`
  - 3D: `threejs`
  - Desktop: `wpf`, `winui`, `avalonia`, `uno`, `uwp`, `javafx`

---

## 🛡️ Bảng Kiểm Đoán & Điều Cấm Kỵ (Do NOTs)

1. **Tránh tím gradient mặc định**: Cấm dùng gradient tím/hồng AI cho các ứng dụng ngân hàng, y tế, spa, hành chính.
2. **Cấm Emoji làm Icon**: Luôn dùng icon SVG có ngữ nghĩa (`aria-hidden="true"` nếu trang trí).
3. **Độ tương phản chữ $\ge 4.5:1$**: Tuân thủ chuẩn WCAG AA cho văn bản thường, $\ge 3:1$ cho tiêu đề lớn.
4. **Hỗ trợ Motion Accessibility**: Bắt buộc hỗ trợ `@media (prefers-reduced-motion: reduce)` cho người dễ chóng mặt.
5. **Interactive Feedback**: Bắt buộc `cursor-pointer` cho mọi nút bấm, link và thẻ tương tác.

---

## 🧪 Kiểm Thử Hệ Thống (Tests)

Chạy toàn bộ 172 unit tests:
```bash
pytest
```
Tất cả tests đều chạy bằng thư viện chuẩn (`unittest` / `pytest`), thời gian thực thi $< 7$ giây.
