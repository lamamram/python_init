print("hello")

# %%
print("hello cell!")
# %%
# création variable
# création par affectation
import sys
x = 1
type(x)
# valeur max d'un entier en 64 bit
# taille en octet d'une variable, 
# i.e de l'objet qu'elle référence
print(sys.maxsize, sys.getsizeof(x))
# %%
# typage dynamique
x = 1
x = "bonjour"
type(x)

# %%
# affectation de variable et d'expression
x = 1
# passage de valeur par référence
# x et y référencent le même emplacement mémoire
y = x
# affectation d'une expression
z = (x + y)/2
# une instruction n'est pas évaluable
# print(x = 0)
# %%
# mécanisme d'optimisation de la mémoire à  m'affectatin
x = 2
y = 2
# la fonction id retrourne l'identenfiant de l'emlacement
# mémoire d'une variable
print(id(x), id(y))


# %%
# correct mais non pythonique
x = 1;y = 0
x = y = 1
# %%
# correct et pythonique: l'"unpacking"
x, y, z = 1, "coucou", 3.14

# %%
## types buit-ins
from math import pi
# par convention on utilise le snake_case pour 
# nommer les variables
entier_negatif = -33
# le CamelCase n'est utilisé que pour les classes
# EntierNegatif = -33
# par convention, une variable en majuscule est une constante
PI = 3.14
# chaine de caractère
user_name = "matthieu"
# chaine d'octets
byte_str = b"matthieu"
# == bytes("matthieu", "utf8")
# les listes: ensemble indexé de valeurs de type qq
nombres = [33, 1.1, -3, pi]
# les tuples: idem que liste mais non modifiable
ro_numbers = (33, 1.1, -3, pi)
# les dictionnaires: ensembles de valeurs associées à des clés
user = {
    "name": "LAMAMRA",
    "age": 39,
    -5: [2, 3],
    3.14: "PI",
    (-0.1342, 43.334545): "nantes"
}
# les sets: ensembles de valeurs uniques non indexées, itérable
enum = {"pomme", "banane", "framboise"}

# changement des séparateurs de valeurs et de ligne
print(nombres[0], ro_numbers[3], user["age"], sep=",", end="|")
print(enum, "end")

# %%
# fonction input: saisie au clavier
age = input("veuillez saisir votre âge: ")
print(age, type(age))
# help: documentation interne
help(str)
# dir: retourne la liste des attributs de l'objet
# en paramètre
dir(age)
# %%
