import moviepy.editor

video = moviepy.editor.VideoFileClip("Nvidia.mp4")
audio = video.audio

audio.write_audiofile('Nvidia.mp3')
audio.write_audiofile('Nvidia (1).mp3')