import joblib
import pandas as pd
import streamlit as st


def app():
    # load model
    model = joblib.load("Data_Science_Salary_Predictor.pkl")

    # html style template
    html_temp = """
    <div style ="background-color:white;padding:5px">
    <h1 style ="color:black;text-align:center;">Data Science Salary Prediction App</h1>
    </div>
    """

    st.markdown(html_temp, unsafe_allow_html=True)

    # App description
    expander_bar = st.expander('App Description')
    expander_bar.markdown(
    'This Application provides insight on annual salary of a Data Scientist. The features (the user input) used for\n'
    'input are **Experience Level**, **Employment Type**, **Job Title**, **Company Location**, **Company Size** and\n'
    '**Employee Residence**. The Job Title is based upon a choice from the **Job Category** input.'
    'The output (label) expected is **Salary in US Dollars ($)**.\n'
    'The data used for training was collected from a period of **4 years** (2020-2023).'
    )

    # Input form for user to enter data
    st.sidebar.header("User Input")

    # Define job title groups and associated jobs
    job_title_groups = {
    "Data Scientist": [
    'Principal Data Scientist',
    'Data Scientist',
    'Applied Scientist',
    'Applied Data Scientist',
    'Lead Data Scientist',
    'Data Science Engineer',
    'Data Scientist Lead',
    'Product Data Scientist',
    'Staff Data Scientist'
    ],

    "Machine Learning Engineer": [
    'ML Engineer',
    'Research Engineer',
    'Machine Learning Engineer',
    'Computer Vision Engineer',
    'Applied Machine Learning Engineer',
    'MLOps Engineer',
    'Machine Learning Infrastructure Engineer',
    'Deep Learning Engineer',
    'Machine Learning Software Engineer',
    'Computer Vision Software Engineer',
    'Machine Learning Research Engineer',
    'NLP Engineer',
    'Machine Learning Developer',
    '3D Computer Vision Researcher',
    'Principal Machine Learning Engineer',
    'Lead Machine Learning Engineer'
    ],

    "Data Analyst": [
    'Data Analyst',
    'Data Modeler',
    'Data Strategist',
    'Data Quality Analyst',
    'Compliance Data Analyst',
    'Data Analytics Manager',
    'Business Data Analyst',
    'Staff Data Analyst',
    'Data Specialist',
    'Lead Data Analyst',
    'Financial Data Analyst',
    'Data Analytics Specialist',
    'Insight Analyst',
    'Product Data Analyst',
    'Data Analytics Lead',
    'Data Analytics Engineer',
    'Data Analytics Consultant',
    'Marketing Data Analyst',
    'Principal Data Analyst',
    'Finance Data Analyst'
    ],

    'Data Engineer': [
    'Analytics Engineer',
    'Data Engineer',
    'Data Architect',
    'ETL Engineer',
    'Data DevOps Engineer',
    'Big Data Engineer',
    'Cloud Database Engineer',
    'Data Infrastructure Engineer',
    'Software Data Engineer',
    'Data Operations Engineer',
    'Big Data Architect',
    'Azure Data Engineer',
    'Marketing Data Engineer',
    'Cloud Data Engineer',
    'Data Operations Analyst',
    'Principal Data Architect',
    'ETL Developer',
    'Cloud Data Architect',
    'Lead Data Engineer',
    'Principal Data Engineer'
    ],

    'Business Intelligence': [
    'Business Intelligence Engineer',
    'BI Data Engineer',
    'BI Developer',
    'BI Analyst',
    'BI Data Analyst',
    'Power BI Developer'
    ],

    'AI Developer': [
    'AI Developer',
    'AI Scientist',
    'Autonomous Vehicle Technician',
    'AI Programmer'
    ],

    'Research Scientist': [
    'Research Scientist',
    'Machine Learning Researcher',
    'Machine Learning Scientist',
    'Applied Machine Learning Scientist',
    'Deep Learning Researcher'
    ],

    'Manager': [
    'Head of Data',
    'Data Science Manager',
    'Data Manager',
    'Director of Data Science',
    'Data Science Lead',
    'Data Science Consultant',
    'Head of Data Science',
    'Data Lead',
    'Manager Data Management',
    'Data Management Specialist',
    'Data Science Tech Lead',
    'Machine Learning Manager',
    'Head of Machine Learning'
    ]
    }

    # Streamlit app title
    st.title("Selected Options")

    # User selects a job category
    selected_category = st.sidebar.selectbox("Select a Job Category", list(job_title_groups.keys()))

    # Based on the selected category, allow the user to choose a job
    selected_job = st.sidebar.selectbox("Select a Job", job_title_groups[selected_category])

    # Other user inputs (experience_level, employment_type, etc.)
    experience_level = st.sidebar.selectbox("Experience Level", ['Senior ', 'Mid', 'Entry', 'Executive'])
    employment_type = st.sidebar.selectbox("Employment Type", ['Full Time', 'Contractor', 'Freelancer', 'Part Time'])
    company_location = st.sidebar.selectbox("Company Location",
                                     ['Spain', 'USA', 'Canada', 'Denmark', 'Nigeria', 'United Kingdom',
                                      'India', 'Hong Kong', 'Netherlands', 'Swizerland',
                                      'Central African Republic', 'France', 'Finland', 'Ukraine',
                                      'Ireland', 'Israel', 'Ghana', 'Colombia', 'Singarpore',
                                      'Australia', 'Sweden', 'Slovenia', 'Mexico', 'Brazil', 'Portugal',
                                      'Russia', 'Thailand', 'Croatia', 'Vietnam', 'Estonia', 'Armenia',
                                      'Bosnia and Herzegovina', 'Kenya', 'Greece', 'North Macedonia',
                                      'Latvia', 'Romania', 'Pakistan', 'Italy', 'Morocco', 'Poland',
                                      'Albania', 'Argentina', 'Lithuania', 'American Samoa',
                                      'Costa Rica', 'Iran', 'Bahamas', 'Hungary', 'Austria', 'Slovakia',
                                      'Czech Republic', 'Turkey', 'Puerto Rico', 'Bolivia',
                                      'Philippines', 'Belgium', 'Indonesia', 'Egypt',
                                      'United Arab Emirates', 'Luxembourg', 'Malaysia', 'Honduras',
                                      'Japan', 'Algeria', 'Iraq', 'China', 'New Zealand', 'Chile',
                                      'Moldova', 'Malta'])
    company_size = st.sidebar.selectbox("Company Size", ['Large', 'Small', 'Medium'])

    employee_residence = st.sidebar.selectbox('Employee Residence',
                                       ['Spain', 'USA', 'Canada', 'Germany', 'United Kingdom', 'Nigeria',
                                        'India', 'Hong Kong', 'Portugal', 'Netherlands', 'Switzerland',
                                        'Central African Republic', 'France', 'Australia', 'Finland',
                                        'Ukraine', 'Ireland', 'Israel', 'Ghana', 'Austria', 'Colombia',
                                        'Singapore', 'Sweden', 'Slovenia', 'Mexico', 'Uzbekistan',
                                        'Brazil', 'Thailand', 'Croatia', 'Poland', 'Kuwait', 'Viet Nam',
                                        'Cyprus', 'Argentina', 'Armenia', 'Bosnia and Herzegovina',
                                        'Kenya', 'Greece', 'Macedonia', 'Latvia', 'Romania', 'Pakistan',
                                        'Italy', 'Morocco', 'Lithuania', 'Belgium', 'American Samoa',
                                        'Iran', 'Hungary', 'Slovakia', 'China', 'Czech Republic',
                                        'Costa Rica', 'Turkey', 'Chile', 'Puerto Rico', 'Denmark',
                                        'Bolivia', 'Philipines', 'Dominican Republic', 'Egypt',
                                        'Indonesia', 'United Arab Emirates', 'Malaysia', 'Japan',
                                        'Estonia', 'Honduras', 'Tunisia', 'Russia', 'Algeria', 'Iraq',
                                        'Bulgaria', 'Jersey', 'Serbia', 'New Zealand', 'Moldova',
                                        'Luxembourg', 'Malta'])

    st.write(f"**Job Category**: {selected_category}")
    st.write(f"**Selected Job**: {selected_job}")

    # Rest of the user inputs
    st.write(f"**Experience Level**: {experience_level}")
    st.write(f"**Employment Type**: {employment_type}")
    st.write(f"**Company Location**: {company_location}")
    st.write(f"**Company Size**: {company_size}")
    st.write(f'**Employee Residence**: {employee_residence}')

    user_input = {
    'experience_level': [experience_level],
    'employment_type': [employment_type],
    'job_title': [selected_job],
    'company_location': [company_location],
    'company_size': [company_size],
    'employee_residence': [employee_residence]
    }

    user_df = pd.DataFrame(user_input)
    predicted_salary = model.predict(user_df)

    st.header("Predicted Salary in USD (**$**):")
    col1, col2 = st.columns(2)
    col1.metric('**Annual Salary**', round(predicted_salary[0]))
    col2.metric('**Monthly Salary**', round(predicted_salary[0]/12))
