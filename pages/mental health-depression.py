import streamlit as st
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import seaborn as sns 
import warnings
warnings.filterwarnings("ignore")


df = pd.read_csv(r'C:\Users\SHRUTI\Desktop\MHDD\data\Mental health Depression disorder Data.csv')
df = pd.DataFrame(df, columns=df.columns)
df = df.drop("index",axis=1)
df_1 = df.iloc[0:6468, :]
# drop extra columns
df_1.drop(columns=['Code'], inplace=True)
# rename the columns
map_names = {'Entity': 'country',
             'Year' : 'year',
             'Schizophrenia (%)':'schizo', 
             'Bipolar disorder (%)':'bipolar',
             'Eating disorders (%)' : 'eating_dis',
             'Anxiety disorders (%)' : 'anxiety',
             'Drug use disorders (%)':'drug',
             'Depression (%)':'depres',
             'Alcohol use disorders (%)':'alcohol'}
df_1.rename(columns=map_names,inplace=True)

# change the type of columns so that we could analyze better
df_1['year'] = df_1['year'].astype(int)
df_1['schizo'] = df_1['schizo'].astype(float)
df_1['bipolar'] = df_1['bipolar'].astype(float)
df_1['eating_dis'] = df_1['eating_dis'].astype(float)
df_1['anxiety'] = df_1['anxiety'].astype(float)
df_1['drug'] = df_1['drug'].astype(float)
df_1['depres'] = df_1['depres'].astype(float)
df_1['alcohol'] = df_1['alcohol'].astype(float)

cont_1 = ['cont',
          'country',
          'schizo',
          'bipolar',
          'eating_dis',
          'anxiety',
          'drug', 
          'depres',
          'alcohol']
cont_2017 = pd.DataFrame(columns = cont_1)

country_asia = ['China','India',
               'Indonesia','Pakistan',
               'Bangladesh','Japan',
               'Philippines','Vietnam',
               'Turkey','Iran',
               'Thailand','Myanmar',
               'South Korea','Iraq',
               'Afghanistan','Saudi Arabia',
               'Uzbekistan','Malaysia',
               'Yemen','Nepal',
               'North Korea','Sri Lanka',
               'Kazakhstan','Syria',
               'Cambodia','Jordan',
               'Azerbaijan','United Arab Emirates',
               'Tajikistan','Israel',
               'Laos','Lebanon',
               'Kyrgyzstan','Turkmenistan',
               'Singapore','Oman',
               'Kuwait','Georgia',
               'Mongolia','Armenia',
               'Qatar','Bahrain',
               'Cyprus','Bhutan']


sel_year = st.selectbox("select a year", range(1990,2018))
df_2017 = df_1.loc[df_1.year==sel_year]
with st.expander("Show country wise distribution"):  
    st.dataframe(df_2017)

mean_asia = {}
for row in range(len(df_2017)):
    country = df_2017.iloc[row]['country']
    if country in country_asia:
        if 'Asia' not in mean_asia:
            mean_asia['Asia'] = {'schizo': [], 'bipolar': [], 'eating_dis': [], 'anxiety': [], 'drug': [], 'depres': [], 'alcohol': []}
            mean_asia['Asia']['schizo'].append(df_2017.iloc[row]['schizo'])
            mean_asia['Asia']['bipolar'].append(df_2017.iloc[row]['bipolar'])
            mean_asia['Asia']['eating_dis'].append(df_2017.iloc[row]['eating_dis'])
            mean_asia['Asia']['anxiety'].append(df_2017.iloc[row]['anxiety'])
            mean_asia['Asia']['drug'].append(df_2017.iloc[row]['drug'])
            mean_asia['Asia']['depres'].append(df_2017.iloc[row]['depres'])
            mean_asia['Asia']['alcohol'].append(df_2017.iloc[row]['alcohol'])

