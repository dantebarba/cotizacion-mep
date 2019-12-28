import cotizacion_mep.mep_api_strategy as strategy
import cotizacion_mep.model.bond as bond
import pymongo


class MongodbMepStrategy(strategy.MEPApiStrategy):

    def __init__(self, url="mongodb://mongodb:27017/"):
        self._db = pymongo.MongoClient(url)["mep_bonds"]

    def get_bonds(self, bond_list):
        bond_list = self._db["bonds"].find({"code": {"$in": bond_list}})
        bonds = []
        for db_bond in bond_list:
            bonds.append(bond.Bond(
                db_bond["code"], db_bond["price"], db_bond["currency"], db_bond["last_update"]))
        return bonds

    def drop(self):
        self._db["bonds"].drop()

    def persist_bonds(self, bond_list):
        for abond in bond_list:
            self._db["bonds"].insert_one(abond.__dict__)