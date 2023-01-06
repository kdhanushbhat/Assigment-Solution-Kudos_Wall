def convertToPigLatin(line):
    line = line.split(' ')
    res = []
    for word in line:
        word = word[1:] + word[0] + 'ay'
        res.append(word)
    return " ".join(res)

def convertToEnglish(line):
    
    line = line.split(' ')
    res = []
    for word in line:
        word = word[-3]+word[:-3]
        res.append(word)
    return " ".join(res)

line = input("Enter the sentence: ").strip()
piglatin = convertToPigLatin(line)

print("Pig latin string:",piglatin)
print("Original english text:",convertToEnglish(piglatin))