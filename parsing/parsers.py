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