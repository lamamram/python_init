# %%
# instanciations d'un dictionnaire
# litéral
dico = {"k1": "v1", "k2": "v2"}
print(dico)

# à partir d"une liste de tuples
dico = dict([ ("k1", "v1"), ("k2", "v2") ])
print(dico)

# à partir des aramètres nommés de la classe dict
dico = dict(k1="v1", k2="v2")
print(dico)
# %%
# accès aux valeurs
dico = {"k1": "v1", "k2": "v2"}
print(dico["k1"])

# KeyError
# print(dico["k3"])

if "k3" in dico:
    print(dico["k3"])
else:
    print("default")

# équivalent à
print(dico.get("k3", "default"))
# %%
dico = {"k1": "v1", "k2": "v2"}
# itérations

# sur les clés
print(list(dico))
for k in dico: print(k)

# sur les valeurs
print(dico.values())
for v in dico.values(): print(v)

# sur les paires clés valeurs
print(dico.items())
for t in dico.items(): print(t)
for k, v in dico.items(): print(k, v)

# %%

# attention à la mutabilité (list, dict)

l1 = [1, 2, 3]
l2 = l1
# copy => list et dict
l3 = l1.copy()
# slicing du début à la fin => copie indépendante en mémoire
l4 = l1[:]

l2.append(4)
l3.append(5)

print(l1)
print(l1 is l2, l1 is l3)
# %%
