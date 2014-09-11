__author__ = 'Philip Liberato'

"""
This file contains the class definition for the OurSet object.
This simple implementation of the Set ADT includes the following methods:
    add(item_to_be_added) - attempts to add an element to the OurSet object
    addList(list_of_items_to_be_added) - attempts to add elements from a list to the OurSet object
    __str__ - returns a string representation of the OurSet object
    __len__ - returns the number of elements in the OurSet object
    __iter__ - enables the ability to cycle through the OurSet object
    union(other) - returns a new OurSet object representing the union of the original and other OurSet objects
    intersection(other) - returns a new OurSet object representing the intersection of the original and other OurSet objects
    contains(item_to_be_checked) - returns true if the item is contained within the OurSet object
"""


class OurSet(object):

    def __init__(self):
        """Default constructor which initializes an empty OurSet object."""
        self.body = []

    def add(self, item):
        """The add method returns True if the given element is successfully added to the OurSet object."""
        if self.contains(item) is False:
            self.body.append(item)
            return True
        return False

    def addList(self, list):
        """The addList method returns True if any element from the given list is added to the OurSet object."""
        was_item_added = False
        if len(list) == 0:
            return was_item_added
        for item in list:
            if self.contains(item) is False:
                self.body.append(item)
                was_item_added = True
        return was_item_added

    def __str__(self):
        """The __str__ method returns a string representation of the OurSet object."""
        if len(self.body) == 0:
            return "<>"
        set_representation = "<"
        for item in self.body:
            if item != self.body[-1]:
                set_representation += str(item) + ", "
        return set_representation + str(self.body[-1]) + ">"

    def __len__(self):
        """The __len__ method returns the number of items in the OurSet object."""
        return len(self.body)

    def __iter__(self):
        """The __iter__ method enables OurSet objects to be traversed."""
        return iter(self.body)

    def union(self, set2):
        """The union method returns an independent OurSet object that is the union of two OurSet objects."""
        new_set = OurSet()
        new_set.addList(self.body)
        if len(set2) == 0:
            return new_set
        for item in set2.body:
            if new_set.contains(item) is False:
                new_set.body.append(item)
        return new_set

    def intersection(self, set2):
        """The intersection method returns an independent OurSet object that is the intersection of two OurSet objects."""
        new_set = OurSet()
        if len(self.body) == 0 or len(set2.body) == 0:
            return new_set
        for item in set2:
            if self.contains(item):
                new_set.body.append(item)
        return new_set

    def contains(self, item):
        """The contains method determines if a given item is contained in the OurSet object."""
        if len(self.body) == 0:
            return False
        for elements in self.body:
            if elements == item:
                return True
        return False


def main():
    """The main function."""


if __name__ == '__main__':
    main()