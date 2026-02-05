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

# Run the web UI
uv run streamlit run streamlit_app.py

# Build package
uv build

# Publish to PyPI
uv publish --token <token>
```

## Architecture

```
merleau/
├── merleau/
│   ├── __init__.py    # Package version
│   └── cli.py         # CLI + core analyze_video() function
├── streamlit_app.py   # Web UI (run with: streamlit run streamlit_app.py)
├── website/           # Landing page (GitHub Pages)
│   └── index.html     # Single-page site
├── research/          # Market research and positioning
├── pyproject.toml     # Package config with [project.scripts] entry point
└── analyze_video.py   # Legacy standalone script
```

### CLI Flow (merleau/cli.py)
1. Parse arguments (video path, prompt, model, cost flag)
2. Load API key from environment or `.env`
3. Upload video to Gemini Files API
4. Poll for processing completion
5. Generate content analysis
6. Display results and optional cost breakdown

## Key Differentiators

- **Native Gemini video** - Only CLI with true video understanding (not frame extraction)
- **YouTube URL support** - Direct analysis via Gemini's preview feature
- **Cost transparency** - Token usage and pricing shown by default

## Configuration

- `.env` - Contains `GEMINI_API_KEY` (required)
- `pyproject.toml` - Package metadata, dependencies, and CLI entry point
