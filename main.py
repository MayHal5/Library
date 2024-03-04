"""
    Running functions from other modules
    Author: Maysan Halaby
    Date: 03/03/2024
"""
import file_types.text_reader
from file_types.file_read.file_read import FileRead
from file_types.text_reader import TextReader


def main():
    """
    Entry point
    """
    file_path = file_types.text_reader.TextReader(r"C:\Users\User\Desktop\hellooo.txt")
    file_path.read()


if __name__ == '__main__':
    main()
