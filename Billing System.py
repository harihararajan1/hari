from tkinter.ttk import*
from tkinter import *
import mysql.connector as mysql
import random
from datetime import datetime

root= Tk()
root.geometry("1200x650+100+20")
root.title("RESTAURANT MANAGEMENT SYSTEM")

f= Frame(root, bd=10, relief=GROOVE)
f.pack(side=TOP)

f1 = Frame(root, bd=10, height=400,width=300, relief= RAISED)
f1.pack(side=LEFT,fill="both", expand=1)

f2 = Frame(root, bd=10,height=400, width=300, relief=RAISED)

lbl_info= Label(f, font=('aria', 30, 'bold'),text="MURUGAN IDLY KADAI")
lbl_info.grid(row=0, column=0)

now = datetime.now()
localtime = now.strftime("%d/%m/%Y %H:%M:%S")

rand         = StringVar()
Moongdalidli = StringVar()
Oatsravaidli = StringVar()
Quickravaidli= StringVar()
Soojiidli     = StringVar()
Doubleduckeridli = StringVar()
Pohaidli      = StringVar()
Total          = StringVar()
Tax            = StringVar()
cost           = StringVar()
date           = StringVar()
service_charge = StringVar()

lbl_Moongdalidli = Label(f1, font=('aria', 20, 'bold'),text="Moong dal idli Rs.180")
lbl_Moongdalidli.grid(row=1,column=0)
txt_Moongdalidli = Entry(f1, font=('ariel', 20, 'bold'),textvariable=Moongdalidli)
txt_Moongdalidli.grid(row=1,column=1)

lbl_Oatsravaidli = Label(f1, font=('aria', 20, 'bold'),text="Oats rava idli Rs.150")
lbl_Oatsravaidli.grid(row=2,column=0)
txt_Oatsravaidli = Entry(f1, font=('ariel', 20, 'bold'),textvariable=Oatsravaidli)
txt_Oatsravaidli.grid(row=2,column=1)

lbl_Quickravaidli = Label(f1, font=('aria', 20, 'bold'),text="Quick rava idli Rs.150")
lbl_Quickravaidli.grid(row=3,column=0)
txt_Quickravaidli= Entry(f1, font=('ariel', 20, 'bold'),textvariable=Quickravaidli)
txt_Quickravaidli.grid(row=3,column=1)

lbl_Soojiidli  = Label(f1, font=('aria', 20, 'bold'),text="Sooji idli  Rs.200")
lbl_Soojiidli .grid(row=4,column=0)
txt_Soojiidli  = Entry(f1, font=('ariel', 20, 'bold'),textvariable=Soojiidli )
txt_Soojiidli .grid(row=4,column=1)

lbl_Doubleduckeridli  = Label(f1, font=('aria', 20, 'bold'),text="Double ducker idli Rs.200")
lbl_Doubleduckeridli .grid(row=5,column=0)
txt_Doubleduckeridli = Entry(f1, font=('ariel', 20, 'bold'),textvariable=Doubleduckeridli)
txt_Doubleduckeridli.grid(row=5,column=1)

lbl_Pohaidli  = Label(f1, font=('aria', 20, 'bold'),text="Poha idli   Rs.200")
lbl_Pohaidli.grid(row=6,column=0)
txt_Pohaidli = Entry(f1, font=('ariel', 20, 'bold'),textvariable=Pohaidli )
txt_Pohaidli.grid(row=6,column=1)

