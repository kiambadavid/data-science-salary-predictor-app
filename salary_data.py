import pandas as pd
import streamlit as st


def app():
    df = pd.read_csv('ds_salaries.csv')

    st.title('The dataset')
    st.write('The data is from [Kaggle](https://www.kaggle.com/datasets/harishkumardatalab/data-science-salary-2021-to-2023) datasets.')
    st.dataframe(df)

    st.download_button(
        label="Download data as CSV",
        data=df.to_csv().encode('utf-8'),
        key='download_button',
        file_name='https://www.kaggle.com/datasets/harishkumardatalab/data-science-salary-2021-to-2023.csv',
        mime='text/csv'
    )











