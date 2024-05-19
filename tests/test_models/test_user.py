#!/usr/bin/python3
"""
Module for User unittest
"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """
    Test case class for the User class.
    """
    def test_instance_creation(self):
        """
        Test the initialization of the User instance.
        """
        user = User()
        self.assertIsInstance(user, User)
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")


if __name__ == '__main__':
    unittest.main()
