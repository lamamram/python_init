# %%
# import global
# l'import recherche le nom de module
# 1. dans le dossier courant
# 2. dans la lib standard
# 3. dans les libs installées par pip (venv)
# 4. ModuleNotFoundError
# avec import on importe que les modules (ou les packages si manipulation)
from posixpath import dirname
import templating

print(templating.parse_tpl(
    templating._template, {"key1": "blabla"}, slot=("((", "))")))

# attention, les modules importés sont exécutés

# %%
# import partiel
from templating import parse_tpl, _template
from templating import *

print(parse_tpl(
    _template, {"key1": "blabla"}, slot=("((", "))")))
# %%
# aliasing de modules et de leur contenu
# pour éviter les conflits de noms

import templating as tpling
from templating import parse_tpl as p_tpl

def parse_tpl():
    pass

print(p_tpl(
    tpling._template, {"key1": "blabla"}, slot=("((", "))")))
# %%
import templating
help(templating)
dir(templating)

# %%
# module principal vs module importé
import templating, os
# import os

if __name__ == "__main__":
    print("module principal")
    # chemin absolu du répertoire projet
    PROJECT_PATH = os.path.dirname(__file__)
    print(templating.__name__)

# %%
# import de modules depuis un package (ou sous package)
import parsing.parsers as parser
from parsing.templates.utils import _template



print(parser.parse_tpl(
    _template, {"key1": "blabla"}, slot=("((", "))")))

# %%
# même chose avec des import intermédiaires dans le __init__.py
from parsing import parse_tpl, _template

print(parse_tpl(
    _template, {"key1": "blabla"}, slot=("((", "))")))
# %%
