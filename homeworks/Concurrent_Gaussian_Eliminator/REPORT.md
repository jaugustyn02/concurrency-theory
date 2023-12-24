# Teoria Współbieżności
## Zadanie Domowe 3
### Autor: Jan Augustyn

## Opis programu
### Program podzielony jest na 3 główne części:
1. **DependencyAnalysisTool** - Własna biblioteka oparta na zadaniu domowym 2, która dla danego alfabetu, słowa oraz transakcji tworzy graf zależności i zwraca ciąg symboli w postaci normalnej Foaty.
2. **GaussianEliminationDependencyAnalysisTool** - Klasa, która dla danego rozmiaru macierzy generuje alpabet, słowa oraz transakcje, a następnie wykorzystuje bibliotekę z punktu 1. do wygenerowania grafu zależności i zwraca ciąg symboli opisujących algorytm współbieżnej eliminacji Gaussa w postaci normalnej Foaty.
3. **ConcurrentGaussianEliminator** - Klasa, która przyjmuje jako argument macierz wejściową. Wykorzystuje bibliotekę z punktu 2. do wygenerowania opisu algorytmu w postaci normalnej Foaty. Następnie na jego podstawie wykonuje współbieżną eliminację Gaussa (doprowadza macierz do postaci schodkowej). W ostatnim kroku dokonuje redukcji macierzy do postaci diagonalnej i zwraca wynik.

### Funkcjonalność programu
- Program działa dla dowolnego rozmiaru macierzy wejściowej.
- Program pozwala na zapisywanie oraz wyświetlanie grafu zależności.
- Program pozwala na zapisywanie oraz wyświetlanie ciągu symboli w postaci normalnej Foaty.
- Program pozwala na zapisywanie oraz wyświetlanie wynikowej macierzy w postaci diagonalnej.
- Program jest w stanie wykonywać operację pivotingu.