from business import *
from uicontrol import UIControl

# from mysqlcontrol import *


def main():
    print("Welcome to ALCOHOL SHOP")
    UI = UIControl()
    userselect = None
    try:
        while True:
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
                case "Exit": exit()
    except Exception as Error:
        print(Error)
        print("ERROR: At Main() Func The Program's Restarting")
        main()
if __name__ == "__main__":
    main()