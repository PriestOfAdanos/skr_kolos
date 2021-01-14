# Projekt na kolokwium z języków skryptowych 
## Problem:
Należy zliczyć częstość występowania wyrazów w tekście.

## Zaimplementowane funkcje:

```python
my_split(<string>)-> <arr>
```

Która jako argument przyjmuje łańcuch znaków, w których spacje odzielają poszczególne słowa.
Zwraca listę słów w łańcuchu znaków

```python
word_count(<arr>)-> <dictionary>
```

Która jako argument przyjmuje listę.
Zwraca słownik gdzie kluczami są elemnty wprowadzonej listy a wartościami jest ich ilość w liście.

## Przykładowe użycie:

```python
>> st = "ala ma kota ala ala ala"
>> print(word_count(my_split(st)))
>> {'ala': 4, 'ma': 1, 'kota': 1}
```

## Złożoność czasowa
### my_split
długość tekstu -> n

ilość spacji -> m (m+1 -> il.słów)


Rozważmy 2 sytuacje, gdzie długość łańcucha  wejścia będzie wynosiła 10:

```
l1 = "qwe rty ui"
l2 = "qwer tyuio"
```

Zarówno dla l1 i l2 warunek zostanie sprawdzony dla każdego znaku.Jednak w przupdaku l2 mniej razy zostanie ten warunek 
spełniony, co oznacza, że zostanie wykonane mniej operacji.


Zgodnie z zasadą działania algorytmu, dla każdego elementu wykonywana jest operacja, a za każdym razem gdy spełniony 
jest warunek wykonywane są dodatkowe 2 operacje.


Z tego wynika wzór złożoności czasowej:

```
O(n+(m+1)*2)
```

Dla przykładu l1 ilość operacji to: 
```
10+3*2
```
Dla przykładu l2 ilość operacji to: 
```
10+2*2
```
### word_count
ilosć słów -> n

Tutaj sytuacja jest bardzo prosta, dokładnie tyle ile elemntów ma lista, dokładnie tyle wykona się operacji, zwiększenie ilości elelmentów o 1 doda liniowo jedną operacje:
```
O(n)
```


## Pseudokod


```
DEFINE FUNCTION my_split(st):
    SET yld TO EMPTY LIST
    SET word TO ""
    FOR ch IN st:
        IF ch==" ":
            APPEND word TO yld
            SET word TO ""
            SKIP TO NEXT ITERATION
        CONCATENATE ch TO word
    APPEND word TO yld
    RETURN yld

DEFINE FUNCTION word_count(arr):
    SET dct AS EMPTY DICTIONARY
    FOR word IN arr:
        IF word IN KEYS OF dct:
            ADD 1 TO VALUE OF KEY word IN dct
        ELSE:
            CREATE KEY IN dct WITH VALUE OF 1
    RETURN dct

```





