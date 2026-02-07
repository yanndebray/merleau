# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Merleau is a CLI tool for video understanding using Google's Gemini API. Named after Maurice Merleau-Ponty, the phenomenologist philosopher. The CLI command is `ponty`.

- **Website:** https://merleau.cc (hosted on GitHub Pages from `website/`)
- **Web App:** https://merleau.streamlit.app/ (deployed from `streamlit_app.py`)
- **PyPI:** https://pypi.org/project/merleau/

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

# Smoke tests (after making changes to cli.py)
uv run ponty --version
uv run ponty --help
```

## Architecture

```
merleau/
├── merleau/
│   ├── __init__.py    # Package version (__version__)
│   └── cli.py         # CLI + core analyze_video() + is_youtube_url()
├── streamlit_app.py   # Web UI (file upload, YouTube URL, screen recording tabs)
├── website/           # Landing page (merleau.cc via GitHub Pages)
│   └── index.html     # Single-page site with version badge + CLI reference
├── img/               # Images used by README and Streamlit app
├── research/          # Market research, positioning, and video analysis exports
├── .github/workflows/
│   └── python-publish.yml  # Auto-publish to PyPI on GitHub release
├── pyproject.toml     # Package config, classifiers, [project.scripts] entry point
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

### Streamlit App (streamlit_app.py)
- **Tab 1:** File upload with video preview
- **Tab 2:** YouTube URL input with video preview and direct analysis
- **Tab 3:** Screen recording guide with Streamlit built-in screencast screenshot
- Uses `analyze_video()` and `is_youtube_url()` from `merleau.cli`
- Images loaded via `pathlib.Path(__file__).parent` for Streamlit Cloud compatibility

## Key Differentiators

- **Native Gemini video** — Only CLI with true video understanding (not frame extraction)
- **YouTube URL support** — Direct analysis via `Part.from_uri()`, supports youtube.com/watch, youtu.be, youtube.com/shorts
- **Markdown export** — Save analysis with metadata header (`-e md`)
- **Cost transparency** — Token usage and pricing shown by default
- **Web UI** — Streamlit app with file upload, YouTube URL, and screen recording support

## Configuration

- `.env` — Contains `GEMINI_API_KEY` (required)
- `pyproject.toml` — Package metadata, classifiers, dependencies, CLI entry point, and `readme = "README.md"` (required for PyPI description)

## Release Procedure

Follow these steps **in order** when making a release:

### 1. Update version in all three places
- `merleau/__init__.py` — `__version__ = "X.Y.Z"`
- `pyproject.toml` — `version = "X.Y.Z"`
- `website/index.html` — version badge `<span>vX.Y.Z</span>`

### 2. Update website and README if needed
- If new CLI flags were added, update the CLI reference in `website/index.html` (the `api-grid` div) and the Options table in `README.md`
- If new features were added, update the Features list in `README.md`

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
- Streamlit Cloud auto-deploys from main (no action needed)

## Important Notes

- **Package manager:** Always use `uv` (not pip) for local development
- **PyPI publishing:** Handled automatically by GitHub Actions on release — do NOT run `uv publish` manually
- **Website:** Hosted at merleau.cc (GitHub Pages from `website/index.html`) — update version badge and CLI reference with every release
- **Version:** Must be kept in sync across `__init__.py`, `pyproject.toml`, and `website/index.html`
- **README:** The `readme = "README.md"` field in `pyproject.toml` is required for PyPI to display the project description
- **Classifiers:** Python version classifiers in `pyproject.toml` are required for the shields.io Python badge to render
- **Streamlit Cloud:** Images must use absolute paths via `pathlib.Path(__file__).parent`, not relative paths
- **YouTube detection:** `is_youtube_url()` in `cli.py` handles youtube.com/watch, youtu.be, and youtube.com/shorts patterns
- **URLs:** Website is merleau.cc (not yanndebray.github.io/merleau)
