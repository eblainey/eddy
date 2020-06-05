#!/usr/bin/env python3

import sys
import rospy

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn 
from pandas.plotting import scatter_matrix

#load the data
ping1d_dist = pd.read_csv('ping1d_dist.csv')

#plot histogram 
ping1d_dist.hist(bins=50, figsize=(20,15))
plt.savefig('ping1d_dist.png')
plt.show()

#set data
X = ping1d_dist[".header.seq"]
y = ping1d_dist[".range"]

#show plot scatter
ping1d_dist.plot(kind='scatter', x= ".header.seq", y='.range')
plt.savefig('ping1d_range.png')
plt.show()

#correlation methons 
#density and include max range vs. range
ping1d_dist.plot(kind='scatter', x= ".header.seq", y='.range', alpha = 0.1, c=".max_range", cmap=plt.get_cmap("jet"), colorbar=True)
plt.savefig('ping1d_max_range.png')
plt.show()

#correlations
corr_matrix=ping1d_dist.corr()
corr_matrix[".range"].sort_values(ascending=False)

#scatter matrix 
attributes = [".range", ".max_range", ".header.seq", ".header.stamp.secs"]
scatter_matrix(ping1d_dist[attributes], figsize=(12,8))
plt.savefig('ping1d_corrs.png')
plt.show()