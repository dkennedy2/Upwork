# -*- coding: utf-8 -*-
"""
IDLE
I recommend using anaconda spyder as an idle when Wrangling data. You can view variables with the variable explorer, as well as plots. 
-----Data Wrangling packages------
Pandas: Gives us dataframes, can perform math operations across entire dataset or just a column
Numpy: Gives us numpy arrays, can perform math operations across entire array
-----Graphing packages------------
matplotlib
Seaborn: I did not use this but another option to check out.
"""



# First we need to import packages to use their functionality. Use "import as pd" so we 
# can write pd.whatever instead of pandas.whatever when we call a function. Basically just a shortcut
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson
import matplotlib.pyplot as plt
import random
import scipy.stats

# bring csv file into dataframe with pd.read_csv, the string is the path to the file. Note: this is for windows, path for mac will be structured different
# bring xcel file into dataframe with pd.read_excel
background_df = pd.read_csv(r'C:\Users\cc-ch\Desktop\Upwork\Physics\background.csv')
cesium_df = pd.read_csv(r'C:\Users\cc-ch\Desktop\Upwork\Physics\cesium.csv')
muon_df = pd.read_excel(r'C:\Users\cc-ch\Desktop\Upwork\Physics\muon.xls')  # I added a header to the excel file and deleted the index
muon_df = muon_df.to_numpy() # I changed dataframe into a numpy array

# calculate the mean for the background
mean_background = background_df.mean() # I used the datafram function .mean() to calculate the mean across the entire dataset for each column, it returns a series
mean_background = mean_background[0] # df.mean() gave me a series but I just want a value. Here I just indexed the series to pull the value. (a series is kind of like a list, you can pull a single value from the series/list using an index)
# subract mean background counts from your measurements (cesium)
cesium_df = cesium_df - mean_background # applying math function (subtraction) to entire dataframe. You can apply it to a single column if you specify the column like this df['name_of_column']

# calculate the mean for your data sample
mean_cesium = cesium_df.mean() # same as above
mean_cesium = mean_cesium[0]

# plot histogram of cesium using the matplotlib package
first_edge, last_edge = cesium_df.min(), cesium_df.max() # first edge is the minimum value of your dataset. last_edge is the maximum. min() grabs the minimum value in the df, max() grabs the maximum value in the df
first_edge, last_edge = first_edge[0], last_edge[0] # because the above returned a series we need to index it to get the value
plt.hist(cesium_df, range=[first_edge, last_edge], bins = 7, edgecolor='black') # plots histogram, use range = to define the range of values to be included in the histogram, use bins = to define the number of bins, edgecolor controls the color outline of the bars
plt.xlabel('bins') # add x axis lables 
plt.ylabel('Frequency')
plt.title('Cesium Histogram') # add title
plt.show() # shows the plot, not needed in spyder because you have the plot explorer. If you are using something else you may need this to show the plot

# generate Poisson distribution with sample size 50
x = poisson.rvs(mu=mean_cesium, size=50)

#create plot of Poisson distribution
plt.hist(x, density=True, edgecolor='black')

# plot two histograms on same plot (page 6), To do so use two plt.hist functions
y = cesium_df # cesium data
x = x # poisson data
plt.hist(x, bins=7, alpha=0.5, label='Poisson') # alpha makes chart ligher color and more transparent
plt.hist(y, bins=7, alpha=0.5, label='Cesium', edgecolor='black')
plt.legend(loc='upper right') # add legend, loc stands for location (location of legend)
plt.xlabel('bins')
plt.ylabel('Frequency')
plt.title('Cesium Histogram with Poisson distrubution')
plt.show()
##############################################################################


# calculate the standard deviation of cesium
sigma = cesium_df.std()
sigma = sigma[0]
# use np.histogram to find counts in each bin 
counts, bin_edges = np.histogram(cesium_df, bins=7)
counts = list(counts) # can use list() to turn variable into a list. Sometimes you need different variable types.
# use numpy to take square root of counts to get standard deviation
error = list(np.sqrt(counts)) 


# Define Data
x = list(bin_edges[1:].astype(int)) 
# I turn bin_edges into a list  with list(), 
# I slice bin_edges with [1:] 1= the second value in the array, the blank means it goes to the end of the array. 
# So [1:] takes everything except the first element.
# [:3] would take the firstthree elements
# [1] would take the element at index 1 (the second element)
# used astype(int) to change the variable to type intiger from a float(number with decimals)
y= counts

# Plot Bar chart 
plt.bar(x,y, width = 4) # width increases the width of the bars. x = data on the x axis, y = data data on the y axis
plt.plot(x,y, linestyle='dotted') # Here you can plot the line graph ontop of the bar graph. linestyle is set to dotted. This should be your trend line nq
plt.errorbar(x, y, yerr = error, fmt='o',ecolor = 'red') # Plot error bars, set yeer equal to the error, ecolor controls the color of the error bars
# Set axes limit
plt.xlim(320, 380) # limits x axis on graph
plt.ylim(0,16)      # limits y axis on graph
plt.xlabel('bins')
plt.ylabel('Counts')
plt.title('Cesium Histogram with error bars')
plt.show()

#######################################################################################

 
# plot histogram of muon using the matplotlib package
# ADC channel numbers less than	125	and	greater	than 4075, userange parameter, set number of bins to 200 using the bin parameter
first_edge, last_edge = muon_df.min(), muon_df.max()
plt.hist(muon_df, range=[125, 4075], bins = 200)
plt.xlabel('Data')
plt.ylabel('Counts')
plt.title('Muon Decay')
plt.grid(True)
plt.show()

###

counts, bin_edges = np.histogram(muon_df, bins=200)
counts = list(np.log10(counts))
error = list(np.sqrt(counts))
# counts, bin_edges = np.histogram(muon_df, bins=200)
# counts = list(counts)
# error = list(counts)

# Define Data
x = list(bin_edges[1:].astype(int))
y= counts

# Plot Bar chart
plt.bar(x,y, width = 25)
plt.xlim(125,4075) # limits data range along x axis
# plt.errorbar(x, y), yerr = error, fmt='o',ecolor = 'red') # Plot error bars, I think I did the calculation wrong here
plt.xlabel('ADC Channel')
plt.ylabel('Number of Evens (log)')
plt.title('Muon Decay')

# Getting the mean and standard deviation of the sample data dt using scipy.stats
mn, std = scipy.stats.norm.fit(muon_df) 
y_curve = scipy.stats.norm.pdf(bin_edges, mn, std)
# plot trend line
z = np.polyfit(x, y, 1) # Least squares polynomial fit.
p = np.poly1d(z) # A one-dimensional polynomial class.
plt.plot(x,p(x),"r--") # p(x) you are multiplying two vectors and plotting this as y




# # plot histogram of background using the matplotlib package
# plt.hist(background_df, bins=[3,4,5,6,7,8,9,10,11,12,13,14])
