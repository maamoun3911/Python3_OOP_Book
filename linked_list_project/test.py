import unittest
from chapter7_project_llist import LinkedList

class TestDelete(unittest.TestCase):
    def setUp(self) -> None:
        self.object1 = LinkedList([1, 2, 3])
    
    def test_from_begging(self):
        self.object1.delete(1)
        length = len(self.object1)
        index1 = self.object1.index(2)
        element = self.object1.get_element(1)
        
        self.assertEqual(length, 2)
        self.assertEqual(index1, 0)
        self.assertEqual(element, 3)
    
    def test_from_midlle(self):
        self.object1.delete(2)
        length = len(self.object1)
        value = self.object1.get_element(1)
        self.object1.set_element(1, 2)
        set1 = self.object1.get_element(1)
        
        self.assertEqual(2, length)
        self.assertEqual(value, 3)
        self.assertEqual(2, set1)
    
    def test_from_end(self):
        self.object1.delete(3)
        
        length = len(self.object1)
        self.assertEqual(2, length)
        
        index1 = self.object1.get_element(0)
        self.assertEqual(index1, 1)
        
        index2 = self.object1.get_element(1)
        self.assertEqual(index2, 2)


class TestPopping(unittest.TestCase):
    
    def setUp(self) -> None:
        self.llist = LinkedList([1, 2, 3])
    
    def test_default_pop(self):
        self.llist.pop()
        
        length = len(self.llist)
        self.assertEqual(length, 2)
        
        index1 = self.llist.get_element(1)
        self.assertEqual(index1, 2)
        
        index2 = self.llist.get_element(0)
        self.assertEqual(index2, 1)
    
    def test_pop_last(self):
        self.llist.pop(-1)
        
        length = len(self.llist)
        self.assertEqual(length, 2)
        
        index1 = self.llist.get_element(1)
        self.assertEqual(index1, 2)
        
        index2 = self.llist.get_element(0)
        self.assertEqual(index2, 1)
    
    def test_pop_last(self):
        self.llist.pop(2)
        
        length = len(self.llist)
        self.assertEqual(length, 2)
        
        index1 = self.llist.get_element(1)
        self.assertEqual(index1, 2)
        
        index2 = self.llist.get_element(0)
        self.assertEqual(index2, 1)
    
    def test_pop_start(self):
        self.llist.pop(0)
        
        length = len(self.llist)
        self.assertEqual(length, 2)
        
        index1 = self.llist.get_element(1)
        self.assertEqual(index1, 3)
        
        index2 = self.llist.get_element(0)
        self.assertEqual(index2, 2)
        
    def test_pop_start(self):
        self.llist.pop(1)
        
        length = len(self.llist)
        self.assertEqual(length, 2)
        
        index1 = self.llist.get_element(1)
        self.assertEqual(index1, 3)
        
        index2 = self.llist.get_element(0)
        self.assertEqual(index2, 1)
    
    def test_start_insertion(self):
        self.llist.insert(0, 0)
        
        for i in range(4):
            element = self.llist.get_element(i)
            self.assertEqual(i, element)

    def test_middle_insertion(self):
        self.llist.insert(1, 1.5)
        
        i = 0
        for node in self.llist:
            self.assertEqual(i, node.index)
            i += 1
        
    def test_last_insertion(self):
        self.llist.insert(-1, 4)
        
        i = 0
        for node in self.llist:
            self.assertEqual(i, node.index)
            i += 1
    
    def test_insertion(self):
        self.llist.insert(2, 4)
        
        i = 0
        for node in self.llist:
            self.assertEqual(i, node.index)
            i += 1
    
    def test_index(self):
        self.assertEqual(self.llist.index(1), 0)
        self.assertEqual(self.llist.index(2), 1)
        self.assertEqual(self.llist.index(3), 2)
        self.assertRaises(ValueError, self.llist.index, 8)
    
    def test_getter_method(self):
        self.assertEqual(self.llist.get_element(1), 2)
        self.assertEqual(self.llist.get_element(0), 1)
        self.assertEqual(self.llist.get_element(2), 3)
        self.assertRaises(IndexError, self.llist.get_element, 8)
    
    def test_setter_method(self):
        self.llist.set_element(1, 5)
        self.llist.set_element(2, 6)
        self.llist.set_element(0, 4)
        
        self.assertEqual(self.llist.get_element(1), 5)
        self.assertEqual(self.llist.get_element(0), 4)
        self.assertEqual(self.llist.get_element(2), 6)
    
unittest.main()