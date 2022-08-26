#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 19:39:43 2021

@author: pablo
"""


import numpy as np
import pandas as pd
from numpy import nan

donne = pd.read_csv('DonneesVachesLait.csv', index_col='Dates')
stats = donnee.describe()
dimension=donnee.shape

#Question 1
X1 = donnee.fillna(donnne.mean())


#question 2

dimensions = donnee.shape
NR=dimensions[0]
Nnan=donnee.isnull().sum()
DegCompletude=(NR-Nnan)/NR

X2 = donnee.drop('Eau',1)

donnee_val = donnee.values

