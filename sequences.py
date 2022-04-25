# %%
# conversions entre str list tuple
alpha = "abcde"
# liste des lettres
letters = list(alpha)
print(letters, tuple(letters))

# serialisation d'une liste
letters = str(letters)
print(letters, type(letters))

# %%
# décomposer une chaine en sous chaines séparées par un délimiteur
msg = "à bon chat bon rat"
mots = msg.split()
print(mots)

# recomposer une chaine à partir d'une liste de chaines
msg = " ".join(mots)
print(msg)

# %%
# accès aux éléments par l'index
alpha = "abcde"
stuff = [1, "ok", [2, 1, alpha]]

print(alpha[3], stuff[2][0])
# IndexError
# print(stuff[3])

# indices négatifs
print(alpha[-1], stuff[-3])
# %%
# mutable vs immutable
alpha = "abcde"
stuff = [1, "ok", [2, 1, alpha]]

## mutablilité
# opération à l'intérieur de l'objet référencé par la variable
stuff[0] = "new first elem"
# indexError
# stuff[4] = "end"
stuff.append("end")
print(stuff)

## immutabilité
# pas d'opérations internes possibles avec str et tuple
# TypeError
# alpha[0] = "A"
# tuple(stuff)[0] = 0
# %%
# slicing => extraction d'une sous séquence (str, list, tuple)
alpha = "abcde"

bcd = alpha[1:4]
print(bcd)

abc, cde = alpha[:3], alpha[2:]
print(abc, cde, alpha[-3:])

# dbut -> fin tous les 2 caractères
ace = alpha[::2]
# inversion chaine de caractère
edcba = alpha[::-1]
print(ace, edcba)
# %%
# accès aux indices par les valeurs
phrase = "à bon chat bon rat"
# nb d'occurences de bon dans la phrase
print(phrase.count("bon"))

# indice de la 1ère occurence
index0 = phrase.index("bon")
# indice de la 1ère occurence après un indice donné
index1 = phrase.index("bon", index0 + len("bon"))
print(index0, index1)
print(phrase[index1:])
# %%
# ValueError
# "abcde".index("z")
# %%
# recherche d'un élément dans une séquence

stuff = [1, "ok", [2, 1, alpha]]

print("ok" in stuff, [1, "ok"] not in stuff)
# %%
# itération
alpha = "abcde"
for letter in alpha:
    print(letter)

# %%
# opérateurs et fonctions communs
alpha = "abcde"
stuff = [1, 2, 3, 4]

# +: concaténation
print(alpha + "fgh", stuff + ["cinq", "six"])

# * répétition
print(3 * "rien", [0] * 10)

# fonctions
print(min(stuff), sum(stuff))

# %%
# utilisation de numpy
import numpy as np

stuff = np.array([1, 2, 3, 4])
print(stuff.mean())
# %%
