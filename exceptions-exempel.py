"""
Ett exempelprogram om exceptions

Vi vill skriva ett gissningsspel. Användaren ska
gissa tal som vi tänker på.

Om användaren skriver in något annat än ett tal
då får hen försöka igen.
"""

def input_int(prompt=""):
    """
    Skriver ut prompt och låter användaren mata in en int.
    Repeterar så länge användaren inte matar in något av
    korrekt typ.

    Returvärdet är garanterat av typen int.
    """
    try:
        inmatning = int(input(prompt))
        return inmatning
    except ValueError as err:
        print(f"Det var fel, det måste vara ett heltal: {err}")
        return input_int(prompt)


def main():
    """Huvudprogrammet"""
    talet = input_int("Skriv in vilket tal vi ska tänka på: ")
    gissning = input_int("Gissa vilket tal vi tänker på: ")

    if talet == gissning:
        print("Grattis, det var rätt gissat!")
    else:
        print("Tyvärr, det var fel!")

main()