"""
    Running functions from other modules
    Author: Maysan Halaby
    Date: 03/03/2024
"""
import os
from abc import ABC, abstractmethod


class FileRead(ABC):
    """
    An abstract class, receives a path to a file,
    finds its size and name, and contains an abstract method
    """
    def __init__(self, file_path: str):
        """
        :param file_path: file path
        """
        self.file_path = file_path
        isfile = os.path.isfile(file_path)
        if isfile is True:
            print("this is a file")
        else:
            raise Exception("this is not a file , please enter a valid path")

    def size(self) -> int:
        """
        Find the size of the file
        :return: file size
        """
        file_size = os.path.getsize(self.file_path)
        return file_size

    def name(self) -> str:
        """
        Finds the name of the file that is in the path
        :return: file name
        """
        file_name = os.path.basename(self.file_path)
        return file_name

    @abstractmethod
    def read(self):
        """
        reads what the file contains
        """
        pass
