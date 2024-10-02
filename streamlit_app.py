import streamlit as st
import pandas as pd
import numpy as numpy
from PIL import Image
import seaborn as sns


st.title("🎈 Data Science App (test)")
# st.write(
#     "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
# )

df = pd.read_csv("wine_quality_red.csv")

st.dataframe(df.head(5))
image = Image.open("15_bottles_red_1.webp")
st.image(image)
st.subheader("01 Description of the dataset")
st.dataframe(df.describe())

st.subheader("02 Missing values")
dfnull = df.isnull()/len(df)*100
total_missing = dfnull.sum().round(2)
st.write(total_missing)
if total_missing[0] < 0.1:   
    st.success("Congrats on no missing values")
# st.write(dfnull)

st.subheader("03")
list_columns = df.columns
values = st.multiselect("Select two variables: ", list_columns, ["quality", "citric acid"] )

st.line_chart(df, x=values[0],y=values[1])


st.bar_chart(df, x=values[0], y=values[1])

values_pairplot = st.multiselect("Select 4 variables: ", list_columns, ["quality", "citric acid", "alcohol", "chlorides"])

df2 = df[[values_pairplot[0], values_pairplot[1], values_pairplot[2], values_pairplot[3]]]
sns.pairplot(df2)