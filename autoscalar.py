import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import matplotlib
matplotlib.use("Agg")
import seaborn as sns
import base64
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import plotly.express as px

def run():
    st.subheader("Auto-Scaler")
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.dataframe(df.head())

        scalarcolumns = []  # Initialize the variable
        df_scaled = None  # Initialize the variable

        if st.checkbox("Show Columns"):
            scalarcolumns = df.columns.to_list()
            st.write(scalarcolumns)

        # Select the columns to scale
        selected_columns = st.multiselect("Select columns to scale", scalarcolumns)
        if len(selected_columns) > 0:
            scaler = StandardScaler()
            df_scaled = pd.DataFrame(scaler.fit_transform(df[selected_columns]), columns=selected_columns)

        if df_scaled is not None:  # Check if df_scaled is assigned a value
            st.write("Scaled Data")
            st.write(df_scaled.head(10))

            # Showing the difference between the original and scaled data
            fig, ax = plt.subplots()
            ax.plot(df[selected_columns], label="Original")
            ax.plot(df_scaled, label="Scaled")
            ax.set_xlabel("Sample")
            ax.set_ylabel("Value")
            ax.set_title("Difference between Original and Scaled Data")
            ax.legend()
            st.pyplot(fig)

            # Download Scaled
            csv = df_scaled.to_csv(index=False)
            b64 = base64.b64encode(csv.encode()).decode()
            href = f'<a href="data:file/csv;base64,{b64}" download="scaled_data.csv">Download Scaled Data</a>'
            st.markdown(href, unsafe_allow_html=True)