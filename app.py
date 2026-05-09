import streamlit as st
import os
import glob

from modules.cutter import cut_video
from modules.gif_converter import convert_to_gif
from modules.frame_extractor import extract_frames
from modules.format_converter import convert_format
from modules.speed_controller import change_speed
from modules.metadata import get_metadata


# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Video Processing Studio",
    page_icon="🎬",
    layout="wide"
)

st.title("🎬 Video Processing Studio")
st.markdown("### One Platform For All Video Operations")


# =========================
# CREATE FOLDERS
# =========================

os.makedirs("uploads", exist_ok=True)
os.makedirs("outputs", exist_ok=True)


# =========================
# SIDEBAR
# =========================

st.sidebar.title("📌 Features")

feature = st.sidebar.radio(
    "Choose Tool",
    [
        "Video Cutter",
        "GIF Converter",
        "Frame Extractor",
        "Format Converter",
        "Speed Controller",
        "Metadata Viewer"
    ]
)


# =========================
# FILE UPLOAD
# =========================

uploaded_file = st.file_uploader(
    "Upload Video File",
    type=["mp4", "avi", "mov", "mkv"]
)

if uploaded_file is not None:

    upload_path = os.path.join(
        "uploads",
        uploaded_file.name
    )

    # Save uploaded file
    with open(upload_path, "wb") as f:
        f.write(uploaded_file.read())

    st.success("✅ Video Uploaded Successfully!")

    # =========================
    # VIDEO PREVIEW
    # =========================

    st.subheader("🎥 Video Preview")

    st.video(upload_path)

    st.divider()

    # =========================================================
    # 1. VIDEO CUTTER
    # =========================================================

    if feature == "Video Cutter":

        st.header("✂️ Video Cutter")

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

        if st.button("Cut Video"):

            output_path = "outputs/cut_video.mp4"

            with st.spinner("Processing Video..."):

                cut_video(
                    upload_path,
                    start_time,
                    end_time,
                    output_path
                )

            st.success("✅ Video Trimmed Successfully!")

            st.video(output_path)

            with open(output_path, "rb") as file:
                st.download_button(
                    "⬇️ Download Video",
                    file,
                    file_name="cut_video.mp4"
                )

    # =========================================================
    # 2. GIF CONVERTER
    # =========================================================

    elif feature == "GIF Converter":

        st.header("🎞️ Video to GIF Converter")

        duration = st.slider(
            "GIF Duration (seconds)",
            1,
            15,
            5
        )

        if st.button("Convert to GIF"):

            output_path = "outputs/output.gif"

            with st.spinner("Creating GIF..."):

                convert_to_gif(
                    upload_path,
                    output_path
                )

            st.success("✅ GIF Created Successfully!")

            st.image(output_path)

            with open(output_path, "rb") as file:
                st.download_button(
                    "⬇️ Download GIF",
                    file,
                    file_name="output.gif"
                )

    # =========================================================
    # 3. FRAME EXTRACTOR
    # =========================================================

    elif feature == "Frame Extractor":

        st.header("🖼️ Frame Extractor")

        interval = st.slider(
            "Extract Every N Frames",
            10,
            100,
            30
        )

        if st.button("Extract Frames"):

            with st.spinner("Extracting Frames..."):

                extract_frames(
                    upload_path,
                    "outputs",
                    interval
                )

            st.success("✅ Frames Extracted Successfully!")

            frames = glob.glob("outputs/frame_*.jpg")

            if frames:

                st.subheader("Extracted Frames")

                for frame in frames[:10]:
                    st.image(frame, width=250)

    # =========================================================
    # 4. FORMAT CONVERTER
    # =========================================================

    elif feature == "Format Converter":

        st.header("🔄 Video Format Converter")

        format_choice = st.selectbox(
            "Choose Output Format",
            ["mp4", "avi"]
        )

        if st.button("Convert Format"):

            output_path = f"outputs/converted_video.{format_choice}"

            with st.spinner("Converting Format..."):

                convert_format(
                    upload_path,
                    output_path
                )

            st.success("✅ Format Converted Successfully!")

            st.video(output_path)

            with open(output_path, "rb") as file:
                st.download_button(
                    "⬇️ Download Converted Video",
                    file,
                    file_name=f"converted_video.{format_choice}"
                )

    # =========================================================
    # 5. SPEED CONTROLLER
    # =========================================================

    elif feature == "Speed Controller":

        st.header("⏩ Video Speed Controller")

        speed_factor = st.slider(
            "Speed Factor",
            0.5,
            3.0,
            1.0
        )

        if st.button("Apply Speed Change"):

            output_path = "outputs/speed_changed.mp4"

            with st.spinner("Changing Video Speed..."):

                change_speed(
                    upload_path,
                    speed_factor,
                    output_path
                )

            st.success("✅ Speed Modified Successfully!")

            st.video(output_path)

            with open(output_path, "rb") as file:
                st.download_button(
                    "⬇️ Download Video",
                    file,
                    file_name="speed_changed.mp4"
                )

    # =========================================================
    # 6. METADATA VIEWER
    # =========================================================

    elif feature == "Metadata Viewer":

        st.header("📊 Video Metadata")

        data = get_metadata(upload_path)

        st.info(f"🎥 Duration : {round(data['Duration'], 2)} seconds")
        st.info(f"⚡ FPS : {data['FPS']}")
        st.info(f"📺 Resolution : {data['Resolution'][0]} x {data['Resolution'][1]}")

else:

    st.warning("⚠️ Please Upload a Video File")
