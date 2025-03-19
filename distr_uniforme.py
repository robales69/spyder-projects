#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 21:29:47 2025

@author: robertabalestrino
"""

import numpy as np
import pandas as pd

# Generazione
uniform_data = np.random.uniform(low=0, high=10, size=100)

# Analisi con pandas
df_uniform = pd.DataFrame(uniform_data, columns=["Uniform"])
print(df_uniform.describe())

print(df_uniform)
df_uniform.plot(kind='hist', bins=30, title="Distribuzione Uniforme", legend=False)







