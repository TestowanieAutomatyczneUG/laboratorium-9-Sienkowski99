import unittest
from src.car import Car
from unittest.mock import *


class CarTest(unittest.TestCase):

    def test_needsFuel_true(self):
        car = Car()
        car.needsFuel = Mock(name='needsFuel')
        car.needsFuel.return_value = True

        self.assertEqual(car.needsFuel(), True)

    def test_needsFuel_false(self):
        car = Car()
        car.needsFuel = Mock(name='needsFuel')
        car.needsFuel.return_value = False

        self.assertEqual(car.needsFuel(), False)

    def test_getEngineTemperature(self):
        car = Car()
        car.getEngineTemperature = Mock(name='getEngineTemperature')
        car.getEngineTemperature.return_value = 69

        self.assertEqual(car.getEngineTemperature(), 69)

    def test_driveTo(self):
        car = Car()
        car.driveTo = Mock(name='driveTo')
        car.driveTo.return_value = 'Rotmanka'

        self.assertEqual(car.driveTo('Rotmanka'), 'dawaj dawaj dawaj')

if __name__ == '__main__':
    unittest.main()
