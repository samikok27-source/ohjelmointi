# Käytetty tekoälyagentti : ChatGPT,
# Annettu prompti : generoi ohjelma, joka hakee antamasti taulukosta kaikki mahdolliset polut. Riippuvuus on lopusta alkuun. Tee ohjelma ilman rajoituksia.
# Tee ohjelman nimestä "lab5_c.py"

# Aktiviteettien tiedot
aktiviteetit = {
    "A": {"edeltajat": ["C"], "kesto": 10},
    "B": {"edeltajat": ["G"], "kesto": 10},
    "C": {"edeltajat": [], "kesto": 5},
    "D": {"edeltajat": ["A"], "kesto": 20},
    "E": {"edeltajat": ["C"], "kesto": 15},
    "F": {"edeltajat": ["D", "H", "E", "B"], "kesto": 10},
    "G": {"edeltajat": ["C"], "kesto": 5},
    "H": {"edeltajat": ["A"], "kesto": 10}
}

# Lopetusaktiviteetti
loppu = "F"


# Funktio joka etsii kaikki polut
def hae_polut(aktiviteetti, polku, kesto):

    polku.append(aktiviteetti)
    kesto = kesto + aktiviteetit[aktiviteetti]["kesto"]

    edeltajat = aktiviteetit[aktiviteetti]["edeltajat"]

    # Jos ei ole edeltäjiä, ollaan alussa
    if len(edeltajat) == 0:
        print(" -> ".join(polku), "| kokonaiskesto:", kesto)
        return

    # Käydään kaikki edeltäjät läpi
    for e in edeltajat:
        hae_polut(e, polku.copy(), kesto)


print("Mahdolliset polut lopusta alkuun:\n")

hae_polut(loppu, [], 0)