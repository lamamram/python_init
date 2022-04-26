# %%
## calculer la moyenne d'une liste de nombre entiers renseignés au clavier

# 1. saisir une série de nombres entiers séparés par "," (en une seule saisie)

nbs = input("saisir des nombres entiers séparés par ,: ")
print(nbs)
# 2. pour chaque nombre, vérifier qu'il s'agit d'un entier
#    regarder la fonction isnumeric du type str
#    séparer le cas >= 0 et < 0
true_nbs = []
nbs = nbs.split(",")
for nb in nbs:
    # on traite le cas ""
    if nb and (
        # si entier >= 0
        nb.isnumeric() 
        # ... ou entier < 0
        or nb[0] == "-" and nb[1:].isnumeric()):
        true_nbs.append(int(nb))
    else:
        print(nb, "n'est pas un entier !")

# 3. si tous les nombres sont des entiers, calculer et afficher la moyenne
if len(nbs) == len(true_nbs):
    moyenne = round(sum(true_nbs)/len(true_nbs), 2)
    # styles d'affichage
    print("moyenne: " + str(moyenne))
    print("moyenne: ", moyenne)
    # templating
    print("moyenne: %f" % moyenne)
    print("moyenne: %.2f" % moyenne)
    print("{1}: {0:5.2f}".format(moyenne, "moy"))
    # f-string
    label = "moyenne"
    print(f"{label.upper()}: {moyenne:5.2f}")
# %%
"-1".isnumeric()
# %%

# %%
nbs = input("saisir des nombres entiers séparés par ,: ")
nbs = nbs.split(",")
for i, nb in enumerate(nbs):
    if nb and (
        # si entier >= 0
        nb.isnumeric() 
        # ... ou entier < 0
        or nb[0] == "-" and nb[1:].isnumeric()):
        nbs[i] = int(nb)
    else:
        print(f"{nb} n'est pas un entier !")
        break
else:
    moyenne = round(sum(nbs)/len(nbs), 2)
    print(f"moyenne : {moyenne:.2f}")
# %%
