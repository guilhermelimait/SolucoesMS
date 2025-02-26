# 📝 WordPress to GitHub Export

Simple tool to export WordPress posts into categorized Markdown files for GitHub.

## 🚀 Quick Start

1. Install Python requirements:
```bash
pip install requests
```

2. Update your WordPress URL in the script:
```python
site_url = "https://your-wordpress-site.com"
```

3. Run the export:
```bash
python exportwordpressposts.py
```

## 📂 Output Format

Posts are organized by categories:
```
github_solutions/
├── category1/
│   └── post-title-1.md
└── category2/
    └── post-title-2.md
```

Each file contains:
```markdown
# Post Title
Date: YYYY-MM-DD
Categories: Category1, Category2
---
Content here...
```

## ⚠️ Troubleshooting

SSL errors are automatically handled with certificate verification disabled.

## 📜 License

MIT License