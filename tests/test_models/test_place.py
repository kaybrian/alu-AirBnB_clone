#!/usr/bin/python3
"""
Module documentation
"""

import unittest
from models.base_model import BaseModel
from model.Place import Place
from models.city import City
from models.user import User


class TestPlace(BaseModel):
    """ Test Place Class """

    def test_isntance(self):
        """ Test instance """
        p = Place()
        self.assertIsInstance(p, Place)

    def test_is_subclass(self):
        """test the instance of sub classes"""
        p = Place()
        self.assertTrue(issubclass(type(p), BaseModel))

    def test_attrs(self):
        """test attributes"""
        city = City()
        user = User()
        place = Place()
        place.user_id = user.id
        place.city_id = city.id
        self.assertIsNotNone(place.id)
        self.assertEqual(place.user_id, user.id)
        self.assertEqual(place.city_id, city.id)
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0)
        self.assertEqual(place.longitude, 0)
        self.assertEqual(place.amenity_ids, [])


if __name__ == "__main__":
    unittest.main()
