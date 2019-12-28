import requests
import model.authentication as auth
import model.bond as bond
import model.mep_value as mep_value
import datetime
import cotizacion_mep.iol_mep_strategy as iol_mep_strategy
import cotizacion_mep.mep_calculator as mep_calculator


class MEPApi():
    def __init__(self, strategy=None):
        if (strategy is None):
            raise AssertionError("No strategy was set.")
        self._strategy = strategy
        self._calculator = mep_calculator.MEPCalculator(self)

    def get_bonds(self, bonds_list):
        return self._strategy.get_bonds(bonds_list)

    def get_bonds_pair(self, ars_bond, usd_bond):
        return mep_value.MepValue(self._strategy.get_bonds([usd_bond])[0], self._strategy.get_bonds([ars_bond])[0], datetime.datetime.now())

    def calculate(self, bonds_list=[]):
        return self._calculator.calculate(bonds_list)
