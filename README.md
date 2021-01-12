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
## Pseudokod


```
SET st TO "ala ma kota ala ala ala"

DEFINE FUNCTION my_split(st):
    word=""
    FOR ch IN st:
        IF ch==" ":
            yield word
            SET word TO ""
            continue
        word+=ch
    yield word
   
DEFINE FUNCTION word_count(arr):
    SET dct TO dict()
    FOR word IN arr:
        OUTPUT(word)
        IF word IN dct.keys():
            dct[word]+=1
        ELSE:
            dct[word]=1
    RETURN dct
OUTPUT(word_count(my_split(st)))
```





