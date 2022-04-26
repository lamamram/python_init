# %%
# opérateur ternaire

cond = False

if cond: param = "vrai"
else: param = "faux"
print(param)

# équivalent à
param = "vrai" if cond else "faux"
print(param)
# %%
# transformations d'une liste
# conserve la liste initiale
fruits = ["pomme", "poire", "framboise"]
fruits_maj = []
for fruit in fruits:
    fruits_maj.append(fruit.upper())
print(fruits_maj)

# %%
# sans conserver la liste initiale
# i = 0
fruits = ["pomme", "poire", "framboise"]
# for fruit in fruits:
#     fruits[i] = fruit.upper()
#     i += 1

for i, fruit in enumerate(fruits):
    fruits[i] = fruit.upper()

print(fruits)

# %%
# idem avec liste en intension
fruits = ["pomme", "poire", "framboise"]
print( [ f.upper() for f in fruits ] )
# + filtre
print( [ f.upper() for f in fruits if f[0] == "p" ] )

# %%
import sys
# fonction range
# 1 paramètre => de 0 à n non compris
r = range(10)
print(r, list(r))

# 2 params => début compris, fin non comprise
r2 = range(1, 11)
print(list(r2))

# de début à fin non comprise avec pas de prélèvement
r3 = range(2, 21, 2)
print(list(r3))

r4 = range(10, -1, -1)
print(list(r4))

for i in r4: print(i)

# range est un générateur
# calcul les valeurs à la volée
r5 = range(100000000)
print(sys.getsizeof(r5))
# %%
# break, continue, else
# afficher nb_multiple multiples de multiple <= n
n, multiple, nb_multiple = 100, 10, 6

for i in range(1, n + 1):
    # continue: interrompt l'itération courante
    # et passe à l'itération suivante
    if i % multiple: continue
    # break: sort immédiatement de la boucle
    if i > multiple * nb_multiple: break
    print(i)
# exécute le code si la boucle for se termine
# normalement i.e sans rencontrer break
else:
    print("tous les multiples sont affichés")


# %%
# idem avec while
n, multiple, nb_multiple = 100, 10, 10
i = 0
while i <= n:
    i += 1
    if i % multiple: continue
    if i > multiple * nb_multiple: break
    print(i)
else:
    print("tous les multiples sont affichés")

# %%
