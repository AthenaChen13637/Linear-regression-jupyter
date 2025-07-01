import sys
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

if len(sys.argv) != 4:
    print("Usage: python linear_regression_python.py <filename> <x_column> <y_column>")
    sys.exit(1)

filename = sys.argv[1]
x_col = sys.argv[2]
y_col = sys.argv[3]

data = pd.read_csv(filename)
model = LinearRegression()
model.fit(data[[x_col]], data[[y_col]])

plt.scatter(data[[x_col]], data[[y_col]], color='red')
plt.plot(data[[x_col]], model.predict(data[[x_col]]), color='blue')
plt.title(f'{y_col} vs {x_col}')
plt.xlabel(x_col)
plt.ylabel(y_col)
plt.savefig("linear_regression_python_output.png")
plt.show()



#!/usr/bin/env python
# coding: utf-8

# This notebook demonstrates a simple linear regression analysis using [Python] to model Salary based on Years of Experience.

# This step use pandas to load the CSV into DataFrame

# In[1]:


import pandas as pd
dataset = pd.read_csv("regression_data.csv")  ## Read the data file


# This step use matplotlib to generate a scatter plot

# In[2]:


import matplotlib.pyplot as plt
plt.scatter(dataset["YearsExperience"], dataset["Salary"], color="red")  ## Make the origrinal plot without any processing


# This step use scikit-learn to fit a linear regression model

# In[3]:


from sklearn.linear_model import LinearRegression
model = LinearRegression()  ## Tell Python which model to fit in ##
model.fit(dataset[["YearsExperience"]], dataset[["Salary"]])  ## Tell Python how to fit in the model ##


# This step plot the predicted regression line

# In[4]:


plt.plot(dataset["YearsExperience"], model.predict(dataset[["YearsExperience"]]), color="blue")  ## Tell Python how to draw the fitted plot ##
plt.title("Salary vs Experience")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()


# This step gives the R^2 value

# In[6]:


model.score(dataset[["YearsExperience"]], dataset[["Salary"]])  # R-squared

