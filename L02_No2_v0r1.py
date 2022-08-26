# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 01:38:25 2021

@author: pmarc

Résolution Problème L02 - #1 par Pierre-Marc Juneau, 14 mars 2021
"""

import numpy as np
import pandas as pd
from numpy import nan


donnee = pd.read_csv('DonneesVachesLait.csv', index_col='Dates')
stats=donnee.describe()
dimensions=donnee.shape



"Question 1"
X1=donnee.fillna(donnee.mean())

"Question 2"

dimensions=donnee.shape
NR=dimensions[0]
Nnan=donnee.isnull().sum()
DegCompletude=(NR-Nnan)/NR


X2 = donnee.drop('Eau', 1)


donnee_val=donnee.values
Somme_théo=pd.DataFrame(donnee_val[:,0]+donnee_val[:,1]+donnee_val[:,2]+donnee_val[:,3]+donnee_val[:,4])



Somme_théo.columns=['Somme théorique']
Somme_théo.index=donnee.index


X3 = X2[(Somme_théo["Somme théorique"] < 100.01) & (Somme_théo["Somme théorique"] > 99.99)]

