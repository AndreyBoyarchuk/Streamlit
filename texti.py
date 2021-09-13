import streamlit as st

fname =st.text_input("Enter Firstname",max_chars=20)
st.title(fname)

lname =st.text_input("Enter barcode")

st.title(lname)

message =st.text_area("Enter Message")

number =st.number_input("Enter Number",1,25)

dateinputst= st.date_input("Appoitment")

tinput=st.time_input("myTime")

password=st.text_input("EnterPassword", type='password')

color=st.color_picker("Select Color")