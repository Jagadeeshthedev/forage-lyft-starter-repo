import unittest

from tires.carrigan_tires import CarriganTires


class TestCarriganTires(unittest.TestCase):
    def test_needs_service_true(self):
        tire_wear = [0, 0.3, 0.5, 0.9]
        tires = CarriganTires(tire_wear)
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        tire_wear = [0, 0.3, 0.5, 0.1]
        tires = CarriganTires(tire_wear)
        self.assertFalse(tires.needs_service())