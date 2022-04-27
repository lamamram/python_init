# %%
# 1. créer un package text_analyser
# 2. créer deux modules cleaner et counter 
# dans le package
# 3. dans cleaner, créer une classe Cleaner
# but: prend un texte en paramètre et retourne le texte 
# nettoyé pour analyse du contenu

# 3.1. écrire un __init__ qui prend en paramètres
# - un texte
# - une chaine de caractère contenant des signes de ponctuation
#   voir la variable punctuation du module string
# - une longueur minimale de mot pour être signifiant dans le texte

# 3.2 écrire 4 petites méthodes privées pour => regex
# - nettoyer le texte de la ponxtuation
# - nettoyer le texte des sauts de lignes (windows et linux)
# - nettoyer les suites de 2+ espaces
# - nettoyer les mots de longueur inférieure au paramètre correspondant

# 3.3 écrire une méthode publique qui appelle successivement les 
# 4 méthodes privées et retourne le texte nettoyé en minuscules

# 4. écrire une classe Counter dans le module counter
# - le module counter import la classe Cleaner du module Counter

# 4.1 Counter prend en paramètre: __init__ 
# - le texte
# - la chaine de ponctuation et le minimum signifiant
# - l'attribut text du Counter doit être nettoyé dès l'initialisation

# 4.2 écrire une méthode publique get_occurences
# - en paramètre: le nombre de mots qu'on veut afficher
# - renvoie un dictionnaire des mots du texte en clé avec leur occurence dans le texte
# - en valeur, triés par ordre décroissants
from text_analyser.cleaner import Cleaner

text = """
Python (prononcé /pi.tɔ̃/) est un langage de programmation interprété, multi-paradigme et multiplateformes. Il favorise la programmation impérative structurée, fonctionnelle et orientée objet. Il est doté d'un typage dynamique fort, d'une gestion automatique de la mémoire par ramasse-miettes et d'un système de gestion d'exceptions ; il est ainsi similaire à Perl, Ruby, Scheme, Smalltalk et Tcl.

Le langage Python est placé sous une licence libre proche de la licence BSD4 et fonctionne sur la plupart des plates-formes informatiques, des smartphones aux ordinateurs centraux, de Windows à Unix avec notamment GNU/Linux en passant par macOS, ou encore Android, iOS, et peut aussi être traduit en Java ou .NET. Il est conçu pour optimiser la productivité des programmeurs en offrant des outils de haut niveau et une syntaxe simple à utiliser.

Il est également apprécié par certains pédagogues qui y trouvent un langage où la syntaxe, clairement séparée des mécanismes de bas niveau, permet une initiation aisée aux concepts de base de la programmation.
"""

if __name__ == "__main__":
    cl = Cleaner(text)
    print(cl.clean())
# %%

# %%
