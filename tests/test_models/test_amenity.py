#!/usr/bin/python3
"""
Module for Amenity unittest
"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    Test case class for the Amenity class.
    """
    def test_instance_creation(self):
        """
        Test the initialization of the Amenity instance.
        """
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertEqual(amenity.name, "")


if __name__ == '__main__':
    unittest.main()
