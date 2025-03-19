#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 21:54:14 2025

@author: robertabalestrino
"""

import numpy as np
import pandas as pd


# Generazione dati secondo distribuzione binomiale
binomial_data = np.random.binomial(n=10, p=0.5, size=1000)

df_binomial = pd.DataFrame(binomial_data, columns=["Binomial"])
print(df_binomial["Binomial"].value_counts().sort_index())
df_binomial.plot(kind='hist', bins=30, title="Distribuzione binomiale", legend=False)


# Generazione dati secondo distribuzione poissoniana
poisson_data = np.random.poisson(lam=3, size=1000)

df_poisson = pd.DataFrame(poisson_data, columns=["Poisson"])
print(df_poisson["Poisson"].value_counts().sort_index())
df_poisson.plot(kind='hist', bins=30, title="Distribuzione poissoniana", legend=False)


# Generazione dati secondo distribuzione esponenziale
exponential_data = np.random.exponential(scale=1, size=1000)

df_exponential = pd.DataFrame(exponential_data, columns=["Exponential"])
print(df_exponential.describe())
df_exponential.plot(kind='hist', bins=30, title="Distribuzione esponenziale", legend=False)




