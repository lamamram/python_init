# %%
# gestion du format csv
# création

import csv

from numpy import mat

header = ["name", "age", "sex", "role"]
users = [["bob", 32, "M;F", "dev"], ["jane", 28, "F", "admin"]]

# rajouter newline = "" sous windows pour éviter les lignes vides
with open("users.csv", "w", encoding="utf8", newline="") as csv_f:
    # QUOTE_MINIMAL => uniquement les cellules contenant ";"
    # QUOTE_ALL => rapide, fichier + lourd
    # QUOTE_NONE => rapide, uniquement si valeurs numériques
    # QUOTE_NON_NUMERIC => - rapide
    writer = csv.writer(
        csv_f, delimiter=";", quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(header)
    writer.writerows(users)



    
# %%
#lecture csv
import csv
with open("users.csv", "r", encoding="utf8") as csv_f:
    reader = csv.reader(
        csv_f, delimiter=";", quotechar='"')
    print(f"header: {next(reader)}")
    print(reader.line_num)
    # for line in reader: print(line)
    print(list(reader))

# %%
# json
import json

users = {
    "users": [
        {"name": "bob", "age": 32, "sex": "M;F", "role": "dev"},
        {"name": "jane", "age": 28, "sex": "F", "role": "admin", "city": "paris"},
    ]
}

json_str = json.dumps(users)
print(json_str, type(json_str))

with open("users.json", "w", encoding="utf8") as json_f:
    # json.dump(users, json_f, indent=2)
    json.dump(users, json_f, separators=(",", ":"))

# %%
import os
import json
# if os.system("pip install jsonpath-ng"):
# pip install jsonpath-ng
from jsonpath_ng.ext import parse

with open("users.json", "r", encoding="utf8") as json_f:
    obj = json.load(json_f)
    print(obj["users"][1]["city"])

with open("users.json", "r", encoding="utf8") as json_f:
    obj = json.loads(json_f.read())
    print(obj["users"][1]["city"])

# expression JSONPATH
# les valeurs de city pour les élements de la liste
# users qui possède un champs age à 28
expr = parse("$.users[?(@.age==28)].city")
for match in expr.find(obj):
    print(match.value)
# %%
# lecture xml
