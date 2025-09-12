import streamlit as st

st.set_page_config(
    page_title="PROHI Dashboard",
    page_icon="👋",
)
# Sidebar configuration
st.sidebar.image("./assets/project-logo.jpg",)
st.sidebar.success("Select a tab above.")

# # Page information

st.write("# Welcome to PROHI Dashboard! 👋")

st.markdown(
"""
    ## Aims

    After completing the course the student should be able to:
    - explain basic project management methods
    - be able to account for success factors in Health Informatics projects
    - understand basic methods and tools in the field of data science and machine learning
    - explain process models for data mining projects
    - explain the difference between rule-based methods and machine learning methods
    - apply basic project management methods
    - work in an international multidisciplinary project group
    - independently lead and implement a limited project in health informatics - document the steps in the design of a prototype for a health informatics project
    - apply the steps in a process model for data mining projects
    - apply methods from the field of text mining on different types of health informatics problems
    - explain and argue for their positions regarding the implementation of a health informatics project
    - explain how to work with sensitive health information in a safe and ethical way.

"""
)

# You can also add text right into the web as long comments (""")
"""
The final project aims to apply data science concepts and skills on a 
medical case study that you and your team select from a public data source.
The project assumes that you bring the technical Python skills from 
previous courses (*DSHI*: Data Science for Health Informatics), as well as 
the analytical skills to argue how and why specific techniques could
enhance the problem domain related to the selected dataset.
"""

### UNCOMMENT THE CODE BELOW TO SEE EXAMPLE OF INPUT WIDGETS

## DATAFRAME MANAGEMENT
import numpy as np

dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)

#Add a slider to the sidebar:
add_slider = st.slider(
     'Select a range of values',
     0.0, 100.0, (25.0, 75.0)
 )
## Input Widgets
#date and time
import datetime
d = st.date_input("What is today's date", datetime.date(2025, 9, 11))
st.write("Today date is:", d)
# add color
color = st.color_picker("Pick your favorite Color for today", "#00f900")
st.write("Your Favourite color today is", color)
# Rate
st.write("How great was your day?")
sentiment_mapping = ["one", "two", "three", "four", "five"]
selected = st.feedback("stars")
if selected is not None:
    st.markdown(f"You selected {sentiment_mapping[selected]} star(s).")
    
## Input DATA
import pandas as pd
from numpy.random import default_rng as rng
st.write("Which app are you going to choose today?")
df = pd.DataFrame(
    {
        "name": ["Roadmap", "Extras", "Issues"],
        "url": [
            "https://maze.toys/",
            "https://www.boredbutton.com/",
            "https://mondrianandme.com/",
        ],
        "stars": rng(0).integers(0, 1000, size=3),
        "views_history": rng(0).integers(0, 5000, size=(3, 30)).tolist(),
    }
)

st.dataframe(
    df,
    column_config={
        "name": "App name",
        "stars": st.column_config.NumberColumn(
            "Github Stars",
            help="Number of stars on GitHub",
            format="%d ⭐",
        ),
        "url": st.column_config.LinkColumn("App URL"),
        "views_history": st.column_config.LineChartColumn(
            "Views (past 30 days)", y_min=0, y_max=5000
        ),
    },
    hide_index=True,
)

## Input Chart
from numpy.random import default_rng as rng
st.write("Check out this great chart!")
df = pd.DataFrame(
    {
        "col1": list(range(20)) * 3,
        "col2": rng(0).standard_normal(60),
        "col3": ["a"] * 20 + ["b"] * 20 + ["c"] * 20,
    }
)

st.area_chart(df, x="col1", y="col2", color="col3")


