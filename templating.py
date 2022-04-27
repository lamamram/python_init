"""
module de templating
"""

_template = """
lorem ipsum (blabla) ... ((key1)) blabla ....
lorem ipsum (blabla) ... ((key2)) blabla ....
lorem ipsum (blabla) ... ((key3)) blabla ....
lorem ipsum (blabla) ... ((key4)) blabla ....
"""

def parse_tpl(tpl: str, vars: dict, *, slot: tuple=("{{", "}}"), default: str="N/A") -> str:
    """
    moteur de templating    
    """
    while tpl.count(slot[0]):
        start_index = tpl.index(slot[0]) + len(slot[0])
        end_index = tpl.index(slot[1])
        key = tpl[start_index:end_index]
        tpl = tpl.replace(
            slot[0] + key + slot[1], 
            vars.get(key, default)
        )
    return tpl

# attention, les modules importés sont exécutés
if __name__ == "__main__":
    print("coucou")