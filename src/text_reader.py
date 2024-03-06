"""
    A class inherited from the main class
    Author: Maysan Halaby
    Date: 04/03/2024
"""
from src.file_read import FileRead


class TextReader(FileRead):
    """
    Inherited from the file reading class,
    used the abstract function of reading
    """

    def read(self):
        """
        Opens a file in read mode and returns its contents
        """
        data_file = open(self.file_path, "r")
        return data_file.read()
