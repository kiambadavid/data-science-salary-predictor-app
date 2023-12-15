import streamlit as st
from streamlit_option_menu import option_menu
import salary_model, salary_data, salary_visuals


st.set_page_config(page_title='Data Science Salary Predictor App', layout='wide', initial_sidebar_state='expanded')
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def run():
    with st.sidebar:
        app = option_menu(
            menu_title='Data Science Salary Predictor App',
            options=['Salary ML Model', 'Salary Data Visuals', 'The Dataset'],
            menu_icon=['app'],
            icons=['robot', 'bar-chart', 'table'],
            default_index=1,
            styles={
                'menu-title': {'color': 'white'},
                'container': {'padding': '5!important', 'background-color':'black'},
                'icon': {'color': 'white', 'font-size': '23px'},
                'nav-link': {'color': 'white', 'font-size': '20px', 'text-align': 'left', 'margin':'0px'},
                'nav-link-selected': {'background-color': '#02ab21'},
            }
        )

    if app == 'Salary ML Model':
        salary_model.app()

    if app == 'The Dataset':
        salary_data.app()
        
    if app == 'Salary Data Visuals':
        salary_visuals.app()




class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, function):
        self.apps.append(
            {
                'title': title,
                'function': function
            }
        )

    run()

st.sidebar.markdown("""
---
Created by [David Kiamba](https://github.com/kiambadavid)
""")

    
