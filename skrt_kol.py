st = "ala ma kota ala ala ala"

def my_split(st):
    yld = []
    word=""
    for ch in st:
        if ch==" ":
            yld.append(word)
            word = ""
            continue
        word+=ch
    yld.append(word)
    return yld
    

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



