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

#Streamlit Page creation

st.set_page_config(
    page_title="Phonepe Pulse Data Visualization",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Creating connection with mysql workbench

config = {'host' : 'localhost',
              'user' : 'root',
              'password' : 'Arulezhil@71',
              'database' : 'phonepe_data'}

conn = mysql.connector.connect(**config)
cursor = conn.cursor(buffered=True)

# Creating option menu in the side bar

with st.sidebar:
    selected = option_menu("Menu", ["Home","Top Charts","Explore Data","About"],
                    icons = ["house","graph-up-arrow","bar-chart-line", "exclamation-circle"],
                    menu_icon = "menu-button-wide",
                    default_index = 0,
                    styles = {"nav-link": {"font-size": "20px", "text-align": "left", "margin": "-2px", "--hover-color": "#6F36AD"},
                        "nav-link-selected": {"background-color": "#6F36AD"}})
    

#Menu-1 Home

if selected == "Home":
    st.markdown("# :violet[PHONEPE PULSE DATA VISUALIZATION AND EXPLORATION]")
    st.markdown("## :violet[A User-Friendly Tool Using Streamlit and Plotly]")
    col1,col2 = st.columns([3,2],gap="medium")
    
    with col1:
        st.write(" ")
        st.write(" ")
        st.header(':violet[PHONEPE]')
        st.subheader("INDIA'S BEST TRANSACTION APP")
        st.markdown("PhonePe  is an Indian digital payments and financial technology company")
        st.write("****FEATURES****")
        st.write("**-> Credit & Debit card linking**")
        st.write("**-> Bank Balance check**")
        st.write("**->Money Storage**")
        st.write("**->PIN Authorization**")
        st.write("**-> Easy Transactions**")
        st.write("**-> One App For All Your Payments**")
        st.write("**-> Your Bank Account Is All You Need**")
        st.write("**-> Multiple Payment Modes**")
        st.write("**-> PhonePe Merchants**")
        st.write("**-> Multiple Ways To Pay**")
        st.write("**-> 1.Direct Transfer & More**")
        st.write("**-> 2.QR Code**")
        st.write("**-> Earn Great Rewards**")
        st.write("**->No Wallet Top-Up Required**")
        st.write("**->Pay Directly From Any Bank To Any Bank A/C**")
        st.write("**->Instantly & Free**")
      
    with col2:
        st.image("/Users/arul/Downloads/phonepe.png")
        st.markdown(" ")
        st.markdown(" ")
        st.video("/Users/arul/Downloads/Phone Pe Ad.mp4")
        st.markdown(" ")
        st.markdown(" ")
        st.download_button("DOWNLOAD THE APP NOW", "https://www.phonepe.com/app-download/")
       
# Menu-2 Top chart
if selected == "Top Charts":
    st.markdown("## :violet[Top Charts]")
    Type = st.sidebar.selectbox("**Type**", ("Transactions", "Users"))
    col1, col2 = st.columns([1, 1.5], gap="large")
    
    with col1:
        Year = st.selectbox("**Year**", list(range(2018, 2024)))
        Quarter = st.slider("Quarter", min_value=1, max_value=4)
    
    with col2:
        st.info(
            """
            #### From this menu, we can get insights like:
            - Overall ranking on a particular Year and Quarter.
            - Top 10 State, District, Pincode based on Total number of transactions and Total amount spent on PhonePe.
            - Top 10 State, District, Pincode based on Total PhonePe users and their app opening frequency.
            - Top 10 mobile brands and their percentage based on how many people use PhonePe.
            """
        )

    # Top Charts - TRANSACTIONS    
        
    if Type == "Transactions":

        st.subheader("Top 10 State, District, Pincode based on Total number of Transactions and Total Amount spent on PhonePe")
        st.markdown(" ")
        st.markdown(" ")
        st.markdown("### :violet[STATE]")
        cursor.execute(f"select States, sum(Transaction_count) as Total_Transactions_Count, sum(Transaction_amount) as Total from aggregated_transaction where Years = {Year} and Quarter = {Quarter} group by States order by Total desc limit 10")
        df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Transactions_Count','Transaction_amount'])
        fig = px.pie(df, values='Transaction_amount',
                        names='State',  
                        title='Top 10',
                        color_discrete_sequence=px.colors.cyclical.Edge,
                        hover_data=['Transactions_Count'],
                        labels={'Transactions_Count':'Transactions_Count'})

        fig.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig, use_container_width=True)

        st.markdown("### :violet[DISTRICT]")
        cursor.execute(f"select Districts, sum(Transaction_count) as Total_Count, sum(Transaction_amount) as Total from map_transaction where Years = {Year} and Quarter = {Quarter} group by Districts order by Total desc limit 10")
        df = pd.DataFrame(cursor.fetchall(), columns=['District', 'Transactions_Count','Transaction_amount'])

        fig = px.pie(df, values='Transaction_amount',
                        names='District',  
                        title='Top 10',
                        color_discrete_sequence=px.colors.diverging.Spectral,
                        hover_data=['Transactions_Count'],
                        labels={'Transactions_Count':'Transactions_Count'})

        fig.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig, use_container_width=True)

        st.markdown("### :violet[PINCODE]")
        cursor.execute(f"select Pincodes, sum(Transaction_count) as Total_Transactions_Count, sum(Transaction_amount) as Total from top_transaction where Years = {Year} and Quarter = {Quarter} group by Pincodes order by Total desc limit 10")
        df = pd.DataFrame(cursor.fetchall(), columns=['Pincode', 'Transactions_Count','Transaction_amount'])
        fig = px.pie(df, values='Transaction_amount',
                            names='Pincode',
                            title='Top 10',
                            color_discrete_sequence=px.colors.sequential.Agsunset,
                            hover_data=['Transactions_Count'],
                            labels={'Transactions_Count':'Transactions_Count'})

        fig.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig,use_container_width=True)
    
    # Top Charts - USERS          
    if Type == "Users":

        st.subheader("Top 10 Mobile Brands and their Percentage based on How many people use PhonePe")
        st.markdown(" ")
        st.markdown(" ")
        st.markdown("### :violet[BRANDS]")
        if Year == 2023 and Quarter in [4]:
            st.markdown("#### Sorry No Data to Display for 2023 Qtr 4")
        else:
            cursor.execute(f"select Brands, sum(Count) as Total_Count, avg(Percentage)*100 as Avg_Percentage from aggregated_user where Years = {Year} and Quarter = {Quarter} group by Brands order by Total_Count desc limit 10")
            df = pd.DataFrame(cursor.fetchall(), columns=['Brand', 'Total_Users','Avg_Percentage'])
            fig = px.bar(df,
                            title='Top 10',
                            x="Total_Users",
                            y="Brand",
                            orientation='h',
                            color='Avg_Percentage',
                            color_continuous_scale=px.colors.sequential.Agsunset)
            st.plotly_chart(fig,use_container_width=True)

        st.subheader("Top 10 State, District, Pincode based on Total PhonePe Users and their App Opening Frequency")
        st.markdown(" ")
        st.markdown(" ")
        st.markdown("### :violet[STATE]")
        if Year == 2023 and Quarter in [4]:
            st.markdown("#### Sorry No Data to Display for 2023 Qtr 4")
        else:
            cursor.execute(f"select States, sum(RegisteredUser) as Total_Users, sum(AppOpens) as Total_Appopens from map_user where Years = {Year} and Quarter = {Quarter} group by States order by Total_Users desc limit 10")
            df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Total_Users','Total_Appopens'])
            fig = px.pie(df, values='Total_Users',
                            names='State',
                            title='Top 10',
                            color_discrete_sequence=px.colors.sequential.Agsunset,
                            hover_data=['Total_Appopens'],
                            labels={'Total_Appopens':'Total_Appopens'})

            fig.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig,use_container_width=True)
        
        st.markdown("### :violet[DISCRICT]")
        if Year == 2023 and Quarter in [4]:
            st.markdown("#### Sorry No Data to Display for 2023 Qtr 4")
        else:
            cursor.execute(f"select Districts, sum(RegisteredUser) as Total_Users, sum(AppOpens) as Total_Appopens from map_user where Years = {Year} and Quarter = {Quarter} group by Districts order by Total_Users desc limit 10")
            df = pd.DataFrame(cursor.fetchall(), columns=['District', 'Total_Users','Total_Appopens'])
            df.Total_Users = df.Total_Users.astype(float)
            fig = px.bar(df,
                        title='Top 10',
                        x="Total_Users",
                        y="District",
                        orientation='h',
                        color='Total_Appopens',
                        color_continuous_scale=px.colors.sequential.Agsunset)
            st.plotly_chart(fig,use_container_width=True)

        st.markdown("### :violet[PINCODE]")
        if Year == 2023 and Quarter in [4]:
            st.markdown("#### Sorry No Data to Display for 2023 Qtr 4")
        else:
            cursor.execute(f"select Pincodes, sum(RegisteredUser) as Total_Users from top_user where Years = {Year} and Quarter = {Quarter} group by Pincodes order by Total_Users desc limit 10")
            df = pd.DataFrame(cursor.fetchall(), columns=['Pincode', 'Total_Users'])
            fig = px.pie(df,
                        values='Total_Users',
                        names='Pincode',
                        title='Top 10',
                        color_discrete_sequence=px.colors.sequential.Agsunset,
                        hover_data=['Total_Users'])
            fig.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig,use_container_width=True)

