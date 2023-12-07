#!/usr/bin/python3
"""Test case for FileStorage"""

import models
from models.base_model import BaseModel
import unittest


class TestFileStorageMethods(unittest.TestCase):
    """Tests FileStorage methods"""
    def test_all(self):
        """Tests all() method"""
        a = BaseModel()
        self.assertTrue(a in models.storage.all().values())
