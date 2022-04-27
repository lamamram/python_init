# %% 
# module datetime
from datetime import datetime, timedelta
import time
# %%
# instanciation canonique
dt = datetime(2022, 4, 27, 12, 1, 23)
print(dt, type(dt))

time_chunks = (2022, 4, 27, 12, 1, 23)
dt = datetime(*time_chunks)
print(dt)
# %%
# autres instanciations

now = datetime.now()
print(now)

# date en str avec format donné
dt = datetime.strptime("2022-04-27", "%Y-%m-%d")
print(dt)

# à partir d'un timestamp
dt = datetime.fromtimestamp(86400 * (365 * 52 + 129) + 3600 * 12)
print(dt)

# fuseau horaire
print(time.localtime().tm_zone)

# %%
# getters

now = datetime.now()
print(now.year, now.month, now.day)
print(f"jour de la semaine: {now.weekday()}")
print(now.date(), now.time())
print(now.timestamp())

# %%
# affichage dans un format donné
now = datetime.now()

print(now.strftime("%d/%m/%Y"), f"semaine {now.strftime('%W')}")



# %%
# arithmétique de dates

vacances_matthieu = datetime(2022, 8, 1)
now = datetime.now()
remaining_time = vacances_matthieu - now
print(remaining_time, type(remaining_time))


cuisson_oeuf_coque = timedelta(minutes=3)
atable = now + cuisson_oeuf_coque
print(atable)

# %%
# module re => regular expression, expression rationnelle
# => chaine de caractère décrivant un modèle de chaines de caractères

# ex: numéro de téléphone français
# => 5 paires de chiffres séparés par ' ' ou '-' ou pas
# avec la première commence par 0 ou +33

# "^" => commence par
# "$" => finit par
# "|" => alternative (chat|Chat)
# "." => n'importe quel caractère

# "[]" => classe de caractère, i.e ensemble de caractères possibles
#         pour un caractère de la cible (ex [cC]hat)
# valeurs spécifique aux classes
# a-z => lettre min
# A-Z => lettre maj
# 0-9 => chiffre
# on place le "-" à la fin de la classe
# "^" au début de la classe )=> tout sauf les caractères suivants
# ex. [^0-9]: tout sauf un chiffre

# quantifieurs
# * => ce qui précède autant de fois qu'on veut
# + => idem           1 fois ou plus
# ? => iden           au + une fois
# {n}, {n, m}, {n,}, {,m} => n x, entre n et m x, au - n x, au + m fois

import re

french_tel_strict = "^(0|\+33)[0-9]([ -]?[0-9]{2}){4}$"
french_tel = "(0|\+33)[0-9]([ -]?[0-9]{2}){4}"

# fonction match => test la regex sur la cible depuis le début de la cible
target = "+336 05 12 65 98"
target2 = "0705126598"
bad_target = "2022"
begin_target = "0705126598 (fixe)"

#match
m = re.match(french_tel_strict, target)
print(m)
# accès au groupes de capture
print(m.groups())
print(m.group())
print(m.group(0))

print("------------match-----------------")
# match
m = re.match(french_tel_strict, target2)
print(m)

# !match
m = re.match(french_tel_strict, bad_target)
print(m)

# !match
m = re.match(french_tel_strict, begin_target)
print(m)

m = re.match(french_tel, begin_target)
print(m)

fm = re.fullmatch(french_tel, begin_target)
print(fm)

print("------------search-----------------")

txt = """
blabla blabla blabla blabla +336-05-12-65-98 blabla
blabla blabla blabla 0705126598 blabla
"""

# premier match
s = re.search(french_tel, txt)
print(s)

# iterateur sur tous les matches
matches = re.finditer(french_tel, txt)
print(list(map(lambda m: m.group(), matches)))

# récupérer les groupes de captures dans la target
captures_groups = re.findall(french_tel, txt)
print(captures_groups)

print("------------sub-----------------")

print(re.sub(french_tel, "##########", txt))

# %%
