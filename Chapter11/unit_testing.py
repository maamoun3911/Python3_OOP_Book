# import unittest

# import unittest
# def average(seq):
#     return sum(seq) / len(seq)

# class TestAverage(unittest.TestCase):
#     def test_python30_zero(self):
#         self.assertRaises(ZeroDivisionError, average, [])
        
#     def test_python31_zero(self):
#         with self.assertRaises(ZeroDivisionError):
#             average([])

# unittest.main()

# Reducing boilerplate and cleaning up
import unittest
import sys
from statelist import StateList


class InputTest(unittest.TestCase):
    def setUp(self) -> None:
        self.f_situation = StateList(range(10))
        self.f_situation.append(1)
        self.s_situation = StateList()
        self.t_situation = StateList("Maamoun")
    
    def test_mean(self):
        
        value = self.f_situation.mean()
        self.assertEqual(value, 23)
        
        value2 = self.s_situation.mean()
        self.assertTrue(0.0 == value2)

    
    def test_median(self):
        
        self.f_situation.append(10)
        self.assertEqual(6, self.f_situation.median())
        
        self.assertTrue(0 == self.s_situation.median())
        
        self.assertEqual(3, self.t_situation.median())
        
        
    @unittest.skipUnless(sys.platform.startswith("linux"), "just experting decorater")
    def test_mode(self):
        
        value1 = self.f_situation.mode()
        self.assertEqual([1], value1)
        
        value3 = self.t_situation.mode()
        self.assertEqual(["a"], value3)
        
    @unittest.expectedFailure
    def test_mode_value_2(self):
        value2 = self.s_situation.mode()
        self.assertRaises(ValueError, self.s_situation.mode())
    
    @unittest.skip("Until study self.assertRaises")
    def test_mean_value3(self):
        self.assertRaises(TypeError, self.t_situation.mean())
    
