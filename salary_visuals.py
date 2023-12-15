import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import seaborn as sns
import streamlit as st


def app():
    data = pd.read_csv('ds_salaries.csv')

    # Streamlit app title
    st.title("Interactive Data Visualization")

    # Sidebar options for plot selection
    st.sidebar.header("Select Plot Type")
    plot_type = st.sidebar.selectbox("Choose Plot Type", ["Scatter Plot", "Histogram", "Bar Plot", "Box Plot", "Correlation Heatmap"])

    # Sidebar options for customization
    st.sidebar.header("Customize Plot")
    selected_x = st.sidebar.selectbox("Select X-axis", data.columns)
    selected_y = st.sidebar.selectbox("Select Y-axis", data.columns)

    # Generate and display the selected plot
    st.subheader(f"{plot_type} based on {selected_x} and {selected_y}")

    if plot_type == "Scatter Plot":
        fig = px.scatter(data, x=selected_x, y=selected_y, title=f"{plot_type} of {selected_x} vs. {selected_y}")
        st.plotly_chart(fig)

    elif plot_type == "Histogram":
        fig, ax = plt.subplots(figsize=(18,5))
        ax.hist(data[selected_x], bins=30)
        ax.set_xlabel(selected_x)
        ax.set_ylabel("Frequency")
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

    elif plot_type == "Bar Plot":
        fig, ax = plt.subplots(figsize=(18,5))
        sns.barplot(data=data, x=selected_x, y=selected_y, ax=ax)
        ax.set_xlabel(selected_x)
        ax.set_ylabel(selected_y)
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

    elif plot_type == "Box Plot":
        fig, ax = plt.subplots(figsize=(18,5))
        sns.boxplot(data=data, x=selected_x, y=selected_y, ax=ax)
        ax.set_xlabel(selected_x)
        ax.set_ylabel(selected_y)
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

    elif plot_type == "Correlation Heatmap":

        # Filter out non-numeric columns before creating the heatmap
        numeric_data = data.select_dtypes(include='number')
        corr = numeric_data.corr()
        fig, ax = plt.subplots()
        sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
        ax.set_title(f"Correlation Heatmap of Numeric Columns")

        # Save the heatmap as a file
        plt.savefig("correlation_heatmap.png")

        # Display the saved heatmap
        st.image("correlation_heatmap.png")
