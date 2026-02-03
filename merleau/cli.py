"""Command-line interface for Merleau video analysis."""

import argparse
import os
import sys
import time

from dotenv import load_dotenv
from google import genai


def wait_for_processing(client, file):
    """Wait for file to finish processing."""
    while file.state.name == "PROCESSING":
        print(".", end="", flush=True)
        time.sleep(2)
        file = client.files.get(name=file.name)
    print()
    return file


def print_usage(usage):
    """Print token usage and cost estimation."""
    print("\n--- Usage Information ---")
    print(f"Prompt tokens: {usage.prompt_token_count}")
    print(f"Response tokens: {usage.candidates_token_count}")
    print(f"Total tokens: {usage.total_token_count}")

    # Gemini 2.5 Flash pricing (as of 2025):
    # Input: $0.15 per 1M tokens (text/image), $0.075 per 1M tokens for video
    # Output: $0.60 per 1M tokens, $3.50 for thinking tokens
    input_cost = (usage.prompt_token_count / 1_000_000) * 0.15
    output_cost = (usage.candidates_token_count / 1_000_000) * 0.60
    total_cost = input_cost + output_cost
    print(f"\nEstimated cost:")
    print(f"  Input:  ${input_cost:.6f}")
    print(f"  Output: ${output_cost:.6f}")
    print(f"  Total:  ${total_cost:.6f}")


def analyze(video_path, prompt, model, show_cost):
    """Analyze a video file using Gemini."""
    load_dotenv()

    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY not found in environment or .env file", file=sys.stderr)
        sys.exit(1)

    if not os.path.exists(video_path):
        print(f"Error: Video file not found: {video_path}", file=sys.stderr)
        sys.exit(1)

    client = genai.Client(api_key=api_key)

    # Upload video
    print(f"Uploading video: {video_path}")
    myfile = client.files.upload(file=video_path)
    print(f"Upload complete. File URI: {myfile.uri}")

    # Wait for processing
    print("Waiting for file to be processed...", end="")
    myfile = wait_for_processing(client, myfile)

    if myfile.state.name == "FAILED":
        print(f"Error: File processing failed", file=sys.stderr)
        sys.exit(1)

    print(f"File state: {myfile.state.name}")

    # Generate analysis
    print(f"\nAnalyzing video with {model}...")
    response = client.models.generate_content(
        model=model,
        contents=[myfile, prompt]
    )

    print("\n--- Video Analysis ---")
    print(response.text)

    # Show usage if requested
    if show_cost and hasattr(response, 'usage_metadata'):
        print_usage(response.usage_metadata)


def main():
    """Main entry point for the CLI."""
    parser = argparse.ArgumentParser(
        prog="ponty",
        description="Analyze videos using Google's Gemini API"
    )
    parser.add_argument(
        "video",
        help="Path to the video file to analyze"
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
    analyze(args.video, args.prompt, args.model, show_cost=not args.no_cost)


if __name__ == "__main__":
    main()
