import cotizacion_mep.mongodb_mep_strategy as mongodb_mep_strategy


class MEPCalculator():
    def __init__(self, api):
        self._api = api

    def calculate(self, bonds_list, min_volume=1, min_operations=1, min_volume_usd=1, min_operations_usd=1):
        mep_value_pairs = []
        for bond in bonds_list:
            mep_value_pairs.append(self._api.get_bonds_pair(bond, bond+"D"))
        return MEPCalculator.filter_volume(MEPCalculator.lowest_rate(mep_value_pairs), min_volume, min_operations, min_volume_usd, min_operations_usd)

    @staticmethod
    def filter_volume(mep_value_pairs, min_volume=1, min_operations=1, min_volume_usd=1, min_operations_usd=1):
        return list(filter(lambda mep_value: (mep_value.bond_ars().volume > min_volume and mep_value.bond_usd().volume > min_volume_usd and mep_value.bond_ars().cantidad_operaciones > min_operations and mep_value.bond_usd().cantidad_operaciones > min_operations_usd), mep_value_pairs))

    @staticmethod
    def lowest_rate(mep_value_pairs):
        mep_value_pairs.sort(cmp=lambda a, b: int(
            a.mep_value()*1000 - b.mep_value()*1000))
        return mep_value_pairs
