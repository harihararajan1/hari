from tkinter.ttk import*
from tkinter import *
import mysql.connector as mysql

#to create parent window
#-----------------------
root = Tk()
root.geometry("350x450")
root.title("Student Data Window")


Label(root, text='STUDENT DATA',font=('arial',10,'bold')).pack()

Label(root, text='student name',font=('arial',10)).pack()
e1 = Entry(root,width=30)
e1.pack()

Label(root, text='student age',font=('arial',10)).pack()
e2 = Entry(root,width=30)
e2.pack()

Label(root, text='student city',font=('arial',10)).pack()
e3 = Entry(root,width=30)
e3.pack()

Label(root, text='student qualification',font=('arial',10)).pack()
c1 = Combobox(root)
c1['value'] = ('BE','BTECH','ME','MTECH','BSc','MSc','MBA')
c1.current(0)
c1.pack()

Label(root, text='academic year',font=('arial',10)).pack()
s1 = Spinbox(root, from_=2017,to=2021)
s1.pack()

Label(root,text='current semester',font=('arial',10)).pack()
s2 = Spinbox(root, from_=1,to=8)
s2.pack()

Label(root, text='student gender',font=('arial',10)).pack()
c2 = Combobox(root)
c2['value'] = ('Male','Female','Transgender')
c2.current(0)
c2.pack()

Label(root,text='student mail id',font=('arial',10)).pack()
e4 = Entry(root,width=30)
e4.pack()

Label(root,text='student contact number',font=('arial',10)).pack()
e5 = Entry(root,width=30)
e5.pack()




#to create toplevel of parent window
#------------------------
def extra_root():
    new_root = Toplevel(root)
    new_root.title("Student Information Window")
    new_root.geometry("350x450")
    
    Label(new_root,text='STUDENT INFORMATION',font=('arial',10,'bold')).pack()
    
    Label(new_root, text=e1.get(),font=('arial',10)).pack()
    
    Label(new_root, text=e2.get(),font=('arial',10)).pack()
    
    Label(new_root, text=e3.get(),font=('arial',10)).pack()
    
    Label(new_root, text=c1.get(),font=('arial',10)).pack()
    
    Label(new_root, text=s1.get(),font=('arial',10)).pack()
    
    Label(new_root, text=s2.get(),font=('arial',10)).pack()
    
    Label(new_root, text=c2.get(),font=('arial',10)).pack()
    
    Label(new_root, text=e4.get(),font=('arial',10)).pack()
    
    Label(new_root, text=e5.get(),font=('arial',10)).pack()
    

    new_root.mainloop()


Button(root,text='Get Details', command=extra_root).pack()
#database connection
#-------------------
def save_data():
    name = e1.get()
    age = e2.get()
    city = e3.get()
    qualification = c1.get()
    acadyear = s1.get()
    cursem = s2.get()
    gender = c2.get()
    mail = e4.get()
    contact = e5.get()

    con = mysql.connect(host="localhost",user="root",password="",database="student_record")
    cursor = con.cursor()
    cursor.execute("insert into stud_info values('"+ name +"','"+ age +"','"+ city +"','"+ qualification +"','"+ acadyear +"','"+ cursem +"','"+ gender +"','"+ mail +"','"+ contact +"')")
    cursor.execute("commit")

    con.close()
   
    

Button(root,text='Save Details', command=save_data).pack()

root.mainloop()


