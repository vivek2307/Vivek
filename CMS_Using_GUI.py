from tkinter import *
from tkinter import messagebox
import sqlite3
# from playsound import playsound
#from tkinter.ttk import *


globals()
def randomID():
    import random
    import string
    global randID
    randID = ''.join([random.choice(string.digits) for n in range(10)])
    return randID

def add_check(x):

    if len(Mob)==10:
        if (int(Age)>=10) and (int(Age)<=80):
            x=' '.join(x)
            file=open("CMS.txt","a+")
            file.write(x)
            file.write("\n")
            file.close()
            messagebox.showinfo("CMS","Customer Added Successfully...")
            messagebox.showinfo("Customer Id is...",randID)
            addcust.destroy()
        else:
            messagebox.showinfo("Error","Invalid Age...")
            addCustomer()
    else:
        messagebox.showinfo("Error","Invalid Mobile No....")
        addCustomer()

def add_cust():
    global Name,Age,Mob,Email,Address,Pin,L
    L=[]
    Name=entryName.get()
    Age=entryAge.get()
    Mob=entryMob.get()
    Email=entryEmail.get()
    Address=entryAddress.get()
    Pin=entryPin.get()

    if(Name!="",Age!="",Mob!="",Email!="",Address!="",Pin!=""):
        randomID()
        L.append(randID)
        L.append(Name)
        L.append(Age)
        L.append(Mob)
        L.append(Email)
        L.append(Address)
        L.append(Pin)
        add_check(L)
    else:
        messagebox.showerror("Error","Invalid....")

def addCustomer():
    global entryName,entryAge,entryMob,entryEmail,entryAddress,entryPin
    global addcust
    addcust = Tk()
    addcust.geometry("700x500+332+100")
    addcust["bg"] = "light green"
    addcust.title("Add Customer")
    ma_fram = Frame(addcust, bg='light green')
    frame_la = Frame(ma_fram, bg='light green')
    frame_en = Frame(ma_fram, bg='light green')
    lbaddcus = Label(addcust, text="Add Customer", font=('comic sans', 20, 'italic bold'), bg="yellow", fg="Green")
    lbaddcus2 = Label(addcust, text=" ------------------------------------------------------------------------ ",fg="black", bg="light green")
    lbaddcus3= Label(addcust, text=" ------------------------------------------------------------------------ ",fg="black", bg="light green")
    lblname = Label(frame_la, text=" Name ", font=("arial", 12, "bold"), bg="light green", fg="red")
    lblgen = Label(frame_la, text=" Gender ", font=("arial", 12, "bold"), bg="light green", fg="red")
    lblage = Label(frame_la, text=" Age ", font=("arial", 12, "bold"), bg="light green", fg="red")
    lblmob = Label(frame_la, text=" Mobile ", font=("arial", 12, "bold"), bg="light green", fg="red")
    lblemail = Label(frame_la, text=" E-Mail ", font=("arial", 12, "bold"), bg="light green", fg="red")
    lbladd = Label(frame_la, text=" Address ", font=("arial", 12, "bold"), bg="light green", fg="red")
    lblpin = Label(frame_la, text=" Pincode ", font=("arial", 12, "bold"), bg="light green", fg="red")

    rbmale = Radiobutton(frame_en,value=1,text='  Male ',bg='light green')
    rbfemale = Radiobutton(frame_en, value=2, text=' Female ',bg='light green')

    bsubmit = Button(addcust, text=" submit ", font=15, bg="green", fg="black",command=add_cust)
    btnclose = Button(addcust, text = "Close", bg="yellow",fg="Green", command = addcust.destroy)

    varName = StringVar()
    entryName = Entry(frame_en, textvariable=varName, font=1)
    varAge = IntVar()
    entryAge = Entry(frame_en, textvariable=varAge, font=1)
    varMob = IntVar()
    entryMob = Entry(frame_en, textvariable=varMob, font=1)
    varEmail = StringVar()
    entryEmail = Entry(frame_en, textvariable=varEmail, font=1)
    varName = StringVar()
    entryAddress = Entry(frame_en, textvariable=varName, font=1)
    varPin = IntVar()
    entryPin = Entry(frame_en, textvariable=varPin, font=1)

    lbaddcus2.pack(pady='8')
    lbaddcus.pack()
    lbaddcus3.pack(pady='8')

    ma_fram.pack(pady='8')
    frame_la.pack(side='left')
    lblname.pack(padx='20')
    lblage.pack(padx='20')
    lblmob.pack(padx='20')
    lblemail.pack(padx='20')
    lbladd.pack(padx='20')
    lblpin.pack(padx='20')
    lblgen.pack(padx='20')
    frame_en.pack(side='right', anchor='n', pady='4')
    entryName.pack(pady='2')
    entryAge.pack(pady='2')
    entryMob.pack(pady='2')
    entryEmail.pack(pady='2')
    entryAddress.pack(pady='2')
    entryPin.pack(pady='2')
    rbmale.pack(side='left', pady='5')
    rbfemale.pack(side='right')
    bsubmit.pack(pady='8')
    btnclose.pack()

    addcust.mainloop()