if 'Asia' in mean_asia:
    asia_mean = {'cont': 'Asia',
                 'country':'Asian countries',
                 'schizo': np.mean(mean_asia['Asia']['schizo']),
                 'bipolar': np.mean(mean_asia['Asia']['bipolar']),
                 'eating_dis': np.mean(mean_asia['Asia']['eating_dis']),
                 'anxiety': np.mean(mean_asia['Asia']['anxiety']),
                 'drug': np.mean(mean_asia['Asia']['drug']),
                 'depres': np.mean(mean_asia['Asia']['depres']),
                 'alcohol': np.mean(mean_asia['Asia']['alcohol'])}
    print(asia_mean) 
    cont_2017 =  pd.concat([cont_2017,pd.DataFrame(asia_mean, index=range(1))])

country_europe = ['Albania','Andorra',
                 'Austria','Belarus',
                 'Belgium','Bulgaria',
                 'Crotia','Cyprus',
                 'Czech Republic','Denmark',
                 'Estonia','Finland',
                 'France','Germany',
                 'Greece','Hungary',
                 'Iceland','Ireland',
                 'Italy','Kosovo',
                 'Latvia','Liechtenstein',
                 'Lithuania','Luxembourg',
                 'Malta','Moldova',
                 'Monaco','Montenegro',
                 'Netherlands','North Macedonia',
                 'Norway','Norway',
                 'Poland','Portugal',
                 'Romania','Russia',
                 'San Marino','Serbia',
                 'Slovakia','Slovenia',
                 'Spain','Sweden',
                 'Switzerland','Ukraine',
                 'United Kingdom','Vatican']
mean_europe = {}
for row in range(len(df_2017)):
    country = df_2017.iloc[row]['country']
    if country in country_europe:
        if 'Europe' not in mean_europe:
            mean_europe['Europe'] = {'schizo': [], 'bipolar': [], 'eating_dis': [], 'anxiety': [], 'drug': [], 'depres': [], 'alcohol': []}
            mean_europe['Europe']['schizo'].append(df_2017.iloc[row]['schizo'])
            mean_europe['Europe']['bipolar'].append(df_2017.iloc[row]['bipolar'])
            mean_europe['Europe']['eating_dis'].append(df_2017.iloc[row]['eating_dis'])
            mean_europe['Europe']['anxiety'].append(df_2017.iloc[row]['anxiety'])
            mean_europe['Europe']['drug'].append(df_2017.iloc[row]['drug'])
            mean_europe['Europe']['depres'].append(df_2017.iloc[row]['depres'])
            mean_europe['Europe']['alcohol'].append(df_2017.iloc[row]['alcohol'])
if 'Europe' in mean_europe:
    europe_miangin = {'cont':'Europe',
                      'country':'European countries',
                     'schizo': np.mean(mean_europe['Europe']['schizo']),
                     'bipolar' : np.mean(mean_europe['Europe']['bipolar']),
                     'eating_dis': np.mean(mean_europe['Europe']['eating_dis']),
                     'anxiety': np.mean(mean_europe['Europe']['anxiety']),
                     'drug' : np.mean(mean_europe['Europe']['drug']),
                     'depres' : np.mean(mean_europe['Europe']['depres']),
                     'alcohol' : np.mean(mean_europe['Europe']['alcohol'])}
    print(europe_miangin)
    cont_2017 =  pd.concat([cont_2017,pd.DataFrame(europe_miangin, index=range(1))], axis=0)   
