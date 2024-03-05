"""
    A function used for printing
    which is used in a class in another module
    Author: Maysan Halaby
    Date: 05/03/2024
"""


def print_csv_as_table(max_num_of_char, cell):
    """
    Prints according to a certain format
    It is used in the CsvReader class
    :param:num_of_char: Maximum number of characters
    :param:cell:
    """
    difference1 = max_num_of_char - len(cell)
    if difference1 > 0:
        print(cell[:max_num_of_char], end=f"{' ' * difference1}| ")
    else:
        print(cell[:max_num_of_char], end="| ")
