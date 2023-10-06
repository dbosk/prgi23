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
    while True:
        try:
            gissning = int(input("Gissa vilket tal vi tänker på: "))
            break
        except ValueError:
            print("Det var fel, det måste vara ett heltal.")

    if talet == gissning:
        print("Grattis, det var rätt gissat!")
    else:
        print("Tyvärr, det var fel!")

try:
    main()
except:
    print("Det har uppstått ett okänt fel.")