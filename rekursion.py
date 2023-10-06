"""
Ett exempel på när rekursion är trevligt.

Vi vill skriva ett program som beräknar siffersumman för
ett tal som användaren matar in.
"""

import exceptions

def beräkna_siffersumma(tal):
    """
    Tar ett tal och returnerar dess siffersumma.

    Siffersumman för 123 är 1+2+3.
    """
    if tal <= 0:
        return 0
    sista_siffran = tal % 10 # 3:an
    första_siffrorna = tal // 10 # 12
    siffersumman = sista_siffran + beräkna_siffersumma(första_siffrorna)
    return siffersumman

def main():
    """
    Huvudprogrammet
    """
    tal = exceptions.input_int("Ange ett heltal för att beräkna siffersumman: ")
    siffersumma = beräkna_siffersumma(tal)
    print(f"Siffersumman för {tal} är {siffersumma}.")

main()