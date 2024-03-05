"""
    A class inherited from the main class
    Author: Maysan Halaby
    Date: 03/03/2024
"""
import csv
from file_types.csv_file import print_csv_file
from file_types.file_read.file_read import FileRead


class CsvReader(FileRead):
    """
    A class inherited from the main class
    and implements an abstract method
    """
    def read(self, num_of_char: int = 5):
        """
        Opens a file in read mode and calls the "print_csv_as_table" function
        to print the contents of the Csv file in the format defined in the function
        """
        with open(self.file_path, 'r') as csvfile:
            list_rows = csv.reader(csvfile)
            for row in list_rows:
                for cell in row:
                    print_csv_file.print_csv_as_table(num_of_char, cell)
                print()




