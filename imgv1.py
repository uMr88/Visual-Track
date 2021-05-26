import cv2
import os
import moviepy.editor as mpe

# duration 
import mutagen
from mutagen.wave import WAVE

image_folder = 'musicv'
video_name = 'video1.avi'
audio_name='123.wav'
outname='v1'

#duration
audio = WAVE(audio_name)

audio_info = audio.info
length = int(audio_info.length)
print(length)

#create video from images

images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]

lenimg=len(images)
print(lenimg)

frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')

duration=int(lenimg/length)

print(duration)
#duration=duration+1
video = cv2.VideoWriter(video_name, fourcc, duration, (width,height))


for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

cv2.destroyAllWindows()
video.release()

#add audio to created video


clip = mpe.VideoFileClip(video_name)
audio_bg = mpe.AudioFileClip(audio_name)

final_clip = clip.set_audio(audio_bg)
final_clip.write_videofile("output1.mp4")