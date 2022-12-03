from tkinter.ttk import*
from tkinter import *
from PIL import ImageTk,Image
import mysql.connector as mysql
import random
from datetime import datetime

root= Tk()
root.geometry("1200x650+100+20")
root.title("RESTAURANT MANAGEMENT SYSTEM")

f= Frame(root,bd=30, relief=RAISED)
f.pack(side=TOP)

f1 = Frame(root,bd=20,height=300,width=100,relief=RAISED)
f1.pack(side=LEFT,fill="both", expand=1)

f2 = Frame(root,bd=20,height=400, width=300, relief=RAISED)

f3 = Frame(root,bd=20, height=400,width=450,relief=RAISED)
f3.pack(side=BOTTOM)

lbl_info= Label(f, font=('aria', 30, 'bold'),text="MURUGAN IDLY KADAI")
lbl_info.pack(side=LEFT)

now = datetime.now()
localtime = now.strftime("%d/%m/%Y %H:%M:%S")

rand         = StringVar()
Moongdalidly = StringVar()
Oatsravaidly = StringVar()
Quickravaidly= StringVar()
Soojiidly     = StringVar()
Doubleduckeridly = StringVar()
Pohaidly      = StringVar()
Total          = StringVar()
Tax            = StringVar()
cost           = StringVar()
date           = StringVar()
service_charge = StringVar()

lbl_Moongdalidly = Label(f1,bd=5, font=('roman', 20, 'bold'),relief=RIDGE,text="Moong dal idly Rs.180")
lbl_Moongdalidly.grid(row=1,column=0)
txt_Moongdalidly = Entry(f1,bd=5, font=('roman', 20, 'bold'),relief=SUNKEN,textvariable=Moongdalidly)
txt_Moongdalidly.grid(row=1,column=1)

lbl_Oatsravaidly = Label(f1, font=('roman', 20, 'bold'),relief=RIDGE,text="Oats rava idly Rs.150")
lbl_Oatsravaidly.grid(row=2,column=0)
txt_Oatsravaidly = Entry(f1,bd=5, font=('roman', 20, 'bold'),relief=SUNKEN,textvariable=Oatsravaidly)
txt_Oatsravaidly.grid(row=2,column=1)

lbl_Quickravaidly = Label(f1, font=('roman', 20, 'bold'),relief=RIDGE,text="Quick rava idly Rs.150")
lbl_Quickravaidly.grid(row=3,column=0)
txt_Quickravaidly= Entry(f1,bd=5, font=('roman', 20, 'bold'),relief=SUNKEN,textvariable=Quickravaidly)
txt_Quickravaidly.grid(row=3,column=1)

lbl_Soojiidly  = Label(f1, font=('roman', 20, 'bold'),relief=RIDGE,text="Sooji idly  Rs.200")
lbl_Soojiidly .grid(row=4,column=0)
txt_Soojiidly  = Entry(f1,bd=5, font=('roman', 20, 'bold'),relief=SUNKEN,textvariable=Soojiidly )
txt_Soojiidly .grid(row=4,column=1)

lbl_Doubleduckeridly  = Label(f1, font=('roman', 20, 'bold'),relief=RIDGE,text="Double ducker idly Rs.200")
lbl_Doubleduckeridly .grid(row=5,column=0)
txt_Doubleduckeridly = Entry(f1,bd=5, font=('roman', 20, 'bold'),relief=SUNKEN,textvariable=Doubleduckeridly)
txt_Doubleduckeridly.grid(row=5,column=1)

lbl_Pohaidly  = Label(f1, font=('roman', 20, 'bold'),relief=RIDGE,text="Poha idly   Rs.200")
lbl_Pohaidly.grid(row=6,column=0)
txt_Pohaidly = Entry(f1,bd=5, font=('roman', 20, 'bold'),relief=SUNKEN,textvariable=Pohaidly )
txt_Pohaidly.grid(row=6,column=1)

def generate_bill():
    bill_no = str(random.randint(15000, 50000))
    rand.set(bill_no)
    date.set(localtime)
    try: qm = int(Moongdalidly.get())
    except: qm = 0
    try: qo = int(Oatsravaidly.get())
    except: qo = 0
    try: qq = int(Quickravaidly.get())
    except: qq = 0
    try: qs = int(Soojiidly.get())
    except: qs = 0
    try: qd = int(Doubleduckeridly.get())
    except: qd = 0
    try: qp = int(Pohaidly.get())
    except: qp = 0

    costofmoongdalidly = qm * 180 
    costofoatsravaidly = qo * 150
    costofquickravaidly = qq * 150
    costofsoojiidly    = qs * 200
    costofdoubleducker = qd * 200
    costofpohaidly     = qp * 200

    f2.pack(side=RIGHT, fill="both", expand=1)
    
    lbl_bill = Label(f2, font=('aria', 15, 'bold'), text="Bill no")
    lbl_bill.grid(row=1,column=0)


    lbl_date = Label(f2, font=('aria', 15, 'bold'), text="Date")
    lbl_date.grid(row=2,column=0)
   

    lbl_cost = Label(f2, font=('aria', 15, 'bold'), text="Cost")
    lbl_cost.grid(row=3,column=0)
    

    lbl_service = Label(f2, font=('aria', 15, 'bold'), text="Service charge")
    lbl_service.grid(row=4,column=0)
    
    lbl_tax = Label(f2, font=('aria', 15, 'bold'), text="Tax")
    lbl_tax.grid(row=5,column=0)
    

    lbl_total = Label(f2, font=('aria', 15, 'bold'), text="Total")
    lbl_total.grid(row=6,column=0)
    
    Totalcost= costofmoongdalidly + costofoatsravaidly + costofquickravaidly + costofsoojiidly + costofdoubleducker + costofpohaidly
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

