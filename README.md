# Nebula Curriculum — Quarto Single-Source Starter

This repo lets you write **one source of truth** (Markdown/Quarto) and generate:
- Module Handbooks (HTML + PDF)
- Lesson Slides (Reveal.js + PDF)
- Checklists/Rubrics (PDF)

## 1) Install
- Install **Quarto CLI**: https://quarto.org/docs/get-started/
- (For PDF) Install TinyTeX: `quarto install tinytex`
- Optional: Git, GitHub Desktop

## 2) Render locally
```bash
quarto render
# or live preview website/slides
quarto preview
```

Outputs go to `/_site/` by default.

## 3) Repo structure
```
./
  quarto.yml
  _theme/
    nebula.scss
    nebula-reveal.scss
  _partials/
    outcomes.md
    tools.md
    rubric.md
  beginner-l1/
    programming-fundamentals/
      handbook.qmd
      slides/
        L01-intro.qmd
  .github/workflows/
    build.yml
  scripts/
    upload_to_django.py
```

## 4) Publish site (optional)
- Enable GitHub Pages on `gh-pages` branch.
- Push to `main`; GitHub Actions will build and publish.

## 5) Auto-attach PDFs to your Django LMS (optional)
- Add `DJANGO_API_BASE`, `DJANGO_TOKEN` secrets in your repo.
- The workflow calls `scripts/upload_to_django.py` after rendering to POST PDFs as Module Materials.
