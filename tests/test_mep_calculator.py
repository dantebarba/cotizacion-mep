import context
import cotizacion_mep.mep_calculator as calculator
import cotizacion_mep.model.mep_value as mep
import cotizacion_mep.model.bond as bond
import unittest

class MepCalculatorTestSuite(unittest.TestCase):
    """ Test mep_value class """

    def test_mep_value_ordering(self):
        ay24 = bond.Bond("AY24", 1000)
        ay24d = bond.Bond("AY24D", 25) # 40
        ao20 = bond.Bond("AO20", 1500)
        ao20d = bond.Bond("AO20D", 30) # 50
        ac17 = bond.Bond("AC17", 2300)
        ac17d = bond.Bond("AC17D", 32) # 71
        mep1 = mep.MepValue(ay24d,ay24, "last_update")
        mep2 = mep.MepValue(ao20d, ao20, "Last update")
        mep3 = mep.MepValue(ac17d, ac17, "Last update")
        mep_calculator = calculator.MEP_Calculator.lowest_rate([mep2, mep1, mep3])
        self.assertEqual(mep_calculator.mep_value(), 40, "Mep value incorrecto: "+str(mep_calculator.mep_value()))

if __name__ == '__main__':
    unittest.main()