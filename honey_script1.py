#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 18:41:23 2021

@author: ericaschultz
"""

#DATA SOURCE: https://usda.library.cornell.edu/concern/publications/hd76s004z?locale=en#release-items


#Import packages
#############################################################################
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#Read in data and some cleaning
#############################################################################
path = '../../DATA/honey/fixed tables/honey20'
file_names = list(range(10, 21))
file_names = [path + str(x) + '.csv' for x in file_names]


for i in range(len(file_names)):
    if i == 0:
        honey_df = pd.read_csv(file_names[i])
    else:
        temp_df = pd.read_csv(file_names[i])
        honey_df = pd.concat([honey_df, temp_df], ignore_index=True)
    
honey_df.dropna(inplace = True)
honey_df.reset_index(drop = True, inplace = True)

honey_df.loc[(honey_df.state == 'Other States 5/ 6/'), 'state'] = 'Other States'
honey_df.loc[(honey_df.state == 'United States 6/ 7/'), 'state'] = 'United States'

print(honey_df.info())

#honey_df.to_excel("honey.xlsx")

desc_honey = honey_df.describe()

#Exlporatory Data Analysis
#############################################################################
# _ = plt.bar('state', 'production', data = honey_df.loc[honey_df.year == 2020])
# _ = plt.xlabel('state')
# _ = plt.xticks(rotation = 90)
# _ = plt.ylabel('production (in 1000 pounds)')
# plt.show()


#QUESTIONS TO ANSWER:
    # What are the 5 most productive states?
    # What is production over time in each of the most productive states
    # How is price related to production?
    # How do stocks change over time (any relation to price?)
    