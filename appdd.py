import streamlit as st
import pandas as pd

df= pd.read_csv('iris.csv')

st.dataframe(df)
st.dataframe(df,200,100)
st.dataframe(df.style.highlight_max(axis=0))

st.write(df.head(2))
st.json({'data':'name'})

mycode ="""
def sayhello():
  print("hello :)")
"""
st.code(mycode,language='python')