from moviepy.editor import VideoFileClip

def convert_format(input_path, output_path):

    clip = VideoFileClip(input_path)

    if output_path.endswith(".mp4"):

        clip.write_videofile(
            output_path,
            codec="libx264",
            audio_codec="aac"
        )

    elif output_path.endswith(".avi"):

        clip.write_videofile(
            output_path,
            codec="mpeg4"
        )

    clip.close()
