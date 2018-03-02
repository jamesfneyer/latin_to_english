import json


def parse_dict():
    with open('utils/latin-to-english.json') as fh:
        return json.load(fh)

DICT_LIST = parse_dict()

CODES = {
    'latin_to_english': {c['latin'].lower(): c['english'] for c in DICT_LIST},
    'english_to_latin': {c['english'].lower(): c['latin'] for c in DICT_LIST},
}