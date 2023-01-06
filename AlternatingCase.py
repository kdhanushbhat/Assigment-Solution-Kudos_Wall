def alternateCase(word):
    # return word.swapcase()                ------------> this is also a solution two switch case
    res = ''
    for char in word:
        if char.isupper():
            res+= char.lower()
        else:
            res+= char.upper()
    
    return res

word = input("Enter the word: ").strip()
print(alternateCase(word))