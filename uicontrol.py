import os
import sys

class UIControl():
    def __init__(self):
        pass

    @classmethod
    def menustart(self)->str:
        selectmenu_text = "Please select menu (input 1 digit only)"
        print(selectmenu_text.center(50,"="))
        print("1.buy alcohol")
        print("2.check/add/delete")
        print("3.BUYlog")
        print("4.Exit Program")
        userinput = input("Your Input: ")
        match userinput:
            case 1: userselect = "BUY"
            case 2: userselect = "Manage Stock"
            case 3: userselect = "BUYlog"
            case 4: userselect = "Exit"
        return userselect
    def buyalcohol():
        pass
    def stock():
        pass
    def buylog():
        pass