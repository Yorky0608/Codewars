from string import ascii_lowercase

def is_pangram(st):
    st = st.lower()
    for c in ascii_lowercase:
        if c in st:
            pass
        else:
            return False
    return True

print(is_pangram("abcdefghijklm opqrstuvwxyz"))