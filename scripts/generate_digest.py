#!/usr/bin/env python3
"""Daily LangFlow Digest Generator"""
import os
import json
from datetime import datetime
from pathlib import Path

def generate_daily_digest():
    today = datetime.now().strftime("%Y-%m-%d")
    digest = f"""# LangFlow Daily Digest - {today}

## Status
- LangFlow: Active
- RAG: Configured
- Security: Active

## Files
- LangFlow_Digest_Summary.md
- requirements.txt
- .github/workflows/daily-digest.yml
- scripts/generate_digest.py
"""
    digest_path = Path(f"digests/digest_{today}.md")
    digest_path.parent.mkdir(exist_ok=True)
    with open(digest_path, "w") as f:
        f.write(digest)
    print(f"✅ Digest generated: {digest_path}")

if __name__ == "__main__":
    generate_daily_digest()
