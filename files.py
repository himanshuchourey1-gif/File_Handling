import streamlit as st
import pandas as pd
st.subheader('Loading a file')
df =st.file_uploader('Load a .csv/.xlxs file', type = ['csv','xlsx'])
if df is not None:
    st.dataframe(df)
df = pd.read_csv(r"C:\Users\himan\Desktop\Streamlit\ref\product_template.csv")
st.table(df.head())
st.subheader("Images")
st.image(r'C:\Users\himan\Pictures\Screenshots\Screenshot (3).png')
st.subheader("Dealing with image while uploading")
img = st.file_uploader('Load a image',type = ['jpeg','png'])
if img is not None:
    st.image(img)

video_file = st.file_uploader('Load a videofile',type = ['mkv','mp4'])
if video_file is not None:
    st.video(video_file)
