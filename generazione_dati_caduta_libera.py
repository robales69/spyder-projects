#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 

@author: robertabalestrino
"""


import numpy as np
import pandas as pd
   
N = 100  # Numero di dati
h = 20  # Altezza di partenza in metri

std_dev_time = 0.2

max_time =np.sqrt(2 * h / 9.81)
max_time_rnd = np.random.normal(max_time, std_dev_time)  # Tempo massimo per cadere da h


times = np.linspace(0, max_time_rnd, N)  # Tempi da 0 a max_time
times = np.round(times,3)   

theorical_heights = np.round(h - 0.5 * 9.81 * times**2,3)
experimental_heights = np.random.normal(theorical_heights, std_dev_time, N)
experimental_heights = np.round(experimental_heights,3)

if experimental_heights[0] != 0:
    experimental_heights[0] = h

if experimental_heights[99] != 0:
    experimental_heights[99] = 0


matrix = np.array([times, theorical_heights, experimental_heights])

df = pd.DataFrame({'Tempo (s)': times, 'Altezza t(m)': theorical_heights, 'Altezza s(m)': experimental_heights})

# Definisci le opzioni di visualizzazione
pd.set_option('display.max_rows', None)         # Mostra tutte le righe
pd.set_option('display.max_columns', None)      # Mostra tutte le colonne
pd.set_option('display.width', None)            # Adatta la larghezza alla console
pd.set_option('display.colheader_justify', 'left')  # Allinea le intestazioni a sinistra

# Visualizza il dataframe
print(df)


# esporta i dati in un file csv
dfexp = pd.DataFrame({'x': times, 'y':experimental_heights})
dfexp.to_csv('dati_caduta.csv', index = False, sep=" ", header=True) 


print("File 'dati_caduta.csv' creato con successo.")






