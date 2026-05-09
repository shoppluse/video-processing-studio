from moviepy.editor import VideoFileClip

def convert_to_gif(input_path, output_path):

    clip = VideoFileClip(input_path).subclip(0, 5)

    clip.write_gif(output_path)

    clip.close()
