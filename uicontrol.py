from business import *
import os
class UIControl():

    bill_id_counter = 0

    def __init__(self):
        pass
    
    def print_itemall_stock(self)->None:
        selectmenu_text = "All Item Data In Stock"
        print(selectmenu_text.center(50,"="))
        for items in stock.readitem_stock(stock):
            print(items)
    @classmethod
    def menustart(self)->str:
        selectmenu_text = "Please select menu (input 1 digit only)"
        print(selectmenu_text.center(50,"="))
        print("1.Buy alcohol")
        print("2.Check/Add/Delete Stock")
        print("3.Buylog")
        print("4.Exit Program")
        userinput = input("Your Input: ")
        userselect = None
        match int(userinput):
            case 1: userselect = "BUY"
            case 2: userselect = "Manage Stock"
            case 3: userselect = "BUYlog"
            case 4: userselect = "Exit"
        return userselect
    
    @classmethod
    def limitage(self)->bool:
        selectmenu_text = "\033[1;33m Caution: Please check the customer's age.\033[0m"
        print(selectmenu_text.center(50,"="))

        print("\033[31m พ.ร.บ.ควบคุมเครื่องดื่มแอลกอฮอล์ พ.ศ. 2551 และ พ.ร.บ.คุ้มครองเด็ก พ.ศ.2546 ที่คุ้มครองเด็กอายุต่ำกว่า 18 ปี ต้องระวางโทษจำคุกไม่เกิน 3 เดือน หรือปรับไม่เกิน 3 หมื่นบาท หรือทั้งจำทั้งปรับ\033[0m")
        
        userinput = input("Please Input 1 letter Y (Customer Is 20+ years old)  N (Customer Is under 20 years old): ")
        if(userinput == "Y" or userinput == "y"):return True
        else: return False

    def select_alcohol(self):
        selectmenu_text = "Buy Alcohol menu (input 1 order only)"
        print(selectmenu_text.center(50,"="))
        for sequence,items in enumerate(stock.readitem_stock(stock), start=1):
            print(f"ลำดับที่:{sequence},รหัส:{items["id"]},ชื่อ:{items["name"]},จำนวน:{items["quantity"]},ราคา:{items["price"]}")
        idselect_userinput = uuid.UUID(input("Input id item want will buy: "))
        qty_userinput = int(input("Input quantity want buy: "))
        item = stock.readitemid_stock(shop,idselect_userinput)

        if(qty_userinput <= item["quantity"] and qty_userinput != 0 and shop.readbasket_id(shop,idselect_userinput) is None):
            if(shop.additembasket_shop(shop,item["id"],item["name"],item["price"],qty_userinput)):
                print("Add item in to basket Success")
            else:
                print("can't add item in basket.")
        else:
            print(f"Sorry Product quantity Limit {item["quantity"]} Or Has this item in basket.")
        print("1. pay now")
        print("2. Shoping again")
        print("3. back to mainmenu(if your exit basket data will delete auto)")
        action_user = int(input("Please Input 1 (digit): "))
        match(action_user):
            case 1:
                UIControl.buyalcohol()
            case 2:
                UIControl.select_alcohol(shop)
            case 3: 
                shop.basket.clear
                shop.order.clear
                from main import main
                main()
    def buyalcohol():
        data = shop.calculate_item_shop(shop)
        select_text = "Please comfirm order(Y/n))"
        print(select_text.center(50,"="))
        selectmenu_text = input("Y/n: ")
        if(selectmenu_text == "Y" or selectmenu_text == "y"):
            return shop.buyitem_shop(shop,data)
        elif(selectmenu_text == "Q" or selectmenu_text == "q"):
            from main import main
            return main()
        else: 
            return UIControl.select_alcohol(UIControl)

    @classmethod
    def stock(self) -> any:
        selectmenu_text = "Please action stock(input 1 digit only)"
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
            case 2: 
                UIControl.print_itemall_stock(stock)
                selectmenu_text = "Please Input Name Or uuid want deleted"
                print(selectmenu_text.center(50,"="))
                while True:
                    try:
                        select_item_delete = str(input("id: "))
                        print(select_item_delete)
                        print(uuid.UUID(select_item_delete))
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
                        else: return UIControl.stock(stock)
            case 3: 
                UIControl.print_itemall_stock(stock)
                return UIControl.stock()
            case 4: 
                from main import main
                main()

    def buylog(self):
        try:
            with open(os.path.abspath("./data/buylog.txt"), "r", encoding="utf-8") as file:
                print("== ข้อมูลใน Buy Log ==")
                for line in file:  # อ่านทีละบรรทัด
                    print(line.strip())  # ใช้ .strip() เพื่อตัดช่องว่างและ newline
        except FileNotFoundError:
            print("\033[31mError: Log file not found.\033[0m")
        except Exception as e:
            print(f"\033[31mError reading buy log: {e}\033[0m")
