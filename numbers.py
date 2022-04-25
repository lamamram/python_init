# %%
# les complexes
from cmath import phase, polar

z = complex(33, 3)
z = 33 + 3j
print(z, (z.real, z.imag), z.conjugate())
# module, argument
print(abs(z), phase(z))
# unpacking
mod, arg = polar(z)
print(mod, arg)
# %%
# exo: saisir un entier < 86400 au clavier
# 1. convertir en entier
# 2. afficher heure minute seconde depuis minuit
nb_seconds = input("veuillez saisir un nb de secondes")
# conversion via la classe int
nb_seconds = int(nb_seconds)
heures = nb_seconds // 3600
minutes = (nb_seconds % 3600) // 60
seconds = nb_seconds % 60

# print("Il est", heures, "h", minutes, "mn", seconds, "s")
display = "il est " + str(heures) + "h, " + str(minutes) + "mn"
print(display)
# %%
from math import floor, ceil 
# arrondi d'un nombre
# arrondi à 2 chiffres significatifs
bad_pi = 3.14559
print(round(bad_pi, 2), floor(bad_pi * 100)/100, ceil(bad_pi* 100)/100)

# %%
# opérateurs logique
x, y, z = 3, "truc", [1, 2, 3]
t, u, v = 0, "", None
# or retourne la première expression vraie
print("or vrai: ", x or y or z)
# ... ou la dernière expression fausse
print("or faux: ", t or u or v)
# or retourne la dernière expression vraie
print("and vrai: ", x and y and z)
# ... ou la première expresion fausse
print("and faux: ", t and u and z)
# %%
# utilisation de or pour des valeurs par défaut
expected_result = 0
default = 33
param = expected_result or default
print(param)
# %%
# vrai et faux en python
True;False
# %%
# structure conditionnelle
x = int(input("entier"))

if x > 0:
    print("positif")
elif not x:
    print("nul")
else:
    print("negatif")

# %%
# opérations en binaire

n1, n2 = 0b10110010, 0b00011100

print(bin(n1 | n2), bin(n1 & n2), bin(n1 ^ n2))
print(bin(~n2))
# décalage à gauche et à droite => multiplacation ou division par deux
print(bin(n1 << 1), bin(n2 >> 2))
# %%
# ordre d'exécution des opérateurs
x, y, z = 2, 3, 4

# pass: instruction neutre => ne fait rien
# Rappel: () > op arithmétique > logique > comparaison
if (x * y + z > 5 or x * (y + z) < 20) and True:
    pass
# %%
# opérateur d'incrémentation
x = 2

# fonctionne avec + -, *, /, **
# équivalent à x = x ** 2
x **= 2
print(x)

# pour str
_str = ""
_str += "chunk1|"
_str += "chunk2|"
_str += "chunk3"
print(_str)
# %%
