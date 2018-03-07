import json


class CardSet(object):
    def __init__(self, card_set: dict):
        self._card_set = card_set

    @property
    def code(self):
        return self._card_set["code"]

    @property
    def name(self):
        return self._card_set["name"]

    def to_file(self, path):
        with open(path, 'w') as out_file:
            json.dump(self._card_set, out_file)
