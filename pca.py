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
		st.subheader("Principal Component Analysis")
		data = st.file_uploader("Upload a Dataset", type=["csv", "txt", "xlsx"])
		if data is not None:
			df = pd.read_csv(data)
			st.dataframe(df.head())
			
			st.write("Shape  of the dataset")
			st.write(df.shape)

			# Performing PCA with three components
			pca = PCA(n_components=3)
			pca.fit(df)
			transformed = pca.transform(df)


			# Creating a 3D scatter plot with plotly
			fig = px.scatter_3d(
				transformed, x=transformed[:, 0], y=transformed[:, 1], z=transformed[:, 2],
				color=np.arange(len(df)), labels={'color': 'Index'}
			)

			fig.update_traces(marker=dict(size=5))
			fig.update_layout(title="PCA 3D Scatter Plot")
			st.plotly_chart(fig)
			

			# Names of the columns
			column_names = df.columns.tolist()

			# Extracting the first two principal components
			first_pc = pca.components_[0]
			second_pc = pca.components_[1]
			third_pc = pca.components_[2]

			# Creating a data frame with the principal component names and values
			pc_df = pd.DataFrame({'PC1': first_pc, 'PC2': second_pc, 'PC3': third_pc}, index=column_names)

			# Printing the data frame
			st.write("Principal Components and Values")
			st.write(pc_df)

			# Showing the explained variance ratio of the principal components
			st.write("Explained Variance Ratio")
			st.write(pca.explained_variance_ratio_)

			# Download Dataset
			csv = pc_df.to_csv(index=False)
			b64 = base64.b64encode(csv.encode()).decode()
			href = f'<a href="data:file/csv;base64,{b64}" download="principal_components.csv">Principal Components Data</a>'
			st.markdown(href, unsafe_allow_html=True)