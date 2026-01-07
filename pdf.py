from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

w, h = A4
c = canvas.Canvas("invoice.pdf", pagesize=A4)
#c.drawString(50, h - 50, "Hello, world!")

c.drawString(50, h-100,"------------------------------Invoice-------------------------------")
c.drawString(50, h-150,"Invoice Number :",invoice_no)
c.drawSrting(50, h-200,"date time :",dt)
c.drawString(50, h-250,"--------------------------------------------------------------------")
c.drawString(50, h-300,"Item Id   Item name  Quantity  price  q*price")
c.drawString(50, h-350,"--------------------------------------------------------------------")
t=0
for i in buy_items:
    c.drawString(50, h-400,f"{i}  {buy_items[i]["name"]}  {buy_items[i]["quantity"]}  {buy_items[i]["price"]}  {buy_items[i]["total"]}")
    t=t+buy_items[i]["total"]
buy_items["grand total"]=t   
c.drawString(50, h-450,"--------------------------------------------------------------------")
c.drawString(50, h-500,f"Total amount={t}" )
c.drawString(50, h-550,"**********************************")
c.drawString(50, h-600,"Thank you visit again")
c.showPage()
c.save()


'''print("------------------------------Invoice-------------------------------")
            print("Invoice Number :",invoice_no)
            print("date time :",dt)
            print("--------------------------------------------------------------------")
            print("Item Id   Item name \t Quantity \t price \t q*price")
            print("--------------------------------------------------------------------")
            t=0
            ''''''for i in buy_items:
                print(i)''''''
            for i in buy_items:
                print(f"{i} \t {buy_items[i]["name"]} \t {buy_items[i]["quantity"]} \t \t {buy_items[i]["price"]} \t {buy_items[i]["total"]}")
                t=t+buy_items[i]["total"]
            buy_items["grand total"]=t    
            print("--------------------------------------------------------------------")
            print(f"Total amount=\t \t \t \t \t{t}" )
            print("\t \t  **********************************")
            print("\t \t \t Thank you visit again")'''
            '''print("Do you want to print the bill..? \n 1.Yes \n 2.delete some items \n 3.Cancel bill")
            b=int(input("Enter your choice="))
            if b == 1:
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
                    os.popen(invoice_name)
                    #print(buy_items)
                invoice()    
                break
                print("Thank you..")
            if b == 2:
                i_id=input("Enter item id=")
                if i_id in buy_items:
                    buy_items.pop(i_id)
                    invoice()
                if i_id not in buy_items:
                    print("Item Id not found")
            if b == 3:
                print("Thank you..")'''
        #if i_id not in inventory:
            #print("Item Id not found")  
    #invoice_no=invoice_no+1