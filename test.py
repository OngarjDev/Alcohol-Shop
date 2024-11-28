import unittest
from business import *
from uicontrol import *
import os
# class TestFileHandler(unittest.TestCase):
#     def __init__(self, methodName: str = "runTest") -> None:
#         super().__init__(methodName)
        
#     def test_selectdatabase():
#         db = MySQLDatabase("localhost","root","alcoholshop123@","alcoholshop")
#         db.connect()
#         name = "เหล้าขาว"
#         data = MySQLDatabase.execute_query(f"SELECT * From stock Where name == {name}")
#         print(data)
    
class Testbusinesslogic(unittest.TestCase):
    def test_adddata_stock(self):
        stock.additem_stock("เหล้าเขียวส้มฟ้า",25,900)

        print(stock.readitem_stock(stock))
        for i in stock.readitem_stock(stock):
            self.assertEqual(i["name"],"เหล้าเขียวส้มฟ้า")

    def test_uuid(self):
        print(stock.get_uuid())

    # def test_delete_stock(self):
    #     stock.deleteitem_stock()
class Testui(unittest.TestCase):
    def test_deletestock_ui(self):
        UIControl.stock()
    
if __name__ == '__main__':
    # unittest.main()
    # Testui.test_deletestock_ui(Testui)
    # UIControl.buyalcohol()
    UIControl.select_alcohol(UIControl)
