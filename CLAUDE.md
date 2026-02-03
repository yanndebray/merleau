# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Merleau is a Python utility for video analysis using Google's Gemini 2.5 Flash API. See README.md for installation and usage instructions.

## Commands

```bash
# Install dependencies (using uv)
uv sync

# Run the video analyzer
uv run python analyze_video.py

# Alternative with pip
pip install -r requirements.txt
python analyze_video.py
```

## Architecture

Single-script application (`analyze_video.py`) with linear flow:
1. Load API key from `.env` via `python-dotenv`
2. Initialize Gemini client using `google-genai` SDK
3. Upload video file to Gemini Files API
4. Poll for file processing completion (2-second intervals)
5. Generate content analysis using `gemini-2.5-flash` model
6. Display results with token usage and cost breakdown

## Configuration

- `.env` - Contains `GEMINI_API_KEY` (required)
- `pyproject.toml` - Project metadata and dependencies for uv
- `video_path` variable in `analyze_video.py` - Path to video file to analyze
