!pip install conllu
!pip install pyconll

import conllu, pyconll, io
from conllu import parse_incr

from io import open
import requests

path = 'https://raw.githubusercontent.com/aleksandertomazdesouza/add_corpus_snl/main/add_corpus.conllu'

r = requests.get(path, allow_redirects=True)
open('conll_', 'wb').write(r.content)

bl = pyconll.load_from_file('conll_')
