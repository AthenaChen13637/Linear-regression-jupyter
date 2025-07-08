#!/usr/bin/env python
# coding: utf-8

# This notebook demonstrates a simple linear regression analysis using [Python] to model Salary based on Years of Experience.
#This step sets up the environment and use pandas to read the CSV into DataFrame
# In[12]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
from sklearn.metrics import mean_squared_error

#Read the data

df = pd.read_csv("regression_data.csv")  ## Read the data file
x = df["YearsExperience"].values
y = df["Salary"].values

# This step do a linear regression using linregress function and outputs parameters that evaluates the fit.

# In[13]:

# Linear regression

slope, intercept, r_value, p_value, std_err = linregress(x, y)
y_pred = slope * x + intercept
mse = mean_squared_error(y, y_pred)

print(f"Slope: {slope:.2f}")
print(f"Intercept: {intercept:.2f}")
print(f"r: {r_value:.2f}")
print(f"std: {std_err:.2f}")
print(f"MSE: {mse:.2f}")

# This step makes the scatter plot and the fitted plot

# In[26]:

# Plot

plt.scatter(x, y, color="green", label="row data")
plt.plot(x, y_pred, 'r-', label='Fitted Line')
plt.text(0.97, max(y) + 3500,
         f"y = {slope:.2f}x + {intercept:.2f}\n"
         f"r = {r_value:.2f}\nMSE = {mse:.2f}",
         fontsize=12)
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.title("Linear Regression")
plt.legend()
plt.savefig("regression_plot_python.png")
plt.show()

