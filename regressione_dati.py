#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 22:17:53 2025

@author: robertabalestrino
"""

import numpy as np
import pandas as pd

# Lettura del file CSV
df = pd.read_csv("dati_caduta.csv", sep="\s+")

print(df)


# Estrazione dei dati
x = df["x"].values
y = df["y"].values

# Calcolo della regressione quadratica
coeffs = np.polyfit(x, y, 2)  # grado 2 => ax^2 + bx + c
a, b, c = coeffs
print(f"Coefficienti della parabola: a={a:.2f}, b={b:.2f}, c={c:.2f}")

# Calcolo dei valori previsti dalla regressione
df["y_fit"] = np.polyval(coeffs, x)

# Calcolo dell'errore quadratico medio (facoltativo)
rmse = np.sqrt(np.mean((df["y"] - df["y_fit"]) ** 2))
print(f"Errore quadratico medio (RMSE): {rmse:.2f}")

# Grafico dei dati sperimentali e della curva di regressione
ax = df.plot(x="x", y="y", kind="scatter", label="Dati sperimentali", title="Regressione quadratica",s=10)
df.plot(x="x", y="y_fit", kind="line", color="red", label="Regressione quadratica", ax=ax)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.grid(True)
