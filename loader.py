import json

from pymongo import MongoClient

from allsetsreader import AllSetsReader
from cardset import CardSet
from settings import ALL_SETS_JSON_PATH
from settings import SETS_DIRECTORY
from settings import MONGO_HOST

def import_set(set_json_path, collection):
    with open(set_json_path) as json_file:
        json_data = json.loads(json_file.read())
        collection.insert_one(json_data)


def make_files():
    all_sets_json = AllSetsReader.read(ALL_SETS_JSON_PATH)

    for card_set_dict in AllSetsReader.split_sets(all_sets_json):
        card_set = CardSet(card_set_dict)

        path = "{sets_directory}/{set_name}.json".format(
            sets_directory=SETS_DIRECTORY, set_name=''.join([char for char in card_set.name if char.isalnum()])
        )

        card_set.to_file(path)

        yield path


def main():
    client = MongoClient(MONGO_HOST)
    db = client.magic
    sets_collection = db.sets

    for path in make_files():
        import_set(path, sets_collection)


if __name__ == "__main__":
    main()
