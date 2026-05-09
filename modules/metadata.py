from moviepy.editor import VideoFileClip

def get_metadata(video_path):

    clip = VideoFileClip(video_path)

    data = {
        "Duration": clip.duration,
        "FPS": clip.fps,
        "Resolution": clip.size
    }

    clip.close()

    return data
