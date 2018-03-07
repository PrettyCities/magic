from typing import List
from typing import Generic

from pymongo import MongoClient
from pymongo.collection import Collection

from attributes.attribute import Attribute
from attributes.types import GenericCardPool
from settings import MONGO_HOST


class DeckBuilder(object):
    @classmethod
    def build(cls, card_pool: Generic[GenericCardPool], attribute_group: List[List[Attribute]]):
        client = MongoClient(MONGO_HOST)
        db = client.magic
        sets_collection: Collection = db.sets

        pipeline = [
            attribute.projection
            for attributes in attribute_group
            for attribute in attributes
        ]

        pipeline.insert(0, card_pool.projection())

        return sets_collection.aggregate(pipeline)
