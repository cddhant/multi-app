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
		st.subheader("Outliers Remover")
		data = st.file_uploader("Upload a Dataset", type=["csv", "txt", "xlsx"])
		if data is not None:
			df = pd.read_csv(data)
			st.dataframe(df.head())

			# Select the column to plot box_plot
			selected_column = st.selectbox("Single Columns", df.columns)

			# Visualizing the outliers using box-plot
			fig, ax = plt.subplots()
			sns.boxplot(x=df[selected_column], ax=ax)
			ax.set_xlabel(selected_column)
			ax.set_title("Box Plot of {}".format(selected_column))
			st.pyplot(fig)

			# Multiple Box Plot
			selected_columns = st.multiselect("Select a column to remove outliers from", df.columns)
			if len(selected_columns) > 0:
				cust_plot= df[selected_columns].plot(kind="box")
				st.write(cust_plot)
				st.pyplot()
			else:
				st.warning("Please select at least one column.")


			# Removing the outliers from the selected column using IOR
			Q1 = df[selected_column].quantile(0.25)
			Q3 = df[selected_column].quantile(0.75)
			IQR = Q3 - Q1
			df_cleaned = df[(df[selected_column] >= Q1 - 1.5*IQR) & (df[selected_column] <= Q3 + 1.5*IQR)]

			# Showing the cleaned data
			st.write("Cleaned Data")
			st.write(df_cleaned.head(10))

			# Showing the difference between the original and cleaned data
			fig, ax = plt.subplots()
			ax.scatter(df.index, df[selected_column], label="Outliers")
			ax.scatter(df_cleaned.index, df_cleaned[selected_column], label="Data Points")
			ax.set_xlabel("Sample")
			ax.set_ylabel(selected_column)
			ax.set_title("Visual Representation of Outlliers")
			ax.legend()
			st.pyplot(fig)

			# # Boxplot After Cleaning the data
			# # Select the column to remove outliers from
			# selected_column = st.selectbox("Select the column", df.columns)

			# # Visualize the outliers using a box plot
			# fig, ax = plt.subplots()
			# sns.boxplot(x=df[selected_column], ax=ax)
			# ax.set_xlabel(selected_column)
			# ax.set_title("Updated Box Plot of {}".format(selected_column))
			# st.pyplot(fig)
			
			# Download Cleaned data
			csv = df_cleaned.to_csv(index=False)
			b64 = base64.b64encode(csv.encode()).decode()
			href = f'<a href="data:file/csv;base64,{b64}" download="cleaned_data.csv">Download Cleaned Data</a>'
			st.markdown(href, unsafe_allow_html=True)




			# selected_columns = st.multiselect("Select columns to plot", df.columns)
			# if len(selected_columns) > 0:
			# 	st.subheader("Box Plots")
			# 	fig, ax = plt.subplots()
			# 	data.boxplot(selected_columns, ax)
			# 	ax.set_xticklabels(selected_columns)
			# 	ax.set_ylabel('Value')
			# 	st.pyplot(fig)
			# else:
			# 	st.warning("Please select at least one column.")