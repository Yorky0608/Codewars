def generate_hashtag(s):
    hash = "#"
    list = s.split()
    s = s.replace(' ', '')
    if not s:
        return False
    if len(s) >= 140:
        return False
    for word in list:
        word = word.title()
        hash += word
    return hash

print(generate_hashtag('Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat'))