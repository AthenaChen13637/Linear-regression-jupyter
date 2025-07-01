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