country_africa = ['Nigeria','Ethiopia',
                 'Egypt','DR Congo',
                 'Tanzania','South Africa',
                 'Kenya','Uganda',
                 'Algeria','Sudan',
                 'Morocco','Angola',
                 'Mozambique','Ghana',
                 'Madagascar','Cameroon',
                 'Côte d Ivoire','Niger',
                 'Burkina Faso','Mali',
                 'Malawi','Zambia',
                 'Senegal','Chad',
                 'Somalia','Zimbabwe',
                 'Guinea','Rwanda',
                 'Benin','Burundi',
                 'Tunisia','South Sudan',
                 'Togo','Sierra Leone',
                 'Libya','Congo',
                 'Liberia','Central African Republic',
                 'Mauritania','Eritrea',
                 'Namibia','Gambia',
                 'Botswana','Gabon',
                 'Lesotho','Guinea-Bissau',
                 'Equatorial Guinea','Mauritius',
                 'Eswatini','Djibouti',
                 'Comoros','Cabo Verde']

mean_africa = {}
for row in range(len(df_2017)):
    country = df_2017.iloc[row]['country']
    if country in country_africa:
        if 'Africa' not in mean_europe:
            mean_africa['Africa'] = {'schizo': [], 'bipolar': [], 'eating_dis': [], 'anxiety': [], 'drug': [], 'depres': [], 'alcohol': []}
            mean_africa['Africa']['schizo'].append(df_2017.iloc[row]['schizo'])
            mean_africa['Africa']['bipolar'].append(df_2017.iloc[row]['bipolar'])
            mean_africa['Africa']['eating_dis'].append(df_2017.iloc[row]['eating_dis'])
            mean_africa['Africa']['anxiety'].append(df_2017.iloc[row]['anxiety'])
            mean_africa['Africa']['drug'].append(df_2017.iloc[row]['drug'])
            mean_africa['Africa']['depres'].append(df_2017.iloc[row]['depres'])
            mean_africa['Africa']['alcohol'].append(df_2017.iloc[row]['alcohol'])
if 'Africa' in mean_africa:
    africa_miangin = {'cont' : 'Africa',
                      'country':'African countries',
                     'schizo': np.mean(mean_africa['Africa']['schizo']),
                     'bipolar' : np.mean(mean_africa['Africa']['bipolar']),
                     'eating_dis': np.mean(mean_africa['Africa']['eating_dis']),
                     'anxiety': np.mean(mean_africa['Africa']['anxiety']),
                     'drug' : np.mean(mean_africa['Africa']['drug']),
                     'depres' : np.mean(mean_africa['Africa']['depres']),
                     'alcohol' : np.mean(mean_africa['Africa']['alcohol'])}
    print(africa_miangin)
    
    cont_2017 = pd.concat([cont_2017,pd.DataFrame(africa_miangin, index=range(1))], axis=0)

country_america = ['United States','Brazil',
                  'Mexico','Colombia',
                  'Argentina','Canada',
                  'Peru','Venezuela',
                  'Chile','Ecuador',
                  'Guatemala','Bolivia',
                  'Haiti','Dominican Republic',
                  'Cuba','Honduras',
                  'Nicaragua','Paraguay',
                  'El Salvador','Costa Rica',
                  'Panama','Uruguay']
mean_america = {}
for row in range(len(df_2017)):
    country = df_2017.iloc[row]['country']
    if country in country_america: 
        if 'America' not in mean_america:
            mean_america['America'] = {'schizo': [], 'bipolar': [], 'eating_dis': [], 'anxiety': [], 'drug': [], 'depres': [], 'alcohol': []}
            mean_america['America']['schizo'].append(df_2017.iloc[row]['schizo'])
            mean_america['America']['bipolar'].append(df_2017.iloc[row]['bipolar'])
            mean_america['America']['eating_dis'].append(df_2017.iloc[row]['eating_dis'])
            mean_america['America']['anxiety'].append(df_2017.iloc[row]['anxiety'])
            mean_america['America']['drug'].append(df_2017.iloc[row]['drug'])
            mean_america['America']['depres'].append(df_2017.iloc[row]['depres'])
            mean_america['America']['alcohol'].append(df_2017.iloc[row]['alcohol'])
