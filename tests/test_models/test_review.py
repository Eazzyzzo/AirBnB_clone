#!/usr/bin/python3
"""
Module for Review unittest
"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """
    Test case class for the Review class.
    """
    def test_instance_creation(self):
        """
        Test the initialization of the Review instance.
        """
        review = Review()
        self.assertIsInstance(review, Review)
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")


if __name__ == '__main__':
    unittest.main()
