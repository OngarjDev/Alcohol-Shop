import unittest
import uuid
from io import StringIO
import os
from business import *
from contextlib import redirect_stdout

class TestStockAndShop(unittest.TestCase):

    def setUp(self):
        self.stock = stock()
        stock.stock_data = [
            {"id": uuid.UUID('efb843c4-4de5-41a6-85ec-bd931e2faa9e'), "name": "เหล้าขาว", "quantity": 5, "price": 1990},
            {"id": uuid.UUID('af8230e7-560b-4fa5-b9e4-ecf629be30f5'), "name": "เหล้ารัม", "quantity": 4, "price": 2510},
        ]
        self.shop = shop()
        shop.basket.clear()
        shop.calculate_item.clear()
        shop.order.clear()

    def test_additem_stock(self):
        result = self.stock.additem_stock("เหล้าจิน", 3, 3000)
        self.assertTrue(result)
        self.assertEqual(len(stock.stock_data), 3)

    # def test_additem_stock_duplicate(self):
    #     result = self.stock.additem_stock("เหล้าขาว", 3, 3000)
    #     self.assertFalse(result)
    #     self.assertEqual(len(stock.stock_data), 2)

    def test_deleteitem_stock(self):
        item_id = stock.stock_data[0]["id"]
        result = self.stock.deleteitem_stock(item_id)
        self.assertTrue(result)
        self.assertEqual(len(stock.stock_data), 1)

    def test_deleteitem_stock_not_found(self):
        result = self.stock.deleteitem_stock(uuid.uuid4())
        self.assertFalse(result)
        self.assertEqual(len(stock.stock_data), 2)

    def test_additembasket_shop(self):
        item = stock.stock_data[0]
        result = self.shop.additembasket_shop(item["id"], item["name"], item["price"], 2)
        self.assertTrue(result)
        self.assertEqual(len(shop.basket), 1)

    def test_is_duplicatebasket_shop(self):
        self.shop.basket = self.stock.stock_data[0]
        result = self.shop.is_duplicatebasket_shop(self.stock.stock_data[0])
        self.assertFalse(result)
        self.assertGreater(len(self.stock.stock_data[0]),0)

    def test_buyitem_shop(self):
        item = stock.stock_data[0]
        self.shop.additembasket_shop(item["id"], item["name"], item["price"], 2)
        order = self.shop.calculate_item_shop()
        result = self.shop.buyitem_shop(order)
        self.assertTrue(result)
        self.assertEqual(stock.stock_data[0]["quantity"], 3)

    def test_savelog_shop(self):
        item = stock.stock_data[0]
        self.shop.additembasket_shop(item["id"], item["name"], item["price"], 2)
        order = self.shop.calculate_item_shop()

        log_file = "./data/buylog.txt"
        if os.path.exists(log_file):
            os.remove(log_file)

        result = self.shop.savelog_shop(order)
        self.assertTrue(result)
        self.assertTrue(os.path.exists(log_file))

if __name__ == "__main__":
    unittest.main()