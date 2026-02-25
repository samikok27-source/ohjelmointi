import random
import matplotlib.pyplot as plt

A = float(input("Anna saapumistodennäköisyys (0-1): "))
B = float(input("Anna palvelun valmistumistodennäköisyys (0-1): "))
kierrokset = int(input("Anna kierrosten määrä: "))

s1 = 0
s2 = 0
s3 = 0

for k in range(100):

    jono = 0
    max_jono = 0
    tyhja = 0
    max_tyhja = 0
    asiakkaita = 0

    for i in range(kierrokset):

        if random.random() < A:
            jono += 1
            asiakkaita += 1
            if jono > max_jono:
                max_jono = jono

        if jono > 0:
            if random.random() < B:
                jono -= 1
        else:
            tyhja += 1
            if tyhja > max_tyhja:
                max_tyhja = tyhja

    s1 += asiakkaita
    s2 += max_jono
    s3 += max_tyhja

plt.bar(["Asiakkaat", "Max jono", "Max tyhjä"],
        [s1/100, s2/100, s3/100],
        color="blue")

plt.show()