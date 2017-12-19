"""solution for problem 3
"""
import unittest

class MyDict(object):

    def __init__(self, input_dict):
        for key, value in input_dict.items():
            setattr(self, key, value)

    def __getattr__(self, name):
        if name in self.__dict__:
            return self.name
        else:
            return None

    def items(self):
        return self.__dict__.items()

    def __add__(self, other):
        if type(other) == type(dict()) or type(other) == type(MyDict({})):
            for key, value in other.items():
                # key collision
                if key in self.__dict__:
                    # TODO: when collided values are not the same type, convert or raise exception
                    new_value = getattr(self, key) + value
                    setattr(self, key, new_value)
                else:
                    setattr(self, key, value)
        return self

# tests

class TestP3(unittest.TestCase):
    def test_can_set_get_using_dot_notation(self):
        myDict = MyDict({})
        myDict.wh = 123
        self.assertEqual(myDict.wh, 123)

    def test_can_add_with_a_dict_type_object_and_return_MyDict_object(self):
        myDict = MyDict({
            "integer": 123,
            "string" : "abc"
        })
        myDict_combine = myDict + {"object":{}}
        self.assertIsInstance(myDict_combine, MyDict)
        self.assertEqual(myDict_combine.integer, 123)
        self.assertEqual(myDict_combine.object, {})
        # collision
        myDict_combine = myDict + {"integer":1}
        myDict_combine = myDict + {"string":"xyz"}
        self.assertEqual(myDict_combine.integer, 124)
        self.assertEqual(myDict_combine.string, "abcxyz")
        
    def test_can_add_with_a_MyDict_type_object_and_return_MyDict_object(self):
        myDict = MyDict({
            "integer": 123,
            "string" : "abc"
        })
        myDict_add = MyDict({
            "integer": 1,
        })
        myDict_combine = myDict + myDict_add
        self.assertIsInstance(myDict_combine, MyDict)
        self.assertEqual(myDict_combine.integer, 124)



if __name__ == "__main__":
    unittest.main()