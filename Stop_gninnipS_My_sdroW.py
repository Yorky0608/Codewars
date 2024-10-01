def spin_words(sentence):
    list = ""
    for word in sentence.split():
        if len(word) >= 5:
            word = word[::-1]
        list += f" {word}"
    list = list.replace(' ', '', 1)
    return list

print(spin_words("Hey fellow warriors"))