import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px


# Title of the app
st.title("EAG Employee Survey Overview")

# Sidebar for navigation
st.sidebar.title("Navigation")
question_options = ["Introduction", "Question 1", "Question 2", "Question 3", "Question 4", "Question 5", "Question 6", "For Future Surveys"]
selected_question = st.sidebar.radio("Go to", question_options)

# Load the survey data
encodings = ['latin1', 'iso-8859-1', 'cp1252']
for encoding in encodings:
    try:
        df = pd.read_csv('EAG_survey.csv', encoding=encoding)
        print(f"Successfully read the file with encoding: {encoding}")
        break
    except UnicodeDecodeError:
        print(f"Failed to read the file with encoding: {encoding}")

# Function to plot a pie chart
def plot_pie_chart(dataframe, column_name):
    value_counts = dataframe[column_name].value_counts()
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.pie(value_counts, labels=value_counts.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired(range(len(value_counts))))
    ax.set_title(f'EAG Activity {column_name} Distribution')
    ax.axis('equal')
    plt.tight_layout()
    return fig

# Function to plot a bar chart
def plot_bar_chart(dataframe, column_name):
    value_counts = dataframe[column_name].value_counts()
    value_counts_df = pd.DataFrame(value_counts).reset_index()
    value_counts_df.columns = [column_name, 'Count']
    value_counts_df_sorted = value_counts_df.sort_values(by='Count', ascending=False)
    fig, ax = plt.subplots()
    bars = ax.bar(value_counts_df_sorted[column_name], value_counts_df_sorted['Count'], color='skyblue')
    ax.set_title(f'Preference for {column_name.replace("_", " ").title()}')
    ax.set_xlabel(column_name.replace('_', ' ').title())
    ax.set_ylabel('Count')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{int(height)}', xy=(bar.get_x() + bar.get_width() / 2, height / 2), ha='center', va='center', fontsize=10, color='black')
    return fig

# Main content based on selected question
if selected_question == "Introduction":
    st.write("This report aims to provide a comprehensive understanding of the 2024 EAG employee survey. By understanding the EAG members' feedback on the previous events and their expectations for future events, we can identify key areas of improvement and tailor our future initiatives to better meet their needs. This report will cover various aspects such as the preferred activities, preferred time and frequency, and any additional comments and suggestions.")
    st.subheader("Survey Results Dataset")
    st.dataframe(df)
    # st.write('Please note that we did not asked for any personal information in the survey. The City and State/Region come from their IP addresses. Most of the IP addresses are in Ocala, Florida with the coordinates (-81.62210083, 28.63439941). One assumption is this is their VPN IP. If interested, we might need to turn to IT team for a more accurate explaination.')
    # state_count = df['State/Region'].value_counts()
    # # Convert to DataFrame and reset the index
    # df_state = pd.DataFrame(state_count).reset_index()
    # df_state.columns = ['State_Code', 'count']
    # # 
    # # Create a choropleth map
    # fig = px.choropleth(
    #     df_state,
    #     locations='State_Code',
    #     locationmode="USA-states",
    #     color='count',
    #     scope="usa",
    #     color_continuous_scale="reds",
    #     title="State Counts"
    #     )
    # # Show the plot in Streamlit
    # st.plotly_chart(fig)


if selected_question == "Question 1":
    st.subheader("Question 1")
    st.markdown("""
    **Which of the following EAG-sponsored activities are you most interested in participating? Please select your top three:** 
    - Professional Development
    - Mentoring
    - Cross-functional networking
    - Social activities & events
    - I wish I had time, but I'm too busy
    - Other - Write In (Required)
    """)
    st.write("Let's take a look at the result:")
    data = {
        "Category": ["Professional Development", "Mentoring", "Cross-functional networking", "Social activities & events", "I wish I had time, but I'm too busy", "Other"],
        "Count": [107, 50, 80, 115, 31, 16]
    }
    df_1 = pd.DataFrame(data)
    df_sorted = df_1.sort_values(by="Count", ascending=False)
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(df_sorted["Category"], df_sorted["Count"], color='skyblue')
    ax.set_ylabel('Count')
    ax.set_title('Most interested EAG activities')
    ax.set_xticklabels(df_sorted["Category"], rotation=30, ha='right')
    plt.tight_layout()
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height / 2, f'{int(height)}', ha='center', va='center')
    st.pyplot(fig)

    st.write('Among the 140 respondents, social activities and events emerged as the most popular, with 115 individuals showing interest. Professional development was also highly valued by 107 respondents, indicating a strong desire for skill enhancement and career growth opportunities. Cross-functional networking attracted 80 respondents, emphasizing the importance of building relationships across different areas of the organization. Mentoring programs were of interest to 50 respondents, highlighting the need for guidance from experienced professionals. However, 31 respondents cited time constraints as a barrier to participation, and 16 respondents had other unspecified interests.')

    st.write("""
             The 'Other' input duplicates with Question 2 that asked for 'Others EAG acticities to participate', Please see the combined answers under Question 2.
             """)
    

