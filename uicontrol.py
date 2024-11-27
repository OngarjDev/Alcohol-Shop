import os
import sys
from main import *
from business import *
class UIControl():
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
        selectmenu_text = "\033[93m Caution: Please check the customer's age.\033[0m"
        print(selectmenu_text.center(50,"="))

        print("พ.ร.บ.ควบคุมเครื่องดื่มแอลกอฮอล์ พ.ศ. 2551 และ พ.ร.บ.คุ้มครองเด็ก พ.ศ.2546 ที่คุ้มครองเด็กอายุต่ำกว่า 18 ปี ต้องระวางโทษจำคุกไม่เกิน 3 เดือน หรือปรับไม่เกิน 3 หมื่นบาท หรือทั้งจำทั้งปรับ")
        
        userinput = input("Please Input 1 letter Y(Customer Is adult)/n: ")
        if(userinput == "Y" or userinput == "y"):return True
        else: return False

    def buyalcohol(self):
        selectmenu_text = "Buy Alcohol menu (input 1 order only)"
        print(selectmenu_text.center(50,"="))
        for sequence,items in enumerate(stock.readitem_stock(stock), start=1):
            print(f"ลำดับที่:{sequence},ชื่อ:{items["name"]},จำนวน:{items["quantity"]},ราคา:{items["price"]}")
        userinput = input("Input Order want will buy(digit): ")
        if(shop.additembasket_shop(userinput)):
            print("Add item in to basket Success")
        else:
            print("Not found order item")


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
                    stock()
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
                    if(stock.deleteitem_stock(select_item_delete)):
                        print("Delete Success")
                        stock()
                    else:
                        print("Error can't Delete,Id Is not correct")
                        userinput = input("try again?(Y = Try)/n: ")
                        if(userinput == "Y" or userinput == "y"): continue
                        else: return UIControl.stock(stock)
            case 3: 
                UIControl.print_itemall_stock(stock)
                return UIControl.stock(stock)
            case 4: main()
    def buylog(self):
        pass
