__author__ = 'Philip Liberato'


"""
Assume the parameter is a any valid list containing comparable values of the same type. Return a tuple where the first
value is the maximum value found in the list (based on the > operator) and the second value in the tuple is the minimum
value found in the list (based on the < operator).  If the list is empty, return the special Python value None.

Examples:
    For the list [1, 3, 3], return (3, 1)
    For the list [3, 1, -2], return (3, -2)
    For the list ['Q', 'Z', 'C', 'A'], return ('Z', 'A')

Note: Constraint for this homework: do not use the built-in Python methods max() or min() for this.
"""


def maxmin(list):
    max_val = ""
    min_val = ""
    for element in list:
        if element is list[0]:
            max_val = element
            min_val = element
        if element > max_val:
            max_val = element
        if element < min_val:
            min_val = element
    return max_val, min_val

"""
Assume that list1 and list2 are valid lists.  Return a list that contains items that are found in both lists.
If there are no such common items, return an empty list.  The list returned will not contain any duplicate items.

Note: Constraint for this homework: do not use the built-in Python support for sets for this.
"""


def common_items(list1, list2):
    common_elements = []
    for items1 in list1:
        for items2 in list2:
            if items1 == items2 and contains(common_elements, items1) is False:
                common_elements.append(items1)
    return common_elements


# Helper function to determine if an element is contained in a list.
def contains(list, element):
    for item in list:
        if item == element:
            return True
    return False

"""
Assume that list1 and list2 are valid lists. Return a list that contains items that only occur in one of list1 or list2
(i.e. not in both lists). The list returned will not contain any duplicate items.

Note: Constraint for this homework: do not use the built-in Python support for sets for this.
"""


def notcommon_items(list1, list2):

    
    print list1 + list2

"""
Assume the parameter is a valid list that may contain duplicate items.  Return a dictionary that stores counts of how
often each item occurs, i.e. each key in the dictionary will be a unique item from the list, and that key's value will
be how often it occurs in the list.

Example:
    For the list [1, 3, 2, 2, 3, 1, 1, 2], the dictionary returned would contain {1: 3, 2: 3, 3: 2}
"""


def count_list_items(list):
    print list


# Test function to assert that maxmin() works properly.
def test_maxmin():
    assert maxmin(['a', 'b', 'c']) == ('c', 'a')
    assert maxmin([2, 8, -4, 9]) == (9, -4)


def test_common_items():
    assert common_items([1, 2, 3], [1, 2, 3]) == [1, 2, 3]
    assert common_items([1, 2, 3], [4, 5, 6]) == []
    assert common_items([1, 2, 3], [1, 7, 5]) == [1]
    assert common_items(['A', 'Z', 'G'], ['G', 'B', 'D', 'G']) == ['G']
    assert common_items(['a', 'A'], ['A']) == ['A']


def main():
    test_maxmin()
    test_common_items()

if __name__ == '__main__':
    main()