txt_bill = Entry(f2,width=17, font=('ariel', 12, 'bold'),textvariable=rand)
txt_bill.grid(row=1, column=1)

txt_date = Entry(f2,width=17, font=('ariel', 12, 'bold'),textvariable=date)
txt_date.grid(row=2, column=1)

txt_cost = Entry(f2,width=17, font=('ariel', 12, 'bold'),textvariable=cost)
txt_cost.grid(row=3, column=1)

txt_service = Entry(f2,width=17, font=('ariel', 12, 'bold'),textvariable=service_charge)
txt_service.grid(row=4, column=1)

txt_tax = Entry(f2,width=17, font=('ariel', 12, 'bold'),textvariable=Tax)
txt_tax.grid(row=5, column=1)

txt_total = Entry(f2,width=17, font=('ariel', 12, 'bold'),textvariable=Total)
txt_total.grid(row=6, column=1)

def qexit():
    root.destroy()

def reset():
    Moongdalidly.set('') 
    Oatsravaidly.set('')  
    Quickravaidly.set('') 
    Soojiidly.set('')      
    Doubleduckeridly.set('')  
    Pohaidly.set('')
    date.set('')
    f2.pack_forget()

btn_Total = Button(f1, bd=10, fg="black", font=('ariel', 12, 'bold italic'),text="CALCULATE BILL",relief=GROOVE,command=generate_bill)
btn_Total.grid(row=9,column=0)

btn_Reset = Button(f1, bd=10, fg="black", font=('ariel', 12, 'bold italic'),text="RESET",relief=GROOVE,command=reset)
btn_Reset.grid(row=9,column=1)

btn_Exit = Button(f1, bd=10, fg="black", font=('ariel', 12, 'bold italic'),text="EXIT",relief=GROOVE,command=qexit)
btn_Exit.grid(row=9,column=2)

#Calculator


operator=''#7+9
def buttonClick(numbers):#9
    global operator
    operator=operator+numbers
    calculaterField.delete(0,END)
    calculaterField.insert(END,operator)

def clear():
    global operator
    operator=''
    calculaterField.delete(0,END)

def answer():
    global operator
    result=str(eval(operator))
    calculaterField.delete(0,END)
    calculaterField.insert(0,result)
    operator=''



calculaterField=Entry(f3,font=('arial',16,'bold'),width=32,bd=4)
calculaterField.grid(row=0,column=0,columnspan=4)

button7=Button(f3,text='7',font=('arial',16,'bold'),fg='white',bg='blue',bd=6,width=6,
               command=lambda:buttonClick('7'))
button7.grid(row=1,column=0)

button8=Button(f3,text='8',font=('arial',16,'bold'),fg='white',bg='blue',bd=6,width=6,
               command=lambda:buttonClick('8'))
button8.grid(row=1,column=1)

button9=Button(f3,text='9',font=('arial',16,'bold'),fg='white',bg='blue',bd=6,width=6,
               command=lambda:buttonClick('9'))
button9.grid(row=1,column=2)

buttonPlus=Button(f3,text='+',font=('arial',16,'bold'),fg='white',bg='blue',bd=6,width=6,
                  command=lambda:buttonClick('+'))
buttonPlus.grid(row=1,column=3)

button4=Button(f3,text='4',font=('arial',16,'bold'),fg='white',bg='blue',bd=6,width=6,
               command=lambda:buttonClick('4'))
button4.grid(row=2,column=0)

button5=Button(f3,text='5',font=('arial',16,'bold'),fg='red4',bg='white',bd=6,width=6,
               command=lambda:buttonClick('5'))
button5.grid(row=2,column=1)

button6=Button(f3,text='6',font=('arial',16,'bold'),fg='red4',bg='white',bd=6,width=6,
               command=lambda:buttonClick('6'))
button6.grid(row=2,column=2)

buttonMinus=Button(f3,text='-',font=('arial',16,'bold'),fg='white',bg='blue',bd=6,width=6,
                   command=lambda:buttonClick('-'))
buttonMinus.grid(row=2,column=3)

button1=Button(f3,text='1',font=('arial',16,'bold'),fg='white',bg='blue',bd=6,width=6,
               command=lambda:buttonClick('1'))
button1.grid(row=3,column=0)

button2=Button(f3,text='2',font=('arial',16,'bold'),fg='red4',bg='white',bd=6,width=6,
               command=lambda:buttonClick('2'))
button2.grid(row=3,column=1)

button3=Button(f3,text='3',font=('arial',16,'bold'),fg='red4',bg='white',bd=6,width=6,
               command=lambda:buttonClick('3'))
button3.grid(row=3,column=2)

buttonMult=Button(f3,text='*',font=('arial',16,'bold'),fg='white',bg='blue',bd=6,width=6,
                  command=lambda:buttonClick('*'))
buttonMult.grid(row=3,column=3)

buttonAns=Button(f3,text='Ans',font=('arial',16,'bold'),fg='white',bg='blue',bd=6,width=6,
                 command=answer)
buttonAns.grid(row=4,column=0)

buttonClear=Button(f3,text='Clear',font=('arial',16,'bold'),fg='white',bg='blue',bd=6,width=6,
                   command=clear)
buttonClear.grid(row=4,column=1)

button0=Button(f3,text='0',font=('arial',16,'bold'),fg='white',bg='blue',bd=6,width=6,
               command=lambda:buttonClick('0'))
button0.grid(row=4,column=2)

buttonDiv=Button(f3,text='/',font=('arial',16,'bold'),fg='white',bg='blue',bd=6,width=6,
                 command=lambda:buttonClick('/'))
buttonDiv.grid(row=4,column=3)




root.mainloop()







