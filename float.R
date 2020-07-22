Precyzja obliczeń liczb zmiennoprzecinkowych w R:
Porównanie obliczeń na 3 równaniach typu float.

As.numeric konwertuje współczynniki na wektor numeryczny.Tylko w zmiennej b wynik wynosi 0,
w pozostałych zmiennych jest jedynie zbliżony do 0.

```{r}
a=as.numeric((2.3 * 3.0)-6.9)
b=as.numeric((3.45 * 2.0) - 6.9)
c=as.numeric((3.45 * 3.0) - 10.35)

print(a)
print(b)
print(c)
```

Funkcja round() zaookrągla wyniki.Wynikiem tej funkcji jest liczba zaokrąglona do zadanego miejsca po przecinku
(domyślnie do zerowego miejsca dziesiętnego).
Wyniki wynoszą 0,w każdym przypadku,co znaczy,że są zgodne z wynikiem przypuszczanym.
```{r}
g=round(as.numeric(2.3 * 3.0) - 6.9)
h=round(as.numeric(3.45 * 2.0) - 6.9)
i=round(as.numeric(3.45 * 3.0) - 10.35)

print(g)
print(h)
print(i)
```
Zaokrąglana jest tylko pierwsza wymnożona liczba co powoduje uzyskanie innego wyniku niż przewidywany.
Ze wszystkich przewidywanych do tej pory wyników,te są najdalsze od 0.
```{r}
m=round(2.3 * 3.0) - 6.9
n=round(3.45 * 2.0) - 6.9
s=round(3.45 * 3.0) - 10.35

print(m)
print(n)
print(s)
```

Porównanie dwóch wartości,w przypisanej zmiennej.Powoduje zwrot wartości logicznych(True or False).
Tylko w drugim przypadku wynikiem jest True,co oznacza,że wartości są sobie równe.
```{r}
(2.3 * 3.0) - 6.9 == 0
(3.45 * 2.0) - 6.9 == 0 
(3.45 * 3.0) - 10.35 == 0
```



