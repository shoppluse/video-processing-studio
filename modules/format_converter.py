from moviepy.editor import VideoFileClip

def convert_format(input_path, output_path):

    clip = VideoFileClip(input_path)

    clip.write_videofile(output_path)

    clip.close()
