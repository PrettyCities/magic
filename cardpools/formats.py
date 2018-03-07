from cardpools.cardpool import CardPool


class Standard(CardPool):
    @classmethod
    def sets(cls):
        # TODO: Replace with dynamic retrieval
        return [
            "Aether Revolt", "Kaladesh",
            "Welcome Deck 2017",
            "Amonkhet", "Hour of Devastation",
            "Ixalan", "Rivals of Ixalan",
        ]

    @classmethod
    def projection(cls):
        return {
            "$match": {
                "name": {"$in": Standard.sets()}
            }
        }
