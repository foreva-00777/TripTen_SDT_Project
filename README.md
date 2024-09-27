# Project 4 - Software Development Tools - Car Sales Dashboard Web Application

## Project Overview.

This project is designed to enjance your software deelopment skills by building and deploying a web application dashboard to the Render cloud service. The dashboard will utilize a dataset of car sales advertisements. 

## Objectives 
- Develop a web application that visualizes care sales data.
- Deploy the application to a cloud service (Render).
- Make the application publicly accessible.
- Apply best practices in software development and deployment. 

## Table of Contents

- [Demo](#demo)
- [Features](#Features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Exploratory Data Analysis](#exploratory-data-analysis)
- [Development Instructions](#development-instructions)
- [Deployment](#deployment)
- [How to Submit - Feedback Process](#submit-feedback-process)

## Demo 

You can view the app live at: (https://tripten-sdt-project.onrender.com)

## Features

- Interactive visualizations including histograms and scatter plots.
- User controls to filter and manipulate data displays.

## Technologies Used

- **Frontend:** Streamlit, HTML 
- **Backend:** Python Plotly.Express, Altair
- **Deployment:** Render (for hosting)

## Installation

### Step 1: Getting Started

1. **Create a GitHub account** at [github.com](https://github.com).
2. **Create a new Git repository** with a `README.md` file and a `.gitignore` file (select the Python template).
3. **Set up a Python environment** and install the necessary packages:
```bash
pip install pandas streamlit plotly-express altair 
```
4. **Create Render Account** 
Create an account on Render and link it to your GitHub account.

5. **Clone the repository (to local machine):**
```bash
git clone https://github.com/foreva-00777/TripTen_SDT_Project.git
cd TripTen_SDT_Project
```
6. **VS Code** Open the project in VS Code and set the Python interpreter to the one used by your virtual environment.

7. **Installed Packages** Ensure all required packages are installed in your virtual environment.

2. **Install dependencies** Make sure you have Python and pip installed, then run:
```bash
pip install -r requirements.txt
```
3. **Run the application** 
```bash
python app.py
```
4. **Access the application** : Open your browser and go to (http://127.0.0.1:10000/)

### Step 2: Download the Data File. 

Download the car advertisement dataset (e.g., vehicles_us.csv) and place it in the root directory of the project.

### Step 3: Exploratory Data Analysis
Create an EDA.ipynb Jupyter notebook in VS Code and save it in the notebooks directory.
Perform exploratory data analysis on the dataset and create histograms and scatter plots using Plotly Express.

## Development Instructions 

### Step 4: Develop the Web Application Dashboard

1. Create an app.py file in the root of the project directory.
2. In app.py, import the necessary libraries
```python
import streamlit as st
import pandas as pd
import plotly.express as px
```
3. Load the dataset into a Pandas DataFrame.

4. Add components to Streamlit app
- At least one header.
- At least one histogram and scatter plot using Plotly
- At least one checkbox to toggle components.

## Important Note

Throughout the project changes, modifications and updates were committed and pushed to the GitHub repository after each milestone, ensuring that all files were present for Render to build the project successfully. 

## Deployment

### Step 5: Deploy the Application to Render

1. **Create a requirements.txt** 
- Location: Create a requirements.txt file in the root directory:
```makefile
pandas==2.0.3
streamlit==1.25.0
altair==5.0.1
plotly==5.15.0
```
2. Create a .streamlit/config.toml file with the following content
```toml
[server]
headless = true
port = 10000

[browser]
serverAddress = "0.0.0.0"
serverPort = 10000
```
3. Commit and Push to remote repository

```bash
git add requirements.txt .streamlit/config.toml
git commit -m "Add deployment configuration for Render"
git push origin main
```

4. Deploy on Render. Open Render and create a new web service linked to the Github repository. 

5. In the Render settings, set the Build Command:
```
pip install -r requirements.txt
```
6. Set the Start Command: 
```arduino
streamlit run app.py
```
7. Deploy the application and wait for the build to succeed.

8. Verify the application at https://tripten-sdt-project.onrender.com


## How to Submit - Feedback Process 

Submit a link to your GitHub repository and the URL of your deployed app on Render. Ensure your README.md includes this information. Once you have completed the project, submit your work to the project reviewer for assessment. Feedback will typically be provided within 24 hours. Use this feedback to make necessary adjustments before resubmitting.

### Revision Cycles

Expect to go through multiple cycles of feedback and revision. This iterative process is normal and helps refine your application.
