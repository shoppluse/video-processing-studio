from moviepy.editor import VideoFileClip

def cut_video(input_path, start_time, end_time, output_path):

    clip = VideoFileClip(input_path)

    trimmed = clip.subclip(start_time, end_time)

    trimmed.write_videofile(output_path)

    clip.close()
    trimmed.close()
