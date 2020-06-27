import json
from pathlib import Path

strings = {}
langs = ['en', 'fr']

for lang in langs:
    path = Path(__file__).parent.parent.joinpath('text', f'{lang}.json')
    with open(path, 'r', encoding='utf-8') as file:
        strings[lang] = json.load(file)

def get_text(key, lang='en'):
    return strings[lang][key]

def get_all_text(key):
    return [ strings[s][key] for s in langs ]