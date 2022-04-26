# %%
# définition et appel

# définition de la fonction
def func():
    print("func")

print("start")
# appel de la fonction
print(f"return: {func()}")
print(func)
print("end")

# %%
# instruction return

# return sort de la fonction immédiatement
# return donne une valeur de retour à l'appel
def func():
    return "func"
    print("qqch")

print(f"return: {func()}")

# %%
# unpacking de la valeur de retour
def func():
    return "func", "funk"

t = func()
print(t[0], t[1])
ret1, ret2 = func()
print(ret1, ret2)
# %%
# les paramètres n'ont pas de type a priori
# polymorphisme
def fois3(x):
    return x * 3

print(fois3(9), fois3("rien"))
# %%
# docstring
def func():
    """
    fonction indispensable
    @param: ...
    @returns: ...
    """
    pass

# %%
help(func)
print(func.__doc__)
# %%
# annotations: valeurs indicatives
def vitesse(
    distance: float, 
    temps: float, 
    unit: str="m/s") -> str:
    return f"{distance/temps:.2f} {unit}"

print(vitesse(100, 10))
print(vitesse.__annotations__)
# %%
## types des paramètres
# paramètres positionnels / obligatoires

def func(p1, p2):
    return p1, p2

print(func("p1", "p2"))
# TypeError
# print(func("p1"))
# %%
# appel nommé: flechage des paramètres et des valeurs

def func(p1, p2):
    return p1, p2

print(func(p2="p1", p1="p2"))

# %%
# paramètres nommés à la def => valeurs par défaut
# toujours placer es param positionnels 
# avant les params nommés à la def
def func(p1, p2=None, p3={}):
    return p1, p2, p3

print(func("p1", "p2"))
print(func("p1", p3={"k": "v"}))
# %%

# *args: paramètres positionnels supplémentaires
def func(pos, *params):
    return pos, params

func("pos", "opt1", "opt2", "opt3")
# %%
def my_sum(*values):
    return sum(values)

print(my_sum(1, 4, 5, 6))

# %%
# kwargs: paramètres nommés supplémentaires
def func(pos, **options):
    return pos, options

print(func("pos", opt1="v1", opt2="v2"))

# %%
# *args à l'appel

def func(p1, p2, p3):
    return p1, p2, p3

params = ["p1", "p2", "p3"]
kw_params = {"p2": "v2", "p3": "v3", "p1": "v1"}

# print(func(params[0], params[1], params[2]))
print(func(*params))
print(func(**kw_params))
# %%

def my_sum(*values):
    return sum(values)

params = list(range(20))
print(my_sum(*params))
# %%
def func(pos, /, param="dflt", *, opt="val"):
    return pos, param, opt

# TypeError: à gauche du / les paramètres
# doivent être appelés de manière positionnelle
# func(pos="pos")

func("pos")
# TypeError: à droite du * on doit appeler les paramètres
# de manière nommée
# func("pos", "param", "v")
func("pos", "param", opt="v")
# %%
