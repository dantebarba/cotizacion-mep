import cotizacion_mep.mongodb_mep_strategy as mongodb_mep_strategy

class MEPCalculator():
    def __init__(self, api):
        self._api = api

    def calculate(self, bonds_list):
        mep_value_pairs = []
        for bond in bonds_list:
            mep_value_pairs.append(self._api.get_bonds_pair(bond, bond+"D"))
        return MEPCalculator.lowest_rate(mep_value_pairs)

    @staticmethod
    def lowest_rate(mep_value_pairs):
        mep_value_pairs.sort(cmp=lambda a, b: int(a.mep_value()*1000 - b.mep_value()*1000))
        return mep_value_pairs
