st = "ala ma kota ala ala ala"

def my_split(st):
    word=""
    for ch in st:
        if ch==" ":
            yield word
            word = ""
            continue
        word+=ch
    yield word
    

def word_count(arr):
    dct = dict()
    for word in arr:
        print(word)
        if word in dct.keys():
            dct[word]+=1
        else:
            dct[word]=1
    return dct



print(word_count(my_split(st)))



