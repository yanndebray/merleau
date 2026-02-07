"""Streamlit web interface for Merleau video analysis."""

import os
import tempfile

import streamlit as st
from dotenv import load_dotenv

from merleau.cli import AnalysisResult, analyze_video, is_youtube_url

# Page config
st.set_page_config(
    page_title="Merleau - Video Understanding",
    page_icon="👁️",
    layout="centered",
)

# Load environment variables
load_dotenv()


# Header
st.title("👁️ Merleau")
st.markdown("*Video understanding from your browser*")

# Sidebar for settings
with st.sidebar:
    st.header("Settings")

    api_key = st.text_input(
        "Gemini API Key",
        type="password",
        value=os.getenv("GEMINI_API_KEY", ""),
        help="Get your key from [Google AI Studio](https://aistudio.google.com/apikey)"
    )

    model = st.selectbox(
        "Model",
        ["gemini-2.5-flash", "gemini-2.0-flash", "gemini-1.5-pro"],
        index=0,
    )

    st.divider()
    st.markdown("""
    **Links**
    - [GitHub](https://github.com/yanndebray/merleau)
    - [PyPI](https://pypi.org/project/merleau/)
    - [Documentation](https://yanndebray.github.io/merleau/)
    """)

# Main content
tab1, tab2, tab3 = st.tabs(["📁 Upload Video", "🔗 YouTube URL", "🎬 Record Screen"])

with tab1:
    uploaded_file = st.file_uploader(
        "Choose a video file",
        type=["mp4", "mov", "avi", "mkv", "webm"],
        help="Supported formats: MP4, MOV, AVI, MKV, WebM"
    )

    if uploaded_file:
        st.video(uploaded_file)

with tab2:
    youtube_url = st.text_input(
        "YouTube URL",
        placeholder="https://www.youtube.com/watch?v=... or https://youtu.be/...",
        help="Paste a YouTube video URL to analyze directly"
    )

    if youtube_url and is_youtube_url(youtube_url):
        st.video(youtube_url)
    elif youtube_url:
        st.warning("Please enter a valid YouTube URL.")

with tab3:
    st.info("🎥 **Screen Recording** - Record your screen, then upload the recording in the Upload tab.")
    st.markdown("""
    **Quick recording options:**
    1. **Streamlit built-in** — Click the screencast button in the bottom-right corner of this app
    2. **Windows** — `Win + G` → Record
    3. **Mac** — `Cmd + Shift + 5` → Screen Recording
    4. **Chrome** — Extensions like Loom or Screencastify
    """)
    st.image("img/streamlit-screencast.png", caption="Streamlit's built-in screencast recorder")

# Prompt input
st.divider()
prompt = st.text_area(
    "What would you like to know about the video?",
    value="Explain what happens in this video",
    height=100,
)

# Analyze button
col1, col2 = st.columns([3, 1])
with col1:
    analyze_btn = st.button("🔍 Analyze Video", type="primary", use_container_width=True)
with col2:
    show_cost = st.checkbox("Show cost", value=True)

# Determine video source
has_youtube = youtube_url and is_youtube_url(youtube_url)
has_upload = uploaded_file is not None

# Analysis
if analyze_btn:
    if not api_key:
        st.error("Please enter your Gemini API key in the sidebar.")
    elif not has_upload and not has_youtube:
        st.warning("Please upload a video file or enter a YouTube URL.")
    else:
        tmp_path = None
        if has_youtube:
            video_source = youtube_url
            source_name = youtube_url
        else:
            # Save uploaded file to temp location
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as tmp:
                tmp.write(uploaded_file.getvalue())
                tmp_path = tmp.name
            video_source = tmp_path
            source_name = uploaded_file.name

        try:
            # Progress indicators
            progress_text = st.empty()
            progress_bar = st.progress(0)

            if has_youtube:
                progress_text.text("🔗 Sending YouTube URL to Gemini...")
            else:
                progress_text.text("📤 Uploading video...")
            progress_bar.progress(10)

            def on_upload(uri):
                if not has_youtube:
                    progress_text.text("⏳ Processing video...")
                progress_bar.progress(30)

            processing_dots = [0]
            def on_processing():
                processing_dots[0] += 1
                progress = min(30 + (processing_dots[0] * 5), 70)
                progress_bar.progress(progress)

            def on_analyzing():
                progress_text.text("🧠 Analyzing with Gemini...")
                progress_bar.progress(80)

            result: AnalysisResult = analyze_video(
                video_path=video_source,
                prompt=prompt,
                model=model,
                api_key=api_key,
                on_upload=on_upload,
                on_processing=on_processing,
                on_analyzing=on_analyzing,
            )

            progress_bar.progress(100)
            progress_text.empty()
            progress_bar.empty()

            # Display results
            st.success("Analysis complete!")

            st.markdown("### 📝 Analysis")
            st.markdown(result.text)

            if show_cost:
                st.divider()
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Prompt Tokens", f"{result.prompt_tokens:,}")
                with col2:
                    st.metric("Response Tokens", f"{result.response_tokens:,}")
                with col3:
                    st.metric("Total Cost", f"${result.total_cost:.4f}")

            # Store in session for history
            if "history" not in st.session_state:
                st.session_state.history = []
            st.session_state.history.append({
                "filename": source_name,
                "prompt": prompt,
                "result": result.text,
                "cost": result.total_cost,
            })

        except Exception as e:
            st.error(f"Error: {e}")
        finally:
            # Cleanup temp file
            if tmp_path and os.path.exists(tmp_path):
                os.unlink(tmp_path)

# History section
if "history" in st.session_state and st.session_state.history:
    st.divider()
    with st.expander(f"📜 Analysis History ({len(st.session_state.history)} items)"):
        for i, item in enumerate(reversed(st.session_state.history)):
            st.markdown(f"**{item['filename']}** - ${item['cost']:.4f}")
            st.caption(f"Prompt: {item['prompt'][:50]}...")
            if st.button(f"Show full analysis", key=f"history_{i}"):
                st.markdown(item['result'])
            st.divider()
