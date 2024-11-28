import uuid
import os
class stock():
    stock_data = [
        {"id": uuid.UUID('efb843c4-4de5-41a6-85ec-bd931e2faa9e'),"name":"เหล้าขาว","quantity": 5,"price": 900},
        {"id": uuid.UUID('af8230e7-560b-4fa5-b9e4-ecf629be30f5'),"name":"เหล้ารัม","quantity": 4,"price": 2500},
    ]

    def __init__(self) -> None:
        pass

    def get_uuid() -> uuid:
        return uuid.uuid4()
    
    def readitem_stock(self)->list:
        return self.stock_data
    
    @classmethod
    def additem_stock(self,name: str,qty: int,price: int)->bool:
        try:
            if(stock.is_duplicate_stock(None,name)):
                print("Has duplicate more One. can't save new data")
                return False
            else:
                stock.stock_data.append({"id": self.get_uuid(), "name": name, "quantity": qty, "price": price})
                return True
        except Exception as Error:
            print(Error)
            print("Error can't Save Data To List")
            return False
        
    @classmethod
    def is_duplicate_stock(self,id:uuid,name:str):
        for item in stock.stock_data:
            if item["id"] == id or item["name"] == name:
                return True
        return False
    
    @classmethod
    def deleteitem_stock(self,id:uuid)-> bool:
        for item in stock.stock_data:
            if item["id"] == id:
                stock.stock_data.remove(item)
                return True
        return False
    
    def readitemid_stock(self,id:uuid)->dict:
        for item in stock.stock_data:
            if item["id"] == id:
                return item
        return False
class shop():
    basket = []
    calculate_item = []
    order = []
    def __init__(self) -> None:
        pass
    
    def additembasket_shop(self,iditem:uuid,name:str,price:int,qty:int)->bool:
        try:
            if(shop.is_duplicatebasket_shop(id)):
                print("Has this item in backet.")
                return False
            else:
                shop.basket.append({"id": iditem, "name": name, "quantity": qty,"price":price})
                return True
        except Exception as Error:
            print(Error)
            print("Error can't Save Data To List")
            return False
        
    def readbasket_id(self,iditem:uuid)->dict:
        for item in shop.basket:
            if item["id"] == iditem:
                return item
 
    @classmethod
    def is_duplicatebasket_shop(self,id:uuid):
        for item in shop.basket:
            if item["id"] == id:
                return True
        return False
    def calculate_item_shop(self)->list:
        total = 0
        for sequence,item in enumerate(shop.basket,start = 1):
            subtotal = item["price"] * item["quantity"]
            print(f"order: {sequence} ,name: {item["name"]},price: {item["price"]},quantity: {item["quantity"]},subtotal: {subtotal}")
            shop.calculate_item.append({"id": item["id"],"name": item["name"],"price": item["price"],"quantity": item["quantity"]})
            total += subtotal
        selectmenu_text = f"Total Price: {total}"
        print(selectmenu_text.center(50,"="))
        return shop.calculate_item   
    
    def buyitem_shop(self,orderlist:list)-> bool:
        shop.savelog_shop(shop,orderlist)
        for order in orderlist:
            for item in stock.stock_data:
                if item["id"] == order["id"]:
                    item["quantity"] -= order["quantity"]
        shop.basket.clear
        return True

    def savelog_shop(self,order: list)-> bool:
        try:
            with open(os.path.abspath("./data/buylog.txt"), "a", encoding="utf-8") as file:
                idorder = stock.get_uuid()  # สร้าง UUID สำหรับคำสั่งซื้อ
                file.write(f"รหัสคำสั่งซื้อ: {idorder}\n")  # เขียน UUID ลงในไฟล์
                file.write("รายการสินค้า:\n")

                # ลูปข้อมูลใน order แล้วต่อ string
                for item in order:
                    product_info = f" - ชื่อสินค้า: {item['name']}, จำนวน: {item['quantity']}, ราคา: {item['price']}\n"
                    file.write(product_info)

                file.write("\n")  # เว้นบรรทัด
                print("\033[92mBill data has been logged successfully!\033[0m")
                return True
        except Exception as e:
            print(f"\033[31mError saving buy log: {e}\033[0m")
        return False