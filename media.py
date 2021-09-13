import  streamlit as st
from PIL import Image

# display image
img = Image.open('image_03.jpg')
st.image(img,use_column_width=True)

video_file =open('secret_of_success.mp4','rb').read()
st.video(video_file,start_time=3)
audio_file=open("song.mp3","rb")
st.audio(audio_file.read())