if 'America' in mean_america:
    america_miangin = {'cont':'America',
                       'country':'American countries',
                      'schizo': np.mean(mean_america['America']['schizo']),
                      'bipolar' : np.mean(mean_america['America']['bipolar']),
                      'eating_dis': np.mean(mean_america['America']['eating_dis']),
                      'anxiety': np.mean(mean_america['America']['anxiety']),
                      'drug' : np.mean(mean_america['America']['drug']),
                      'depres' : np.mean(mean_america['America']['depres']),
                      'alcohol' : np.mean(mean_america['America']['alcohol'])}
    print(america_miangin)
    cont_2017 = pd.concat([cont_2017,pd.DataFrame(america_miangin, index=range(1))], axis=0)
country_oceania = ['Australia',
                  'New Zealand',
                  'Papua New Guinea',
                  'Fiji',
                   'Solomon Islands']

mean_oceania = {}
for row in range(len(df_2017)):
    country = df_2017.iloc[row]['country']
    if country in country_oceania: 
        if 'Oceania' not in mean_oceania:
            mean_oceania['Oceania'] = {'schizo': [], 'bipolar': [], 'eating_dis': [], 'anxiety': [], 'drug': [], 'depres': [], 'alcohol': []}
            mean_oceania['Oceania']['schizo'].append(df_2017.iloc[row]['schizo'])
            mean_oceania['Oceania']['bipolar'].append(df_2017.iloc[row]['bipolar'])
            mean_oceania['Oceania']['eating_dis'].append(df_2017.iloc[row]['eating_dis'])
            mean_oceania['Oceania']['anxiety'].append(df_2017.iloc[row]['anxiety'])
            mean_oceania['Oceania']['drug'].append(df_2017.iloc[row]['drug'])
            mean_oceania['Oceania']['depres'].append(df_2017.iloc[row]['depres'])
            mean_oceania['Oceania']['alcohol'].append(df_2017.iloc[row]['alcohol'])
if 'Oceania' in mean_oceania:
    oceania_miangin = {'cont':'Oceania',
                       'country':'Oceania',
                      'schizo': np.mean(mean_oceania['Oceania']['schizo']),
                      'bipolar' : np.mean(mean_oceania['Oceania']['bipolar']),
                      'eating_dis': np.mean(mean_oceania['Oceania']['eating_dis']),
                      'anxiety': np.mean(mean_oceania['Oceania']['anxiety']),
                      'drug' : np.mean(mean_oceania['Oceania']['drug']),
                      'depres' : np.mean(mean_oceania['Oceania']['depres']),
                      'alcohol' : np.mean(mean_oceania['Oceania']['alcohol'])}
    print(oceania_miangin)
    cont_2017 = pd.concat([cont_2017,pd.DataFrame(oceania_miangin, index=range(1))], axis=0)

with st.expander("Show continent wise mean distribution"):  
    st.dataframe(cont_2017)

plt.style.use('ggplot')
fig, ax = plt.subplots(figsize=(15,6))
cont_2017.set_index('cont').plot(kind='bar', ax=ax, logy=True)
ax.set_xlabel('Continent', fontsize=14)
ax.set_ylabel('Rate of Mental Disorders', fontsize=14)
ax.set_title(f'Mental Disorders rate by Continent in {sel_year}', fontsize=16)
ax.legend(['Schizophrenia', 'Bipolar Disorder', 'Eating Disorder','Anxiety Disorder','Drug Abuse', 'Depression','Alcohol Abuse'], fontsize=12)
st.pyplot(fig)

col = st.selectbox("select a column", df_2017.columns.tolist()[2:])   

fig = px.bar(df_2017, x=col, y=df_2017.country)
st.plotly_chart(fig)

value = st.selectbox("select a column to summarize", df_1.columns.tolist()[2:])
years_wise_df = pd.pivot_table(df_1, index='country', columns='year', values=value)
st.dataframe(years_wise_df)
fig= px.histogram(years_wise_df, x=sel_year, y=years_wise_df.index)
st.plotly_chart(fig)
