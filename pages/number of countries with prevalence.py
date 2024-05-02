import streamlit as st 
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import seaborn as sns 
import altair as alt
import warnings
warnings.filterwarnings("ignore")

df = pd.read_csv(r"data\7- number-of-countries-with-primary-data-on-prevalence-of-mental-illnesses-in-the-global-burden-of-disease-study.csv")
with st.expander("Show raw data"):
    st.dataframe(df, use_container_width=True)

df = df.rename(columns={
    'Number of countries with primary data on prevalence of mental disorders':'Countries',
})

num_cols = df.select_dtypes(include='number').columns.tolist()
num_cols.remove('Year')
cat_cols = df.select_dtypes(exclude='number').columns.tolist()
cat_cols.append('Year')

c1, c2, c3 = st.columns(3)
c1.markdown(f'''
<p style="color:blue"> Columns in the dataset</p>
{"<br>".join(df.columns.tolist())}
''', unsafe_allow_html=True)

c1, c2 = st.columns(2)
x = c1.selectbox("Select a numerical column", num_cols, key='x1')
y = c2.selectbox("Select a categorical column", cat_cols, key='y1')
fig = px.scatter(df, x=x, y=y)
fig2 = px.histogram(df, x=x, y=y,)
c1.plotly_chart(fig, use_container_width=True)
c2.plotly_chart(fig2, use_container_width=True)

c1= st.columns(1)
c1 = (
   alt.Chart(df)
   .mark_bar()
   .encode(x="Entity", y="Countries")
)

st.altair_chart(c1, use_container_width=True)

