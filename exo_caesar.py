# %%
# 1. créer un package crypto
# 2. créer un module caesar

# 3. créer une fonction generate_key 
# qui opère une permutation sur les 26 
# lettres de l'alphabet en minuscules
# => qui renvoie une string de longueur 26
# avec les 26 lettres en désordre
# avec toutes les lettres permutées "abcd...xyz" => "dfgn...vba"
# pas "adcfe...vwz"
# hint: étudier les fonctions choice ou shuffle de random
# hint2: utiliser la variable ascii_lowercase du module standard string

# 4. écrire deux fonctions de chiffrement et déchiffrage pour
# échanger des messages => crypt et uncrypt

# hint: fonctions ord() et chr()
# ex.
# print(ord("a") - 97, ord("z") -97)
# print(chr(97), chr(122))

from crypto.caesar import *

if __name__ == "__main__":
    # for _ in range(100):
    key = generate_key()
    # print(key)
    msg = "alattaque"
    crypted = crypt(msg, key)
    clean_msg = uncrypt(crypted, key)
    print(clean_msg)
# %%

# %%
