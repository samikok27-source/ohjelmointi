def luo_kortti():
    kortit = []
    while True:
        nimi = input("Aktiviteetin nimi (enter lopettaa): ").upper()
        if nimi == "":
            break
        edeltajat = input("Edeltajat pilkulla (enter jos ei ole): ").upper()
        if edeltajat == "":
            ed_lista = []
        else:
            ed_lista = [e.strip() for e in edeltajat.split(",")]
        while True:
            try:
                kesto = float(input("Kesto tunneissa: "))
                break
            except:
                print("Anna numero!")
        kortit.append({"nimi": nimi, "edeltajat": ed_lista, "kesto": kesto})
    return kortit
def nayta_kortit(kortit):
    print("Nimi  Edeltajat  Kesto")
    for k in kortit:
        ed = ", ".join(k["edeltajat"]) if k["edeltajat"] else "-"
        print(k["nimi"], ed, k["kesto"])
def rakenna_riippuvuudet(kortit):
    kd = {k["nimi"]: k for k in kortit}
    kaikki_ed = [e for k in kortit for e in k["edeltajat"]]
    loppusolmut = [k["nimi"] for k in kortit if k["nimi"] not in kaikki_ed]
    polut = []
    def etsi(nimi, polku):
        k = kd[nimi]
        uusi = [{"nimi": nimi, "kesto": k["kesto"]}] + polku
        if not k["edeltajat"]:
            polut.append(uusi)
        else:
            for e in k["edeltajat"]:
                if e in kd:
                    etsi(e, uusi)

    for loppu in loppusolmut:
        etsi(loppu, [])
    return polut
def nayta_polut(polut):
    if not polut:
        print("Ei polkuja")
        return
    kestot = [sum(a["kesto"] for a in p) for p in polut]
    pisin = max(kestot)
    print("Polut:")
    for i, (p, k) in enumerate(zip(polut, kestot)):
        reitti = " -> ".join(a["nimi"] for a in p)
        merkki = " <-- kriittinen" if k == pisin else ""
        print(str(i+1) + ". " + reitti + "  " + str(k) + "h" + merkki)