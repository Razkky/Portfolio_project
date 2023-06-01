#!/usr/bin/python3
"""This module runs a unittest on BaseModel"""
from models.base import BaseModel
import unittest
from datetime import datetime
from uuid import uuid4

class TestBaseModel_Instance(unittest.TestCase):
    """Test instances of BaseModel"""

    def test_type_model(self):
        """Test for the type of the model"""
        print("Running test")
        self.assertEqual(BaseModel, type(BaseModel()))
    
    def test_type_id(self):
        """Test for the type of id"""
        self.assertEqual(str, type(BaseModel().id))

    def test_type_created_at(self):
        """Test for the type of created_at"""
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_type_updated_at(self):
        """Test for the type of updated_at"""
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_unique_id(self):
        """Test id of every model is unique"""
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model1.id, model2.id)

    def test_updated_at_less_created_at(self):
        """Test updated_at always less than created_at"""
        model1 = BaseModel()
        self.assertLess(model1.created_at, model1.updated_at)
    
    def test_dict_as_argument(self):
        """Test passing dict as an argument"""
        model1 = BaseModel()
        model = model1.to_dict()
        model2 = BaseModel(**model)
        self.assertEqual(model1.id, model2.id)


if __name__ == "__main__":
    unittest.main()
