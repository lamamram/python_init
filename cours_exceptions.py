# %%
def _inv(x):
    return 1/x

# %%
# capture d'une erreur se prduisant dans le bloc try
# par défaut, toutes les erreurs sont capturées par except
try:
    x = int(input("int: "))
    x = _inv(x)
    print(x)
except:
    print("zero div")

# %%
# afficher l'erreur
import traceback as tb
try:
    x = int(input("int: "))
    x = _inv(x)
    print(x)
except Exception as exc:
    print(type(exc), exc)
    tb.print_tb(exc.__traceback__)

# %%
# spécialisation des blocs except
try:
    x = int(input("int: "))
    x = _inv(x)
    print(x)
except ZeroDivisionError as ze:
    print(type(ze), ze)
    print("traitement zero div")
except ValueError as ve:
    print(type(ve), ve)
    print("traitement bad conversion")

# %%
# même traitement pour n exceptions spécifiques
try:
    x = int(input("int: "))
    x = _inv(x)
    print(x)
except (ZeroDivisionError, ValueError) as zve:
    print(type(zve), zve)
    print("traitement zero div & bad conversion")

# %%
import sys
# else: bloc exécuté si aucune erreur dans le bloc try
# finally: bloc exécuté avant de sortir de du bloc exception
# quoi qu'il arrive (exception non gérée, ou sortie du programme)
try:
    x = int(input("int: "))
    x = _inv(x)
except (ZeroDivisionError, ValueError) as zve:
    print(type(zve), zve)
    print("traitement zero div & bad conversion")
else:
    print(f"inverse = {x}")
    sys.exit(0)
finally:
    print("final code !!!")

print("after code !!!")

# %%
# déclenchement d"une exception par le dev

def notes_avg(notes: list) -> float:
    if not notes: raise ValueError(f"liste vide !")
    for note in notes:
        if not 0 <= note <= 20:
            raise ValueError(f"{note} doit être entre 0 et 20")
    return round(sum(notes)/len(notes), 2)

try:
    print(notes_avg([]))
    print(notes_avg([3, -6, 12]))
except ValueError as ve:
    print(ve)
# %%
# exception custom

class RangeError(Exception):
    def __init__(self, val, min_val, max_val) -> None:
        self.val = val
        self.min_val = min_val
        self.max_val = max_val
    
    def __str__(self) -> str:
        return f"{self.val} not in [{self.min_val}, {self.max_val}]"

def notes_avg(notes: list) -> float:
    if not notes: raise ValueError(f"liste vide !")
    for note in notes:
        if not 0 <= note <= 20:
            raise RangeError(note, 0, 20)
    return round(sum(notes)/len(notes), 2)

try:
#    print(notes_avg([]))
    print(notes_avg([3, -6, 12]))
except (ValueError, RangeError) as vre:
    print(vre)
# %%
class RangeError(Exception):
    def __init__(self, val, min_val, max_val) -> None:
        self.val = val
        self.min_val = min_val
        self.max_val = max_val
    
    def __str__(self) -> str:
        return f"{self.val} not in [{self.min_val}, {self.max_val}]"

# decorateur paramétré

def check_range(min_val, max_val):
    def deco(f):
        def wrapper(l: list, *a, **kw):
            for elem in l:
                if not min_val <= elem <= max_val:
                    raise RangeError(elem, min_val, max_val)
            return f(l, *a, **kw)
        return wrapper
    return deco

@check_range(0, 20)
def _avg(l: list):
    if not l: raise ValueError(f"liste vide !")
    return round(sum(l)/len(l), 2)

try:
#    print(notes_avg([]))
    print(notes_avg([3, -6, 12]))
except (ValueError, RangeError) as vre:
    print(vre)
# %%
