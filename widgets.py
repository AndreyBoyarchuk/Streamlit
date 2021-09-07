import streamlit as st

name = "Issabella"
if st.button("Submit"):
    st.write("Name : {}".format(name.upper()))

status  =st.radio("What is your status", ("Active", "Inactive"))

if status =='Active':
    st.success("You are active")
elif status =="Inactive":
    st.warning("Inactive")

if st.checkbox("Show/Hide"):
    st.text("Showing something")

if st.expander("Python"):
    st.success("Hello Python")

if st.expander("Python"):
    st.text("Hello Python")

with st.expander("Python"):
    st.text("Hello Python")

my_lang= ["Python", "Julia", "Go","Rust"]

choice= st.selectbox("Language", my_lang)
st.write("You selected {}".format(choice))

spoken_lang = ("English", "French","Spanish", "Russian")
my_spoken_lang=st.multiselect("Spoken Lang", spoken_lang, default="English")

age= st.slider("Age", 1,100)

color= st.select_slider("Choose color", options=['yellow','red', 'blue',"black","white"])

