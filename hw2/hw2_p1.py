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
    """The maxmin function returns a tuple of the max value followed by the min value in the given list."""
    max_val = ""
    min_val = ""
    if len(list) == 0:
        return None
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
    """The common_items function returns a list of common elements found in both provided lists."""
    common_elements = []
    for items1 in list1:
        for items2 in list2:
            if items1 == items2 and contains(common_elements, items1) is False:
                common_elements.append(items1)
    return common_elements


def contains(a_list, element):
    """The contains function returns True if an element is contained in a list."""
    for item in a_list:
        if item == element:
            return True
    return False

"""
Assume that list1 and list2 are valid lists. Return a list that contains items that only occur in one of list1 or list2
(i.e. not in both lists). The list returned will not contain any duplicate items.

Note: Constraint for this homework: do not use the built-in Python support for sets for this.
"""


def notcommon_items(list1, list2):
    """The notcommon_items function returns a list containing the elements found in only one of the two given lists."""
    notcommon_elements = []
    for items1 in list1:
        if contains(list2, items1) is False and contains(notcommon_elements, items1) is False:
            notcommon_elements.append(items1)
    for items2 in list2:
        if contains(list1, items2) is False and contains(notcommon_elements, items2) is False:
            notcommon_elements.append(items2)
    return notcommon_elements

"""
Assume the parameter is a valid list that may contain duplicate items.  Return a dictionary that stores counts of how
often each item occurs, i.e. each key in the dictionary will be a unique item from the list, and that key's value will
be how often it occurs in the list.

Example:
    For the list [1, 3, 2, 2, 3, 1, 1, 2], the dictionary returned would contain {1: 3, 2: 3, 3: 2}
"""


def count_list_items(list):
    """The count_list_items function returns a dictionary of the frequency each element appears in a given list."""
    dictionary = {}
    if len(list) == 0:
        return dictionary
    for item in list:
        if contains(dictionary.keys(), item):
            dictionary[item] += 1
        else:
            dictionary[item] = 1
    return dictionary


def test_maxmin():
    """Test function to assert that maxmin() works properly."""
    assert maxmin(['a', 'b', 'c']) == ('c', 'a')
    assert maxmin([2, 8, -4, 9]) == (9, -4)


def test_common_items():
    """Test function to assert that common_items() works properly."""
    assert common_items([1, 2, 3], [1, 2, 3]) == [1, 2, 3]
    assert common_items([1, 2, 3], [4, 5, 6]) == []
    assert common_items([1, 2, 3], []) == []
    assert common_items([], [4, 5, 6]) == []
    assert common_items([], []) == []
    assert common_items([1, 2, 3], [1, 7, 5]) == [1]
    assert common_items(['A', 'Z', 'G'], ['G', 'B', 'D', 'G']) == ['G']
    assert common_items(['a', 'A'], ['A']) == ['A']


def test_notcommon_items():
    """Test function to assert that notcommon_items() works properly."""
    assert notcommon_items([1, 2], [3, 4]) == [1, 2, 3, 4]
    assert notcommon_items([4, 7, 8], [3, 6, 8]) == [4, 7, 3, 6]
    assert notcommon_items([7, 8, 9], [7, 8, 9]) == []
    assert notcommon_items([], [3, 6, 8]) == [3, 6, 8]
    assert notcommon_items([], []) == []


def test_count_list_items():
    """Test function to assert that count_list_items() works properly."""
    assert count_list_items([1, 2, 3, 4, 5]) == {1: 1, 2: 1, 3: 1, 4: 1, 5: 1}
    assert count_list_items([1, 4, 7, 2, 9, 1, 7, 7, 4]) == {1: 2, 2: 1, 4: 2, 7: 3, 9: 1}
    assert count_list_items([]) == {}


def main():
    """main function"""
    test_maxmin()
    test_common_items()
    test_count_list_items()
    test_notcommon_items()

if __name__ == '__main__':
    main()