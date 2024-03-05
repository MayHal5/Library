"""
    Running functions from other modules
    Author: Maysan Halaby
    Date: 03/03/2024
"""
import file_types.csv_file.csv_reader


def main():
    """
    Entry point
    """
    file_path = file_types.csv_file.csv_reader.CsvReader(r"C:\Users\User\Documents\name_age.csv")
    file_path.read()


if __name__ == '__main__':
    main()
