#!/usr/bin/python3
"""
Module documentation
"""

from models.base_model import BaseModel
from models.review import Review
import unittest


class TestReview(unittest):
    """ Test the Review Class """

    def test_isinstance(self):
        """ Test if user is an instance of BaseModel """
        review = Review()
        self.assertIsInstance(review, Review)

    def test_is_subclass(self):
        """test the instance of sub classes"""
        review = Review()
        self.assertTrue(issubclass(type(review), BaseModel))

    def test_text(self):
        """test text"""
        review = Review()
        self.assertIsNotNone(review.id)
        self.assertEqual(review.text, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.place_id, "")


if __name__ == "__main__":
    unittest.main()
