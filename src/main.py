"""
    Running functions from other modules
    Author: Maysan Halaby
    Date: 03/03/2024
"""

import src.json_reader


def main():
    """
    Entry point
    """
    file_path = src.json_reader.JsonReader(r"C:\Users\User\Documents\name_singer.json")
    file_path.read()


if __name__ == '__main__':
    main()
