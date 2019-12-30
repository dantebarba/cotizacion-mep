import context
import cotizacion_mep.mep_calculator as calculator
import cotizacion_mep.model.mep_value as mep
import cotizacion_mep.model.bond as bond
import unittest


class MepCalculatorTestSuite(unittest.TestCase):
    """ Test mep_value class """

    def test_mep_value_ordering(self):
        ay24 = bond.Bond("AY24", 1000)
        ay24d = bond.Bond("AY24D", 25)  # 40
        ao20 = bond.Bond("AO20", 1500)
        ao20d = bond.Bond("AO20D", 30)  # 50
        ac17 = bond.Bond("AC17", 2300)
        ac17d = bond.Bond("AC17D", 32)  # 71
        mep1 = mep.MepValue(ay24d, ay24, "last_update")
        mep2 = mep.MepValue(ao20d, ao20, "Last update")
        mep3 = mep.MepValue(ac17d, ac17, "Last update")
        calculated_bonds = calculator.MEPCalculator.lowest_rate(
            [mep2, mep1, mep3])
        self.assertTrue(calculated_bonds, "La lista no puede ser vacia")
        self.assertEqual(calculated_bonds[0].mep_value(
        ), 40, "Mep value incorrecto: "+str(calculated_bonds[0].mep_value()))

    def test_filter_volume(self):
        ay24 = bond.Bond("AY24", 1000, 'ARS', 25, 25)
        ay24d = bond.Bond("AY24D", 25, 'USD', 25, 25)  # 40
        ao20 = bond.Bond("AO20", 100, 'ARS', 0, 0)
        ao20d = bond.Bond("AO20D", 30, 'USD', 1, 1)
        ac17 = bond.Bond("AC17", 2300, 'ARS', 100, 100)
        ac17d = bond.Bond("AC17D", 32, 'USD', 10000, 10000)  # 71
        mep1 = mep.MepValue(ay24d, ay24, "last_update")
        mep2 = mep.MepValue(ao20d, ao20, "Last update")
        mep3 = mep.MepValue(ac17d, ac17, "Last update")
        calculated_bonds = calculator.MEPCalculator.lowest_rate(
            [mep2, mep1, mep3])
        filtered = calculator.MEPCalculator.filter_volume(
            calculated_bonds, min_volume=1, min_operations=1, min_volume_usd=1, min_operations_usd=1)

        self.assertEqual(filtered[0].mep_value(
        ), 40, "Mep value incorrecto: "+str(filtered[0].mep_value()))

        new_filter = calculator.MEPCalculator.filter_volume(
            filtered, min_volume=25, min_operations=25, min_volume_usd=25, min_operations_usd=25)

        self.assertEqual(new_filter[0].mep_value(
        ), 71, "Mep value incorrecto: "+str(new_filter[0].mep_value()))


if __name__ == '__main__':
    unittest.main()
