import pandas as pd
import seaborn as sns
import streamlit as st

fieldNumber = ['popularity', 'acousticness', 'danceability', 'energy', 'instrumentalness', 'liveness', 'speechiness', 'valence', 'duration_ms']
dataNumber = pd.read_csv("data/data.csv", usecols=fieldNumber)
data = pd.read_csv("data/data.csv")

dataNSample = dataNumber.sample(500)
dataSample = data.sample(500)
top100Popular = data.sort_values(by='popularity')


st.markdown('### Présentation des données : ')
st.write(dataSample.head())

catplotGenrePopularity = sns.catplot(x="genre",y="popularity",data=dataSample,  kind='bar', height=20)
st.markdown('### Catplot des musiques par genre : ')
st.pyplot(catplotGenrePopularity)


catplot100 = sns.catplot(x="genre",y="popularity",data=top100Popular.tail(100),  kind='bar', height=10)
st.markdown('### Catplot des 100 meilleurs musiques par genre : ')
st.pyplot(catplot100)

catplot100Duration = sns.catplot(x="genre",y="duration_ms",data=top100Popular.tail(100),  kind='bar', height=10)
st.markdown('### Catplot de durée par rapport au  top 100 : ')
st.pyplot(catplot100Duration)

