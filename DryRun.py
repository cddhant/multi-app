# Core Packages
import streamlit as st

# EDA Packages
import pandas as pd 
import numpy as np 

# Data Viz Packages
import matplotlib.pyplot as plt 
import matplotlib
matplotlib.use("Agg")
import seaborn as sns

# AutoScaller Packages
import base64
from sklearn.preprocessing import StandardScaler

# PCA Packages
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import plotly.express as px


st.set_option('deprecation.showPyplotGlobalUse', False)

def main():
	""" Multi-App """

	activities = ["EDA","Plots", "AutoScaller", "Outliers Remover", "PCA"]	
	choice = st.sidebar.selectbox("Select Activities",activities)

	if choice == 'EDA':
		st.subheader("Exploratory Data Analysis")

		data = st.file_uploader("Upload a Dataset", type=["csv", "txt"])
		if data is not None:
			df = pd.read_csv(data)
			st.dataframe(df.head())
			

			if st.checkbox("Show Shape"):
				st.write(df.shape)

			if st.checkbox("Show Columns"):
				all_columns = df.columns.to_list()
				st.write(all_columns)

			if st.checkbox("Summary"):
				st.write(df.describe())

			if st.checkbox("Show Selected Columns"):
				selected_columns = st.multiselect("Select Columns",all_columns)
				new_df = df[selected_columns]
				st.dataframe(new_df)


			if st.checkbox("Correlation Plot(Seaborn)"):
				st.write(sns.heatmap(df.corr(),annot=True, cmap='YlGnBu', vmin=-1, vmax=1))
				st.pyplot()


			if st.checkbox("Pie Plot"):
				all_columns = df.columns.to_list()
				column_to_plot = st.selectbox("Select 1 Column",all_columns)
				pie_plot = df[column_to_plot].value_counts().plot.pie(autopct="%1.1f%%")
				st.write(pie_plot)
				st.pyplot()



	elif choice == 'Plots':
		st.subheader("Data Visualization")
		data = st.file_uploader("Upload a Dataset", type=["csv", "txt", "xlsx"])
		if data is not None:
			df = pd.read_csv(data)
			st.dataframe(df.head())


			if st.checkbox("Show Value Counts"):
				st.write(df.iloc[:,-1].value_counts().plot(kind='bar'))
				st.pyplot()
		
			# Customizable Plot

			all_columns_names = df.columns.tolist()
			type_of_plot = st.selectbox("Select Type of Plot",["area","bar","line","hist","box","kde"])
			selected_columns_names = st.multiselect("Select Columns To Plot",all_columns_names)

			if st.button("Generate Plot"):
				st.success("Generating Customizable Plot of {} for {}".format(type_of_plot,selected_columns_names))

				# Plot By Streamlit
				if type_of_plot == 'area':
					cust_data = df[selected_columns_names]
					st.area_chart(cust_data)

				elif type_of_plot == 'bar':
					cust_data = df[selected_columns_names]
					st.bar_chart(cust_data)

				elif type_of_plot == 'line':
					cust_data = df[selected_columns_names]
					st.line_chart(cust_data)

				# Custom Plot 
				elif type_of_plot:
					cust_plot= df[selected_columns_names].plot(kind=type_of_plot)
					st.write(cust_plot)
					st.pyplot()


	
	elif choice == 'AutoScaller':
		st.subheader("Auto-Scaler")
		uploaded_file = st.file_uploader("Choose a file")
		if uploaded_file is not None:
			df = pd.read_csv(uploaded_file)
			st.dataframe(df.head())

			if st.checkbox("Show Columns"):
				all_columns = df.columns.to_list()
				st.write(all_columns)

			# Select the columns to scale
			selected_columns = st.multiselect("Select columns to scale", all_columns)

			# Scale the selected columns using an autoscaler
			scaler = StandardScaler()
			df_scaled = pd.DataFrame(scaler.fit_transform(df[selected_columns]), columns=selected_columns)


			st.write("Scaled Data")
			st.write(df_scaled.head(10))

			 # Show the difference between the original and scaled data
			fig, ax = plt.subplots()
			ax.plot(df[selected_columns], label="Original")
			ax.plot(df_scaled, label="Scaled")
			ax.set_xlabel("Sample")
			ax.set_ylabel("Value")
			ax.set_title("Difference between Original and Scaled Data")
			ax.legend()
			st.pyplot(fig)

			# Allow the user to download the scaled data
			csv = df_scaled.to_csv(index=False)
			b64 = base64.b64encode(csv.encode()).decode()
			href = f'<a href="data:file/csv;base64,{b64}" download="scaled_data.csv">Download Scaled Data</a>'
			st.markdown(href, unsafe_allow_html=True)

    
	elif choice == 'Outliers Remover':
		st.subheader("Outliers Remover")
		data = st.file_uploader("Upload a Dataset", type=["csv", "txt", "xlsx"])
		if data is not None:
			df = pd.read_csv(data)
			st.dataframe(df.head())

			# Select the column to remove outliers from
			selected_column = st.selectbox("Select a column to remove outliers from", df.columns)

			# Visualize the outliers using a box plot
			fig, ax = plt.subplots()
			sns.boxplot(x=df[selected_column], ax=ax)
			ax.set_xlabel(selected_column)
			ax.set_title("Box Plot of {}".format(selected_column))
			st.pyplot(fig)

			# Remove the outliers from the selected column
			Q1 = df[selected_column].quantile(0.25)
			Q3 = df[selected_column].quantile(0.75)
			IQR = Q3 - Q1
			df_cleaned = df[(df[selected_column] >= Q1 - 1.5*IQR) & (df[selected_column] <= Q3 + 1.5*IQR)]

			# Show the cleaned data
			st.write("Cleaned Data")
			st.write(df_cleaned.head(10))

			# Show the difference between the original and cleaned data
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
			
			# Allow the user to download the cleaned data
			csv = df_cleaned.to_csv(index=False)
			b64 = base64.b64encode(csv.encode()).decode()
			href = f'<a href="data:file/csv;base64,{b64}" download="cleaned_data.csv">Download Cleaned Data</a>'
			st.markdown(href, unsafe_allow_html=True)

	elif choice == 'PCA':
		st.subheader("Principal Component Analysis")
		data = st.file_uploader("Upload a Dataset", type=["csv", "txt", "xlsx"])
		if data is not None:
			df = pd.read_csv(data)
			st.dataframe(df.head())

			# Perform PCA with two components
			pca = PCA(n_components=3)
			pca.fit(df)
			transformed = pca.transform(df)


			# Create a 3D scatter plot with plotly
			fig = px.scatter_3d(
				transformed, x=transformed[:, 0], y=transformed[:, 1], z=transformed[:, 2],
				color=np.arange(len(df)), labels={'color': 'Index'}
			)

			fig.update_traces(marker=dict(size=5))
			fig.update_layout(title="PCA 3D Scatter Plot")
			st.plotly_chart(fig)
			

			# Get the names of the columns
			column_names = df.columns.tolist()

			# Get the first two principal components
			first_pc = pca.components_[0]
			second_pc = pca.components_[1]
			third_pc = pca.components_[2]

			# Create a data frame with the principal component names and values
			pc_df = pd.DataFrame({'PC1': first_pc, 'PC2': second_pc, 'PC3': third_pc}, index=column_names)

			# Print the data frame
			st.write("Principal Component Names and Values")
			st.write(pc_df)

			# Show the explained variance ratio of the principal components
			st.write("Explained Variance Ratio")
			st.write(pca.explained_variance_ratio_)

		
if __name__ == '__main__':
	main()
