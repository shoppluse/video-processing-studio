from moviepy.editor import VideoFileClip
import moviepy.video.fx.all as vfx

def change_speed(input_path, factor, output_path):

    clip = VideoFileClip(input_path)

    final = clip.fx(vfx.speedx, factor)

    final.write_videofile(output_path)

    clip.close()
    final.close()
