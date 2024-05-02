import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import seaborn as sns 
import streamlit as st
import altair as alt
import warnings
warnings.filterwarnings("ignore")

df = pd.read_csv(r"data\6- depressive-symptoms-across-us-population.csv")
with st.expander("Show raw data"):
    st.dataframe(df, use_container_width=True)

c1, c2 ,c3  = st.columns(3)
c1.markdown(f'''
<p style="color:blue"> Columns in the dataset</p>
{"<br>".join(df.columns.tolist())}
''', unsafe_allow_html=True)

num_cols = df.select_dtypes(include='number').columns.tolist()
num_cols.remove('Year')
cat_cols = df.select_dtypes(exclude='number').columns.tolist()
cat_cols.append('Year')

sel_col = c2.selectbox("select column for stats", df.columns)
if sel_col in cat_cols:
    c2.metric(f"Column size", value=df[sel_col].size)
    c2.metric(f"Total Unique value", value=df[sel_col].nunique())
    c2.metric(f'Most common value', value=df[sel_col].value_counts().idxmax())
else:
    c2.metric(f"Column size", value=df[sel_col].size)
    c2.metric(f"Mean", value=df[sel_col].mean())
    c2.metric(f"Max ", value=df[sel_col].max())
    c2.metric(f"Min ", value=df[sel_col].min())

c3.dataframe(df[sel_col], use_container_width=True)


c1, c2 = st.columns(2)
x = c1.selectbox("Select a numerical column", num_cols, key='x1')
y = c2.selectbox("Select a categorical column", cat_cols, key='y1')
c1= st.columns(1)
c1 = (
   alt.Chart(df)
   .mark_bar()
   .encode(x=x, y=y)
)
st.altair_chart(c1, use_container_width=True)



