"""
    A class inherited from the main class
    Author: Maysan Halaby
    Date: 06/03/2024
"""

import json
from file_read import FileRead


class JsonReader(FileRead):
    """
    Inherited from the file reading class,
    used the abstract function of reading
    """
    def read(self):
        """
        print only the keys that contain in Json file
        """
        f = open(self.file_path)
        data = json.load(f)
        for key in data:
            print(key)
