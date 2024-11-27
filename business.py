import uuid
class stock():
    stock_data = [
        {"id": "eae21a1dc-5fbc-490e-90dc-aa19057028e0","name":"เหล้าขาว","quantity": 5,"price": 900},
        {"id": "e3100df65-6ac7-4f4e-80ae-f26266e0748c","name":"เหล้ารัม","quantity": 4,"price": 2500},
    ]

    def __init__(self) -> None:
        pass

    def get_uuid() -> uuid:
        return uuid.uuid4
    
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
    
    def additembasket_shop(self,item:dict)->bool:
        try:
            if(shop.is_duplicate_shop(item)):
                print("Has this item in backet.")
                return False
            else:
                shop.basket.append({"id": self.get_uuid(), "name": item["name"], "quantity": item["quantity"], "price": item["price"]})
                return True
        except Exception as Error:
            print(Error)
            print("Error can't Save Data To List")
            return False
        
    @classmethod
    def is_duplicatebasket_shop(self,item_new:dict):
        for item in shop.basket:
            if item["id"] == item_new["id"] or item["name"] == item_new["name"]:
                return True
        return False