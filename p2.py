"""solution for problem 2
"""
import unittest
from timeit import timeit
from time import sleep, time

def get_function_log(func):
    def wrapper(*args, **kwargs):
        time_start = time()
        result = func(*args, **kwargs)
        time_elapsed = time() - time_start
        func_name = func.__name__
        func_args = list(args)
        return result, "Function Name: %s; Arguments: %s; Time taken for function to return: %s ;" % (func_name, func_args, time_elapsed)
    return wrapper

@get_function_log
def complex_function(argument_x, argument_y=0):
    _ = "%s%s" % (str(argument_x), str(argument_y))
    sleep(3)

# tests
class TestP2(unittest.TestCase):
    def test_function_meta(self):
        _, log = complex_function("dog", 100)
        #print log # for debug and show case
        self.assertIn("Function Name", log)
        self.assertIn("Arguments", log)
        self.assertIn("Time taken", log)


if __name__ == "__main__":
    unittest.main()