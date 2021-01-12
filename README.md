# Projekt na kolokwium z języków skryptowych 
## Problem:
Należy zliczyć częstość występowania wyrazów w tekście.

## Zaoimplementowane funkcje:

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
