import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set the title of the app
st.title('Simple Data Visualization')

# Description of the app
st.write("This is a simple Streamlit app to visualize data using different chart types.")

# Generate a random dataset
data = pd.DataFrame(
    np.random.randn(100, 3),
    columns=['A', 'B', 'C']
)

# Display the dataframe
st.write("Here is the dataset we are working with:")
st.write(data)

# Line chart
st.write("Line chart of the dataset:")
st.line_chart(data)

# Area chart
st.write("Area chart of the dataset:")
st.area_chart(data)

# Bar chart
st.write("Bar chart of the dataset:")
st.bar_chart(data)

# Matplotlib chart
st.write("Histogram of the dataset columns:")
fig, ax = plt.subplots()
data.hist(ax=ax)
st.pyplot(fig)
