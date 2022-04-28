# %%
# création fichier
f = open("test_fic.txt", "w")
chars = f.write("first line content\n")
print(f'{chars} characters written')
f.close()

# lecture
f = open("test_fic.txt", "r")
print(f.read(10))
print(f.read())
f.close()

# append (avec gestionnaire de contexte)
with open("test_fic.txt", "a") as f:
    f.write("second line content\n")

# le fichier est fermé en sortant du bloc with
# f.write("blabla")

# 
# %%
# modes avancés
# r+ => r+a
# curseur en lecture et écriture à la fin
with open("test_fic.txt", "r+") as f:
    print(f.read(10))
    f.write("à bon chat bon rat\n")
# %%
# par défaut, on écrit dans l'encodage de l'os
from asyncio import shield
from fileinput import filename
import os

with open("test_fic.txt", "w", encoding="utf8") as f:
    f.write("à bon chat b on rat\n")

with open("test_fic.txt", "w+", encoding="utf8") as f:
    f.write("à bon chat bon rat\n")
    # pour lire, replacer le curseur à la position désirée
    # seek est bas niveau => déplace le curseur d'un nb d'octet
    # f.seek(1, os.SEEK_SET)
    f.seek(2, os.SEEK_SET)
    print(f.read(5))
# %%
# itération sur un fichier

lines = [
    "à bon chat bon rat\n", 
    "un tiens vaut mieux que deux tu l'auras\n"]
with open("test_fic.txt", "w+", encoding="utf8") as f:
    f.writelines(lines)
    f.seek(0, 0)
    # itération pas à pas
    print(next(f))
    for line in f:
        print(line)
# %%
# 
# objet iterable
class Iter:
    # condition limite
    def __init__(self, limit):
        self.limit = limit
    
    # condition initale
    def __iter__(self):
        self.cpt = 0
        return self
    
    # test condition limite + incrémentation 
    def __next__(self):
        if self.cpt > self.limit:
            raise StopIteration
        ret = self.cpt
        self.cpt += 1
        return ret

it = Iter(10)
it = iter(it)
# for _ in range(12):
#     print(next(it))

it = iter(it)
for i in it:
    print(i)
# %%
# manipulation du module os
import os
import shutil

my_package = {
    "package:my_package": [
        { "package:my_subpackage": [{"module:my_sub_module": ["my_sub_func"]}]},
        { "module:my_module": ["my_func"]}
    ]
}

def build_package(pckg: dict, force=False, encoding="utf8"):
    for key, items in pckg.items():
        ns, path = key.split(":")
        if ns == "package":
            dir_exists = os.path.exists(path)
            if dir_exists and not force: raise FileExistsError
            if dir_exists:
                # "rm -rf dossier"
                shutil.rmtree(path)
            os.mkdir(path)
            with open(f"{path}/__init__.py", "w", encoding=encoding) as f: pass
            for item in items:
                os.chdir(path)
                build_package(item, force=force, encoding=encoding)
                os.chdir("..")
        elif ns == "module":
            filename = f"{path}.py"
            file_exists = os.path.exists(filename)
            if file_exists and not force: raise FileExistsError    
            if file_exists:
                os.remove(f"{path}.py")
            with open(f"{path}.py", "w", encoding=encoding) as f:
                for item in items:
                    f.write(f"def {item}():\n    pass")



    

build_package(my_package, force=True)

# %%
import os
os.mkdir("crypto")

# %%
