import unittest
from models.base_model import BaseModel
import time
class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel ."""

    def test_instance(self):
        """test instance."""
        base = BaseModel()
        self.assertIsInstance(base, BaseModel)

    def test_is_class(self):
        """test instance."""
        base = BaseModel()
        self.assertEqual(str(type(base)),
                         "<class 'models.base_model.BaseModel'>")

    def test_save(self):
        """test save."""
        base = BaseModel()
        time.sleep(1)
        base.save()
        self.assertNotEqual(base.updated_at, base.created_at)
        self.assertTrue(base.updated_at > base.created_at)


if __name__ == "__main__":
    unittest.main()
