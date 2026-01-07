#import os
#import json
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import time
import pyautogui
from txt_file_lib import *
from billread import *
w, h = A4
rd()
print("==========================================================")
print("\t Inventory Managment System")
print("==========================================================")
#print(inventory)
def add():
    i_id=input("Enter Item Id=")
    if i_id.startswith("0"):
        print("Invalid Id... Id dosen't starts with zero")
    else:    
        if i_id in inventory:
            print("This Id is already Exists")
        else:          
            nm=input("Enter Item name=")
            qu=int(input("Enter Quantity="))
            pr=float(input("Enter Price of 1 item="))
            inventory[i_id]={"name":nm,"quantity":qu,"price":pr}
            #os.system(f"break > {filename}")
            #os.system(f"echo {json.dumps(inventory)} >> {filename}")
            #clr()
            wrt()
            print("Item Added Successfully")
def update():
    i_id=input("Enter Item Id=")
    if i_id in inventory:
        print("What do you want to update..?\n 1.Item name \n 2.Quantity \n 3.Price")
        ch=int(input("Enter Your choice="))
        match ch:
            case 1:
                nm=input("Enter Item name=")
                inventory[i_id]["name"]=nm
                wrt()
                print("Name updated successfully")
            case 2:
                print("You wants to \n 1.Add item \n 2.Delete item")
                c_h=int(input("Enter your choice="))
                match c_h:
                    case 1:
                        qu=int(input("Enter quantity to add="))
                        if qu > 0:
                            cqu=inventory[i_id]["quantity"]
                            inventory[i_id]["quantity"]=cqu+qu
                            wrt()
                            print("Quantity updated successfully")
                        else:
                            print("Invalid Quantity")
                    case 2:
                        qu=int(input("Enter quantity to remove="))
                        cqu=inventory[i_id]["quantity"]
                        if qu <= cqu and qu > 0:
                            inventory[i_id]["quantity"]=cqu-qu
                            wrt()
                            print("Quantity updated successfully")
                        if qu > cqu:
                            print("Insufficient quantity..")
                        if qu < 0:
                            print("Invalid quantity")
            case 3:
                pr=float(input("Enter price as per item="))
                inventory[i_id]["price"]=pr
                wrt()
                print("Price updated Successfully")
            case _:
                print("Invalid choice")
    else:
        print("Item Id not found")
        #print(inventory[i_id])
def delete():
    i_id=input("Enter Item Id=")
    if i_id in inventory:
        del inventory[i_id]
        wrt()
        print("Item remove successfully")
    else:
        print("Item id not found")
def check():
    print("--------------------------current Inventory--------------------------")
    print(f"{"Item Id":<10} |  {"Item name":<15} | \t {"Quantity":<10} | \t {"price":<10}")
    print("---------------------------------------------------------------------")
    for keys,values in inventory.items():
        print(f"{keys:<10} \t {values["name"]:<15} \t {values["quantity"]:<8} \t\t {values["price"]:<8}")
    '''for keys in inventory:
        print(keys,":",inventory[keys])'''
    '''print("======================")
    print("Id Name Quantity Price")    
    for keys in inventory:
        for value in keys:
            print(keys,value[name],value[quantity],value[price])'''
            
def search():
    nm=input("Enter item name to search=")
    for keys,values in inventory.items():
        '''if values["name"] == nm:
            print("yes")
        else:
            print("Item not found")'''
        if values["name"] == nm:
            print(f"Item found: Id={keys},Quantity={values["quantity"]},Price={values["price"]}")
