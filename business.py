import uuid
class FileControl():
    def __init__(self) -> None:
        pass

    @staticmethod
    def write_to_file(file_path: str, data: str, mode: str = "a"):
        """
        เขียนข้อมูลลงไฟล์
        :param file_path: ที่อยู่ของไฟล์
        :param data: ข้อมูลที่ต้องการบันทึก
        :param mode: โหมดการเขียน ("w" สำหรับเขียนทับ, "a" สำหรับเพิ่มข้อมูล)
        """
        try:
            with open(file_path, mode, encoding="utf-8") as file:
                file.write(data + "\n")
            print(f"Data written to {file_path} successfully.")
        except Exception as e:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(data + "\n")
            print(f"Create New file to {file_path} successfully.")


            
    @staticmethod
    def read_from_file(file_path: str) -> list[str]:
        """
        อ่านข้อมูลจากไฟล์
        :param file_path: ที่อยู่ของไฟล์
        :return: ข้อมูลทั้งหมดในไฟล์ในรูปแบบลิสต์
        """
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                return file.readlines()
        except FileNotFoundError:
            print(f"File not found: {file_path}")
            return []
        except Exception as e:
            print(f"Error reading from file: {e}")
            return []
        
    @staticmethod
    def is_duplicate(file_path: str, uuid: str, name: str) -> bool:
        """
        ตรวจสอบว่า UUID หรือชื่อสินค้าซ้ำในไฟล์หรือไม่
        :param file_path: ที่อยู่ของไฟล์
        :param uuid: UUID ของสินค้า
        :param name: ชื่อสินค้า
        :return: True ถ้าซ้ำ, False ถ้าไม่ซ้ำ
        """
        try:
            data = FileControl.read_from_file(file_path)
            for line in data:
                parts = line.strip().split(" ")
                if len(parts) < 2:
                    continue
                if parts[0] == uuid or parts[1] == name:
                    return True
            return False
        except Exception as e:
            print(f"Error checking duplicates: {e}")
            return True
            
class Stock():
    def __init__(self) -> None:
        self.pathstock = "./data/stock.txt"
    def get_pathstock(self) ->str:
        return self.pathstock
    def readitem_stock(self,data) -> None:
        return data.split(" ")
    def checkduplicate_stock(self,data,path) -> bool:
        pass
    @classmethod
    def additem_stock(self,name: str,qty: int,price: int)->bool:
        if(FileControl.is_duplicate(self.get_pathstock(),None,name)):
            print("Filedata Has duplicate.")
            return False #ยกเลิกการเพิ่มข้อมูลเนื่องจาก พบ ข้อมูลซ้ำกัน
        else:
            FileControl.write_to_file(self.pathstock, str(name + " " + str(qty) + " " + str(price)),"a")
    @staticmethod
    def generateid()->uuid:
        return uuid.uuid1()