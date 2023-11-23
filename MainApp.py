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

# Setting selection option
st.set_option('deprecation.showPyplotGlobalUse', False)

def main():
	""" Multi-App """

	# Selection List
	activities = ["EDA","Plots", "AutoScaller", "Outliers Remover", "PCA"]	
	choice = st.sidebar.selectbox("Select Activities",activities)

	if choice == 'EDA':
		#subapp1
		import eda
		eda.run()


	elif choice == 'Plots':
		#subapp2
		import plots
		plots.run()


	elif choice == 'AutoScaller':
		#subapp3
		import autoscalar
		autoscalar.run()

    
	elif choice == 'Outliers Remover':
		#subapp4
		import outliers
		outliers.run()

	elif choice == 'PCA':
		#subapp5
		import pca
		pca.run()

		
if __name__ == '__main__':
	main()
