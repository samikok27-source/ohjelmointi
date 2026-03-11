import lab5_b as lb

def main() :
    '''
    ohjelman pääfunktio, joka kutsuu toisia funktioita
    lab5_b moduulista.
    '''

    # kysyy käyttäjältä tiedoston ja luo kortit
    kortit = lb.luo_kortti()

    # tulostaa kortit
    print('Aktiviteetit')
    lb.nayta_kortit(kortit)

    # rakentaa kaikki riippuvuudet ja polut
    polut = lb.rakenna_riippuvuudet(kortit)

    # tulostaa polut (avaimet, nimet ja kestot)
    print('Polut ja kestot')
    lb.nayta_polut(polut)


if __name__ == '__main__' :
    '''
    jos käynnistetään moduuli suoritettavana ohjelmana
    '''
    main()