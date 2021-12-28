import streamlit as st
import pandas as pd
df = pd.read_csv('dataframe2.csv')


data_file = st.file_uploader("Upload CSV",type=["csv"])
if data_file is not None:
	df0 = pd.read_csv(data_file)
	df["AddNum"] = df["AddNum"].apply(pd.to_numeric)

	df0["delstreetno"] = df0["delstreetno"].apply(pd.to_numeric)

	df["jointadd"] = df["AddNum"].astype(str) + " " + df["StPreDir"] + " " + df["StName"] + " " + df["StSuffix"]
	df0["jointadd"] = df0["delstreetno"].astype(str) + " " + df0["delstreet"]

	result3 = pd.merge(df0, df, on="jointadd", how='left')
	result4 = result3.drop_duplicates(subset=["jointadd"])
	result5 = result4.rename(columns={'jointadd': 'Address Line 1', }, inplace=False)

	precircuit = result5[
		['Address Line 1', 'delstreetno', 'delstreet', 'delzip', 'delsuite', 'longitude', 'latitude', 'pieces', 'lbs',
		 'service', 'delname', 'Name']]

	precircuit = precircuit.rename(columns={'Name': 'delRoute', 'delstreetno': 'houseNumber', }, inplace=False)

	# recircuit2 = precircuit.rename(columns = {'jointadd': 'Address Line 1',}, inplace = False)
	st.dataframe(precircuit)

datadownld=precircuit.to_csv('712.csv')

@st.cache
def convert_df(datadownld):
    return df.to_csv().encode('utf-8')


csv = convert_df(df)

st.download_button(
    "Press to Download",
    csv,
    "yur_route.csv",
    "text/csv",
    key='browser-data'
)

