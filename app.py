import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

import streamlit as st

# Define functions for each page

def front_page():
# Title
    st.title('2023 HTU Attendee Analysis')
    
    
# Text
    st.markdown('''
                This report aims to provide a comprehensive analysis of the attendees of the 2023 HTU event. The analysis is broken down into three main sections:  
                - Attendees Overview
                - Member Analysis
                - HCA Attendees Analysis
                ''')




def attendee_overview():
    st.title("Attendee Overview")
    st.write("Welcome to the home page!")
    # Header
st.header('Attendee Overview')

# Subheader
st.subheader('Demographic - Gender & Age')


# dataset loading 
encodings = ['latin1', 'iso-8859-1', 'cp1252']

for encoding in encodings:
    try:
        df = pd.read_csv('HTU_2023_1.csv', encoding=encoding)
        print(f"Successfully read the file with encoding: {encoding}")
        break
    except UnicodeDecodeError:
        print(f"Failed to read the file with encoding: {encoding}")
# Function to convert column names to kebab-case
def to_kebab_case(col_name):
    return col_name.replace(' ', '_')

# Apply the function to all column names
df.columns = [to_kebab_case(col) for col in df.columns]


# Data for the pie chart
labels = ['Female', 'Male']
sizes = [47.35, 52.65]  # Proportions of each category
colors = ['lightcoral', 'lightskyblue']
explode = (0.1, 0)  # "explode" the 1st slice (i.e., 'Female')

# Plotting the pie chart
plt.figure(figsize=(4, 4))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
        shadow=True, startangle=140)

# Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Gender Distribution of 2023 HTU Attendees')
plt.axis('equal')

# Display the chart in Streamlit
st.pyplot(plt)


# Sorting and preparing the data
age_sorted = df.sort_values('Age_Range')
age = age_sorted['Age_Range'].dropna()

# Creating the histogram
plt.figure(figsize=(10, 6))
n, bins, patches = plt.hist(age, bins=20, color='skyblue')

# Adding count number labels on top of each bar
for i in range(len(patches)):
    plt.text(patches[i].get_x() + patches[i].get_width() / 2, 
             patches[i].get_height(), 
             str(int(patches[i].get_height())), 
             ha='center', va='bottom', fontsize=12)

# Adding title and labels
plt.title('Distribution of Age Ranges', fontsize=16)
plt.xlabel('Age Range', fontsize=14)
plt.ylabel('Count', fontsize=14)

# Customizing tick parameters
plt.xticks(fontsize=9)
plt.yticks(fontsize=12)

# Displaying the plot in Streamlit
st.pyplot(plt)

import pandas as pd
import plotly.express as px

# Creating the DataFrame with the provided data
data = {
    'Work_state': ['Texas', 'Tennessee', 'Florida', 'California', 'Pennsylvania', 'Massachusetts', 'New Jersey', 'Michigan', 
                   'Illinois', 'North Carolina', 'Indiana', 'Nevada', 'Ohio', 'Virginia', 'Missouri', 'New York', 
                   'Louisiana', 'Georgia', 'Idaho', 'Colorado', 'Kansas', 'Utah', 'Alabama', 'Minnesota', 'Kentucky', 
                   'South Carolina', 'Oklahoma', 'Arizona', 'Wisconsin', 'New Mexico', 'Mississippi', 'Iowa', 'Maryland', 
                   'Washington', 'Arkansas', 'New Hampshire', 'Nebraska', 'Oregon', 'Connecticut', 'Delaware', 
                   'Maine', 'Vermont', 'Montana', 'Alaska', 'South Dakota', 'West Virginia', 
                   'District of Columbia', 'Wyoming'],
    'count': [293, 258, 135, 133, 102, 66, 63, 61, 60, 56, 54, 52, 50, 47, 43, 41, 40, 37, 37, 35, 32, 31, 26, 25, 21, 19, 17, 15, 
              15, 14, 12, 11, 9, 8, 7, 7, 7, 6, 5, 4, 4, 3, 3, 3, 2, 1, 1, 1]
}
state_counts = pd.DataFrame(data)

state_codes = {
    'Texas': 'TX', 'Tennessee': 'TN', 'Florida': 'FL', 'California': 'CA', 'Pennsylvania': 'PA', 'Massachusetts': 'MA', 
    'New Jersey': 'NJ', 'Michigan': 'MI', 'Illinois': 'IL', 'North Carolina': 'NC', 'Indiana': 'IN', 'Nevada': 'NV', 
    'Ohio': 'OH', 'Virginia': 'VA', 'Missouri': 'MO', 'New York': 'NY', 'Louisiana': 'LA', 'Georgia': 'GA', 'Idaho': 'ID', 
    'Colorado': 'CO', 'Kansas': 'KS', 'Utah': 'UT', 'Alabama': 'AL', 'Minnesota': 'MN', 'Kentucky': 'KY', 'South Carolina': 'SC', 
    'Oklahoma': 'OK', 'Arizona': 'AZ', 'Wisconsin': 'WI', 'New Mexico': 'NM', 'Mississippi': 'MS', 'Iowa': 'IA', 'Maryland': 'MD', 
    'Washington': 'WA', 'Arkansas': 'AR', 'New Hampshire': 'NH', 'Nebraska': 'NE', 'Oregon': 'OR', 'Connecticut': 'CT', 
    'Delaware': 'DE', 'Maine': 'ME', 'Vermont': 'VT', 'Montana': 'MT', 'Alaska': 'AK', 'South Dakota': 'SD','West Virginia': 'WV', 'District of Columbia': 'DC', 'Wyoming': 'WY'
}

state_counts['state_code'] = state_counts['Work_state'].map(state_codes)

# Create a choropleth map
fig = px.choropleth(state_counts,
                    locations='state_code',
                    locationmode="USA-states",
                    color='count',
                    hover_name='Work_state',
                    color_continuous_scale='reds',
                    scope="usa",
                    labels={'count': 'Count'})

fig.update_layout(title_text='Work State Counts, Member')

# Streamlit part
st.title("Work State Counts Visualization")
st.plotly_chart(fig)


def member_analysis():
    st.title("Member Analysis")
    st.write("This is the data analysis page.")
    
    

def hca_analysis():
    st.title("HCA Analysis")
    st.write("This is the contact page.")

# Create a sidebar with navigation
st.sidebar.title("2023 HTU")
page = st.sidebar.radio("Go to", ['Front Page',"Attendee Overview", "Member Analysis", "HCA Analysis"])

# Display the selected page

if page == "Front Page":
    front_page()
elif page == "Attendee Overview":
    attendee_overview()
elif page == "Member Analysis":
    member_analysis()
elif page == "HCA Analysis":
    hca_analysis()


















