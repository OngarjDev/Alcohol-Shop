import os
import sys
from main import main
class UIControl():
    def __init__(self):
        pass

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
        pass

    @classmethod
    def stock(self):
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

            case 2: pass
            case 3: pass
            case 4: main()
    def buylog(self):
        pass