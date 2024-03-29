#!/usr/bin/python3
"""Unittests for city.py"""

import unittest
from datetime import datetime

from models.city import City


class TestCity_instantiation(unittest.TestCase):
    """Tests for instantiation"""

    def test_id(self):
        """Test id values"""
        c1 = City()
        c2 = City()

        self.assertIsInstance(c1, City)
        self.assertTrue(hasattr(c1, "id"))
        self.assertNotEqual(c1.id, c2.id)
        self.assertIsInstance(c1.id, str)

    def test_created_at(self):
        """Tests created_at method"""
        c1 = City()

        self.assertIsInstance(c1, City)
        self.assertTrue(hasattr(c1, "created_at"))
        self.assertIsInstance(c1.created_at, datetime)

    def test_updated_at(self):
        """Tests updated_at attribute"""
        c1 = City()

        self.assertIsInstance(c1, City)
        self.assertTrue(hasattr(c1, "updated_at"))
        self.assertIsInstance(c1.created_at, datetime)

    def test_state_id(self):
        """Test the state id of the state"""
        c1 = City()

        self.assertIsInstance(c1, City)
        self.assertTrue(hasattr(c1, "state_id"))

    def test_name(self):
        """Tests name attribute"""
        c1 = City()

        self.assertIsInstance(c1, City)
        self.assertTrue(hasattr(c1, "name"))
        self.assertIsInstance(c1.name, str)
        self.assertEqual(c1.name, "")

        c1.name = "Nairobi"

        self.assertEqual(c1.name, "Nairobi")


class TestCity_to_dict(unittest.TestCase):
    """Test to_dict() method in Parent class"""

    def check_values(self):
        """Check the value in the dict"""
        c1 = City()

        my_list = [
            "id",
            "__class__",
            "updated_at",
            "created_at",
            "name",
        ]

        my_dict = c1.to_dict()

        for key in my_list:
            if key in {"updated_at", "created_at"}:
                value = my_dict[key]
                self.assertIsInstance(value, str)
            self.assertIn(key, my_dict)


if __name__ == "__main__":
    unittest.main()
