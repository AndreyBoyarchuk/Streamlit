import streamlit as st

# Basics & Fundamentals

#Core Pkgs

#Working with and Displaying text
st.text("hello")
st.header("this is a header")
st.subheader("this is subheader")
st.title("this is subtlte")
st.markdown("this is markdown")

#Displaying colored text
st.success("successful")
st.warning("This is dangerous --Warning message")
st.info("this is information")
st.exception("this is exception")

#Superfunction
st.write("## This is a markdown text")
st.write("This is a normal text")
st.write(1+2)
st.help(range)
st.write(dir(st))