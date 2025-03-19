#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 12 

@author: robertabalestrino
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Visualizzazione dei dati con Pandas

# Specifica le intestazioni e  le intestazioni
intestazioni = ['Pendolo 1', 'Pendolo 2', 'Pendolo 3','Pendolo 4']
df = pd.read_csv('dati_pendolo.txt', sep=',', header = 0, names=intestazioni)  # Usa sep=' ' per spazi

pd.set_option('display.max_rows', None)         # Mostra tutte le righe
pd.set_option('display.max_columns', None)      # Mostra tutte le colonne
pd.set_option('display.width', None)            # Adatta la larghezza alla console
pd.set_option('display.colheader_justify', 'left')  # Allinea le intestazioni a sinistra

# Visualizza il dataframe in una tabella
print(df)

# Elaborazione dei dati con Numpy

# Valori di lunghezza dei pendoli
valori_L = [83.2,56.1,34.2,23.2]

# Lettura degli array dal file .txt
# Numpy crea una matrice con i singoli vettori 
dati = np.loadtxt('dati_pendolo.txt', delimiter=',', skiprows=1)

# Calcolo delle medie dei valori e inserimento in vettore
                                #dati[:1] contiene tutti i dati del vettore i
periodo=[0,0,0,0]
for i in range(0,4):
    periodo[i]=np.mean(dati[:,i])
    print(f'Periodo medio del pendolo {i+1}',"%.2f" % periodo[i])


# Grafico a dispersione con i valori dei due vettori, contenente le lunghezze e i periodi misurati
plt.scatter(valori_L, periodo)
plt.xlabel('Lunghezza (cm)')
plt.ylabel('Periodo (s)')
plt.title('Periodo di oscillazione del pendolo')

plt.grid(True)
plt.show()


