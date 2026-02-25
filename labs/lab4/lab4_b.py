import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('https://taanila.fi/data1.xlsx')
df2 = df[['sukup', 'palveluv', 'palkkat', 'johto', 'työymp', 'perhe']]
df2['tyytyväisyys'] = df2[['johto', 'palkkat']].mean(axis=1)
print(df2.corr())

plt.scatter(df2['johto'], df2['tyytyväisyys'])
plt.xlabel('johto')
plt.ylabel('Tyytyvaisyys')
plt.title('johto vs Tyytyvaisyys')
plt.show()

plt.scatter(df2['palveluv'], df2['tyytyväisyys'])
plt.xlabel('palveluv')
plt.ylabel('Tyytyvaisyys')
plt.title('palveluv vs Tyytyvaisyys')
plt.show()

plt.scatter(df2['työymp'], df2['tyytyväisyys'])
plt.xlabel('työymp')
plt.ylabel('Tyytyvaisyys')
plt.title('työymp vs Tyytyvaisyys')
plt.show()

plt.scatter(df2['palkkat'], df2['tyytyväisyys'])
plt.xlabel('palkkat')
plt.ylabel('Tyytyvaisyys')
plt.title('pakkat vs Tyytyvaisyys')
plt.show()