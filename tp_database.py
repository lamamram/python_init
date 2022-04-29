# %%

import pandas as pd

uri = "http://www.afnic.fr/wp-media/ftp/documentsOpenData/202105_OPENDATA_A-NomsDeDomaineEnPointFr.zip"

dns_df = pd.read_csv(
    uri, 
    sep=";", 
    compression="zip", 
    encoding="iso-8859-1", 
    nrows=1000000)


# %%
# filtre sur DataFrame
# sub_set = dns_df.loc[ dns_df["Pays BE"] == "DE", ["Nom de domaine", "Pays BE"]]
sub_set = dns_df[["Nom de domaine", "Pays BE"]]
# %%
sub_set

# %%
# création base sqlite3
import sqlite3

# 1 connexion
with sqlite3.connect("dns.db") as conn:
    # 2. cursor
    # type de curseur
    # tuple par défaut, dict si Row
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    # 3. exécution d'une requête
    cur.execute("select sqlite_version() as version")
    # 4. récup data
    row = cur.fetchone()
    print(dict(row))
# 5. conn.close() est appelé en sortant du bloc with


# %%
import sqlite3

DB_NAME = "dns.db"

def execute_script(path, conn):
    with open(path, "r", encoding="utf8") as sql_f:
        script = sql_f.read()
    with conn:
        cur = conn.cursor()
        # executescript peut exécuter plusieurs requêtes
        # séparées par ";"
        try:
            cur.executescript(script)
            return "OK"
            return f"last id generated: {cur.lastrowid}"
            return f"{cur.rowcount} rows inserted."
        except sqlite3.OperationalError as oe:
            return oe

def insert_dns(rows, conn):
    """
    :param rows: liste de valeurs à insérer
    """
    # requête préparée
    insert_query = "insert into domain_name (name, iso2) values (?, ?)"
    with conn:
        cur = conn.cursor()
        cur.executemany(insert_query, rows)
        return f"{cur.rowcount} rows inserted."


if __name__ == "__main__":
    db = sqlite3.connect(DB_NAME)
    ret = execute_script("domain_names_sqlite3.sql", db)
    print(ret)
    
    # vérification du nombre de lignes insérées dans la table pays
    with db:
        cur = conn.cursor()
        cur.execute("select count(1) from pays")
        print(cur.fetchone()[0])
    
    # slicing sur les lignes du df  + conversion
    # des données en liste de listes
    # batch = sub_set.loc[:1000].values.tolist()
    batch = sub_set.values.tolist()
    ret = insert_dns(batch, db)
    print(ret)
    

# %%
