"""Przykładowy moduł Python dla kursu początkującego."""


def przywitaj(imie):
    """Wypisuje powitanie dla podanego imienia."""
    print(f"Cześć, {imie}! Witaj w Pythonie.")


def policz_sume(liczby):
    """Zwraca sumę liczb w liście."""
    suma = 0
    for liczba in liczby:
        suma += liczba
    return suma


def pokaz_owoce(owoce):
    """Wypisuje elementy listy owoców."""
    print("Lista owoców:")
    for owoc in owoce:
        print("-", owoc)


def main():
    przywitaj("Ala")
    moje_liczby = [1, 2, 3, 4, 5]
    print("Suma liczb:", policz_sume(moje_liczby))
    pokaz_owoce(["jabłko", "banan", "gruszka", "pomarańcza"])


if __name__ == "__main__":
    main()
