# Merleau - Video Understanding CLI

> **Repository:** [github.com/yanndebray/merleau](https://github.com/yanndebray/merleau)
> **Website:** [merleau.cc](https://merleau.cc)
> **PyPI:** [pypi.org/project/merleau](https://pypi.org/project/merleau/)
> **Web App:** [merleau.streamlit.app](https://merleau.streamlit.app)
> **License:** MIT | **Version:** 0.5.2 | **Python:** 3.10+
> **Maintainer:** slevin48

---

## What Is Merleau?

Merleau is a Python command-line tool that leverages Google's Gemini API to perform **native video understanding** directly from the terminal. Unlike other tools that rely on frame extraction or separate transcription pipelines, Merleau uploads entire videos to Gemini's multimodal API, enabling combined audio-visual analysis using Gemini's 2-million-token context window.

The name is a reference to **Maurice Merleau-Ponty**, the French phenomenologist philosopher known for his work on perception — reflecting the tool's emphasis on genuine understanding of video content rather than mechanical processing.

## Why Merleau?

Merleau positions itself as **the only major CLI offering true native video understanding**. Key differentiators:

- **No frame extraction** — videos are uploaded whole to Gemini, preserving temporal context
- **Audio + visual analysis** — no separate transcription tools needed
- **Long video support** — handles 2+ hour videos via Gemini's massive context window
- **Cost transparency** — shows token usage and estimated cost for every analysis
- **Simple single-command interface** — one command (`ponty`) does everything

## Core Features

| Feature | Description |
|---------|-------------|
| Native video processing | Direct upload to Gemini's multimodal API |
| YouTube URL support | Analyze YouTube videos by pasting a URL |
| Custom prompts | Ask specific questions about video content |
| Multi-model support | Choose between gemini-2.5-flash, gemini-2.0-flash, gemini-1.5-pro |
| Markdown export | Export analysis results to `.md` files |
| Cost tracking | Token usage breakdown with price estimates |
| Web UI | Browser-based interface via Streamlit |
| Video format support | MP4, MOV, AVI, and other common formats |

## Architecture

```
User (CLI: ponty)
    │
    ├── Local video file ──► Upload to Gemini API
    │                              │
    ├── YouTube URL ───────► Gemini preview feature
    │                              │
    │                              ▼
    │                     Google Gemini API
    │                   (multimodal processing)
    │                              │
    │                              ▼
    └──────────────────── Analysis response
                          + token/cost summary
```

The tool also ships with a **Streamlit web app** (`streamlit_app.py`) deployed at `merleau.streamlit.app`, providing a browser-based UI with file upload and YouTube preview capabilities.

## Project Structure

```
merleau/
├── .github/workflows/    # CI/CD
├── merleau/              # Core Python package
├── research/             # Research notes and experiments
├── website/              # Website source (merleau.cc)
├── analyze_video.py      # Standalone analysis script
├── streamlit_app.py      # Web UI application
├── pyproject.toml        # Package configuration
├── requirements.txt      # Dependencies
└── uv.lock               # UV lockfile
```

## Installation

**Via pip:**
```bash
pip install merleau          # CLI only
pip install merleau[web]     # CLI + Streamlit web UI
```

**Via UV (recommended for development):**
```bash
uv sync
```

## Configuration

1. Obtain a Gemini API key from [Google AI Studio](https://aistudio.google.com/)
2. Set via environment variable or `.env` file:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

## CLI Usage

The CLI command is `ponty`:

```bash
# Analyze a local video
ponty video.mp4

# Analyze a YouTube video
ponty https://youtu.be/VIDEO_ID

# Custom prompt
ponty video.mp4 -p "Summarize the key points discussed"

# Choose a specific model
ponty video.mp4 -m gemini-2.0-flash

# Export to markdown
ponty video.mp4 -e md

# Hide cost information
ponty video.mp4 --no-cost

# Show version
ponty -V
```

### CLI Options

| Flag | Long Form | Description |
|------|-----------|-------------|
| `-p` | `--prompt` | Custom analysis prompt |
| `-m` | `--model` | Gemini model selection |
| `-e` | `--export` | Export format (e.g., `md`) |
| | `--no-cost` | Suppress pricing information |
| `-V` | `--version` | Display version number |

## Pricing

Based on Gemini 2.5 Flash (2025 rates):

| Component | Rate |
|-----------|------|
| Input (text/image) | $0.15 / 1M tokens |
| Input (video) | $0.075 / 1M tokens |
| Output | $0.60 / 1M tokens |
| **1-hour video** | **~$0.11 - $0.32** |

### Cost Optimization

Video compression via ffmpeg can reduce API costs by 10-15%:

```bash
ffmpeg -i input.mp4 -vcodec libx264 -crf 28 -preset medium \
  -vf "scale=1280:-2" output.mp4
```

Example result: 1080p to 720p compression achieved 95% file size reduction with 10.8% API cost savings.

## Use Cases

- **Product demos & reviews** — Analyze product walkthrough videos
- **Lecture summarization** — Extract key points from educational content
- **Meeting transcription** — Get summaries and action items from recorded meetings
- **Sports footage analysis** — Break down plays and highlights
- **App UI/UX analysis** — Analyze screencasts for usability insights
- **Code extraction** — Pull code snippets from programming tutorial videos
- **Documentary analysis** — Summarize and analyze documentary content

## Technical Stack

- **Language:** Python 3.10+
- **AI Backend:** Google Gemini API (multimodal)
- **Web Framework:** Streamlit (optional web UI)
- **Package Manager:** UV (development), pip (distribution)
- **Distribution:** PyPI
