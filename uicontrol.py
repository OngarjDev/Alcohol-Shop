from business import *
import os
class UIControl():
    def __init__(self):
        self.menustart()
    
    @classmethod
    def print_itemall_stock(self)->None:
        """
        เมื่อเรียกใช้มันจะ โชว์ข้อมูล สินค้าออกมาเป็น list มีไว้ใช้ซ้ำกับหน้าอื่นๆ
        """
        selectmenu_text = "All Item Data In Stock"
        print(selectmenu_text.center(50,"="))
        for items in stock.readitem_stock():
            print(items)

    @classmethod
    def menustart(self)->str:
        """
        หน้าหลักระบบจะเรียกใช้หน้านี้รับส่งข้อมูล
        """
        selectmenu_text = "\033[1;33m Caution: Please check the customer's age.\033[0m"
        print(selectmenu_text.center(50,"="))
        print("\033[31m พ.ร.บ.ควบคุมเครื่องดื่มแอลกอฮอล์ พ.ศ. 2551 และ พ.ร.บ.คุ้มครองเด็ก พ.ศ.2546 ที่คุ้มครองเด็กอายุต่ำกว่า 18 ปี ต้องระวางโทษจำคุกไม่เกิน 3 เดือน หรือปรับไม่เกิน 3 หมื่นบาท หรือทั้งจำทั้งปรับ\033[0m")
        
        selectmenu_text = " Welcome to ALCOHOL SHOP "
        print(f"{'='*50}")
        print(selectmenu_text.center(50))
        print(f"{'='*50}")
        print("1. 🛒 Buy Alcohol")
        print("2. 📦 Manage Stock")
        print("3. 📜 View Buy Log")
        print("4. ❌ Exit Program")
        print(f"{'='*50}")
        userinput = input("Your Input: ")
        match int(userinput):
            case 1: UIControl.select_alcohol()
            case 2: UIControl.stock()
            case 3: UIControl.buylog()
            case 4: quit()

    @classmethod
    def select_alcohol(cls):
        """
        UI หน้านี้มีไว้เพื่อแสดงผลสินค้าที่เลือก แล้ว รองรับการบันทึกไว้ใน class shop ตัวแปร basket 
        พร้อมส่งต่อไปยังหน้า buyitem 
        """
        selectmenu_text = "Buy Alcohol menu (input 1 order only)"
        print("="*50)
        print(selectmenu_text.center(50))
        print("="*50)

        UIControl.print_itemall_stock()

        idselect_userinput = input("Input id item want will buy(Input Q/q Move to main menu): ")
        if(idselect_userinput == "Q" or idselect_userinput == "q"):UIControl()
        try:
            idselect_userinput = uuid.UUID(idselect_userinput)
        except ValueError:
            print("uuid is not correnty")
            UIControl.select_alcohol()

        qty_userinput = int(input("Input quantity want buy: "))
        item = stock.readitemid_stock(idselect_userinput)

        if(qty_userinput <= item["quantity"] and qty_userinput != 0 and shop.readbasket_id(idselect_userinput) is None):
            if(shop.additembasket_shop(item["id"],item["name"],item["price"],qty_userinput)):
                print("\n\033[92mAdd item in to basket Success\033[0m")
                print("-"*50)
            else:
                print("can't add item in basket.")
        else:
            print(f"\033[31m Sorry Product quantity Limit {item["quantity"]} Or Has this item in basket. \033[0m")
            return UIControl.select_alcohol()
        print("1. pay now")
        print("2. Continue Shopping")
        print("3. back to mainmenu\033[31m(if your exit basket data will delete auto)\033[0m")
        action_user = int(input("Please Input 1 (digit): "))
        match(action_user):
            case 1:
                UIControl.buyalcohol()
            case 2:
                UIControl.select_alcohol()
            case 3: 
                shop.setclear_basket()
                shop.setclear_order()
                UIControl()
            case _:
                UIControl.select_alcohol()

    @classmethod
    def buyalcohol(cls):
        """
        หน้านี้เมื่อต้องการสั่งซื้อจะทำการโชว์รายการสินค้าในตะกร้า แล้ว ให้ User Comfirm ว่าถูกต้องหรือไม่ จากนั้นจะส่งการทำงานไป Buisiness Logic
        """
        data = shop.calculate_item_shop()
        if(data[0] is None): print("Not Found Item In Basket")
        for sequence,item in enumerate(data[0],start=1):
                print(f"order: {sequence} ,name: {item["name"]},price: {item["price"]},quantity: {item["quantity"]},subtotal: {item["subtotal"]}")
        selectmenu_text = f"Total Price: {data[1]}"
        print(selectmenu_text.center(50,"="))
        select_text = "Please comfirm order(Y/n))"
        print(select_text.center(50,"="))
        selectmenu_text = input("Y/n: ")
        if(selectmenu_text == "Y" or selectmenu_text == "y"):
            if(shop.buyitem_shop(data)):
                print("\033[92mBill data has been logged successfully!\033[0m")
            else:
                print("Error data not logged successfully")
        elif(selectmenu_text == "Q" or selectmenu_text == "q"):
            UIControl()
        else: 
            shop.setclear_basket()
            shop.setclear_order()
            return UIControl.select_alcohol()

    @classmethod
    def stock(cls) -> any:
        """
        หน้านี้เป็นส่วนต่อขยาย สำหรับการจัดการ item ใน stock เท่านั้น เช่น เพิ่ม/ลบ/ตรวจสอบ 
        ย้อนกลับ หากต้องการแก้ไขให้ลบสินค้าเท่านั้น
        """
        selectmenu_text = "Stock Management Menu"
        print(selectmenu_text.center(50,"="))
        print("1. Add item")
        print("2. Delete item")
        print("3. Check item")
        print("4. Return to mainmenu")
        userinput = input("Please select action: ")
        match int(userinput):
            case 1: 
                name_item = input("NameItem: ")
                qty_item = int(input("QuantityItem(digit only): "))
                price_item = int(input("PriceItem(digit only): "))
                if(stock.additem_stock(name_item,qty_item,price_item)):
                    print(f"Add New item. name:{name_item},quantity:{qty_item},price:{price_item}")
                    UIControl.stock()
                else:
                    print("Has duplicate more One. can't save new data")
            case 2: 
                UIControl.print_itemall_stock()
                selectmenu_text = "Please Input Name Or uuid want deleted"
                print(selectmenu_text.center(50,"="))
                while True:
                    try:
                        select_item_delete = str(input("id: "))
                    except Exception:
                        print("Sorry, Your Input Is not UUID4")
                        userinput = input("try again?(Y = Try)/n: ")
                        if(userinput == "Y" or userinput == "y"): continue
                        else: return UIControl.stock()
                    if(stock.deleteitem_stock(uuid.UUID(select_item_delete))):
                        print("Delete Success")
                        return UIControl.stock()
                    else:
                        print("Error can't Delete,Id Is not correct")
                        userinput = input("try again?(Y = Try)/n: ")
                        if(userinput == "Y" or userinput == "y"): continue
                        else: return UIControl.stock()
            case 3: 
                UIControl.print_itemall_stock()
                return UIControl.stock()
            case 4: 
                UIControl()

    @classmethod
    def buylog(cls):
        """
        หน้านี้เป็นส่วนต่อขยาย มีหน้าที่แค่แสดงผลประวัติการสั่งซื้อสินค้า ใน ~/data/buylog.txt เท่านั้น
        """
        try:
            with open(os.path.abspath("./data/buylog.txt"), "r", encoding="utf-8") as file:
                print("== ข้อมูลใน Buy Log ==")
                for line in file:  # อ่านทีละบรรทัด
                    print(line.strip())  # ใช้ .strip() เพื่อตัดช่องว่างและ newline
        except FileNotFoundError:
            print("\033[31mError: Log file not found.\033[0m")
        except Exception as e:
            print(f"\033[31mError reading buy log: {e}\033[0m")
        
if __name__ == "__main__":
    UIControl()