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
# pip install lxml
# import lmxl.etree
import xml.etree.ElementTree as ET

# charger le document
tree = ET.parse("clusters.xml")
print(type(tree))
# on travaille à partir du noeud racine
root = tree.getroot()
print(type(root))

# nom de balise
print(f"balise racine: {root.tag}")

# accès par les indices
first_stroke_name = root[3][2][0]
# attributs d'un balise
print(first_stroke_name.attrib)
# contenu d'une balise finale
print(first_stroke_name.text)

cluster = root.find("Cluster")
for tag in cluster.iter("DBL"):
    if "unit" in tag.attrib:
        print(tag.find("Name[@unit='mm']").text)
print(cluster.find("DBL[last()]"))
non_null_dbl_operations = cluster.findall(
    "DBL[Val!='0.00000000000000']/Name")
print([tag.text for tag in non_null_dbl_operations])

# %%
# écriture xml
import xml.etree.ElementTree as ET

cluster = {
    "Name": "PH42",
    "NumElts": 23,
    "phases": [
        {"type": "DBL", "Name": "Bourrine", "Val": 100000},
        {"type": "INT32", "Name": "Vitesse de rot", "Val": 7200},
    ]
}

cluster_tag = ET.Element("Cluster")
for k, v in cluster.items():
    if k == "phases":
        for obj in v:
            type_tag = ET.Element(obj["type"])
            for key, value in obj.items():
                if key != "type":
                    t = ET.Element(key)
                    # les scalaires convertis en str
                    t.text = str(value)
                    type_tag.append(t)
            cluster_tag.append(type_tag)
    else:
        t = ET.Element(k)
        t.text = str(v)
        cluster_tag.append(t)

# print(ET.tostring(cluster_tag))
tree = ET.parse("clusters.xml")
root = tree.getroot()
root.append(cluster_tag)

tree.write("clusters.xml")

# %%
