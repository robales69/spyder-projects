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

# Regressione lineare: y = mx + q
coeffs = np.polyfit(x, y, 1)  # grado 1 => mx + q
m, q = coeffs
print(f"Retta: y = {m:.2f}x + {q:.2f}")

# Calcolo dei valori previsti dalla regressione
df["y_fit"] = np.polyval(coeffs, x)


# Grafico dei dati sperimentali e della curva di regressione
ax = df.plot(kind="scatter", x="x", y="y", label="Dati sperimentali", s=10)
df.plot(x="x", y="y_fit", kind="line", color="red", label="Regressione lineare", ax=ax)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.grid(True)