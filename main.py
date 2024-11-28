from business import *
from uicontrol import UIControl

# from mysqlcontrol import *


def main():
    print("Welcome to ALCOHOL SHOP")
    UI = UIControl()
    userselect = None
    while True:
        try:
            userselect = UI.menustart()
            match userselect:
                case "BUY": 
                    adult = UI.limitage()
                    if adult:
                        UI.select_alcohol()
                    else:
                        print("\033[31m Sorry:Staff can't sale Algohol\033[0m")
                case "Manage Stock": UI.stock()
                case "BUYlog": UI.buylog()
                case "Exit":
                    print("\033[92mExiting the program.\033[0m")
                    break  # ออกจากลูป while และโปรแกรม
        except ValueError:
            print("\033[31mInvalid input. Please enter a valid option.\033[0m")
        except Exception as e:
            print(f"ERROR: {e}")
            print("Program will restart.\n")
            continue  # ให้โปรแกรมดำเนินการต่อและรับคำสั่งใหม่

if __name__ == "__main__":
    main()