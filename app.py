import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.io.parsers import read_csv
import seaborn as sns
import streamlit as st

@st.cache
def load_data():
    df=read_csv("covid_vaccine_statewise.csv")
    return df

st.title("COVID-19 Data Analytics Dashboard")
st.sidebar.header("PROJECT OPTIONS")


choice= st.sidebar.radio("Select one",("About Project","View Dataset","View Graphs"))

if choice == "About Project":
    st.header("INTRODUCTION")
    st.image("cd4.png",width=400)
    st.info('''Coronaviruses are a large family of viruses which may cause illness in animals or humans. In humans, several coronaviruses are known to cause respiratory infections ranging from the common cold to more severe diseases such as Middle East Respiratory Syndrome (MERS) and Severe Acute Respiratory Syndrome (SARS). The most recently discovered coronavirus causes coronavirus disease COVID-19 - World Health Organization
The number of new cases are increasing day by day around the world. This dataset has information from the states and union territories of India at daily level.
State level data comes from Ministry of Health & Family Welfare
Testing data and vaccination data comes from covid19india. Huge thanks to them for their efforts!
Update on April 20, 2021: Thanks to the Team at ISIBang, I was able to get the historical data for the periods that I missed to collect and updated the csv file.
Content
COVID-19 cases at daily level is present in covid_19_india.csv file
Statewise testing details in StatewiseTestingDetails.csv file
Travel history dataset by @dheerajmpai - https://www.kaggle.com/dheerajmpai/covidindiatravelhistory
Acknowledgements
Thanks to Indian Ministry of Health & Family Welfare for making the data available to general public.
Thanks to covid19india.org for making the individual level details, testing details, vaccination details available to general public.
Thanks to Wikipedia for population information.
Thanks to the Team at ISIBang
Photo Courtesy - https://hgis.uw.edu/virus/
Inspiration
Looking for data based suggestions to stop / delay the spread of virus
''')

    st.header("VACCINATION")
    st.image("cd5.png",width=500)
    st.info('''“By working together, national leaders, the private sector and civil society can chart a faster, more equitable course out of the COVID-19 pandemic"''')
    st.info('''After children and adults are fully vaccinated for COVID-19, they can resume many activities that they did before the pandemic.
CDC recommends that fully vaccinated people wear a mask in public indoor settings if they are in an area of substantial or high transmission.
Fully vaccinated people might choose to mask regardless of the level of transmission, particularly if they or someone in their household is immunocompromised or at increased risk for severe disease, or if someone in their household is unvaccinated. People who are at increased risk for severe disease include older adults and those who have certain medical conditions, such as diabetes, overweight or obesity, and heart conditions.''')
    st.header("LIBRARIES USED")
    lib=st.radio("SELECT ONE ",("Pandas", "Numpy" ,"Matplotlib" ,"streamlit" ,"seaborn"))
    if lib=="Pandas":
        st.image("everything-about-pandas.png",width=400)
        st.info('''Pandas is an open source Python package that is most widely used for data science/data analysis and machine learning tasks. It is built on top of another package named Numpy, which provides support for multi-dimensional arrays. As one of the most popular data wrangling packages, Pandas works well with many other data science modules inside the Python ecosystem, and is typically included in every Python distribution, from those that come with your operating system to commercial vendor distributions like ActiveState’s ActivePython. 
    Pandas makes it simple to do many of the time consuming, repetitive tasks associated with working with data, including:

- Data cleansing
- Data fill
- Data normalization
- Merges and joins
- Data visualization
- Statistical analysis
- Data inspection
- Loading and saving data
And much more''')
    if lib=="Numpy":
        st.image("numpy.png",width=400)
        st.info('''NumPy is a Python library used for working with arrays.

It also has functions for working in domain of linear algebra, fourier transform, and matrices.

NumPy was created in 2005 by Travis Oliphant. It is an open source project and you can use it freely.

NumPy stands for Numerical Python.

Python we have lists that serve the purpose of arrays, but they are slow to process.

NumPy aims to provide an array object that is up to 50x faster than traditional Python lists.

The array object in NumPy is called ndarray, it provides a lot of supporting functions that make working with ndarray very easy.

Arrays are very frequently used in data science, where speed and resources are very important.''')
    if lib=="Matplotlib":
        st.image("matplotlib.png",width=400)
        st.info('''Matplotlib is a low level graph plotting library in python that serves as a visualization utility.

Matplotlib was created by John D. Hunter.

Matplotlib is open source and we can use it freely.

Matplotlib is mostly written in python, a few segments are written in C, Objective-C and Javascript for Platform compatibility.t first sight, it will seem that there are quite some components to consider when you start plotting with this Python data visualization library. You’ll probably agree with me that it’s confusing and sometimes even discouraging seeing the amount of code that is necessary for some plots, not knowing where to start yourself and which components you should use.

Luckily, this library is very flexible and has a lot of handy, built-in defaults that will help you out tremendously. As such, you don’t need much to get started: you need to make the necessary imports, prepare some data, and you can start plotting with the help of the plot() function! When you’re ready, don’t forget to show your plot using the show() function''')
    if lib=="streamlit":
        st.image("st.png",width=400)
        st.info(''' Streamlit is an open-source python framework for building web apps for Machine Learning and Data Science. We can instantly develop web apps and deploy them easily using Streamlit. Streamlit allows you to write an app the same way you write a python code. Streamlit makes it seamless to work on the interactive loop of coding and viewing results in the web app.Data flow
Streamlit allows you to write an app the same way you write a python code. The streamlit has a distinctive data flow, any time something changes in your code or anything needs to be updated on the screen, streamlit reruns your python script entirely from the top to the bottom. This happens when the user interacts with the widgets like a select box or drop-down box or when the source code is changed.

If you have some costly operations while rerunning your web app, like loading data from databases, you can use streamlit’s st.cache method to cache those datasets, so that it loads faster.
- Streamlit runs the python script from top to bottom
- Each time the user interacts the script is a rerun from top to bottom
- Streamlit allows you to use caching for costly operations like loading large datasets.''')
    if lib=="seaborn":
        st.image("seaborn.png",width=400)
        st.info(''' Seaborn is an open-source Python library built on top of matplotlib. It is used for data visualization and exploratory data analysis. Seaborn works easily with dataframes and the Pandas library. The graphs created can also be customized easily.
    It provides a high-level interface for drawing attractive and informative statistical graphics.
    Seaborn helps you explore and understand your data. Its plotting functions operate on dataframes and arrays containing whole datasets and internally perform the necessary semantic mapping and statistical aggregation to produce informative plots. Its dataset-oriented, declarative API lets you focus on what the different elements of your plots mean, rather than on the details of how to draw them''')


