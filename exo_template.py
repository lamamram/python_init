# %%
# exercice : remplacer les clés entourées par "((" et "))"
# dans un texte par les valeurs correspondantes dans un dico

# 1. afficher le contenu entre la première occurence de (( et ))
# 2. remplacer ((key1)) par content1 dans _template
# Hint: regarder la fonction str.replace
# 3. itérer sur _template pour remplacer toutes les slots (())
# par la clé correspondante si celle ci existe ou par N/A

_template = """
lorem ipsum (blabla) ... ((key1)) blabla ....
lorem ipsum (blabla) ... ((key2)) blabla ....
lorem ipsum (blabla) ... ((key3)) blabla ....
lorem ipsum (blabla) ... ((key4)) blabla ....
"""

injections = {
    "key1": "content1",
    "key2": "content2",
    "key3": "content3"
}

# %%
while _template.count("(("):
    start_index = _template.index("((") + len("((")
    end_index = _template.index("))")
    key = _template[start_index:end_index]
    _template = _template.replace(
        "((" + key + "))", 
        injections.get(key, "N/A")
    )

print(_template)
# %%
"blabla".replace("bli", "blo")
# %%
import re

for key, content in injections.items():
    _template = _template.replace("((" + key + "))", content)

_template = re.sub("\(\(.*\)\)", "N/A", _template)
print(_template)

# %%
