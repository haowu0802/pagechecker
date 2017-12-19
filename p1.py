"""solution for problem 1
"""
import unittest

# inputs
input0 = [1,2,3,1,5]
input1to3 = ['a','b','c','d','e']
input4 = [11,6,10]

# correct outputs and observations
correct_output0 = [15,11,13,12,11] # input reversed by index add 10
correct_output1 = ['e','d','c','b','a'] # input reversed by index
correct_output2 = ['a','c','e'] # input filtered by even index
correct_output3 = ['b','d'] # input filtered by odd index
correct_output4 = [11,10,6,[27]] # input sorted desc append with sum to end

# transformations
def trans0(input_list):
    return map(lambda x: x + 10, reversed(input_list))
def trans1(input_list):
    return list(reversed(input_list))
def trans2(input_list):
    return input_list[::2]
def trans3(input_list):
    return input_list[1:][::2]
def trans4(input_list):
    result = sorted(input_list, reverse=True)
    result.append([sum(input_list)])
    return result

# tests
class TestP1(unittest.TestCase):
    def test_0(self):
        self.assertEqual(correct_output0, trans0(input0))
    def test_1(self):
        self.assertEqual(correct_output1, trans1(input1to3))
    def test_2(self):
        self.assertEqual(correct_output2, trans2(input1to3))
    def test_3(self):
        self.assertEqual(correct_output3, trans3(input1to3))
    def test_4(self):
        self.assertEqual(correct_output4, trans4(input4))

if __name__ == "__main__":
    unittest.main()