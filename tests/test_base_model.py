import unittest
from models.base_model import BaseModel

class Test_BaseModel(unittest.TestCase):
    """
    This is a Test for all methods in the Basemodel class
    """

    def test__init__(self):
        """
        This tests the init constructor method in the BaseModel
        """
        Bnb_model = BaseModel()
        self.assertIsNotNone(Bnb_model.id)
        self.assertIsNotNone(Bnb_model.created_at)
        self.assertIsNotNone(Bnb_model.updated_at)

    def test_save(self):
        """
        This tests the save method of the BaseModel class
        """
        Bnb_model = BaseModel()
        prior_updated_at = Bnb_model.updated_at
        neo_updated_at = Bnb_model.save()
        self.assertNotEqual(prior_updated_at, neo_updated_at)

    def test_to_dict(self):
        """
        This test the to_dict method that converts the instances into a dict
        """
        Bnb_model = BaseModel()
        my_dict = Bnb_model.to_dict()
    
        self.assertIsInstance(my_dict, dict)

        self.assertEqual(my_dict["__class__"], 'BaseModel')
        self.assertEqual(my_dict["id"], Bnb_model.id)
        self.assertEqual(my_dict["created_at"], Bnb_model.created_at.isoformat)
        self.assertEqual(my_dict["updated_at"], Bnb_model.updated_at.isoformat)

    def test__str__(self):
        """
        This tests the string method for the BaseModel class
        """
        Bnb_model = BaseModel()
        self.assertTrue(str(Bnb_model).startswith('[BaseModel]'))
        self.assertIn(Bnb_model.id, str(Bnb_model))
        self.assertIn(str(Bnb_model.__dict__), str(Bnb_model))

if __name__ == "__main":
    unittest.main()