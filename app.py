# 🚀 Enhanced Video Processing Studio UI

Replace your current `app.py` with the following upgraded version.

```python
import streamlit as st
import os
import glob

from modules.cutter import cut_video
from modules.gif_converter import convert_to_gif
from modules.frame_extractor import extract_frames
from modules.format_converter import convert_format
from modules.speed_controller import change_speed
from modules.metadata import get_metadata

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Video Processing Studio",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================
# CUSTOM CSS
# =====================================================

st.markdown(
    """
    <style>

    .main {
        background: linear-gradient(to bottom right, #050816, #0f172a);
        color: white;
    }

    .hero {
        padding: 40px;
        border-radius: 25px;
        background: linear-gradient(135deg, #7c3aed, #2563eb);
        text-align: center;
        margin-bottom: 30px;
        box-shadow: 0px 0px 25px rgba(0,0,0,0.4);
    }

    .hero h1 {
        color: white;
        font-size: 55px;
        margin-bottom: 10px;
    }

    .hero p {
        color: #e2e8f0;
        font-size: 20px;
    }

    .feature-card {
        background: rgba(255,255,255,0.06);
        padding: 20px;
        border-radius: 20px;
        backdrop-filter: blur(10px);
        box-shadow: 0px 0px 20px rgba(255,255,255,0.08);
        margin-bottom: 20px;
    }

    .metric-box {
        background: linear-gradient(135deg,#1e293b,#111827);
        padding: 20px;
        border-radius: 18px;
        text-align: center;
        box-shadow: 0px 0px 20px rgba(0,0,0,0.3);
    }

    .metric-box h2 {
        color: #38bdf8;
        margin: 0;
    }

    .metric-box p {
        color: #cbd5e1;
        font-size: 18px;
    }

    .stButton>button {
        width: 100%;
        border-radius: 12px;
        height: 3.2em;
        font-size: 18px;
        font-weight: bold;
        background: linear-gradient(135deg,#2563eb,#7c3aed);
        color: white;
        border: none;
        transition: 0.3s;
    }

    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0px 0px 15px rgba(124,58,237,0.5);
    }

    </style>
    """,
    unsafe_allow_html=True
)

# =====================================================
# CREATE REQUIRED FOLDERS
# =====================================================

os.makedirs("uploads", exist_ok=True)
os.makedirs("outputs", exist_ok=True)

# =====================================================
# HERO SECTION
# =====================================================

st.markdown(
    """
    <div class="hero">
        <h1>🎬 Video Processing Studio</h1>
        <p>Professional Video Utilities Platform Built Using Python + Streamlit</p>
    </div>
    """,
    unsafe_allow_html=True
)

# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.title("⚡ Video Tools")

feature = st.sidebar.radio(
    "Choose Feature",
    [
        "✂️ Video Cutter",
        "🎞️ GIF Converter",
        "🖼️ Frame Extractor",
        "🔄 Format Converter",
        "⏩ Speed Controller",
        "📊 Metadata Viewer"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info(
    "Built with Python, OpenCV, MoviePy, and Streamlit"
)

# =====================================================
# FILE UPLOAD
# =====================================================

uploaded_file = st.file_uploader(
    "📤 Upload Your Video",
    type=["mp4", "avi", "mov", "mkv"]
)

if uploaded_file is not None:

    upload_path = os.path.join(
        "uploads",
        uploaded_file.name
    )

    with open(upload_path, "wb") as f:
        f.write(uploaded_file.read())

    st.success("✅ Video Uploaded Successfully")

    # =====================================================
    # VIDEO PREVIEW
    # =====================================================

    st.markdown("## 🎥 Video Preview")

    st.video(upload_path)

    st.markdown("---")

    # =====================================================
    # VIDEO CUTTER
    # =====================================================

    if feature == "✂️ Video Cutter":

        st.markdown("## ✂️ Smart Video Cutter")

        col1, col2 = st.columns(2)

        with col1:
            start_time = st.number_input(
                "Start Time (seconds)",
                min_value=0,
                value=0
            )

        with col2:
            end_time = st.number_input(
                "End Time (seconds)",
                min_value=1,
                value=10
            )

        if st.button("🚀 Process Video"):

            output_path = "outputs/cut_video.mp4"

            progress = st.progress(0)

            for i in range(100):
                progress.progress(i + 1)

            cut_video(
                upload_path,
                start_time,
                end_time,
                output_path
            )

            st.success("✅ Video Trimmed Successfully")

            st.video(output_path)

            with open(output_path, "rb") as file:
                st.download_button(
                    "⬇️ Download Trimmed Video",
                    file,
                    file_name="cut_video.mp4"
                )

    # =====================================================
    # GIF CONVERTER
    # =====================================================

    elif feature == "🎞️ GIF Converter":

        st.markdown("## 🎞️ Video To GIF Converter")

        if st.button("⚡ Generate GIF"):

            output_path = "outputs/output.gif"

            convert_to_gif(
                upload_path,
                output_path
            )

            st.success("✅ GIF Created Successfully")

            st.image(output_path)

            with open(output_path, "rb") as file:
                st.download_button(
                    "⬇️ Download GIF",
                    file,
                    file_name="output.gif"
                )

    # =====================================================
    # FRAME EXTRACTOR
    # =====================================================

    elif feature == "🖼️ Frame Extractor":

        st.markdown("## 🖼️ AI Style Frame Extractor")

        interval = st.slider(
            "Frame Interval",
            10,
            100,
            30
        )

        if st.button("📸 Extract Frames"):

            extract_frames(
                upload_path,
                "outputs",
                interval
            )

            st.success("✅ Frames Extracted")

            frames = glob.glob("outputs/frame_*.jpg")

            cols = st.columns(3)

            for index, frame in enumerate(frames[:9]):
                with cols[index % 3]:
                    st.image(frame)

    # =====================================================
    # FORMAT CONVERTER
    # =====================================================

    elif feature == "🔄 Format Converter":

        st.markdown("## 🔄 Universal Format Converter")

        format_choice = st.selectbox(
            "Choose Output Format",
            ["mp4", "avi"]
        )

        if st.button("🎬 Convert Video"):

            output_path = f"outputs/converted_video.{format_choice}"

            convert_format(
                upload_path,
                output_path
            )

            st.success("✅ Conversion Completed")

            if format_choice == "mp4":
                st.video(output_path)
            else:
                st.info("AVI created successfully. Download to view.")

            with open(output_path, "rb") as file:
                st.download_button(
                    "⬇️ Download Converted Video",
                    file,
                    file_name=f"converted_video.{format_choice}"
                )

    # =====================================================
    # SPEED CONTROLLER
    # =====================================================

    elif feature == "⏩ Speed Controller":

        st.markdown("## ⏩ Playback Speed Controller")

        speed_factor = st.slider(
            "Choose Speed",
            0.5,
            3.0,
            1.0
        )

        if st.button("⚡ Apply Speed Change"):

            output_path = "outputs/speed_changed.mp4"

            change_speed(
                upload_path,
                speed_factor,
                output_path
            )

            st.success("✅ Speed Modified Successfully")

            st.video(output_path)

            with open(output_path, "rb") as file:
                st.download_button(
                    "⬇️ Download Video",
                    file,
                    file_name="speed_changed.mp4"
                )

    # =====================================================
    # METADATA VIEWER
    # =====================================================

    elif feature == "📊 Metadata Viewer":

        st.markdown("## 📊 Advanced Video Analytics")

        data = get_metadata(upload_path)

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown(
                f"""
                <div class="metric-box">
                    <h2>{round(data['Duration'], 2)} s</h2>
                    <p>Duration</p>
                </div>
                """,
                unsafe_allow_html=True
            )

        with col2:
            st.markdown(
                f"""
                <div class="metric-box">
                    <h2>{data['FPS']}</h2>
                    <p>FPS</p>
                </div>
                """,
                unsafe_allow_html=True
            )

        with col3:
            st.markdown(
                f"""
                <div class="metric-box">
                    <h2>{data['Resolution'][0]} x {data['Resolution'][1]}</h2>
                    <p>Resolution</p>
                </div>
                """,
                unsafe_allow_html=True
            )

else:

    st.markdown(
        """
        <div class="feature-card">
            <h2>🚀 Welcome to Video Processing Studio</h2>
            <p>
            Upload a video and access powerful tools like:
            </p>
            <ul>
                <li>✂️ Video Trimming</li>
                <li>🎞️ GIF Conversion</li>
                <li>🖼️ Frame Extraction</li>
                <li>🔄 Format Conversion</li>
                <li>⏩ Speed Control</li>
                <li>📊 Metadata Analysis</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

```

# 🔥 What Changed

* Modern glassmorphism UI
* Gradient hero section
* Better sidebar
* Animated buttons
* Professional cards
* Metadata dashboard
* Better frame gallery layout
* Progress bar effects
* Modern typography
* Improved user experience

This will make your project look like a real startup-level web app instead of a normal college project.
