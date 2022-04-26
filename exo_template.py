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

def parse_tpl(tpl, vars, *, slot=("{{", "}}"), default="N/A"):
    while tpl.count(slot[0]):
        start_index = tpl.index(slot[0]) + len(slot[0])
        end_index = tpl.index(slot[1])
        key = tpl[start_index:end_index]
        tpl = tpl.replace(
            slot[0] + key + slot[1], 
            vars.get(key, default)
        )
    return tpl

print(parse_tpl(_template, injections, slot=("((", "))")))
print(parse_tpl(
    """blabla {{name}}  {{firstname}}""",
    {"name": "LAMAMRA", "firstname": "matt"}
))
# %%
def parse_tpl(tpl, slot=("{{", "}}"), default="N/A", **vars):
    while tpl.count(slot[0]):
        start_index = tpl.index(slot[0]) + len(slot[0])
        end_index = tpl.index(slot[1])
        key = tpl[start_index:end_index]
        tpl = tpl.replace(
            slot[0] + key + slot[1], 
            vars.get(key, default)
        )
    return tpl

print(parse_tpl(_template, slot=("((", "))"), key1="val1", key2="val2"))
# %%
