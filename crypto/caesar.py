# %%
"""
fonctions de chiffrement caesar
"""
from string import ascii_lowercase
from random import shuffle, choice

# ascii_lowercase = "".join([ chr(i) for i in range(97, 123)])
# print(ascii_lowercase)

def generate_key(alphabet=ascii_lowercase):
    key = list(alphabet)
    # while True:
    #     shuffle(key)
    #     # all => vrai si tous les éléments de l'itérable sont vrais
    #     if all(map(lambda a, s: a != s, alphabet, key)):
    #         return "".join(key)
    # any => vrai si au moins un élément de l'itéerable est vrai
    while any(map(lambda a, s: a == s, alphabet, key)):
        shuffle(key)
    return "".join(key)

def generate_key(alphabet=ascii_lowercase):
    key = ""
    for letter in alphabet:
        # appel récursif si impossibilité de permuter la dernière lettre
        if letter == "z" and "z" not in key:
            return generate_key(alphabet)
        while True:
            perm = choice(alphabet)
            if letter != perm and not perm in key:
                key += perm
                break
    return key

def crypt(msg, key):
    crypted = ""
    for letter in msg:
        crypted += key[ord(letter) - 97]
    return crypted

def uncrypt(crypted, key):
    clean_msg = ""
    for letter in crypted:
        clean_msg += chr(key.index(letter) + 97)
    return clean_msg
# %%
