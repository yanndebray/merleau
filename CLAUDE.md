# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python utility for video analysis using Google's Gemini 2.5 Flash API. The project uploads video files to Gemini and generates AI-powered analysis with usage tracking and cost estimation.

## Running the Application

```bash
# Install dependencies
pip install -r requirements.txt

# Run the video analyzer
python analyze_video.py
```

## Prerequisites

- Place the video file in the project root directory (currently expects `MATLAB_Modernizer.mp4`)
- Create a `.env` file with your Gemini API key: `GEMINI_API_KEY=your_key_here`

## Architecture

Single-script application (`analyze_video.py`) with linear flow:
1. Load API key from `.env`
2. Initialize Gemini client
3. Upload video file to Gemini
4. Poll for file processing completion (2-second intervals)
5. Generate content analysis using `gemini-2.5-flash` model
6. Display results with token usage and cost breakdown

## Key Dependencies

- `google-genai`: Google AI SDK (v2) for Gemini API interaction
- `python-dotenv`: Environment variable management
