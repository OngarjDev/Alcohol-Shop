import uuid
import os
class stock():
    """
    class stock มีหน้าที่จัดการสินค้าเท่านั้น เช่น ข้อมูลตัวอย่างสำหรับการดึง ให้ uuid อ่านข้อมูลสินค้าที่มีได้ ฯ
    """
    stock_data = [
        {"id": uuid.UUID('efb843c4-4de5-41a6-85ec-bd931e2faa9e'),"name":"เหล้าขาว","quantity": 5,"price": 1990},
        {"id": uuid.UUID('af8230e7-560b-4fa5-b9e4-ecf629be30f5'),"name":"เหล้ารัม","quantity": 4,"price": 2510},
        {"id": uuid.UUID('029edf24-fef1-40bc-be31-a3a7bfd313d1'),"name":"เหล้าวอดก้า","quantity": 2,"price": 1458},
        {"id": uuid.UUID('633e28e2-d7a1-483d-b02d-01cdaa56432a'),"name":"เหล้าวิสกี้","quantity": 10,"price": 2050},
        {"id": uuid.UUID('25e84a68-423c-4f21-9464-8e795c7e7886'),"name":"เหล้าตากีล่า","quantity": 1,"price": 12200},
        {"id": uuid.UUID('aaffb4f2-f778-4f6c-8860-703f2f209a50'),"name":"เหล้ากาเลียโน่","quantity": 20,"price": 2300},   
    ]

    @classmethod
    def get_uuid(cls) -> uuid:
        return uuid.uuid4()
    
    @classmethod
    def readitem_stock(cls)->list:
        """
            ให้ method นี้เข้าถึงข้อมูลแทน การดึงข้อมูลจาก class โดยตรง
        """
        return cls.stock_data
    
    @classmethod
    def additem_stock(cls,name: str,qty: int,price: int)->bool:
        """
            เพิ่มสินค้าใน สต็อก 
            @name ใส่ชื่อสินค้าใหม่เข้าไป ต้องไม่ซ้ำกับชื่อที่มีอยู่
            @qty ใส่จำนวนสินค้าที่อยู่ในสต๊อก
            @price ใส่ราคา
            @return bool True สินค้าถูกเพิ่ม False สินค้าไม่สามารถเพิ่มได้
        """
        try:
            if(stock.is_duplicate_stock(stock,name)):
                return False
            else:
                stock.stock_data.append({"id": cls.get_uuid(), "name": name, "quantity": qty, "price": price})
                return True
        except Exception as Error:
            raise(f"Error can't Save Data To List {Error}")
    
    @classmethod
    def is_duplicate_stock(cls,id:uuid,name:str)->bool:
        """
        เช็คสินค้าซ้ำกัน ในสต๊อกสินค้า 
        @return True ตรวจพบสินค้าใน Stock
        @return False ไม่พบสินค้าใน Stock
        """
        for item in stock.stock_data:
            if item["id"] == id or item["name"] == name:
                return True
        return False
    @classmethod
    def deleteitem_stock(cls,id:uuid)-> bool:
        for item in stock.stock_data:
            if item["id"] == id:
                stock.stock_data.remove(item)
                return True
        return False
    
    @classmethod
    def readitemid_stock(cls,id:uuid)->dict:
        for item in stock.stock_data:
            if item["id"] == id:
                return item
        return False
    



class shop():
    basket,calculate_item,order = [],[],[]
    @classmethod
    def setclear_basket(cls):cls.basket.clear() 
    @classmethod
    def setclear_order(cls):cls.order.clear()
    @classmethod
    def setclear_calculate(cls):cls.calculate_item.clear()
        
    @classmethod
    def additembasket_shop(cls,iditem:uuid,name:str,price:int,qty:int)->bool:
        try:
            if(shop.is_duplicatebasket_shop(iditem)):
                raise("Has this item in backet.")
            else:
                shop.basket.append({"id": iditem, "name": name, "quantity": qty,"price":price})
                return True
        except Exception as Error:
            raise("Error can't Save Data To List")
    
    @classmethod
    def readbasket_id(cls,iditem:uuid)->dict:
        for item in shop.basket:
            if item["id"] == iditem:
                return item
            
    @classmethod
    def is_duplicatebasket_shop(cls,id:uuid):
        for item in shop.basket:
            if item["id"] == id:
                return True
        return False
    
    @classmethod
    def calculate_item_shop(cls)->list:
        total = 0
        for item in shop.basket:
            subtotal = item["price"] * item["quantity"]
            shop.calculate_item.append({"id": item["id"],"name": item["name"],"price": item["price"],"quantity": item["quantity"],"subtotal": subtotal})
            total += subtotal
        return [shop.calculate_item,total]   
    
    @classmethod
    def buyitem_shop(cls,orderlist:list)-> bool:
        if(len(orderlist) < 1): raise("Not Found basket") ;return False
        if(shop.savelog_shop(orderlist) == False):raise("Error Save Log Order.")
        for order in orderlist[0]:
            for item in stock.stock_data:
                if item["id"] == order["id"]:
                    item["quantity"] -= order["quantity"]
        shop.setclear_basket()
        shop.setclear_order()
        shop.setclear_calculate()
        return True

    @classmethod
    def savelog_shop(cls,order: list)-> bool:
        if(len(order) < 1): print("Not Found order") ;return False
        try:
            with open(os.path.abspath("./data/buylog.txt"), "a", encoding="utf-8") as file:
                idorder = stock.get_uuid()  # สร้าง UUID สำหรับคำสั่งซื้อ
                file.write(f"รหัสคำสั่งซื้อ: {idorder}\n")  # เขียน UUID ลงในไฟล์
                file.write("รายการสินค้า:\n")

                # ลูปข้อมูลใน order แล้วต่อ string
                for item in order[0]:
                    product_info = f" - ชื่อสินค้า: {item['name']}, จำนวน: {item['quantity']}, ราคา: {item['price']}, ราคาสินค้า: {item['subtotal']}\n"
                    file.write(product_info)
                file.write(f"ราคารวม: {order[1]}\n")
                file.write("\n")  # เว้นบรรทัด
                return True
        except Exception as e:
            raise(f"\033[31mError saving buy log: {e}\033[0m")
        return False