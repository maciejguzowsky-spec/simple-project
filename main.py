"""Prosty program Python.

Uruchomienie:
    python main.py
"""

from examples import przywitaj, policz_sume, pokaz_owoce


def main():
    print("Witaj w prostym projekcie Python!")
    przywitaj("Ala")

    moje_liczby = [1, 2, 3, 4, 5]
    print("Suma liczb:", policz_sume(moje_liczby))

    pokaz_owoce(["jabłko", "banan", "gruszka", "pomarańcza"])


if __name__ == "__main__":
    main()
