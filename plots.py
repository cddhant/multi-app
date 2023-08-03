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
		st.subheader("Data Visualization")
		data = st.file_uploader("Upload a Dataset", type=["csv", "txt", "xlsx"])
		if data is not None:
			df = pd.read_csv(data)
			st.dataframe(df.head())


			if st.checkbox("Show Value Counts"):
				st.write(df.iloc[:,-1].value_counts().plot(kind='bar'))
				st.pyplot()
		
			# Customizable Plotting
			all_columns_names = df.columns.tolist()
			type_of_plot = st.selectbox("Select Type of Plot",["area", "bar", "line", "hist", "box", "scatter", "bubble"])
			selected_columns_names = st.multiselect("Select Columns To Plot",all_columns_names)

			if st.button("Generate Plot"):
				st.success("Generating Customizable Plot of {} for {}".format(type_of_plot,selected_columns_names))

				# Plots
				if type_of_plot == 'area':
					cust_data = df[selected_columns_names]
					st.area_chart(cust_data)

				elif type_of_plot == 'bar':
					cust_data = df[selected_columns_names]
					st.bar_chart(cust_data)

				elif type_of_plot == 'line':
					cust_data = df[selected_columns_names]
					st.line_chart(cust_data)

				
				elif type_of_plot == "scatter":
						cust_plot = df.plot.scatter(x=selected_columns_names[0], y=selected_columns_names[1])
						st.write(cust_plot)
						st.pyplot()

				elif type_of_plot == "bubble":
						bubble_size_column = st.selectbox("Select Column for Bubble Sizes", all_columns_names)
						cust_plot = df.plot.scatter(x=selected_columns_names[0], y=selected_columns_names[1], s=df[bubble_size_column])
						st.write(cust_plot)
						st.pyplot()

				# Custom Plot 
				elif type_of_plot:
					cust_plot= df[selected_columns_names].plot(kind=type_of_plot)
					st.write(cust_plot)
					st.pyplot()
