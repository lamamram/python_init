# %%
from abc import ABC, abstractmethod
from string import punctuation
import re

class AbstractCleaner(ABC):
    @abstractmethod
    def __init__(self, text, *args, **kwargs) -> None:
        pass
    
    @abstractmethod
    def clean(self):
        pass


class Cleaner(AbstractCleaner):
    def __init__(self, text, punc=punctuation, min_word=4) -> None:
        self.__text = text
        self.__punc = punc
        self.__min_word = min_word

    def __clean_punc(self):
        self.__text = re.sub(f"[{self.__punc}]", " ", self.__text)

    def __clean_crlf(self):
        self.__text = re.sub("\\r?\\n", " ", self.__text)

    def __clean_spaces(self):
        self.__text = re.sub(" +", " ", self.__text)

    def __clean_words(self):
        words = self.__text.split()
        # filtered_words = []
        # for word in words:
        #     if len(word) >= self.__min_word:
        #         filtered_words.append()
        # self.__text = " ".join(filtered_words)

        # self.__text = " ".join(
        #     [ word for word in words if len(word) >= self.__min_word ]
        # )

        self.__text = " ".join(filter(lambda w: len(w) >= self.__min_word, words))

    # def clean(self):
    #     self.__clean_punc()
    #     self.__clean_crlf()
    #     self.__clean_spaces()
    #     self.__clean_words()
    #     return self.__text.lower()


if __name__ == "__main__":
    # classe abstraite (ABC) => non instancialble
    # abs = AbstractCleaner()
    # classe fille d'une classe abstratie
    # @abstractmethod
    # doit implémenter les méthodes de la classe
    # abstraite
    # cl = Cleaner("blabla")
    pass
# %%
# print(punctuation)
# %%
