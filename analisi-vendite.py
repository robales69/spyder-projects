#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 18:29:18 2025

@author: robertabalestrino
"""

import matplotlib.pyplot as plt

# Dati
mesi = ['Gen', 'Feb', 'Mar', 'Apr', 'Mag', 'Giu', 'Lug', 'Ago', 'Set', 'Ott', 'Nov', 'Dic']
prodotto_a = [150, 180, 200, 220, 250, 280, 300, 320, 350, 380, 400, 420]
prodotto_b = [200, 220, 250, 280, 300, 320, 350, 380, 400, 420, 450, 480]
prodotto_c = [120, 130, 150, 160, 180, 200, 220, 240, 260, 280, 300, 320]

# Crea il grafico
plt.plot(mesi, prodotto_a, label='Prodotto A', color='blue')
plt.plot(mesi, prodotto_b, label='Prodotto B', color='red')
plt.plot(mesi, prodotto_c, label='Prodotto C', color='green')

# Aggiungi titolo ed etichette agli assi
plt.title('Andamento delle vendite dei prodotti nel tempo')
plt.xlabel('Mese')
plt.ylabel('Unità vendute')

# Aggiungi la legenda
plt.legend()

# Mostra il grafico
plt.show()