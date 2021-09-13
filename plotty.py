import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

def main():
    st.title("Plotting in Streamlit with Plotly ")
    df =pd.read_csv("data/prog_languages_data.csv")
    st.dataframe(df)
    fig=px.pie(df, values='Sum', names='lang',title="pip Chart")
    st.plotly_chart(fig)
    fig2=px.bar(df,y='Sum', x='lang',title="bar Chart")
    st.plotly_chart(fig2)



if __name__ == '__main__':
    main()