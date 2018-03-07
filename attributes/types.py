from typing import TypeVar
from cardpools.cardpool import CardPool
from cardpools.formats import Standard

GenericCardPool = TypeVar("GenericCardPool", CardPool, Standard)