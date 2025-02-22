#!/usr/bin/python3
"""test for file storage"""
import unittest
import pep8
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    '''this will test the FileStorage'''

    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.user = User()
        cls.user.first_name = "Kev"
        cls.user.last_name = "Yo"
        cls.user.email = "1234@yahoo.com"
        cls.storage = FileStorage()

    @classmethod
    def teardown(cls):
        """at the end of the test this will tear it down"""
        del cls.user

    def tearDown(self):
        """teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_FileStorage(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_all(self):
        """tests if all works in File Storage"""
        storage = FileStorage()
        obj = storage.all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)
        self.assertIs(obj, storage._FileStorage__objects)

    def test_new(self):
        """test when new is created"""
        storage = FileStorage()
        obj = storage.all()
        user = User()
        user.id = 123455
        user.name = "Kevin"
        storage.new(user)
        key = user.__class__.__name__ + "." + str(user.id)
        self.assertIsNotNone(obj[key])

    def test_reload_filestorage(self):
        """
        tests reload
        """
        self.storage.save()
        Root = os.path.dirname(os.path.abspath("console.py"))
        path = os.path.join(Root, "file.json")
        with open(path, 'r') as f:
            lines = f.readlines()
        try:
            os.remove(path)
        except Exception:
            pass
        self.storage.save()
        with open(path, 'r') as f:
            lines2 = f.readlines()
        self.assertEqual(lines, lines2)
        try:
            os.remove(path)
        except Exception:
            pass
        with open(path, "w") as f:
            f.write("{}")
        with open(path, "r") as r:
            for line in r:
                self.assertEqual(line, "{}")
        self.assertIs(self.storage.reload(), None)


class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class"""
    if storage_t != "db":
        @unittest.skipIf(storage_t == 'db', "not testing file storage")
        def test_all_returns_dict(self):
            """Test that all returns the FileStorage.__objects attr"""
            storage = FileStorage()
            new_dict = storage.all()
            self.assertEqual(type(new_dict), dict)
            self.assertIs(new_dict, storage._FileStorage__objects)

        @unittest.skipIf(storage_t == 'db', "not testing file storage")
        def test_new(self):
            """test that new adds an object to the
            FileStorage.__objects attr"""
            storage = FileStorage()
            save = FileStorage._FileStorage__objects
            FileStorage._FileStorage__objects = {}
            test_dict = {}
            for key, value in classes.items():
                with self.subTest(key=key, value=value):
                    instance = value()
                    instance_key = "{}{}{}".format(
                        instance.__class__.__name__, ".",
                        instance.id)
                    storage.new(instance)
                    test_dict[instance_key] = instance
                    self.assertEqual(test_dict, storage._FileStorage__objects)
            FileStorage._FileStorage__objects = save


if __name__ == "__main__":
    unittest.main()
