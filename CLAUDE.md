# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Merleau is a CLI tool for video understanding using Google's Gemini API. Named after Maurice Merleau-Ponty, the phenomenologist philosopher. The CLI command is `ponty`.

See `research/positioning_merleau.md` for market positioning and differentiation strategy.

## Commands

```bash
# Install dependencies
uv sync
uv sync --extra web  # Include Streamlit

# Run the CLI
uv run ponty video.mp4
uv run ponty video.mp4 -p "Custom prompt" -m gemini-2.0-flash
uv run ponty https://youtu.be/VIDEO_ID          # YouTube URL
uv run ponty video.mp4 -e md                     # Export to markdown

# Run the web UI
uv run streamlit run streamlit_app.py

# Build package
uv build

# Run tests (after making changes to cli.py)
uv run ponty --version
uv run ponty --help
```

## Architecture

```
merleau/
├── merleau/
│   ├── __init__.py    # Package version (__version__)
│   └── cli.py         # CLI + core analyze_video() function
├── streamlit_app.py   # Web UI (run with: streamlit run streamlit_app.py)
├── website/           # Landing page (GitHub Pages)
│   └── index.html     # Single-page site with version badge + CLI reference
├── research/          # Market research, positioning, and video analysis exports
├── .github/workflows/
│   └── python-publish.yml  # Auto-publish to PyPI on GitHub release
├── pyproject.toml     # Package config with [project.scripts] entry point
└── analyze_video.py   # Legacy standalone script
```

### CLI Flow (merleau/cli.py)
1. Parse arguments (video path/URL, prompt, model, cost flag, export format)
2. Load API key from environment or `.env`
3. Detect input type: YouTube URL or local file
4. For local files: upload to Gemini Files API, poll for processing
5. For YouTube URLs: pass directly via `Part.from_uri()` (no upload needed)
6. Generate content analysis
7. Display results and optional cost breakdown
8. If `--export md`: write markdown file named after video/YouTube ID

## Key Differentiators

- **Native Gemini video** - Only CLI with true video understanding (not frame extraction)
- **YouTube URL support** - Direct analysis via `Part.from_uri()`, supports youtube.com/watch, youtu.be, youtube.com/shorts
- **Markdown export** - Save analysis with metadata header (`-e md`)
- **Cost transparency** - Token usage and pricing shown by default

## Configuration

- `.env` - Contains `GEMINI_API_KEY` (required)
- `pyproject.toml` - Package metadata, dependencies, CLI entry point, and `readme = "README.md"` (required for PyPI description)

## Release Procedure

Follow these steps **in order** when making a release:

### 1. Update version in all three places
- `merleau/__init__.py` — `__version__ = "X.Y.Z"`
- `pyproject.toml` — `version = "X.Y.Z"`
- `website/index.html` — version badge `<span>vX.Y.Z</span>`

### 2. Update website CLI reference
If new CLI flags were added, update the CLI reference section in `website/index.html` (the `api-grid` div with `api-item` entries).

### 3. Commit and push
```bash
git add merleau/__init__.py pyproject.toml website/index.html
git commit -m "Bump version to X.Y.Z"
git push origin main
```

### 4. Create GitHub release
```bash
gh release create vX.Y.Z --title "vX.Y.Z" --notes "release notes here"
```

**Do NOT** attach build artifacts manually — the GitHub Action (`.github/workflows/python-publish.yml`) automatically builds and publishes to PyPI via trusted publishing when a release is created.

### 5. Verify
- Check GitHub Actions for successful PyPI publish
- Verify at https://pypi.org/project/merleau/

## Important Notes

- **Package manager:** Always use `uv` (not pip) for local development
- **PyPI publishing:** Handled automatically by GitHub Actions on release — do NOT run `uv publish` manually
- **Website:** Hosted on GitHub Pages from `website/index.html` — update version badge and CLI reference with every release
- **Version:** Must be kept in sync across `__init__.py`, `pyproject.toml`, and `website/index.html`
- **README:** The `readme = "README.md"` field in `pyproject.toml` is required for PyPI to display the project description
- **YouTube detection:** `is_youtube_url()` in `cli.py` handles youtube.com/watch, youtu.be, and youtube.com/shorts patterns
