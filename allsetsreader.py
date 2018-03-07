import json


class AllSetsReader(object):
    @classmethod
    def read(cls, file_path):
        with open(file_path) as all_sets_json_path:
            return json.load(all_sets_json_path)

    @classmethod
    def split_sets(cls, all_sets_json):
        for card_set in all_sets_json.keys():
            yield all_sets_json[card_set]