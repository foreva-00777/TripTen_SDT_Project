# Import libraries 
import streamlit as st
import pandas as pd
import plotly_express as px

# Read the dataset from a CSV file
vehicles = pd.read_csv('vehicles_us.csv')

# Header
st.header("Vehicles Dataset")

# Checkbox to toggle histogram display
show_histogram = st.checkbox("Show Histogram")

# Histogram for Model Year
if show_histogram:
    histogram_fig = px.histogram(vehicles, x='model_year', nbins=20, title='Distribution of Model Year')
    st.plotly_chart(histogram_fig)

# Scatter plot

 # Scatter plot of Odometer versus Price
scatter_fig = px.scatter(
    vehicles,
    x='odometer',
    y='price',
    color='condition',  
    color_discrete_sequence=['red', 'blue', 'green', 'purple', 'yellow', 'orange'],
    title='Scatter Plot of Price vs. Odometer',
    labels={'odometer': 'Odometer (miles)', 'price': 'Price ($)'},
    hover_name='model'  # Optional: Shows the model on hover
    )
st.plotly_chart(scatter_fig)