if choice == "View Dataset":
    st.info("DATASETS USED")
    df=read_csv("covid_vaccine_statewise.csv")
    st.dataframe(df)

df= load_data()
df_state = df[df['State'] != 'India'].copy()
doses_df = df_state.groupby('State')['First Dose Administered'].mean().reset_index().sort_values(by='First Dose Administered',ascending=False)
df_up = df_state[df_state['State'] == 'Uttar Pradesh']


if choice == "View Graphs":
    options=['Total Doses Administered','First Dose Administered',
    'Second Dose Administered','Male (Doses Administered)','Female (Doses Administered)',
    'Transgender (Doses Administered)','18-44 Years (Doses Administered)',
    '45-60 Years (Doses Administered)','60+ Years (Doses Administered)','Total Individuals Vaccinated','Sessions',
    ' Sites '] 
    choice_in = st.sidebar.selectbox("Select an option",options)




    if choice_in == options[0]:
        fig,ax=plt.subplots()
        df_state.groupby('State')['Total Doses Administered'].mean().plot(kind='bar',
            figsize=(15,6),
            color='green',ax= ax)
        st.pyplot(fig)

    if choice_in == options[1]:
        fig,ax=plt.subplots()
        doses_df.set_index('State').head(10)['First Dose Administered'].plot(kind='pie',figsize=(10,12),
                            startangle=90,
                            wedgeprops={'width':.5},
                            radius=1,
                            autopct='%.1f%%',
                            pctdistance = .9, 
                            textprops={'color':'black'},
                            rotatelabels=True,ax=ax)
        plt.ylabel('states')
        plt.xlabel('number of first doses')
        st.pyplot(fig)


    if choice_in == options[2]:
        fig,ax=plt.subplots()
        df_state.groupby('State')['Second Dose Administered'].mean().reset_index().sort_values(by='Second Dose Administered',ascending=False).plot(kind='bar',
                            figsize=(15,6),
                            color='black',ax=ax)
        plt.xlabel('States')
        plt.ylabel('number of second doses')
        st.pyplot(fig)


    if choice_in == options[3]:
        fig,ax=plt.subplots()
        df_state.plot(kind='area',x='Updated On',y='Male (Doses Administered)',
                        figsize=(15,6),
                        color='green',ax=ax)
        plt.title("MALE")
        plt.xlabel('dates')
        plt.ylabel('number of male doses') 
        st.pyplot(fig) 


    if choice_in == options[4]:
        fig,ax=plt.subplots()
        df_state.plot(kind='area',x='Updated On',y='Female (Doses Administered)',
                figsize=(15,6),
                color='purple',ax=ax)
        plt.title("FEMALE")
        plt.xlabel('dates')
        plt.ylabel('number of female doses')
        st.pyplot(fig)
    

    
    if choice_in == options[5]:
        fig,ax=plt.subplots()
        df_state.plot(kind='area',x='Updated On',y='Transgender (Doses Administered)',
                    figsize=(15,6),
                    color='red',ax=ax)
        plt.title("Transgender")
        plt.xlabel('dates')
        plt.ylabel('number of Transgender doses')
        st.pyplot(fig)





    if choice_in == options[6]:
        fig,ax=plt.subplots()
        df_state.groupby('State')['18-44 Years (Doses Administered)'].sum().reset_index().set_index('State').sort_values(by='18-44 Years (Doses Administered)',
                    ascending=False).plot(kind='bar',
                    figsize=(15,6),
                    color='blue',ax=ax)
        plt.xlabel('States')
        plt.ylabel('18-44 years doses')
        st.pyplot(fig)
    

    
    if choice_in == options[7]:
        fig,ax=plt.subplots()
        df_state.groupby('State')['45-60 Years (Doses Administered)'].sum().reset_index().set_index('State').sort_values(by='45-60 Years (Doses Administered)',
                ascending=False).plot(kind='bar',
                figsize=(15,6),
                color='purple',ax=ax)
        plt.xlabel('States')
        plt.ylabel('45-60 years doses')
        st.pyplot(fig)


        

    if choice_in == options[8]:
        fig,ax=plt.subplots()
        df_state.groupby('State')['60+ Years (Doses Administered)'].sum().reset_index().set_index('State').sort_values(by='60+ Years (Doses Administered)',
                    ascending=False).plot(kind='bar',
                    figsize=(15,6),
                    color='black',ax=ax)
        plt.xlabel('States')
        plt.ylabel('60+ years doses')
        st.pyplot(fig)

    


    if choice_in == options[9]:
        fig,ax=plt.subplots()
        df_up.plot(kind='area',x='Updated On',y='Total Individuals Vaccinated',
                figsize=(15,6),
                color='red',ax=ax)
        plt.xlabel('dates')
        plt.ylabel('total individual doses')
        st.pyplot(fig)

    
    if choice_in == options[10]:
        fig,ax=plt.subplots()
        df_up.plot(kind='area',x='Updated On',y='Sessions',
                figsize=(10,6),
                color='green',ax=ax)
        plt.xlabel('dates')
        plt.ylabel('sessions')
        st.pyplot(fig)
    

    if choice_in == options[11]:
        fig,ax=plt.subplots()
        df_up.plot(kind='area',x='Updated On',y=' Sites ',
        figsize=(15,6),
        color='purple',ax=ax)    
        plt.xlabel('dates')
        plt.ylabel('sites')
        st.pyplot(fig)
    

    
    
    
