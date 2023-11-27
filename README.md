# Phonepe-Pulse-Data-Visualization-and-Exploration-A-User-Friendly-Tool-Using-Streamlit-and-Plotly

# Problem Statement:

	Developed an interactive PhonePe Pulse Data Visualization and Exploration dashboard, utilizing Python, Streamlit, and Plotly, to empower comprehensive analysis of transaction and user data, facilitating informed decision-making through dynamic insights and exploration.

NAME : RAMYA KRISHNAN A

BATCH: D98

DOMAIN : DATA SCIENCE

DEMO VIDEO URL : https://www.linkedin.com/posts/ramyakrishnan19_excited-to-share-my-recent-project-phonepe-activity-7134774046772068354-zjzH?utm_source=share&utm_medium=member_desktop

Linked in URL : www.linkedin.com/in/ramyakrishnan19



## What is PhonePe Pulse?

PhonePe Pulse is your window to the world of how India transacts with interesting trends, deep insights and in-depth analysis based on our data put together by the PhonePe team.

Libraries/Modules needed for the project!

       -> Plotly - (To plot and visualize the data)
       
       -> Pandas - (To Create a DataFrame with the scraped data)
       
       -> mysql.connector - (To store and retrieve the data)
       
       -> Streamlit - (To Create Graphical user Interface)
       
       -> json - (To load the json files)
       
       -> git.repo.base - (To clone the GitHub repository)

       
## Importing the Libraries:

              import os
              import json
              import pandas as pd
              import mysql.connector
              import git
              import streamlit as st
              import plotly.express as px
              from streamlit_option_menu import option_menu
              from PIL import Image
              from git.repo.base import Repo


### PhonePe Pulse Dashboard


# Overview

The PhonePe Pulse Dashboard provides a comprehensive view of transaction and user data, allowing users to explore and analyze key metrics. The dashboard consists of several features accessible through the sidebar menu.

## Features

# 1. Home Page

The home page showcases key features of PhonePe, including:

	•	Overview of PhonePe services
 
	•	PhonePe Pulse highlights

# 2. Top Charts

a. Transaction Insights

	•	Dropdown for selecting quarters
 
	•	Top 10 state, district, and pincode for transactions
 
	       	•	India maps displaying overall state data:
		
	       	•	Transactions Amount
		
	       	•	Transactions Count
	
        •	Top Payment Type analysis
       
b. User Analytics

	•	Dropdown for selecting quarters
 
	•	Brand and App Opens insights
 
	•	India map for Overall State Data - User App Opening Frequency
 
	•	Top Payment Type analysis for user data
 
# 3. Explore Data

a. Transaction Exploration

	•	Dropdown for selecting quarters
 
	•	Slider for selecting specific quarters
 
	       	•	India maps displaying:
	 
	       	•	Overall State Data - Transactions Amount
	 
	       	•	Overall State Data - Transactions Count
	 
	•	Top Payment Type insights
 
	•	District-wise transaction details
 
b. User Exploration

	•	Dropdown for selecting quarters
 
	•	Slider for selecting specific quarters
 
	•	India map for Overall State Data - User App Opening Frequency
 
	•	District-wise user details

# 4. About

The "About" section provides information on:

	•	Technologies and domains used
 
	•	Project overview
 
	•	Key features of PhonePe

# Project Overview

This project utilizes Streamlit and Plotly to create an interactive dashboard for exploring PhonePe Pulse data. The dashboard offers insights into transaction and user data, helping users analyze trends and make data-driven decisions.


<img width="1440" alt="Screenshot 2023-11-27 at 10 34 08 AM" src="https://github.com/Ramya19rk/Phonepe-Pulse-Data-Visualization-and-Exploration-A-User-Friendly-Tool-Using-Streamlit-and-Plotly/assets/145639838/135e452c-0c8b-4234-a03f-b06ee8d33679">
