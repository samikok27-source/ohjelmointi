"""
===========================================================
PROMPT (käyttäjän antama):

Kassa toimintaa kuvaavassa skriptissä jokainen kierros vastaa yhtä simuloitua minuuttia. 
Aluksi asiakas tulee kassalle todennäköisyydellä A esim. 20% (yksi viidestä), lisätään kassajonoon, 
jos jono on pidempi kuin aiempi maksimi jono, päivitetään maksimi jono, palvellaan jonon ensimmäistä asiakasta, 
jonka palvelu todennäköisyydellä B esim. 33% (yksi kolmesta) tulee valmiiksi ja hän poistuu kassajonosta. 
Jos palveltavia asiakkaita ei ole päivitetään kassan tyhjäaikaa ja tarvittaessa tyhjäajan maksimia. 
Ohjelmassa kysytään ennen simulaatioiden aloittamista todennäköisyys A asiakkaan saapumiselle ja 
todennäköisyys B asiakkaan palvelun valmistumiselle, jotka sijoitetaan yksittäisen kassan toimintaa simuloivaan silmukkaan. 
Kustakin simulointikierroksesta tehdään pylväskaavio asiakkaiden kokonaismääristä, maksimi jonosta ja maksimi tyhjäkäyntiajasta. 
Kaavio näytetään koko simulaation lopuksi. Tee scripti ilman mitään rajoituksia, ja laita scriptin alkuun osio, 
jossa näkyy antamani prompti, ja että scripti on tehty CHATGPT tekoälyn avulla.
===========================================================
"""

import random
import numpy as np
import matplotlib.pyplot as plt

# ================== SIMULAATIOPARAMETRIT ==================

SIMULATION_RUNS = 15      # Montako simulaatiota
MINUTES_PER_RUN = 1000    # Minuutit per simulaatio

# ================== SYÖTE ==================

A = float(input("Anna asiakkaan saapumistodennäköisyys A (esim 0.2): "))
B = float(input("Anna palvelun valmistumistodennäköisyys B (esim 0.33): "))

# ================== TULOSTEN TALLENNUS ==================

total_customers_list = []
max_queue_list = []
max_idle_list = []

# ================== SIMULAATIO ==================

for run in range(SIMULATION_RUNS):
    queue = []
    total_customers = 0
    max_queue = 0
    idle_time = 0
    max_idle_time = 0

    for minute in range(MINUTES_PER_RUN):

        # Asiakas saapuu
        if random.random() < A:
            queue.append(1)
            total_customers += 1

        # Päivitä maksimi jono
        if len(queue) > max_queue:
            max_queue = len(queue)

        # Palvelu tai tyhjäkäynti
        if queue:
            if random.random() < B:
                queue.pop(0)
            idle_time = 0
        else:
            idle_time += 1
            if idle_time > max_idle_time:
                max_idle_time = idle_time

    total_customers_list.append(total_customers)
    max_queue_list.append(max_queue)
    max_idle_list.append(max_idle_time)

# ================== AMMATTIMAINEN VISUALISOINTI ==================

# Tyyli tieteelliseen data science -grafiikkaan
plt.style.use("seaborn-v0_8-whitegrid")

# Typografia
plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 12,
    "axes.titlesize": 16,
    "axes.labelsize": 14,
    "figure.titlesize": 20
})

runs = np.arange(1, SIMULATION_RUNS + 1)

# Corporate-väripaletti
colors = ["#1f77b4", "#2ca02c", "#d62728"]

fig, axes = plt.subplots(3, 1, figsize=(15, 11), sharex=True)

# Asiakkaiden määrä
axes[0].bar(runs, total_customers_list, color=colors[0])
axes[0].set_title("Total Customers per Simulation Run")
axes[0].set_ylabel("Customers")

# Maksimi jono
axes[1].bar(runs, max_queue_list, color=colors[1])
axes[1].set_title("Maximum Queue Length per Simulation Run")
axes[1].set_ylabel("Queue length")

# Maksimi tyhjäkäynti
axes[2].bar(runs, max_idle_list, color=colors[2])
axes[2].set_title("Maximum Idle Time per Simulation Run")
axes[2].set_ylabel("Minutes")
axes[2].set_xlabel("Simulation run")

# Yleinen otsikko
fig.suptitle("Checkout Queue Monte Carlo Simulation Results", fontweight="bold")

# Layout
plt.tight_layout(rect=[0, 0, 1, 0.96])

# Tallennus julkaisutason resoluutiolla
plt.savefig("checkout_simulation_results.png", dpi=300)

plt.show()