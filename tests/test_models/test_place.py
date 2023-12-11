#!/usr/bin/python3
"""Test case for Place"""

from models.place import Place
import unittest


class TestBaseInit(unittest.TestCase):
    """Class to test for BaseModel init method"""
    def test_created_at(self):
        a = Place()
        b = a.created_at
        c = a.updated_at
        self.assertEqual(b, c)

    def test_kwargs(self):
        dic = {'id': 'a409d045-7f54-48cc-afa8-d8116bb1cc4e',
               'created_at': '2023-12-04T20:47:44.504181',
               'updated_at': '2023-12-04T20:47:44.504183',
               'name': 'First_Model', 'my_number': 9, '__class__': 'BaseModel'}
        a = Place(**dic)
        self.assertEqual(dic['id'], a.id)
        self.assertEqual(dic['created_at'], a.created_at.isoformat())
        self.assertNotEqual(a.__dict__, a.to_dict())


class TestSave(unittest.TestCase):
    """Class to test for save() method"""
    def test_save(self):
        a = Place()
        old = a.updated_at
        a.save()
        new = a.updated_at
        self.assertNotEqual(old, new)


class TestToDict(unittest.TestCase):
    """Class to test for to_dict() method"""
    def test_to_dict(self):
        a = Place()
        dic = a.to_dict()
        self.assertNotEqual(a.__dict__, dic)


if __name__ == "__main__":
    # if it is run directly
    unittest.main()