invoice_no=billrd()           
def bill():
    global invoice_no
    global buy_items
    global buy_items_list
    global dt
    buy_items={}
    buy_items_list={}
    invoice_no=invoice_no+1
    dt=time.ctime()
    #buy_items["date-time"]=dt
    #buy_items["invoice_no"]=invoice_no
    while True:
        i_id=input("Enter Item Id(if done enter zero)=")
        if i_id in inventory:
            qu=int(input("Enter Quantity of Items="))
            cqu=inventory[i_id]["quantity"]
            n=inventory[i_id]["name"]
            ppr=inventory[i_id]["price"]
            if qu <= cqu and qu > 0:
                inventory[i_id]["quantity"]=cqu-qu
                tpr=inventory[i_id]["price"]*qu
                buy_items[i_id]={"name":n,"quantity":qu,"price":ppr,"total":tpr}
                #print(buy_items)
            if qu > cqu:
                print(f"Sorry item quantity is out of stock only {inventory[i_id]["quantity"]} is remaining")
            if qu <= 0:
                print("Invalid Quantity")  
        #invoice_no=0   
        if i_id == "0":
            #invoice_no=invoice_no+1
            break
        if i_id not in inventory:
            print("Item Id not found")     
def invoice():
    invoice_name=f"{invoice_no}.pdf"
    c = canvas.Canvas(invoice_name, pagesize=A4)
    #c.drawString(50, h - 50, "Hello, world!")
    c.drawString(50, h-100,"------------------------------Invoice-------------------------------")
    c.drawString(50, h-120,f"Invoice Number :{invoice_no}")
    c.drawString(50, h-140,f"date time :{dt}")
    c.drawString(50, h-160,"--------------------------------------------------------------------")
    c.drawString(50, h-180,"Item Id")
    c.drawString(100,h-180,"Item name")  
    c.drawString(180,h-180,"Quantity")
    c.drawString(230,h-180,"price")
    c.drawString(280,h-180,"q*price")
    c.drawString(50, h-200,"--------------------------------------------------------------------")
    t=0
    y=h-220
    for i in buy_items:
        c.drawString(50, y,f"{i}") 
        c.drawString(100,y,f"{buy_items[i]["name"]}") 
        c.drawString(180,y,f"{buy_items[i]["quantity"]}")
        c.drawString(230,y,f"{buy_items[i]["price"]}")  
        c.drawString(280,y,f"{buy_items[i]["total"]}")
        y=y-20  
        t=t+buy_items[i]["total"]
    buy_items["grand total"]=t   
    c.drawString(50, y,"--------------------------------------------------------------------")
    y=y-20
    c.drawString(50, y,f"Total amount={t}" )
    y=y-20
    c.drawString(120, y,"**********************************")
    y=y-20
    c.drawString(150, y,"Thank you visit again")
    c.showPage()
    c.save()
    buy_items_list["date-time"]=dt
    buy_items_list[invoice_no]=buy_items
    os.system(f"echo {json.dumps(buy_items_list)} >> {"bill.txt"}")   
    print("Bill saved successfully")
    wrt()
    time.sleep(2)
    os.popen(invoice_name)
    time.sleep(7)
    pyautogui.hotkey('alt','f4')
    #print(buy_items)
    #invoice()    
    #break
    #print("Thank you..") 
            
while True:
    print("What you want to do..?\n 1.Add Items \n 2.Update Items \n 3.Delete Items \n 4.View Inventory \n 5.Search Item \n 6.Bill \n 7.Exit")
    c=int(input("Enter Your Choice="))
    match c:
        case 1:
            add()
            print("___________________________________________")
        case 2:
            update()
            print("___________________________________________")
        case 3:
            delete()
            print("___________________________________________")
        case 4:
            check()
            print("_____________________________________________________________________")
        case 5:
            search()
            print("___________________________________________")
        case 6:
            bill()
            print("Do you want to print the bill..? \n 1.Yes \n 2.delete some items \n 3.Cancel bill")
            b=int(input("Enter your choice="))
            if b == 1:
                invoice()
            if b == 2:   
                i_id=input("Enter item id=")
                if i_id in buy_items:
                    buy_items.pop(i_id)
                    invoice()
                if i_id not in buy_items:
                    print("Item Id not found")
            if b == 3:
                print("Thank you")
            print("____________________________________________________________________")
        case 7:
            print("Thank you..")
            print("___________________________________________")
            break
        case _:
            print("Invalid Choice")
            print("___________________________________________")
#print(inventory)        

