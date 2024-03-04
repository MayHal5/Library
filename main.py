"""
    Running functions from other modules
    Author: Maysan Halaby
    Date: 03/03/2024
"""
import file_read


def main():
    """
    Entry point
    """
    file_read.FileRead(r"C:\Users\User\Documents\ippp.txt")


if __name__ == '__main__':
    main()
