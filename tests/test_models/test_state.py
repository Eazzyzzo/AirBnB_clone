#!/usr/bin/python3
"""
Module for State unittest
"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """
    Test case class for the State class.
    """
    def test_instance_creation(self):
        """
        Test the initialization of the State instance.
        """
        state = State()
        self.assertIsInstance(state, State)
        self.assertEqual(state.name, "")


if __name__ == '__main__':
    unittest.main()
