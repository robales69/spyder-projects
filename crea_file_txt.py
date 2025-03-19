#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 12 

@author: robertabalestrino

Esempio di creazione di file di testo con valori sperimentali
I dati rappresentano i periodi di oscillazione di un pendolo
"""

import numpy as np

# Crea gli array

Ta   = np.array([1.79,1.84,1.84,1.88,1.77,1.92,1.70,1.90,1.79,1.81,1.85,1.87,1.80,1.73,1.85,1.76,1.94,1.73,1.91,1.81,1.77,1.76,1.98,1.81,1.82,1.87,1.79,1.94,1.75,1.83])
Tb   = np.array([1.59,1.64,1.64,1.68,1.57,1.72,1.5,1.7,1.59,1.61,1.65,1.67,1.6,1.53,1.65,1.56,1.74,1.53,1.71,1.61,1.57,1.56,1.78,1.61,1.62,1.67,1.59,1.74,1.55,1.63])
Tc   = np.array([1.34,1.39,1.39,1.43,1.32,1.47,1.25,1.45,1.34,1.36,1.4,1.42,1.35,1.28,1.4,1.31,1.49,1.28,1.46,1.36,1.32,1.31,1.53,1.36,1.37,1.42,1.34,1.49,1.3,1.38])
Td   = np.array([1.18,1.23,1.23,1.27,1.16,1.31,1.09,1.29,1.18,1.2,1.24,1.26,1.19,1.12,1.24,1.15,1.33,1.12,1.3,1.2,1.16,1.15,1.37,1.2,1.21,1.26,1.18,1.33,1.14,1.22])

# Combina gli array in una matrice (se possibile)
try:
    matrice = np.vstack((Ta,Tb,Tc,Td)) 
except ValueError:
    print("Gli array non hanno la stessa lunghezza, non è possibile combinarli in una matrice.")

# Scrivi i dati nel file
with open('dati_pendolo.txt', 'w') as f:
    # Intestazione (opzionale)
    f.write('Pendolo1,Pendolo2,Pendolo3,Pendolo4\n')
    # Dati
    for i in range(len(Ta)):
        f.write(f'{Ta[i]},{Tb[i]},{Tc[i]},{Td[i]}\n')

print("File 'dati_pendolo.txt' creato con successo.")

f.close()