def generate_bill():
    bill_no = str(random.randint(15000, 50000))
    rand.set(bill_no)
    date.set(localtime)
    try: qm = int(Moongdalidli.get())
    except: qm = 0
    try: qo = int(Oatsravaidli.get())
    except: qo = 0
    try: qq = int(Quickravaidli.get())
    except: qq = 0
    try: qs = int(Soojiidli.get())
    except: qs = 0
    try: qd = int(Doubleduckeridli.get())
    except: qd = 0
    try: qp = int(Pohaidli.get())
    except: qp = 0

    costofmoongdalidli = qm * 180 
    costofoatsravaidli = qo * 150
    costofquickravaidli = qq * 150
    costofsoojiidli    = qs * 200
    costofdoubleducker = qd * 200
    costofpohaidli     = qp * 200

    f2.pack(side=RIGHT, fill="both", expand=1)

    lbl_bill = Label(f2, font=('aria', 18, 'bold'), text="Bill no")
    lbl_bill.grid(row=1,column=0)


    lbl_date = Label(f2, font=('aria', 18, 'bold'), text="Date")
    lbl_date.grid(row=2,column=0)
   

    lbl_cost = Label(f2, font=('aria', 18, 'bold'), text="Cost")
    lbl_cost.grid(row=3,column=0)
    

    lbl_service = Label(f2, font=('aria', 18, 'bold'), text="Service charge")
    lbl_service.grid(row=4,column=0)
    
    lbl_tax = Label(f2, font=('aria', 18, 'bold'), text="Tax")
    lbl_tax.grid(row=5,column=0)
    

    lbl_total = Label(f2, font=('aria', 18, 'bold'), text="Total")
    lbl_total.grid(row=6,column=0)
    
    Totalcost= costofmoongdalidli + costofoatsravaidli + costofquickravaidli + costofsoojiidli + costofdoubleducker + costofpohaidli
    costofmeal =  "Rs.", str('%.2f' % Totalcost)
    payTax = (Totalcost * 0.18)
    paidTax = "Rs.", str('%.2f' % payTax)
    ser_charge = (Totalcost * 0.01)
    service = "Rs.", str('%.2f' % ser_charge)
    overall = payTax + Totalcost + ser_charge
    total = "Rs.", str('%.2f' % overall)

    service_charge.set(service)
    cost.set(costofmeal)
    Tax.set(paidTax)
    Total.set(total)

txt_bill = Entry(f2, font=('ariel', 18, 'bold'),textvariable=rand)
txt_bill.grid(row=1, column=1)

txt_date = Entry(f2, font=('ariel', 18, 'bold'),textvariable=date)
txt_date.grid(row=2, column=1)

txt_cost = Entry(f2, font=('ariel', 18, 'bold'),textvariable=cost)
txt_cost.grid(row=3, column=1)

txt_service = Entry(f2, font=('ariel', 18, 'bold'),textvariable=service_charge)
txt_service.grid(row=4, column=1)

txt_tax = Entry(f2, font=('ariel', 18, 'bold'),textvariable=Tax)
txt_tax.grid(row=5, column=1)

txt_total = Entry(f2, font=('ariel', 18, 'bold'),textvariable=Total)
txt_total.grid(row=6, column=1)


    
def extra_root():
    new_root = Toplevel(root)
    new_root.title("RESTAURANT BILL")
    new_root.geometry("350x420")
    Label(new_root,text='TOTAL  BILL AMOUNT').pack()
    Label(new_root,text = txt_bill.get()).pack()
    Label(new_root,text = txt_date.get()).pack()
    Label(new_root,text = txt_cost.get()).pack()
    Label(new_root,text = txt_service.get()).pack()
    Label(new_root,text = txt_tax.get()).pack()
    Label(new_root,text = txt_total.get()).pack()

    new_root.mainloop()

Button(f1, bd=5, fg="black", font=('ariel', 14, 'bold'),text="GET BILL",command=extra_root).grid(row=11,column=0)

 

def qexit():
    root.destroy()

def reset():
    Moongdalidli.set('') 
    Oatsravaidli.set('')  
    Quickravaidli.set('') 
    Soojiidli.set('')      
    Doubleduckeridli.set('')  
    Pohaidli.set('')
    date.set('')
    f2.pack_forget()

btn_Total = Button(f1, bd=5, fg="black", font=('ariel', 16, 'bold'),text="CALCULATE BILL",command=generate_bill)
btn_Total.grid(row=9,column=0)

btn_Reset = Button(f1, bd=5, fg="black", font=('ariel', 16, 'bold'),text="RESET",command=reset)
btn_Reset.grid(row=9,column=1)

btn_Exit = Button(f1, bd=5, fg="black", font=('ariel', 16, 'bold'),text="EXIT",command=qexit)
btn_Exit.grid(row=9,column=2)

def save_data():
    bill_no = txt_bill.get()
    date_time = txt_date.get()
    cost = txt_cost.get()
    service_charge = txt_service.get()
    tax = txt_tax.get()
    total =txt_total.get()

    con = mysql.connect(host="localhost",user="root",password="",database="billing_sys")
    cursor = con.cursor()
    cursor.execute("insert into total_cost values('"+ bill_no +"','"+ date_time +"','"+ cost +"','"+ service_charge +"','"+ tax +"','"+ total +"')")
    cursor.execute("commit")

    con.close()

Button(f1, bd=5, fg="black", font=('ariel', 14, 'bold'),text="SAVE",command=save_data).grid(row=11,column=2)


root.mainloop()







