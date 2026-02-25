"""
AI-työkalun nimi: Microsoft Copilot

Käytetty kehote:
"Tee Python-ohjelma antamani koodin mukaan, joka hakee aineistosta parempaa
korrelaatiota tyytyväisyyden ja jonkun muun sarakkeen kesken kuin oma valintasi.
Tee koodista mahdollisimman hyvä ja kaaviosta mahdollisimman hieno"
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Ladataan aineisto
df = pd.read_excel('https://taanila.fi/data1.xlsx')

# Valitaan sarakkeet
df2 = df[['sukup', 'palveluv', 'palkkat', 'johto', 'työymp', 'perhe']]

# Luodaan tyytyväisyysmuuttuja
df2['tyytyväisyys'] = df2[['johto', 'palkkat']].mean(axis=1)

# Lasketaan korrelaatiot
corr = df2.corr()['tyytyväisyys'].drop('tyytyväisyys')

print("Korrelaatiot tyytyväisyyteen:")
print(corr)

# Etsitään paras korrelaatio
paras_muuttuja = corr.abs().idxmax()
paras_arvo = corr[paras_muuttuja]

print(f"\nParas korrelaatio löytyi muuttujalle: {paras_muuttuja}")
print(f"Korrelaation arvo: {paras_arvo:.3f}")

# Piirretään tyylikäs scatter-kuva matplotlibilla
x = df2[paras_muuttuja]
y = df2['tyytyväisyys']

plt.figure(figsize=(8, 6))

# Scatter-pisteet
plt.scatter(x, y, s=70, alpha=0.7, edgecolor='black', linewidth=0.7)

# Trendiviiva (matplotlib + numpy)
m, b = np.polyfit(x, y, 1)
plt.plot(x, m*x + b, color='red', linewidth=2)

# Akselien ja otsikon muotoilu
plt.xlabel(paras_muuttuja, fontsize=12)
plt.ylabel('Tyytyväisyys', fontsize=12)
plt.title(f'Paras korrelaatio: {paras_muuttuja} vs Tyytyväisyys\n(r = {paras_arvo:.3f})',
          fontsize=14, fontweight='bold')

# Hieno ruudukko
plt.grid(True, linestyle='--', alpha=0.3)

plt.tight_layout()
plt.show()
