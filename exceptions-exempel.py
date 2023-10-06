"""
Ett exempelprogram om exceptions

Vi vill skriva ett gissningsspel. Användaren ska
gissa tal som vi tänker på.

Om användaren skriver in något annat än ett tal
då får hen försöka igen.
"""

def main():
    """Huvudprogrammet"""
    talet = 5
    try:
        gissning = int(input("Gissa vilket tal vi tänker på: "))
    except ValueError:
        print("Det var fel typ, det måste vara ett heltal.")
        return

    if talet == gissning:
        print("Grattis, det var rätt gissat!")
    else:
        print("Tyvärr, det var fel!")

main()