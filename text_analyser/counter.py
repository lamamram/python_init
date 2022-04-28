from text_analyser.cleaner import Cleaner

from text_analyser.cleaner import Cleaner
# from .cleaner import Cleaner
class Counter:
    # injection de dépendance:
    # la classe Counter utilise l'interface publique de Cleaner 
    def __init__(self, cleaner: Cleaner) -> None:
        self.__text = cleaner.clean()
    
    def get_occurences(self, min_occurence=2):
        """
        but: transformer une chaine de mots séparés par " "
        en un dictionnaire avec {"mot unique": occurence}
        trié par occurence décroissante
        rogné aux éléments ayant >= min_occurence
        """
        occurences = {}
        for word in self.__text.split():
            if word in occurences:
                occurences[word] += 1
            else:
                occurences[word] = 1
        # tri sur les occurences décroissantes
        tuples = occurences.items()
        tuples = sorted(tuples, key=lambda t: t[1], reverse=True)
        # filtrer les occurences < min_occurence
        tuples = filter(lambda t: t[1] >= min_occurence, tuples)
        return dict(tuples)
    
    