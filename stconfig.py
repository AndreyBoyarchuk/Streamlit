import streamlit as st
import pandas as pd
#st.set_page_config(page_title='hello', page_icon='✏️', layout='wide', initial_sidebar_state='collapsed')

PAGE_CONFIG= {"page_title":"AndreyB","page_icon":":smiley", "layout":"centered"}
st.set_page_config(**PAGE_CONFIG)

def main():
    st.title("Hello Streamlit Lovers")
    st.sidebar.success("Menu")

    st.title("Plotting in Streamlit with Plotly ")
    df =pd.read_csv("data/prog_languages_data.csv")
    st.dataframe(df)

if __name__ == '__main__':
    main()