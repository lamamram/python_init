from multiprocessing import Process, Manager

def worker(d, li, lo):
    with lo:
        d["k"] = "v"
        li.reverse()

if __name__ == "__main__":
    with Manager() as mgr:
        # utilisation des types et classes redéfinies par le manager
        dico = mgr.dict()
        liste = mgr.list(range(10))
        lock = mgr.Lock()

        p = Process(target=worker, args=(dico, liste, lock))
        p.start()
        p.join()
        print(dico, liste)