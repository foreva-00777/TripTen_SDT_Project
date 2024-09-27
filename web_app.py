# Import libraries 
import streamlit as st
import pandas as pd
import plotly.express as px

# Read the dataset from a CSV file
try: 
    vehicles = pd.read_csv('vehicles_us.csv')
except FileNotFoundError:
    st.error("The file 'vehicles_us.csv; was not found.")
    st.stop() # Stops the execution if the file is not found

# Validate required columns
required_columns = ['model_year', 'odometer', 'price', 'condition', 'model']
for col in required_columns:
    if col not in vehicles.columns:
        st.error(f"The dataset is missing the required column: {col}")
        st.stop()

# Header
st.header("Vehicles Dataset")

# Checkbox to toggle histogram display
show_histogram = st.checkbox("Show Histogram")

# Histogram for Model Year
if show_histogram:
    histogram_fig = px.histogram(vehicles, x='model_year', nbins=20, title='Distribution of Model Year')
    st.plotly_chart(histogram_fig)


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