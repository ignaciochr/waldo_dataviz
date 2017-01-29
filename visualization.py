﻿import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set up dataframe for analysis 
df_original = datasets['set1']
df = df_original[['xaxis', 'yaxis']]

# Define and plot scatterplot with Seaborn
sns.regplot(x="xaxis", y="yaxis", data=df)

# Define and plot kernal density estimation graph with Seaborn
plt.figure(figsize=(15, 10))
sns.set_style("darkgrid")
sns.kdeplot(df['xaxis'],df['yaxis'], shade=True, cmap="Purples", shade_lowest=True)
