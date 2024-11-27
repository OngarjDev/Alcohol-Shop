import os
import sys
from main import main
from business import *
class UIControl():

    bill_id_counter = 0

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
        selectmenu_text = "\033[1;33m Caution: Please check the customer's age.\033[0m"
        print(selectmenu_text.center(50,"="))

        print("\033[31m พ.ร.บ.ควบคุมเครื่องดื่มแอลกอฮอล์ พ.ศ. 2551 และ พ.ร.บ.คุ้มครองเด็ก พ.ศ.2546 ที่คุ้มครองเด็กอายุต่ำกว่า 18 ปี ต้องระวางโทษจำคุกไม่เกิน 3 เดือน หรือปรับไม่เกิน 3 หมื่นบาท หรือทั้งจำทั้งปรับ\033[0m")
        
        userinput = input("Please Input 1 letter Y (Customer Is 20+ years old)  N (Customer Is under 20 years old): ")
        if(userinput == "Y" or userinput == "y"):return True
        else: return False

    def buyalcohol(self):
        """
        แสดงเมนูสินค้าและให้ลูกค้าเลือกซื้อสินค้า
        """
        available_items = [
            {"name": "Beer", "price": 50},
            {"name": "Wine", "price": 120},
            {"name": "Whiskey", "price": 250},
            {"name": "Vodka", "price": 200},
        ]

        # แสดงเมนูสินค้า
        print("\nAvailable Alcohol Items:")
        print("=" * 50)
        print(f"{'No.':<5}{'Item':<20}{'Price (per unit)':<15}")
        print("-" * 50)
        for i, item in enumerate(available_items, start=1):
            print(f"{i:<5}{item['name']:<20}{item['price']:<15}")
        print("=" * 50)

        # รวบรวมการเลือกซื้อ
        items = []
        while True:
            try:
                user_choice = input("Enter the number of the item you want to buy (or type 'done' to finish): ")
                if user_choice.lower() == 'done':
                    break

                item_index = int(user_choice) - 1  # แปลงจากเลขที่ผู้ใช้กรอกเป็น index
                if 0 <= item_index < len(available_items):
                    selected_item = available_items[item_index]
                    quantity = int(input(f"Enter quantity for {selected_item['name']}: "))
                    items.append({"name": selected_item['name'], "quantity": quantity, "price": selected_item['price']})
                else:
                    print("\033[31mInvalid selection. Please choose a valid item number.\033[0m")
            except ValueError:
                print("\033[31mInvalid input. Please enter a number.\033[0m")

        # ส่งต่อไปที่ฟังก์ชัน bill
        if items:
            self.bill(items)
        else:
            print("\033[93mNo items were purchased.\033[0m")

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
                Stock.additem_stock(name_item,qty_item,price_item)

            case 2: pass
            case 3: pass
            case 4: main()
    def buylog(self, bill_data: str):
        """
        ฟังก์ชันนี้จะบันทึกข้อมูลบิลลงในไฟล์ .txt
        """
        try:
            # เปิดไฟล์เพื่อเพิ่มข้อมูล
            with open("buylog.txt", "a") as file:
                # เขียนข้อมูลบิลที่รับมา
                file.write(bill_data + "\n")
                print("\033[92mBill data has been logged successfully!\033[0m")
        except Exception as e:
            print(f"\033[31mError saving buy log: {e}\033[0m")

    def bill(self, items:list[dict])->str:

        # เพิ่ม Bill ID ใหม่
        UIControl.bill_id_counter += 1
        bill_id = UIControl.bill_id_counter

        Alcohol_Shop = "Alcohol Shop"
        bill_data = ""

        # แสดงชื่อร้านและ bill_id
        bill_data += Alcohol_Shop.center(50, "=") + "\n"
        bill_data += f"Bill ID: {bill_id}\n"
        bill_data += f"{'Item':<15}{'Quantity':<10}{'Price':<10}{'Total':<10}\n"
        bill_data += "-" * 50 + "\n"

        total = 0

        # แสดงข้อมูลสินค้า
        for item in items:
            item_total = item["quantity"] * item["price"]
            bill_data += f"{item['name']:<15}{item['quantity']:<10}{item['price']:<10}{item_total:<10}\n"
            total += item_total

        bill_data += "-" * 50 + "\n"
        bill_data += f"{'Total:':<35}{total:<10}\n"

        # แสดงข้อมูล
        print(bill_data)

        # บันทึกข้อมูลลงในไฟล์
        self.buylog(bill_data)  # เรียกใช้ฟังก์ชัน buylog() เพื่อบันทึกข้อมูล
        return bill_data  # ส่งข้อมูลบิลกลับ

