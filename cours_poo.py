# %%
class Account:
    # atttribut de classe
    balance = 100

    # self représente l'objet instancié de la classe
    # self est toujours le premier argument d'une méthode
    def get_balance(self):
        return self.balance

# instanciation d'un objet de classe Account
# les fonctions et les classes sont des callables
acc = Account()
# utilisation externe d'un attribut public
print(acc.balance)

# utilisation interne d'un attribut public
# via une méthode publique
print(acc.get_balance())
# %%
# attributs / méthodes privés
class Account:
    # atribut privé
    __balance = 100

    # méthode privée
    def __update_balance(self, amount):
        self.__balance += amount
    

    # méthodes publiques => préparent les données pour
    # mettre à jur les attributs privés 
    def deposit(self, amount):
        if amount > 0:
            self.__update_balance(amount)
    
    def withdrawal(self, amount):
        if amount > 0:
            self.__update_balance(-amount)
    
    def get_balance(self):
        return self.__balance

acc = Account()
# acc.__balance
acc.deposit(300)
acc.withdrawal(100)
print(acc.get_balance())

print(acc._Account__balance)

# %%
# méthodes

# __new__ est le constructeur python
# on y touche pratiquement jamais
# class Truc:
#     pass

# t = Truc()
# dir(t)

# l'initialiseur __init__
# renseigne les atributs dès l'instanciation
class Account:
    def __init__(self, balance=100) -> None:
        # attribut d'objet
        self.__balance = balance
    
    def __str__(self):
        return f"balance: {self.__balance}"
    
    def __getitem__(self, elem):
        return elem * 2

acc = Account(200)
print(acc, str(acc))
print(acc["hola"])

# %%
# héritage (simple)
from datetime import datetime

class Person:
    def __init__(self, f, l) -> None:
        self.lastname = l
        self.firstname = f
    
    def get_full_name(self):
        return f"{self.firstname.capitalize()} {self.lastname.upper()}"


class Client(Person):
    def __init__(self, f, l, dj, date_format="%Y-%m-%d") -> None:
        # super() appelle l'initialiseur de la classe mère
        # sur l'objet courant
        super().__init__(f, l)
        self.date_joint = datetime.strptime(dj, date_format)
    

    def get_date_joint(self, date_format):
        return self.date_joint.strftime(date_format)

# comportement mixte => surcharge
c = Client("matt", "lamam", "2022-04-27")

# comportement hérité
print(c.get_full_name())

# comportement spécifique
print(c.get_date_joint("%d/%m/%Y"))
# %%
