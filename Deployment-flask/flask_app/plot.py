# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 22:07:32 2020

@author: Abhishek
"""

import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import matplotlib.pyplot as plt
import pandas
import squarify
import missingno as msno
import seaborn as sns



air_data =pandas.read_csv('cond.csv',encoding='latin1')
air_data.spm = air_data['spm'].fillna(air_data['spm'].mean())
air_data.rspm = air_data['rspm'].fillna(air_data['rspm'].mean())
air_data.so2 = air_data['so2'].fillna(air_data['so2'].mean())
air_data.no2 = air_data['no2'].fillna(air_data['no2'].mean())

so2_level  = air_data.groupby(['state']).mean()['so2'].sort_values(ascending = False).to_frame()
sns_plot=sns.barplot(x = 'so2', y = so2_level.index,data = so2_level,palette='inferno')
fig = sns_plot.get_figure()
fig.savefig("static/images/new_plot.png")