# MENU 3 - EXPLORE DATA
if selected == "Explore Data":
    Year = st.sidebar.selectbox("**Year**", list(range(2018, 2024)))
    Quarter = st.sidebar.slider("Quarter", min_value=1, max_value=4)
    Type = st.sidebar.selectbox("**Type**", ("Transactions", "Users"))
 
    # EXPLORE DATA - TRANSACTIONS
    if Type == "Transactions":
        
        st.markdown("## :violet[Overall State Data - Transactions Amount]")
        cursor.execute(f"select States, sum(Transaction_count) as Total_Transactions, sum(Transaction_amount) as Total_amount from map_transaction where Years = {Year} and Quarter = {Quarter} group by States order by States")
        df1 = pd.DataFrame(cursor.fetchall(),columns= ['State', 'Total_Transactions', 'Total_amount'])
        df2 = pd.read_csv('Statenames.csv')
        df1.State = df2

        fig = px.choropleth(df1,geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                    featureidkey='properties.ST_NM',
                    locations='State',
                    color='Total_amount',
                    color_continuous_scale='pubugn')

        fig.update_geos(fitbounds="locations", visible=False)
        st.plotly_chart(fig,use_container_width=True)

    # Overall State Data - TRANSACTIONS COUNT - INDIA MAP
            
        st.markdown("## :violet[Overall State Data - Transactions Count]")
        cursor.execute(f"select States, sum(Transaction_count) as Total_Transactions, sum(Transaction_amount) as Total_amount from map_transaction where Years = {Year} and Quarter = {Quarter} group by States order by States")
        df1 = pd.DataFrame(cursor.fetchall(),columns= ['State', 'Total_Transactions', 'Total_amount'])
        df2 = pd.read_csv('Statenames.csv')
        df1.Total_Transactions = df1.Total_Transactions.astype(int)
        df1.State = df2

        fig = px.choropleth(df1,geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                    featureidkey='properties.ST_NM',
                    locations='State',
                    color='Total_Transactions',
                    color_continuous_scale='purd')

        fig.update_geos(fitbounds="locations", visible=False)
        st.plotly_chart(fig,use_container_width=True)

        # BAR CHART - TOP PAYMENT TYPE
        st.markdown("## :violet[Top Payment Type]")
        cursor.execute(f"select Transaction_Type, sum(Transaction_count) as Total_Transactions, sum(Transaction_amount) as Total_amount from aggregated_transaction where Years= {Year} and Quarter = {Quarter} group by Transaction_Type order by Transaction_Type")
        df = pd.DataFrame(cursor.fetchall(), columns=['Transaction_type', 'Total_Transactions','Total_amount'])

        fig = px.bar(df,
                     title='Transaction Types vs Total_Transactions',
                     x="Transaction_type",
                     y="Total_Transactions",
                     orientation='v',
                     color='Total_amount',
                     color_continuous_scale=px.colors.sequential.Agsunset)
        st.plotly_chart(fig,use_container_width=False)
        
        # BAR CHART TRANSACTIONS - DISTRICT WISE DATA            
        st.markdown("# ")
        st.markdown("# ")
        st.markdown("# ")
        st.markdown("## :violet[Select any State to explore more]")
        selected_state = st.selectbox("",
                             ('Andaman & Nicobar','Andhra Pradesh','Arunachal Pradesh','Assam','Bihar',
                              'Chandigarh','Chhattisgarh','Dadra and Nagar Haveli and Daman and Diu','Delhi','Goa','Gujarat','Haryana',
                              'Himachal Pradesh','Jammu & Kashmir','Jharkhand','Karnataka','Kerala','Ladakh','Lakshadweep',
                              'Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram',
                              'Nagaland','Odisha','Puducherry','Punjab','Rajasthan','Sikkim',
                              'Tamil Nadu','Telangana','Tripura','Uttar Pradesh','Uttarakhand','West Bengal'),index=30)
         
        cursor.execute(f"select States, Districts, Years, Quarter, sum(Transaction_count) as Total_Transactions, sum(Transaction_amount) as Total_amount from map_transaction where Years = {Year} and Quarter = {Quarter} and States = '{selected_state}' group by States, Districts, Years, Quarter order by States, Districts")
        
        df1 = pd.DataFrame(cursor.fetchall(), columns=['State','District','Year','Quarter',
                                                         'Total_Transactions','Total_amount'])
        fig = px.bar(df1,
                     title=selected_state,
                     x="District",
                     y="Total_Transactions",
                     orientation='v',
                     color='Total_amount',
                     color_continuous_scale=px.colors.sequential.Agsunset)
        st.plotly_chart(fig,use_container_width=True)

    # EXPLORE DATA - USERS      
    if Type == "Users":
        
    # Overall State Data - TOTAL APPOPENS - INDIA MAP
        st.markdown("## :violet[Overall State Data - User App opening frequency]")
        cursor.execute(f"select States, sum(RegisteredUser) as Total_Users, sum(AppOpens) as Total_Appopens from map_user where Years = {Year} and Quarter = {Quarter} group by States order by States")
        df1 = pd.DataFrame(cursor.fetchall(), columns=['State', 'Total_Users','Total_Appopens'])
        df2 = pd.read_csv('Statenames.csv')
        df1.Total_Appopens = df1.Total_Appopens.astype(float)
        df1.State = df2
        
        fig = px.choropleth(df1,geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                  featureidkey='properties.ST_NM',
                  locations='State',
                  color='Total_Appopens',
                  color_continuous_scale='rainbow')

        fig.update_geos(fitbounds="locations", visible=False)
        st.plotly_chart(fig,use_container_width=True)
        
     # BAR CHART TOTAL UERS - DISTRICT WISE DATA 
        st.markdown("## :violet[Select any State to explore more]")
        selected_state = st.selectbox("",
                             ('Andaman & Nicobar','Andhra Pradesh','Arunachal Pradesh','Assam','Bihar',
                              'Chandigarh','Chhattisgarh','Dadra and Nagar Haveli and Daman and Diu','Delhi','Goa','Gujarat','Haryana',
                              'Himachal Pradesh','Jammu & Kashmir','Jharkhand','Karnataka','Kerala','Ladakh','Lakshadweep',
                              'Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram',
                              'Nagaland','Odisha','Puducherry','Punjab','Rajasthan','Sikkim',
                              'Tamil Nadu','Telangana','Tripura','Uttar Pradesh','Uttarakhand','West Bengal'),index=30)
        
        cursor.execute(f"select States, Years, Quarter, Districts,sum(RegisteredUser) as Total_Users, sum(AppOpens) as Total_Appopens from map_user where Years = {Year} and Quarter = {Quarter} and States = '{selected_state}' group by States, Districts, Years, Quarter order by States, Districts")
        
        df = pd.DataFrame(cursor.fetchall(), columns=['State','year', 'quarter', 'District', 'Total_Users','Total_Appopens'])
        df.Total_Users = df.Total_Users.astype(int)
        
        fig = px.bar(df,
                     title=selected_state,
                     x="District",
                     y="Total_Users",
                     orientation='v',
                     color='Total_Users',
                     color_continuous_scale=px.colors.sequential.Agsunset)
        st.plotly_chart(fig,use_container_width=True)

