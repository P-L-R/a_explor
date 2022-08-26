# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 01:38:25 2021

@author: pmarc

Résolution Problème L02 - #1 par Pierre-Marc Juneau, 14 mars 2021
"""

import numpy as np
import pandas as pd
from numpy import nan


donnee = pd.read_csv('DonneesVachesLait.csv')
stats=donnee.describe()
dimensions=donnee.shape


"Calcul du degré de complétude pour chaque variable"
NR=dimensions[0]
print(NR)
Nnan=donnee.isnull().sum()
DegCompletude=(NR-Nnan)/NR


"Calcul du degré de validité en fonction des règles"
NNV=sum(i > 40 for i in donnee["Production lait par vache (L/j)"])
Q1=(NR-NNV)/NR

NNV2=sum(i > 50 for i in donnee["Température étable (0C)"])
Q2=(NR-NNV2)/NR

DegValidite=(Q1+Q2)/2

"Calcul du degré de cohérence pour les %"

donnee_val=donnee.values

Somme_théo=donnee_val[:,1]+donnee_val[:,2]+donnee_val[:,3]+donnee_val[:,4]+donnee_val[:,5]

Somme_théo2=donnee_val[:,1:6]

NNC=sum(i > 100.01 for i in Somme_théo)+sum(i < 99.99 for i in Somme_théo)

DegCoherence=(NR-NNC)/NR


