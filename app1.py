import streamlit as st
import pandas as pd
import numpy as np

# Generate sample dataset
data = {
    'Title': ['Movie1', 'Movie2', 'Movie3', 'Movie4', 'Movie5'],
    'Genre': ['Action', 'Comedy', 'Drama', 'Horror', 'Sci-Fi'],
    'Director': ['Director1', 'Director2', 'Director3', 'Director4', 'Director5'],
    'Release Year': [2001, 2002, 2003, 2004, 2005],
    'Duration': [120, 90, 150, 110, 130],
    'IMDb Rating': [7.5, 8.0, 6.5, 7.0, 8.5],
    'Box Office Gross': [1000000, 2000000, 1500000, 1200000, 1800000],
    'Number of Votes': [10000, 15000, 12000, 11000, 13000]
}

df = pd.DataFrame(data)

# Sidebar for chart selection
chart_type = st.sidebar.selectbox(
    "Select Chart Type",
    ("Scatter Chart", "Bar Chart", "Line Chart", "Area Chart")
)

# Display dataset
st.write("Sample Movie Dataset")
st.table(df)

# Display selected chart with caption
if chart_type == "Scatter Chart":
    st.write("Scatter Chart: Movie Duration vs IMDb Rating")
    st.write("This chart shows the relationship between movie duration and IMDb rating.")
    st.scatter_chart(df[['Duration', 'IMDb Rating']])

elif chart_type == "Bar Chart":
    category = st.sidebar.selectbox("Select Category", ("Genre", "Director"))
    value = st.sidebar.selectbox("Select Value", ("Box Office Gross", "Number of Votes"))
    st.write(f"Bar Chart: {category} vs {value}")
    st.write(f"This chart shows the {value} for each {category}.")
    st.bar_chart(df.set_index(category)[value])

elif chart_type == "Line Chart":
    value = st.sidebar.selectbox("Select Value", ("IMDb Rating", "Box Office Gross"))
    st.write(f"Line Chart: Release Year vs {value}")
    st.write(f"This chart shows the trend of {value} over the years.")
    st.line_chart(df.set_index('Release Year')[value])

elif chart_type == "Area Chart":
    st.write("Area Chart: Release Year vs Box Office Gross")
    st.write("This chart shows the trend of box office gross over the years.")
    st.area_chart(df.set_index('Release Year')['Box Office Gross'])