def searchCustomer():
    srcust = Tk()
    srcust.geometry("400x250+332+100")
    srcust["bg"] = "light blue"
    srcust.title("Search Customer")
    lbsearcus = Label(srcust, text="Search Customer", font=('comic sans', 20, 'italic bold'), bg="yellow", fg="Green").pack(pady = 20)
    lblid = Label(srcust, text="Enter Customer ID ",font=('ariel',13,'bold')).pack(pady=10)
    varId = StringVar()
    entryId = Entry(srcust, textvariable=varId, font=1,bd=2).pack(pady=10)
    bsearch = Button(srcust, text=" Search ", font=15, bg="green", fg="black",command=showCustomer).pack(pady=10)
    btnclose = Button(srcust, text="Close", bg="yellow", fg="Green", command=srcust.destroy).pack()

    srcust.mainloop()

def deleteCustomer():
    delcust = Tk()
    delcust.geometry("700x500+332+100")
    delcust["bg"] = "light blue"
    delcust.title("Delete Customer")
    lbsearcus = Label(delcust, text="Delete Customer", font=('comic sans', 20, 'italic bold'), bg="yellow",fg="Green").pack(pady=20)
    lblid = Label(delcust, text="Enter Customer ID ",font=('ariel',13,'bold')).pack(pady=10)
    varId = StringVar()
    entryId = Entry(delcust, textvariable=varId, font=1,bd=2).pack(pady=10)
    bdelete = Button(delcust, text=" Delete ", bg="green", fg="black").pack(pady=10)
    btnclose = Button(delcust, text="Close", bg="yellow", fg="Green", command=delcust.destroy).pack()
    delcust.mainloop()

def modifyCustomer():
    modcust = Tk()
    modcust.geometry("700x500+332+100")
    modcust["bg"] = "light blue"
    modcust.title("Add Customer")
    bmodify = Button(modcust, text=" Modify ", font=15, bg="green", fg="black").pack(pady=10)
    btnclose = Button(modcust, text="Close", bg="yellow", fg="Green", command=modcust.destroy).pack()
    modcust.mainloop()

def showCustomer():
    showcust = Tk()
    showcust.geometry("1000x500+332+100")
    showcust["bg"] = "light blue"
    showcust.title("Show Customer Details")
    lblId1 = Label(showcust,text="CUST ID",font=1,width=12,bg="orange")
    lblName1 = Label(showcust, text="CUST Name", font=1, width=12, bg="orange")
    lblGen1 = Label(showcust, text="CUST Gender", font=1, width=12, bg="orange")
    lblAge1 = Label(showcust, text="CUST Age", font=1, width=12, bg="orange")
    lblMob1 = Label(showcust, text="CUST Mob", font=1, width=12, bg="orange")
    lblEmail1 = Label(showcust, text="CUST Email", font=1, width=12, bg="orange")
    lblAdd1 = Label(showcust, text="CUST Address", font=1, width=12, bg="orange")
    lblPin1 = Label(showcust, text="CUST Pincode", font=1, width=12, bg="orange")
    lblId1.grid(row=0,column=0)
    lblName1.grid(row=0,column=1)
    lblGen1.grid(row=0, column=2)
    lblAge1.grid(row=0,column=3)
    lblMob1.grid(row=0,column=4)
    lblEmail1.grid(row=0,column=5)
    lblAdd1.grid(row=0,column=6)
    lblPin1.grid(row=0,column=7)

    showcust.mainloop()
