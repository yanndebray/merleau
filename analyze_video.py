import os
import time
from dotenv import load_dotenv
from google import genai

# Load environment variables from .env file
load_dotenv()

# Initialize the client with the API key
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Upload the video file
video_path = "MATLAB_Modernizer.mp4"
print(f"Uploading video: {video_path}")
myfile = client.files.upload(file=video_path)
print(f"Upload complete. File URI: {myfile.uri}")

# Wait for the file to be processed (become ACTIVE)
print("Waiting for file to be processed...")
while myfile.state.name == "PROCESSING":
    print(".", end="", flush=True)
    time.sleep(2)
    myfile = client.files.get(name=myfile.name)

if myfile.state.name == "FAILED":
    raise ValueError(f"File processing failed: {myfile.state.name}")

print(f"\nFile state: {myfile.state.name}")

# Generate content using Gemini 2.5 Flash
print("\nAnalyzing video with Gemini 2.5 Flash...")
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[myfile, "Explain what happens in this video"]
)
print("\n--- Video Analysis ---")
print(response.text)

# Show usage/cost information
print("\n--- Usage Information ---")
if hasattr(response, 'usage_metadata'):
    usage = response.usage_metadata
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
