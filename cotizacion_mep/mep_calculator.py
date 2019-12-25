import mep_api as api


class MEP_Calculator():
    def __init__(self, username, password):
        self._api = api.MEP_Api({"username": username, "password": password})

    def calculate(self, bonds_list):
        mep_value_pairs = []
        for bond in bonds_list:
            mep_value_pairs.append(self._api.get_bonds_pair(bond, bond+"D"))
        return MEP_Calculator.lowest_rate(mep_value_pairs)

    @staticmethod
    def lowest_rate(mep_value_pairs):
        mep_value_pairs.sort(cmp=lambda a, b: a.mep_value() - b.mep_value())
        return mep_value_pairs[0]
