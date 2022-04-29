# %%
import requests

# exemple de gestion de requête get
# analyse du status_code
# gestion du header Content-Type et adaption du corps de la réponse
# gestion des evts réseaux et despbs de connexion

try:
    response = requests.get("http://google.fr")
    if 200 <= response.status_code < 300:
        ct = response.headers["Content-Type"]
        if "text/html" in ct:
            print(response.text.encode(response.encoding))
        elif "json" in ct:
            print(response.json())
        else: print(response)
    else:
        raise ValueError(f"{response.status_code}: {response.text}")
except (
    requests.HTTPError, 
    requests.ConnectionError, 
    requests.exceptions.MissingSchema,
    ValueError) as e:
    print(e, type(e))
# %%
from time import time
from concurrent.futures import ThreadPoolExecutor as TPE
from multiprocessing import cpu_count

API_URL = "https://gorest.co.in/public/v2/"
TOKEN = "f272e67cd0429faafae6fba2a892b9464b60fe6fe03621db530f667a62f86cd2"

def api_call(*, url, method, data={}, headers={}, files={}):
    try:
        call_fn = getattr(requests, method.lower())
        if method in ("POST", "PUT", "DELETE", "PATCH"):
            headers["Authorization"] = f"Bearer {TOKEN}"
        response = call_fn(url, data=data, headers=headers, files=files)
        if 200 <= response.status_code < 300:
            ret = {"valid": True, "response": None}
            ct = response.headers["Content-Type"]
            if "text/html" in ct:
                ret["response"] = response.text.encode(response.encoding) 
            elif "json" in ct:
                ret["response"] = response.json()
            return ret
        else:
            raise ValueError(f"{response.status_code}: {response.text}")
    except (
        requests.HTTPError, 
        requests.ConnectionError, 
        requests.exceptions.MissingSchema,
        ValueError) as e:
            ret = {"valid": False, "response": e}

def get_page(page_id):
    print(f"page {page_id} fetched")
    return api_call(url=f"{API_URL}users?page={page_id}", method="GET")

def get_all_users():
    users = []
    for i in range(1, 11):
        r = get_page(i)
        if r["valid"]:
            users += r["response"]
        print(f"page {i} fetched")
    return users

def get_all_users_multithreading(nb_workers=cpu_count()//2):
    users = []
    with TPE(max_workers=nb_workers) as pool:
        # map répartit 100 appels multithreadés à get_page
        # avec 100 valeurs de pages différents, sur 6 threads
        # map est synchrone (map_async pour de l'asynchrone)
        responses = pool.map(get_page, list(range(1, 101)))
        for r in responses:
            if r["valid"]:
                users += r["response"]
        return users

def create_user(user):
    return api_call(url=f"{API_URL}users", method="POST", data=user)




if __name__ == "__main__":
    start = time()
    # users = get_all_users()
    # users = get_all_users_multithreading()
    # print(f"{len(users)} users in {time() - start}s")
    test_user = {
        "name":"matt LAMAM2",
        "email":"mlamam2@example.com",
        "gender":"male",
        "status":"inactive"
    }
    print(create_user(test_user))

# %%
# getattr() et setattr()
class Truc:
    pass

t = Truc()

setattr(t, "name", "toto")
print(t.name)
print(getattr(t, 'name'))
# %%
