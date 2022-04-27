# imports intermédiaires au niveau du package
## les chemins d'imports son calculés depuis le module principal
# from parsing.parsers import parse_tpl
# from parsing.templates.utils import _template

## on peut également importer avec un chemin python relatif (. et ..)
from .parsers import parse_tpl
from .templates.utils import _template
