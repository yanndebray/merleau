# Merleau

> *"The world is not what I think, but what I live through."*
> — Maurice Merleau-Ponty

A CLI tool for video understanding using Google's Gemini API. Named after [Maurice Merleau-Ponty](https://en.wikipedia.org/wiki/Maurice_Merleau-Ponty), the phenomenologist philosopher whose work on perception inspires how this tool helps you perceive your videos.

## Why Merleau?

Google Gemini is the **only major AI provider** with native video understanding—Claude doesn't support video, and GPT-4o requires frame extraction workarounds. Merleau is the first CLI that actually understands video rather than analyzing frames.

## Features

- **Native Gemini video processing** - Upload and analyze videos directly
- **YouTube URL support** - Analyze videos directly from YouTube (free preview)
- **Customizable prompts** - Ask any question about your video
- **Cost estimation** - Token usage tracking and cost breakdown
- **Multiple models** - Support for different Gemini models

## Installation

Using [uv](https://docs.astral.sh/uv/) (recommended):
```bash
uv sync
```

Or install from PyPI:
```bash
pip install merleau
```

## Configuration

1. Get a Gemini API key from [Google AI Studio](https://aistudio.google.com/apikey)
2. Set the API key as an environment variable or create a `.env` file:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

## Usage

```bash
# Basic video analysis
ponty video.mp4

# Custom prompt
ponty video.mp4 -p "Summarize the key points in this video"

# Use a different model
ponty video.mp4 -m gemini-2.0-flash

# Hide cost information
ponty video.mp4 --no-cost
```

### Options

| Option | Description |
|--------|-------------|
| `-p, --prompt` | Prompt for the analysis (default: "Explain what happens in this video") |
| `-m, --model` | Gemini model to use (default: gemini-2.5-flash) |
| `--no-cost` | Hide usage and cost information |

## Output

The CLI provides:
- Video content analysis from Gemini
- Token usage breakdown (prompt, response, total)
- Estimated cost based on Gemini pricing

## Pricing Reference

Gemini 2.5 Flash (as of 2025):
- Input: $0.15 per 1M tokens (text/image), $0.075 per 1M tokens (video)
- Output: $0.60 per 1M tokens, $3.50 for thinking tokens

A 1-hour video costs approximately **$0.11-0.32** to analyze.
