"""Command-line interface for Merleau video analysis."""

import argparse
import os
import re
import sys
import time
from dataclasses import dataclass
from typing import Callable, Optional

from dotenv import load_dotenv
from google import genai
from google.genai import types


def is_youtube_url(path: str) -> bool:
    """Check if the given path is a YouTube URL."""
    return bool(re.match(
        r'(https?://)?(www\.)?(youtube\.com/watch\?v=|youtu\.be/|youtube\.com/shorts/)',
        path
    ))


@dataclass
class AnalysisResult:
    """Result from video analysis."""
    text: str
    prompt_tokens: int
    response_tokens: int
    total_tokens: int
    input_cost: float
    output_cost: float
    total_cost: float


def wait_for_processing(client, file, on_progress: Optional[Callable] = None):
    """Wait for file to finish processing."""
    while file.state.name == "PROCESSING":
        if on_progress:
            on_progress()
        else:
            print(".", end="", flush=True)
        time.sleep(2)
        file = client.files.get(name=file.name)
    if not on_progress:
        print()
    return file


def calculate_cost(usage):
    """Calculate cost from usage metadata."""
    # Gemini 2.5 Flash pricing (as of 2025):
    # Input: $0.15 per 1M tokens (text/image), $0.075 per 1M tokens for video
    # Output: $0.60 per 1M tokens, $3.50 for thinking tokens
    input_cost = (usage.prompt_token_count / 1_000_000) * 0.15
    output_cost = (usage.candidates_token_count / 1_000_000) * 0.60
    return input_cost, output_cost, input_cost + output_cost


def print_usage(usage):
    """Print token usage and cost estimation."""
    print("\n--- Usage Information ---")
    print(f"Prompt tokens: {usage.prompt_token_count}")
    print(f"Response tokens: {usage.candidates_token_count}")
    print(f"Total tokens: {usage.total_token_count}")

    input_cost, output_cost, total_cost = calculate_cost(usage)
    print(f"\nEstimated cost:")
    print(f"  Input:  ${input_cost:.6f}")
    print(f"  Output: ${output_cost:.6f}")
    print(f"  Total:  ${total_cost:.6f}")


def analyze_video(
    video_path: str,
    prompt: str = "Explain what happens in this video",
    model: str = "gemini-2.5-flash",
    api_key: Optional[str] = None,
    on_upload: Optional[Callable[[str], None]] = None,
    on_processing: Optional[Callable] = None,
    on_analyzing: Optional[Callable] = None,
) -> AnalysisResult:
    """
    Analyze a video file or YouTube URL using Gemini.

    Args:
        video_path: Path to the video file or YouTube URL
        prompt: Analysis prompt
        model: Gemini model to use
        api_key: Optional API key (falls back to env var)
        on_upload: Callback when upload completes (receives file URI)
        on_processing: Callback during processing (called repeatedly)
        on_analyzing: Callback when analysis starts

    Returns:
        AnalysisResult with text, tokens, and cost

    Raises:
        ValueError: If API key not found or file doesn't exist
        RuntimeError: If file processing fails
    """
    load_dotenv()

    api_key = api_key or os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in environment or .env file")

    client = genai.Client(api_key=api_key)

    if is_youtube_url(video_path):
        # YouTube URL: pass directly to Gemini
        video_part = types.Part.from_uri(file_uri=video_path, mime_type="video/mp4")
        if on_upload:
            on_upload(video_path)
    else:
        # Local file: upload to Gemini
        if not os.path.exists(video_path):
            raise ValueError(f"Video file not found: {video_path}")

        myfile = client.files.upload(file=video_path)
        if on_upload:
            on_upload(myfile.uri)

        # Wait for processing
        myfile = wait_for_processing(client, myfile, on_progress=on_processing)

        if myfile.state.name == "FAILED":
            raise RuntimeError("File processing failed")

        video_part = myfile

    # Generate analysis
    if on_analyzing:
        on_analyzing()

    response = client.models.generate_content(
        model=model,
        contents=[video_part, prompt]
    )

    # Extract usage info
    usage = response.usage_metadata
    input_cost, output_cost, total_cost = calculate_cost(usage)

    return AnalysisResult(
        text=response.text,
        prompt_tokens=usage.prompt_token_count,
        response_tokens=usage.candidates_token_count,
        total_tokens=usage.total_token_count,
        input_cost=input_cost,
        output_cost=output_cost,
        total_cost=total_cost,
    )


def analyze(video_path, prompt, model, show_cost):
    """Analyze a video file or YouTube URL using Gemini (CLI wrapper)."""
    try:
        youtube = is_youtube_url(video_path)
        if youtube:
            print(f"Analyzing YouTube video: {video_path}")
        else:
            print(f"Uploading video: {video_path}")

        def on_upload(uri):
            if not youtube:
                print(f"Upload complete. File URI: {uri}")
                print("Waiting for file to be processed...", end="")

        def on_processing():
            print(".", end="", flush=True)

        def on_analyzing():
            print()
            print(f"\nAnalyzing video with {model}...")

        result = analyze_video(
            video_path=video_path,
            prompt=prompt,
            model=model,
            on_upload=on_upload,
            on_processing=on_processing,
            on_analyzing=on_analyzing,
        )

        print("\n--- Video Analysis ---")
        print(result.text)

        if show_cost:
            print("\n--- Usage Information ---")
            print(f"Prompt tokens: {result.prompt_tokens}")
            print(f"Response tokens: {result.response_tokens}")
            print(f"Total tokens: {result.total_tokens}")
            print(f"\nEstimated cost:")
            print(f"  Input:  ${result.input_cost:.6f}")
            print(f"  Output: ${result.output_cost:.6f}")
            print(f"  Total:  ${result.total_cost:.6f}")

    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except RuntimeError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    """Main entry point for the CLI."""
    from merleau import __version__

    parser = argparse.ArgumentParser(
        prog="ponty",
        description="Analyze videos using Google's Gemini API"
    )
    parser.add_argument(
        "-V", "--version",
        action="version",
        version=f"%(prog)s {__version__}"
    )
    parser.add_argument(
        "video",
        nargs="?",
        help="Path to video file or YouTube URL to analyze"
    )
    parser.add_argument(
        "-p", "--prompt",
        default="Explain what happens in this video",
        help="Prompt for the analysis (default: 'Explain what happens in this video')"
    )
    parser.add_argument(
        "-m", "--model",
        default="gemini-2.5-flash",
        help="Gemini model to use (default: gemini-2.5-flash)"
    )
    parser.add_argument(
        "--no-cost",
        action="store_true",
        help="Hide usage and cost information"
    )

    args = parser.parse_args()

    if args.video is None:
        parser.print_help()
        sys.exit(1)

    analyze(args.video, args.prompt, args.model, show_cost=not args.no_cost)


if __name__ == "__main__":
    main()
