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