#showCustomer()

def dashboard():
    messagebox.showinfo("CMS", "Login Successful")
    frntpg.destroy()
    dashpg = Tk()
    dashpg["bg"] = "violet"
    dashpg.geometry("700x500+332+100")
    dashpg.title("Dashboard")

    btnAdd = Button(dashpg, text="Add Customer", font=('ariel',15,'italic'), bg="yellow",fg="Green", width=15, command = addCustomer)
    btnAdd.pack()

    btnSearch = Button(dashpg, text="Search Customer", font=('ariel',15,'italic'), bg="yellow",fg="Green", width=15, command = searchCustomer)
    btnSearch.pack()

    btnDelete = Button(dashpg, text="Delete Customer", font=('ariel',15,'italic'), bg="yellow",fg="Green", width=15, command = deleteCustomer)
    btnDelete.pack()

    btnModify = Button(dashpg, text="Modify Customer", font=('ariel',15,'italic'), bg="yellow",fg="Green", width=15, command = modifyCustomer)
    btnModify.pack()

    btnAll = Button(dashpg, text="Display All Customer", font=('ariel',15,'italic'), bg="yellow",fg="Green", width=15, command = showCustomer)
    btnAll.pack()

    btnExit = Button(dashpg, text = "Exit", font=('ariel',15,'italic'), bg="yellow",fg="Green", command = dashpg.destroy)
    btnExit.pack()

    dashpg.mainloop()


def forgetpassword():
    frntpg.destroy()
    frgtpass = Tk()
    frgtpass.geometry("600x450+350+150")
    frgtpass.title("Forgot Password")
    frgtpass["bg"] = "light blue"
    lbemail = Label(frgtpass, text="Enter Your Registered Email ID ", font=2)
    lbemail.pack(pady=15)
    email = StringVar()
    email = Entry(frgtpass, textvariable=email, font=1)
    email.pack(pady=10)
    lbmobileno = Label(frgtpass, text="Enter Your Registered Mobile No. ", font=2)
    lbmobileno.pack(padx=15)
    mobileno = IntVar
    mobileno = Entry(frgtpass, textvariable=mobileno, font=1)
    mobileno.pack(pady=10)
    btsbmt = Button(frgtpass, text="Submit", font=1, bg="red", command=dashboard)
    btsbmt.pack(pady=15)

    frgtpass.mainloop()

# BLL

frntpg = Tk()
frntpg.geometry("700x500+332+100")
frntpg["bg"]="light green"
frntpg.title("Customer Management System")
lbadmin=Label(frntpg,text="ADMIN Login Page",font=('comic sans',20,'italic'), bg="yellow",fg="Green")
lbadmin.pack(pady=80)
lbuser=Label(frntpg,text = "Username",font=2)
lbuser.pack(padx=20)
username=StringVar()
username=Entry(frntpg,textvariable=username,font=1)
username.pack(pady=5)
lbpass=Label(frntpg,text = "Password",font=2)
lbpass.pack(padx=10)
password = StringVar
password=Entry(frntpg,textvariable=password,font=1)
password.pack(pady=5)
btlogin = Button(frntpg,text="Login", font=1, bg = "red",command=dashboard)
btlogin.pack(pady=15)
lbfrgt = Button(frntpg,text="Forgot Password ?",font=1,command=forgetpassword)
lbfrgt.pack()

frntpg.mainloop()

