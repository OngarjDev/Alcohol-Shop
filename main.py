from business import *
from uicontrol import UIControl

def main():
    selectmenu_text = "\033[1;33m Caution: Please check the customer's age.\033[0m"
    print(selectmenu_text.center(50,"="))
    print("\033[31m พ.ร.บ.ควบคุมเครื่องดื่มแอลกอฮอล์ พ.ศ. 2551 และ พ.ร.บ.คุ้มครองเด็ก พ.ศ.2546 ที่คุ้มครองเด็กอายุต่ำกว่า 18 ปี ต้องระวางโทษจำคุกไม่เกิน 3 เดือน หรือปรับไม่เกิน 3 หมื่นบาท หรือทั้งจำทั้งปรับ\033[0m")
        
    UI = UIControl()
    userselect = None
    while True:
        try:
            userselect = UI.menustart()
            match userselect:
                case "BUY": 
                    UI.select_alcohol()
                case "Manage Stock": UI.stock()
                case "BUYlog": UI.buylog()
                case "Exit":
                    print("\033[92mExiting the program.\033[0m")
                    quit()  # ออกจากลูป while และโปรแกรม
        except ValueError:
            print("\033[31mInvalid input. Please enter a valid option.\033[0m")
        except Exception as e:
            print(f"ERROR: {e}")
            print("Program will restart.\n")
            continue  # ให้โปรแกรมดำเนินการต่อและรับคำสั่งใหม่

if __name__ == "__main__":
    main()