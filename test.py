import unittest
from business import *
import os
class TestFileHandler(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        
    def test_notfoundfile(self):
        FileControl.read_from_file("./data/stock.txt")

    
class Testbusinesslogic(unittest.TestCase):
    def test_adddata_stock(self):
        Stock.additem_stock("เหล้าขาว",25,900)
if __name__ == '__main__':
    unittest.main()