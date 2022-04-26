# %%
# variable globale à une fonction

def func():
    print(f"x dans la fonction: {x}")

x = 10
func()
# %%
# variable locale à une fonction
def func():
    x = 5
    print("locales", locals())
    print(f"x dans la fonction: {x}, {id(x)}")

x = 10
func()
print(f"x dans la portée globale: {x}, {id(x)}")
print("globales", globals())
# %%
# modification d'une globale dans une fonction
def func():
    global x, y
    x = 5
    print(f"x dans la fonction: {x}, {id(x)}")

x, y = 10, 15
func()
print(f"x dans la portée globale: {x}, {id(x)}")

# %%
# paramètres: passage par référence

def func(lst: list, elem):
    print(f"paramètre lst: {id(lst)}")
    lst.append(elem)

l = [1, 2, 3]
print(f"l dans la portée globale: {id(l)}")
func(l, 4)
print(l)
# %%

# fonction comme variable

def square(x):
    return x**2

def my_map(f, lst):
    return [ f(elem) for elem in lst ]

print(my_map(square, list(range(6))))

# fonction lambda
print(my_map(lambda x: x**2, range(6)))
# %%
from random import randint

# fonction classique de prog foncitonnelle
# map complexe
print(list(map(lambda x, y: x == y, 
    [1, 4, 5, 7, 2],
    [1, 5, 5, 3, 4])))

# filtre
print(list(filter(lambda x : not x%2, range(20))))

# tri complexe
rows = [ f"row_{randint(1, 30)}" for _ in range(10) ]
print(rows)
# rows.sort()
rows = sorted(rows, key=lambda r: int(r[4:]), reverse=True)
print(rows)

# %%
from time import time
start = time()
squares = [ x**2 for x in range(100000) ]
print(time() - start)

start = time()
squares = map(lambda x: x**2, range(100000))
print(time() - start)

# %%
