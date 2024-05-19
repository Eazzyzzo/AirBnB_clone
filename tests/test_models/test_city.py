#!/usr/bin/python3
"""
Module for City unittest
"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """
    Test case class for the City class.
    """
    def test_instance_creation(self):
        """
        Test the initialization of the City instance.
        """
        city = City()
        self.assertIsInstance(city, City)
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")


if __name__ == '__main__':
    unittest.main()
