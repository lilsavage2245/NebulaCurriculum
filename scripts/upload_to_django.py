#!/usr/bin/env python3
import os, requests, glob

API_BASE = os.environ.get("DJANGO_API_BASE")  # e.g., https://api.nebulacodeacademy.com/api
TOKEN = os.environ.get("DJANGO_TOKEN")
MODULE_SLUG = os.environ.get("MODULE_SLUG", "beginner-program-beg-level-1-core-foundations")

# Example: upload all PDFs found in _site
pdf_files = glob.glob("_site/**/*.pdf", recursive=True)

headers = {
    "Authorization": f"Bearer {TOKEN}"
}

for pdf_path in pdf_files:
    material_title = os.path.basename(pdf_path).replace(".pdf","")
    files = {"file": (os.path.basename(pdf_path), open(pdf_path, "rb"), "application/pdf")}
    data = {
        "title": material_title,
        "type": "PDF",
        "audience": "ENROLLED",  # or BOTH/FREE
        "version": "v1.0",
        "description": f"Auto-uploaded from Quarto CI: {material_title}"
    }
    url = f"{API_BASE}/modules/{MODULE_SLUG}/materials/"
    print(f"Uploading {pdf_path} -> {url}")
    r = requests.post(url, headers=headers, files=files, data=data, timeout=60)
    print(r.status_code, r.text)
