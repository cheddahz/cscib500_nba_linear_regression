# NBA 2017-2018 Player Statistics Using Linear Regression
# Author: Jay Cheatham
# CSCIB500 - Practical Computing for Computational Scientists (Fall 2019)
# Dr. Brian Canada

# Imports the needed modules
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd
import seaborn as sns

# Generates the data from the CSV file
nba = pd.read_csv('nba.csv')
x = nba.MP # MP = Minutes Played
y = nba.PER # PER = Player efficiency rating

# I've decided to see (using linear regression) the relationship
# between a player's Minutes Player (MP) versus their Player Efficiency Rating (PER). 
# MP is a statistical value in sports that complies the amount of minutes a player has played.
# PER is a "all in one basketball rating" created by John Hollinger that puts together
# all the contributions made by a player into one statistical value

# Performing the linear regression [taken from the linear regression code done in class]
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
print("slope: %f    intercept: %f" % (slope, intercept))

# Getting the coefficient of determination (R-squared) [taken from the linear regression code done in class]
print("R-squared: %f" % r_value**2)

# Plots the MP and PER data with a fitted line to show the regression line
sns.set_style('whitegrid')
figure = plt.figure(figsize=(8, 8))
axes = sns.scatterplot(x=nba.MP, y=nba.PER)
axes.set_ylim(-50, 50)
axes.set_title('Using Linear Regression to Find Relationship Between MP and PER')
axes.set_xlabel('Minutes Played (MP)')
axes.set_ylabel('Player Efficiency Rating (PER)')
plt.plot(x, intercept + slope*x, 'r', label='fitted line')
plt.legend()