from multiprocessing import Process, Queue, cpu_count, current_process
# exception queue.Empty
import queue

def do_job(to_do: Queue, jobs_done: Queue):
    while True:
        try:
            p_name = current_process().name
            print(f"{p_name} waiting for todo...")
            # get non bloquant, déclenche l'exception => termine le worker 
            task = to_do.get_nowait()
        except queue.Empty:
            print(f'{p_name} broke !!')
            break
        else:
            # traitement
            jobs_done.put(f"{task} done by {p_name}!")



if __name__ == "__main__":
    to_do, jobs_done = Queue(), Queue()

    # 1. remplissage des jobs à effectuer
    for i in range(200):
        to_do.put(f"todo n°{i}")

    # disptaching des jobs sur les workers
    processes = [ Process(target=do_job, args=(to_do, jobs_done)) for i in range(cpu_count() - 2)]
    for p in processes: p.start()
    for p in processes: p.join(3)

    for p in processes: p.terminate()
    # map(lambda p: p.start(), processes)
    # map(lambda p: p.join(), processes)

    #3. quand tout est traité, retour des résultats
    while not jobs_done.empty():
        print(jobs_done.get())