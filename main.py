from uicontrol import * 
from business import *


def main():
    print("Welcome to ALCOHOL SHOP")
    UI = UIControl()
    userselect = UI.menustart()
    match userselect:
        case "BUY": UI.buyalcohol()
        case "Manage Stock": UI.stock()
        case "BUYlog": UI.buylog()
        case "Exit": exit()
if __name__ == "__main__":
    main()