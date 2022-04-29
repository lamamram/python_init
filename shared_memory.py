from multiprocessing import Process, Value, Array, current_process, Lock
import re, random
from unicodedata import name
from string import ascii_lowercase

def worker(s, v, l: Lock):
    val, repl = random.randint(1, 10), random.choice(ascii_lowercase)
    print(f"process {current_process()} uses val {val} and letter {repl}")
    
    # acquire bloque tout process cherchant à exécuter le code suivant
    # tant que release n'a pas été appeler
    # l.acquire()
    # recommandé: Lock est un gestionnaire de contexte
    with l:
        s.value += val
        _str = v.value.decode('utf8')
        _str = re.sub("[aeiou]", repl, _str)
        v.value = bytes(_str, "utf8")
    # rend le code après acquire() disponible pour un autre process
    # l.release()
    # v.value = b"Bonjour"

if __name__ == "__main__":
    # valeur stockées hors de la zone de mémoire du parent
    # => segment de mem partagée
    scalar = Value("i", 10)
    vector = Array("c", bytes("bonjour", "utf8"))
    lock = Lock()
    print(f"initialisation: {scalar.value}, {vector.value.decode('utf8')}")
    p1 = Process(target=worker, args=(scalar, vector, lock), name="p1")
    p2 = Process(target=worker, args=(scalar, vector, lock), name="p2")

    p1.start();p2.start()
    p1.join();p2.join()

    print(f"mise à jour par le worker: scalar = {scalar.value}, vector = {vector.value.decode('utf8')}")