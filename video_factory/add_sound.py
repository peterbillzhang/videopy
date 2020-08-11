from moviepy.editor import VideoFileClip, AudioFileClip

videoclip = VideoFileClip("covid_19.mp4")
audioclip = AudioFileClip("resources/music/mixkit-valley-sunset-127.mp3")

# set audio and trim to video length, set fadein and fadeout
videoclip.audio = audioclip.set_duration(videoclip.duration + 4).audio_fadeout(2.0).audio_fadein(2.0)

# save file
videoclip.write_videofile("covid_19_music.mp4")