# MENU 4 - ABOUT
if selected == "About":
    col1,col2 = st.columns([3,3],gap="medium")
    with col1:
        st.write(" ")
        st.write(" ")
        st.markdown("### :violet[About PhonePe Pulse:] ")
        st.write("##### BENGALURU, India, On Sept. 3, 2021 PhonePe, India's leading fintech platform, announced the launch of PhonePe Pulse, India's first interactive website with data, insights and trends on digital payments in the country. The PhonePe Pulse website showcases more than 2000+ Crore transactions by consumers on an interactive map of India. With  over 45% market share, PhonePe's data is representative of the country's digital payment habits.")
        
        st.write("##### The insights on the website and in the report have been drawn from two key sources - the entirety of PhonePe's transaction data combined with merchant and customer interviews. The report is available as a free download on the PhonePe Pulse website and GitHub.")
        
        st.markdown("### :violet[About PhonePe:] ")
        st.write("##### PhonePe is India's leading fintech platform with over 300 million registered users. Using PhonePe, users can send and receive money, recharge mobile, DTH, pay at stores, make utility payments, buy gold and make investments. PhonePe forayed into financial services in 2017 with the launch of Gold providing users with a safe and convenient option to buy 24-karat gold securely on its platform. PhonePe has since launched several Mutual Funds and Insurance products like tax-saving funds, liquid funds, international travel insurance and Corona Care, a dedicated insurance product for the COVID-19 pandemic among others. PhonePe also launched its Switch platform in 2018, and today its customers can place orders on over 600 apps directly from within the PhonePe mobile app. PhonePe is accepted at 20+ million merchant outlets across Bharat")
        st.markdown("### :violet[Key features and services offered by PhonePe include:] ")  
        st.subheader("Unified Payments Interface (UPI):")
        st.write("#####         PhonePe leverages UPI, a real-time payment system in India, to facilitate peer-to-peer money transfers and payments.")
        st.subheader("Digital Wallet:")
        st.write("#####         Users can store money in the PhonePe wallet, which can be used for various transactions.")
        st.subheader("Bill Payments:")
        st.write("#####         PhonePe allows users to pay utility bills, including electricity, water, gas, and more, directly through the app.")
        st.subheader("Mobile Recharge:")
        st.write("#####         Users can recharge prepaid mobile phones and pay postpaid mobile bills using the PhonePe app.")
        st.subheader("Online Shopping:")
        st.write("#####         PhonePe offers a platform for users to shop online, make purchases, and avail of discounts and cashback offers.")
        st.subheader("Insurance and Mutual Funds:")
        st.write("#####         The app provides services related to insurance and mutual funds, allowing users to invest and manage their financial portfolio.")
        st.subheader("Gold Purchase:")
        st.write("#####         PhonePe allows users to buy and sell digital gold through the app.")
        st.subheader("Travel Services:")
        st.write("#####         Users can book flights, hotels, and bus tickets using PhonePe for their travel needs.")
                  
    with col2:
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.image("/Users/arul/Downloads/Pulseimg.jpg")
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        st.video("/Users/arul/Downloads/Introducing PhonePe Pulse.mp4")
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        st.video("/Users/arul/Downloads/PhonePe Motion Graphics.mp4")

    with st.sidebar:
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        st.markdown("### :violet[Domain :] Fintech")
        st.markdown("### :violet[Technologies used :] Github Cloning, Python, Pandas, MySQL, mysql-connector-python, Streamlit, and Plotly.")
        st.markdown("### :violet[Overview :] In this streamlit web app you can visualize the phonepe pulse data and gain lot of insights on transactions, number of users, top 10 state, district, pincode and which brand has most number of users and so on. Bar charts, Pie charts and Geo map visualization are used to get some insights.")    
        st.image('/Users/arul/Downloads/home.png')