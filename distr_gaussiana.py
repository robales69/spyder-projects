#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 21:29:47 2025

@author: robertabalestrino
"""

import numpy as np
import pandas as pd

media = 5.0
std_dev = 0.05

# Generazione
normal_data = np.random.normal(media, std_dev, 1000)

# Analisi con pandas
df_normal = pd.DataFrame(normal_data, columns=["Normal"])
print(df_normal.describe())


print(df_normal)
isto = df_normal.plot(kind='hist', bins=30, title="Distribuzione Gaussiana", legend=False)
isto.set_xlim(4, 6)

















