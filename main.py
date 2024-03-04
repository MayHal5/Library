"""
    Running functions from other modules
    Author: Maysan Halaby
    Date: 03/03/2024
"""
<<<<<<< HEAD
import file_read
=======
import file_types.text_reader
from file_types.file_read.file_read import FileRead
from file_types.text_reader import TextReader
>>>>>>> feature/text-reader


def main():
    """
    Entry point
    """
<<<<<<< HEAD
    file_read.FileRead(r"C:\Users\User\Documents\ippp.txt")
=======
    file_path = file_types.text_reader.TextReader(r"C:\Users\User\Desktop\hellooo.txt")
    file_path.read()
>>>>>>> feature/text-reader


if __name__ == '__main__':
    main()
