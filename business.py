import uuid
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
class shop():
    basket = []
    def __init__(self) -> None:
        pass
    
    def additembasket_shop(self,iditem:uuid,name:str,qty:int)->bool:
        try:
            if(shop.is_duplicate_shop(id)):
                print("Has this item in backet.")
                return False
            else:
                shop.basket.append({"id": iditem, "name": name, "quantity": qty})
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
    def calculate_item_shop(self):
        pass