from business import *
import os
class UIControl():
    def print_itemall_stock(self)->None:
        selectmenu_text = "All Item Data In Stock"
        print(selectmenu_text.center(50,"="))
        for items in stock.readitem_stock(stock):
            print(items)

    @classmethod
    def menustart(self)->str:
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
        userselect = None
        match int(userinput):
            case 1: userselect = "BUY"
            case 2: userselect = "Manage Stock"
            case 3: userselect = "BUYlog"
            case 4: userselect = "Exit"
        return userselect

    def select_alcohol(self):
        selectmenu_text = "Buy Alcohol menu (input 1 order only)"
        print("="*50)
        print(selectmenu_text.center(50))
        print("="*50)

        UIControl.print_itemall_stock(UIControl)

        idselect_userinput = input("Input id item want will buy(Input Q/q Move to main menu): ")
        if(idselect_userinput == "Q" or idselect_userinput == "q"):from main import main ;main()
        try:
            idselect_userinput = uuid.UUID(idselect_userinput)
        except ValueError:
            print("uuid is not correnty")
            UIControl.select_alcohol(UIControl)

        qty_userinput = int(input("Input quantity want buy: "))
        item = stock.readitemid_stock(shop,idselect_userinput)

        if(qty_userinput <= item["quantity"] and qty_userinput != 0 and shop.readbasket_id(shop,idselect_userinput) is None):
            if(shop.additembasket_shop(shop,item["id"],item["name"],item["price"],qty_userinput)):
                print("\n\033[92mAdd item in to basket Success\033[0m")
                print("-"*50)
            else:
                print("can't add item in basket.")
        else:
            print(f"\033[31m Sorry Product quantity Limit {item["quantity"]} Or Has this item in basket. \033[0m")
        print("1. pay now")
        print("2. Continue Shopping")
        print("3. back to mainmenu\033[31m(if your exit basket data will delete auto)\033[0m")
        action_user = int(input("Please Input 1 (digit): "))
        match(action_user):
            case 1:
                UIControl.buyalcohol()
            case 2:
                UIControl.select_alcohol(shop)
            case 3: 
                shop.setclear_basket(shop)
                shop.setclear_order(shop)
                from main import main
                main()
            case _:
                UIControl.select_alcohol(UIControl)

    def buyalcohol():
        data = shop.calculate_item_shop(shop)
        if(data[0] is None): print("Not Found Item In Basket")
        for sequence,item in enumerate(data[0],start=1):
                print(f"order: {sequence} ,name: {item["name"]},price: {item["price"]},quantity: {item["quantity"]},subtotal: {item["subtotal"]}")
        selectmenu_text = f"Total Price: {data[1]}"
        print(selectmenu_text.center(50,"="))

        select_text = "Please comfirm order(Y/n))"
        print(select_text.center(50,"="))
        selectmenu_text = input("Y/n: ")
        if(selectmenu_text == "Y" or selectmenu_text == "y"):
            if(shop.buyitem_shop(shop,data)):
                print("\033[92mBill data has been logged successfully!\033[0m")
            else:
                print("Error data not logged successfully")
        elif(selectmenu_text == "Q" or selectmenu_text == "q"):
            from main import main
            return main()
        else: 
            shop.setclear_basket(shop)
            shop.setclear_order(shop)
            return UIControl.select_alcohol(UIControl)

    @classmethod
    def stock(self) -> any:
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