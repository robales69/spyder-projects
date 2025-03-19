#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 12 

@author: robertabalestrino

Esempio di lettura di dati da file .txt

Visualizzazione dei dati con la libreria Pandas
"""

import pandas as pd

# Specifica le intestazioni e leggi il file di testo
intestazioni = ['Pendolo 1', 'Pendolo 2', 'Pendolo 3','Pendolo 4']
df = pd.read_csv('dati_pendolo.txt', sep=',', header = 0, names=intestazioni)  


# Definisci le opzioni di visualizzazione
pd.set_option('display.max_rows', None)         # Mostra tutte le righe
pd.set_option('display.max_columns', None)      # Mostra tutte le colonne
pd.set_option('display.width', None)            # Adatta la larghezza alla console
pd.set_option('display.colheader_justify', 'left')  # Allinea le intestazioni a sinistra

# Visualizza il dataframe
print(df)


