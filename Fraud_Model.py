# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 07:58:49 2022

@author: hambert.cuba
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset_original=pd.read_csv("C:\\Users\\hambert.cuba\\Desktop\\MASTER - PROYECTO\\Dataset_Outpatient_completo.csv",sep=";")

var_x=dataset_original.iloc[:,:-1].values # donde inicia y termina filas(:) , inicia y termina columnas (:) --> -1 penultima columna
var_y=dataset_original.iloc[:,-1].values # variable dependiente


