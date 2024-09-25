import streamlit as st
import pandas as pd
import plotly.express as px

# Load dataset
vehicles = pd.read_csv('vehicles_us.csv') 

# Header
st.header("My Vehicle Data Analysis App")

# Checkbox to toggle histogram
show_histogram = st.checkbox("Show Histogram")

if show_histogram:
    # Create a histogram
    fig_hist = px.histogram(data, x='column_name')  # Replace 'column_name' with your data column
    st.write("Histogram of Column Name")  # Adding a description for the histogram
    st.write(fig_hist)  # Using st.write to display the histogram

# Scatter plot
fig_scatter = px.scatter(data, x='x_column', y='y_column')  # Replace 'x_column' and 'y_column' with your data columns
st.plotly_chart(fig_scatter)  # Displaying scatter plot