if selected_question == "Question 2":
    st.subheader("Question 2")
    st.markdown("""
    **What type of social activities are you most interested in participating? Rank in order of preference:**
    - Clubs (Book, Fitness, etc.)
    - Sports Leagues (Pickleball, Kickball, etc.)
    - Social Outings (Trivia, Happy Hours, etc.)
    - Other (provide your suggestions in the comments box below)
    - None of the above
    """)
    columns_to_plot = ['Clubs', 'Sports Leagues', 'Social Outings']
    for column in columns_to_plot:
        if column in df.columns:
            st.write(f"Bar Chart for {column.replace('_', ' ').title()}")
            fig = plot_bar_chart(df, column)
            st.pyplot(fig)
            st.write("---")
    
    data5 = {
    "Preferred Activities": ["Club", "Sports Leagues", "Social Outings"],
    "Average Score": [2.657142857, 3.2, 2.935714286],
    "Mode Score": [2, 3, 1]
    }
    df5 = pd.DataFrame(data5)
    # Display the DataFrame as a table in Streamlit
    st.table(df5)
    st.markdown('''
                **Clubs**
                The highest preferences for clubs are moderate, with scores of 2 and 3.This indicates that while clubs are not extremely disliked, they tend to be moderately liked.  
                **Sports Leagues**
                The preference for sports leagues is mostly positive, with scores of 3 and 4 indicating a strong favorability towards sports leagues.  
                **Social Outing**
                The distribution suggests that opinions on social outings are polarized, with notable peaks at the extremes of the scale. People who enjoy social outings tend to really appreciate them, whereas those who dislike them have a strong aversion, reflecting starkly contrasting attitudes toward social events.
                
                ''')

    df2_other = df.dropna(subset=['Other interested Activities'])
    # Create a new column 'shortened_ideas' to display truncated comments with a tooltip for full comment
    st.dataframe(df2_other['Other interested Activities'], width=1000)


if selected_question == "Question 3":
    st.subheader("Question 3")
    st.markdown("""
    **Which area should the EAG focus on the most in the next 1-2 years?**
    - Engagement & culture
    - Sense of belonging
    - Professional development
    - Other - Write In (Required)
    """)
    fig = plot_bar_chart(df, 'Focus Areas in Future')
    st.pyplot(fig)
    st.markdown('''
                The dominant preference for "Engagement & Culture" suggests that participants value initiatives that foster a positive, engaging organizational culture. This could guide the EAG's strategic planning and resource allocation to focus primarily on enhancing engagement and cultural aspects within the organization over the next couple of years.
                ''')

if selected_question == "Question 4":
    st.subheader("Question 4")
    st.markdown("""
    **How often would you like to see EAG-sponsored events held?**
    - Monthly
    - Quarterly
    - Annually
    - No preference
    """)
    fig = plot_pie_chart(df, 'Preferred Frequency')
    st.pyplot(fig)

if selected_question == "Question 5":
    st.subheader("Question 5")
    st.markdown("""
    **What hours work best for EAG-sponsored events?**
    - Early morning, prior to 9:00 am
    - Over the lunch hour
    - Afternoon during work hours
    - After 5:00 pm
    """)
    fig = plot_pie_chart(df, 'Preferred Hours')
    st.pyplot(fig)

if selected_question == "Question 6":
    st.subheader("Question 6")
    st.markdown("""
    **Please share any additional ideas or requests that would help add to your employee experience at HealthTrust.**
    """)

    st.write("Please double-click the text for a full display.")
    # Drop rows with NaN values in the 'additional ideas or requests.' column
    df_cleaned = df.dropna(subset=['additional ideas or requests.'])
    # Create a new column 'shortened_ideas' to display truncated comments with a tooltip for full comment
    df_cleaned['shortened_ideas'] = df_cleaned['additional ideas or requests.'].apply(lambda x: (x[:2000] + '...') if len(x) > 2000 else x)

    # Display the DataFrame within a container that has horizontal scrolling enabled
    st.markdown('<div class="dataframe-container">', unsafe_allow_html=True)
    st.dataframe(df_cleaned[['shortened_ideas']],width=1000, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)


if selected_question == "For Future Surveys":
    # st.subheader("Inspirations")
    st.markdown("""
Demographic data, which is crucial for understanding a group's preferences and expectations, is missing in this survey. 
- **Different ages and genders** tend to have varied preferences for activities, food, and availability. For example, younger employees may prioritize professional development, like workshops on new technologies, while established employees might value work-life balance initiatives.
- **Cultural and family backgrounds** also influence preferences. People with similar backgrounds in cultures, marital status, and children often share mutual topics and preferred activities.
- **Work experiences** also play a role. New graduates might feel more comfortable engaging in activities with their peers rather than with senior management. They aslo seek networking and mentoring opportunities. In contrast, mid-career employees might prefer leadership training.

By collecting demographic data, we can gain a better understanding of the engaging group and customize events accordingly to enhance participation and satisfaction.

In future surveys, we might add more questions to obtain data such as **gender**, **age**, **marital status**, **children**, etc. For people who are interested in children's events, charity, community services, or pet events, we might also ask for their **availability during weekends**.
""")

    
    st.write('''Analyst: Holly Hou  
             Position: Intern, Event Marketing  
             Contact: xinyu.hou@healthtrustpg.com''')
  

    

