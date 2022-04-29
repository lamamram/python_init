from multiprocessing import Process, Pool, cpu_count, current_process

def do_job(task):
    # la valeur de retour est rendue au processus parent
    # soit telle quelle (synchrone), soit dans un objet AsyncResult ou MapResult
    return f"{task} done by {current_process().name}"

if __name__ == "__main__":
    with Pool(processes=cpu_count() - 2) as pool:
        # 1 appel synchrone 
        first_call = pool.apply(do_job, args=("task n°1",))
        print(first_call)
        # 5 appels synchrones, pour un job possédant un seul paramètre
        five_calls = pool.map(do_job, [f"task n°{i}" for i in range(2, 7)])
        print(five_calls)

        # pour dispatcher des appels au workers possédants plus d'un paramètre
        # pool.starmap()
        
        # # appels asynchrones
        async_call = pool.apply_async(do_job, args=("task n°8",))
        async_map = pool.map_async(do_job, [f"task n°{i}" for i in range(9, 19)])
        # async_map = pool.map_async(do_job, [f"task n°{i}" for i in range(200)])
        
        # close => la pool n'accepte plus aucun call
        # nécessaire avant join
        pool.close() 
        pool.join()
        
        print(async_call.get(), async_map.get())
        # print(async_map.get())