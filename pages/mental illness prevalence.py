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

st.set_page_config(layout="wide")
st.title("Mental illness prevalence")
st.subheader("analysis")
df = pd.read_csv(r"data\1- mental-illnesses-prevalence.csv")
df = df.rename(columns={
    'Schizophrenia disorders (share of population) - Sex: Both - Age: Age-standardized':'Schizophrenia',
    'Depressive disorders (share of population) - Sex: Both - Age: Age-standardized': 'Depression',
    'Anxiety disorders (share of population) - Sex: Both - Age: Age-standardized':'Anxiety',
    'Bipolar disorders (share of population) - Sex: Both - Age: Age-standardized':'Bipolar disorder',
    'Eating disorders (share of population) - Sex: Both - Age: Age-standardized': 'Eating disorder'
})

num_cols = df.select_dtypes(include='number').columns.tolist()
num_cols.remove('Year')
cat_cols = df.select_dtypes(exclude='number').columns.tolist()
cat_cols.append('Year')

# Data2 = pd.read_csv(r"data\4- adult-population-covered-in-primary-data-on-the-prevalence-of-mental-illnesses.csv")
# Data3 = pd.read_csv(r"data\6- depressive-symptoms-across-us-population.csv")
# Data4 = pd.read_csv(r"data\7- number-of-countries-with-primary-data-on-prevalence-of-mental-illnesses-in-the-global-burden-of-disease-study.csv")

with st.expander("Show raw data"):
    st.dataframe(df, use_container_width=True)

c1, c2, c3 = st.columns(3)
c1.markdown(f'''
<p style="color:green"> Columns in the dataset</p>
{"<br>".join(df.columns.tolist())}
''', unsafe_allow_html=True)


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

st.header("visualization")

c1, c2 = st.columns(2)
x = c1.selectbox("Select a numerical column", num_cols, key='x1')
y = c2.selectbox("Select a categorical column", cat_cols, key='y1')
fig = px.scatter(df, x=x, y=y)
fig2 = px.histogram(df, x=x, y=y,)
c1.plotly_chart(fig, use_container_width=True)
c2.plotly_chart(fig2, use_container_width=True)

st.header("Eating disorder")
c3= st.columns(1)
c3 = (
   alt.Chart(df)
   .mark_bar()
   .encode(x="Eating disorder", y="Entity")
)

st.altair_chart(c3, use_container_width=True)

st.header("Anxiety")
c2= st.columns(1)
c2=(
   alt.Chart(df)
   .mark_bar()
   .encode(x="Anxiety", y="Entity")
)

st.altair_chart(c2, use_container_width=True)

st.header("Bipolar disorder")
c1=st.columns(1)
c1=(
   alt.Chart(df)
   .mark_bar()
   .encode(x="Bipolar disorder", y="Entity")
)

st.altair_chart(c1, use_container_width=True)

st.header("Depression")
c1=st.columns(1)
c1=(
   alt.Chart(df)
   .mark_bar()
   .encode(x="Depression", y="Entity")
)

st.altair_chart(c1, use_container_width=True)

st.header("Schizophrenia")
c2=st.columns(1)
c2=(
   alt.Chart(df)
   .mark_bar()
   .encode(x="Schizophrenia", y="Entity")
)

st.altair_chart(c2, use_container_width=True)








