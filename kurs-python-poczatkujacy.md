# Kurs Python dla początkujących

Ten kurs pokaże Ci podstawy Pythona krok po kroku.

## 1. Co to jest Python?

Python to prosty i czytelny język programowania. Używa się go do tworzenia skryptów, aplikacji i stron internetowych.

## 2. Uruchamianie programu

W naszym projekcie możesz uruchomić program poleceniem:

```bash
python main.py
```

## 3. Podstawowe elementy

### Zmienne i operacje

Zmienne przechowują dane. Możesz wykonywać na nich działania:

```python
wiek = 20
nazwa = "Ala"
print(wiek)
print("Witaj, " + nazwa)

suma = wiek + 5
print("Suma:", suma)
```

Wynik:

```text
20
Witaj, Ala
Suma: 25
```

### Listy

Listy przechowują kilka wartości w jednej zmiennej:

```python
lista = ["jabłko", "banan", "gruszka"]
print(lista)
print(lista[0])
```

Wynik:

```text
['jabłko', 'banan', 'gruszka']
jabłko
```

### Funkcje

Funkcja to blok kodu, który wykonuje zadanie. Możesz przekazywać do niej argumenty:

```python
def przywitaj(imie):
    print(f"Cześć, {imie}!")

przywitaj("Ala")
```

Wynik:

```text
Cześć, Ala!
```

### Instrukcja warunkowa

Możesz podejmować decyzje w kodzie:

```python
x = 5
if x > 3:
    print("x jest większe od 3")
elif x == 3:
    print("x jest równe 3")
else:
    print("x jest mniejsze od 3")
```

Wynik:

```text
x jest większe od 3
```

### Pętle

Pętla powtarza kod wiele razy. Przykład z listą:

```python
for owoc in lista:
    print("Lubię", owoc)
```

Wynik:

```text
Lubię jabłko
Lubię banan
Lubię gruszka
```

### Prosty program: obliczanie sumy

To przykład programu, który używa zmiennych, funkcji i pętli:

```python
def policz_sume(liczby):
    suma = 0
    for liczba in liczby:
        suma += liczba
    return suma

moje_liczby = [1, 2, 3, 4, 5]
print("Suma liczb:", policz_sume(moje_liczby))
```

Wynik:

```text
Suma liczb: 15
```

## 4. Prawdziwy przykład w `main.py`

W pliku `main.py` wykorzystujemy rzeczywisty kod z modułu `examples.py`. Program pokazuje:

- jak wywołać funkcję
- jak obliczyć sumę liczb
- jak przejść przez listę i wydrukować każdy element

Przykładowy kod z `main.py`:

```python
from examples import przywitaj, policz_sume, pokaz_owoce


def main():
    print("Witaj w prostym projekcie Python!")
    przywitaj("Ala")

    moje_liczby = [1, 2, 3, 4, 5]
    print("Suma liczb:", policz_sume(moje_liczby))

    pokaz_owoce(["jabłko", "banan", "gruszka"])


if __name__ == "__main__":
    main()
```

Uruchom ten przykład poleceniem:

```bash
python main.py
```

## 5. Co dalej?

- Spróbuj zmienić tekst w `main.py`
- Dodaj nową zmienną i ją wydrukuj
- Napisz własną funkcję

Powodzenia w nauce Pythona!