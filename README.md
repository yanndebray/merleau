# Merleau

A Python utility for video analysis using Google's Gemini 2.5 Flash API.

## Features

- Upload video files to Google Gemini
- AI-powered video content analysis
- Token usage tracking and cost estimation
- Automatic polling for file processing completion

## Installation

Using [uv](https://docs.astral.sh/uv/) (recommended):
```bash
uv sync
```

Or using pip:
```bash
pip install -r requirements.txt
```

## Configuration

1. Get a Gemini API key from [Google AI Studio](https://aistudio.google.com/apikey)
2. Create a `.env` file in the project root:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

## Usage

1. Place your video file in the project directory
2. Update the `video_path` variable in `analyze_video.py` to point to your video
3. Run the analysis:
   ```bash
   uv run python analyze_video.py
   ```
   Or with pip installation: `python analyze_video.py`

## Output

The script provides:
- Video content analysis from Gemini
- Token usage breakdown (prompt, response, total)
- Estimated cost based on Gemini 2.5 Flash pricing

## Pricing Reference

Gemini 2.5 Flash (as of 2025):
- Input: $0.15 per 1M tokens (text/image), $0.075 per 1M tokens (video)
- Output: $0.60 per 1M tokens, $3.50 for thinking tokens
