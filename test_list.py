from logging import exception
from typing import Tuple
import unittest

class TestList(unittest.TestCase):

    def get_list(self):
        new_list = []
        new_list.append(1)
        new_list.append(2)
        new_list.append(3)
        new_list.append(4)

        return new_list

#### We need to get the size of the list ####

    # Size of a list (len)
    def test_get_size_of_list(self):
        new_list = self.get_list()

        self.assertEqual(4, len(new_list))

    # Size of an empty list (len)
    def test_get_size_of_empty_list(self):
        new_list = []

        self.assertEqual(0, len(new_list))

    # Size of an empty list (not)
    def test_get_size_of_empty_list_boolean(self):
        new_list = []

        self.assertTrue(not new_list)
#############################################

####### We need to clear the list ##########

    # Check the list is clear with len
    def test_clear_list(self):
        new_list = self.get_list()
        new_list.clear()

        self.assertEqual(0, len(new_list))

    # Check the list is clear with not
    def test_clear_list_boolean(self):
        new_list = self.get_list()
        new_list.clear()

        self.assertTrue(not new_list)

    # Check the list is clear after adding two items
    def test_clear_list_after_append(self):
        new_list = []
        new_list.append(5)
        new_list.append(6)

        new_list.clear()

        self.assertEqual(0, len(new_list))

############################################

########### We need to add Items ############
    
    # Add items to a list
    def test_add_items_to_list(self):
        new_list = self.get_list()
        new_list.append(5)

        self.assertEqual(5, len(new_list))

    # Add items to an empty list
    def test_add_items_to_empty_list(self):
        new_list = []
        new_list.append(1)

        self.assertEqual(1, len(new_list))

    # Add items to an list that has been cleared
    def test_add_items_to_clear_list(self):
        new_list = self.get_list()
        new_list.clear()
        new_list.append(1)

        self.assertEqual(1, len(new_list))

#############################################

###### We need to be able to check if an item exists ####

    # Check if item exists in list
    def test_item_exists(self):
        new_list = self.get_list()

        self.assertTrue((2 in new_list))

    # Check if item exists in a list (assertIn)
    def test_item_exists_in(self):
        new_list = self.get_list()

        self.assertIn(2,  new_list)

    # Check if item exists in an empty list
    def test_item_exists_empty_list(self):
        new_list = []

        if not new_list:
            self.assertNotIn(2, new_list)
        else:
            self.assertIn(2, new_list)


###########################################################


######## We need to get elements by index #####

    # Get element by index
    def test_elements_by_index(self):
        new_list = self.get_list()

        self.assertEqual(2, new_list[1])

    # Get element by index validate index
    def test_elements_by_index_validate(self):
        new_list = self.get_list()
        index = 1

        if index >= 0 and index < len(new_list):
            self.assertEqual(2, new_list[1])
        else:
            print("Index out of range")

    # Get element by index of an empty list
    def test_element_by_index_empty_list(self):
        new_list = []

        try:
            self.assertEqual(2, new_list[1])
        except IndexError:
            self.assertEqual(0, len(new_list))
        

#####################################################


######## We need to search the index of an object #######

    # Get the index of an object
    def test_index_of_an_object(self):
        new_list = self.get_list()

        self.assertEqual(1, new_list.index(2))

    # Get the index of an object that is repeated in the list
    def test_index_of_a_repeated_object(self):
        new_list = self.get_list()
        new_list.append(2)

        self.assertEqual(1, new_list.index(2))

    # Get the index of an object that is not in the list
    def test_index_of_an_object_empty_list(self):
        new_list = []
        self.assertNotIn(2, new_list, "Not in the list")

######################################################

############ We need to remove an item by index #######

    # Remove item from a list by index
    def test_remove_item_by_index(self):
        new_list = self.get_list()
        new_list.remove(1)

        self.assertEqual(3, len(new_list))

    # Remove item from a list by index using pop()
    def test_remove_item_by_index_pop(self):
        new_list = self.get_list()

        new_list.pop(1)

        self.assertEqual(3, len(new_list))

    # Remove item from an empty list by index
    def test_remove_item_empty_list(self):
        new_list = []

        try:
            new_list.remove(1)
        except ValueError:
            self.assertEqual(0, len(new_list))


######################################################

if __name__ == '__main__':
    unittest.main()