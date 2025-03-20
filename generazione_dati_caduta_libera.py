#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 

@author: robertabalestrino
"""

import numpy as np
import pandas as pd


N = 100
h = 20     # altezza di partenza in metri
g = 9.81   # accelerazione gravità terrestre
std_dev = 0.8     # deviazione standard per le altezze simulate

# Generazione il tempo di caduta
max_time = np.sqrt(2*h/g)                           # legge fisica
max_time_rnd = np.random.normal(max_time, 0.01)

times = np.linspace(0, max_time_rnd, N)
times= np.round(times, 3)

# Generazione altezze in cui si trova il corpo che cade
theor_heights = np.round(h-1/2*g*times**2, 3)
experim_heights = np.random.normal(theor_heights, std_dev, N)
experim_heights = np.round(experim_heights, 3)


matrix = np.array([times,theor_heights,experim_heights])

df = pd.DataFrame({'Tempo (s)': times, 'Altezza teorica y(m)': theor_heights, 'Altezza sperimentale y(m)':experim_heights})

# Definisci le opzioni di visualizzazione
pd.set_option('display.max_rows', None)         # Mostra tutte le righe
pd.set_option('display.max_columns', None)      # Mostra tutte le colonne
pd.set_option('display.width', None)            # Adatta la larghezza alla console
pd.set_option('display.colheader_justify', 'left')  # Allinea le intestazioni a sinistra

# Visualizza il dataframe come tabella
print(df)


#Visualizzare i dati in un file a dispersione
df.plot(kind='scatter', x='Tempo (s)', y='Altezza sperimentale y(m)')


# Esporto i dati simulati su file CSV

dfexp = pd.DataFrame({'x': times, 'y':experim_heights})
dfexp.to_csv('C:\\Users\\Docente\\Desktop\\dati_cadutalibera.csv', index = False, sep = " ", header = True)

print("FIle creato con successo")





