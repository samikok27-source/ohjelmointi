"""
AI-työkalun nimi: Microsoft Copilot

Käytetty kehote:
"Tee Python-ohjelma antamani koodin mukaan, joka hakee aineistosta parempaa
korrelaatiota tyytyväisyyden ja jonkun muun sarakkeen kesken kuin minun valintani.
Tee koodi mahdollisimman hyvin
"""

import matplotlib.pyplot as plt
import pandas as pd

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

# Piirretään scatter-kuva parhaasta korrelaatiosta
plt.scatter(df2[paras_muuttuja], df2['tyytyväisyys'])
plt.xlabel(paras_muuttuja)
plt.ylabel('tyytyväisyys')
plt.title(f'{paras_muuttuja} vs tyytyväisyys (paras korrelaatio)')
plt.show()
