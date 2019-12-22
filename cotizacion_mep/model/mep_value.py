import json

class MepValue():

    def __init__(self, bond_usd, bond_ars, last_update):
        self._bond_usd = bond_usd
        self._bond_ars = bond_ars
        self._last_update = last_update

    def bond_usd(self):
        return self._bond_usd

    def bond_ars(self):
        return self._bond_ars

    def mep_value(self):
        return self.bond_ars().price / self.bond_usd().price

    def last_update(self):
        return self._last_update

    def to_json(self):
        return json.dumps({"mep_value": self.mep_value(),
                "bond_usd": self.bond_usd().to_json(),
                "bond_ars": self.bond_ars().to_json(),
                "last_update": self.last_update().isoformat()})
