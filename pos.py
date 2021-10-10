from tkinter import *
from tkinter import messagebox
import sqlite3
from tkinter import ttk

window = Tk()
window.geometry('1100x700+100+100')
window.option_add('*font','Leelawadee 14 bold')
window.title("Coffee Cafe POS System")
window.config(bg='dodgerblue4')
window.resizable(width=False, height=False)
window.rowconfigure(0,weight=1)
window.columnconfigure(0,weight=1)

def home(parent) :
    connection()
    fm_login = login(parent)
    userentry.delete(0,END)
    pwdentry.delete(0,END)
    fm_login.place(x=0,y=0)

def mainfunc(parent) :
    global fm
    conn = sqlite3.connect('final.db')
    cursor = conn.cursor()
    sql = 'select * from cashier where username=? '
    cursor.execute(sql,[userinfo.get()])
    info = cursor.fetchone()
    conn.close()
    
    window.option_add('*font','Leelawadee 14 bold')
    #โซนชื่อด้านบน
    fm = Frame(parent,width=1100,height=700,bg='green').place(x=0,y=0)
    Label(fm,image=img0).place(x=-20,y=-20)
    Frame(fm,width=1040,height=640,bg='#A2805D').place(x=30,y=30)
    Label(fm,text="Mocca Coffee Cafe POS System",bg='#A2805D',font=("Leelawadee",24,"bold")).place(x=320,y=40)

    #โซนข่องใส่ข้อมูล
    # Frame(fm,width=950,height=100,bg="blue").place(x=75,y=95)
    Label(fm,image=img5,bg='#A2805D').place(x=75,y=95)
    Label(fm,text='Cashier Information : '+info[0],bg='#C4C4C4').place(x=120,y=120)
    Button(fm,text='Log Out',bg='#F6EEE0',fg='black',font=('Leelawadee', 14, 'bold'),command=lambda:home(parent)).place(x=870,y=115)
    
    
    # Label(fm,text="Customer Information :",font=("Leelawadee",16,"bold")).place(x=95,y=105)
    # Label(fm,text="Bill numbers :",font=("Leelawadee",16,"bold")).place(x=95,y=140)
    # bill_num = Entry(fm,width=12,bd=2)
    # bill_num.place(x=250,y=140)
    # Label(fm,text="Customers name :",font=("Leelawadee",16,"bold")).place(x=495,y=140)
    # bill_num = Entry(fm,width=14,bd=2)
    # bill_num.place(x=700,y=140)
    

    #ช่องกรอกรายละเอียดสินค้าที่จะซื้อ
    # Frame(fm,width=325,height=350,bg="blue").place(x=75,y=200)
    Label(fm,image=img2,bg='#A2805D').place(x=75,y=200)
    Label(fm,text='Customer name :',bg='#C4C4C4').place(x=90,y=215)
    Entry(fm,width=12,bd=2,textvariable=customname).place(x=250,y=215)

    Button(fm,text='OK',bg='#F6EEE0',fg='black',font=('Leelawadee', 13, 'bold'),command=lambda:namecheck(parent)).place(x=400,y=213)

    #เหลือบาน

    #ช่องที่เกี่ยวกับการชำระเงิน
    # Frame(fm,width=325,height=100,bg="green").place(x=75,y=565)
    Label(fm,image=img3,bg='#A2805D').place(x=75,y=580)
    Button(fm,text='Edit product',bg='#F6EEE0',fg='black',font=('Leelawadee', 14, 'bold'),command=lambda:editproduct(parent)).place(x=145,y=600)

    #ขวาบน
    Label(fm,image=img3,bg='#A2805D').place(x=710,y=185)
    Button(fm,text='Check orders history',bg='#F6EEE0',fg='black',font=('Leelawadee', 14, 'bold'),command=lambda:orderhistory(parent)).place(x=740,y=205)

    #ซ้ายล่าง
    Label(fm,image=img6,bg='#A2805D').place(x=75,y=270)
    #Button(fm,text='Total',bg='#A2805D',fg='black',font=('Leelawadee', 14, 'bold')).place(x=900,y=550)

    #ขวาล่าง
    Button(fm,text='Submit order',bg='#F6EEE0',fg='black',font=('Leelawadee', 14, 'bold'),command=lambda:submit(parent)).place(x=560,y=600)
    Button(fm,text='Clear this order',bg='#F6EEE0',fg='black',font=('Leelawadee', 14, 'bold')).place(x=780,y=600)

    return fm


def namecheck(parent) :
    if customname == "" :
        messagebox.showwarning('Admin :','Enter customer name before submit.')
    else :
        buylist(parent)

def buylist(parent) :

    # จำนวนที่จะซื้อกาแฟ
    list_quan = ('0','1', '2', '3', '4', '5')

    #ภาพ + ชื่อกาแฟ + SpinBox
    Label(fm,image=img_cof1,bg='#C4C4C4').place(x=100,y=330)
    cof1_spin = ttk.Combobox(fm, justify=CENTER,font=('Leelawadee', 14, 'bold'), state='readonly', width=4)
    cof1_spin['values'] = list_quan
    cof1_spin.current(0)
    cof1_spin.place(x=218,y=350)
    Label(fm,text='Americano',bg='#C4C4C4',font=('Leelawadee', 12, 'bold')).place(x=210,y=310)

    Label(fm,image=img_cof2,bg='#C4C4C4').place(x=325,y=315)
    cof2_spin = ttk.Combobox(fm, justify=CENTER,font=('Leelawadee', 14, 'bold'), state='readonly', width=4)
    cof2_spin['values'] = list_quan
    cof2_spin.current(0)
    cof2_spin.place(x=443,y=350)
    Label(fm,text='Cappuccino',bg='#C4C4C4',font=('Leelawadee', 12, 'bold')).place(x=430,y=310)

    Label(fm,image=img_cof3,bg='#C4C4C4').place(x=560,y=330)
    cof3_spin = ttk.Combobox(fm, justify=CENTER,font=('Leelawadee', 14, 'bold'), state='readonly', width=4)
    cof3_spin['values'] = list_quan
    cof3_spin.current(0)
    cof3_spin.place(x=678,y=350)
    Label(fm,text='Cortado',bg='#C4C4C4',font=('Leelawadee', 12, 'bold')).place(x=675,y=310)

    Label(fm,image=img_cof4,bg='#C4C4C4').place(x=810,y=305)
    cof4_spin = ttk.Combobox(fm, justify=CENTER,font=('Leelawadee', 14, 'bold'), state='readonly', width=4)
    cof4_spin['values'] = list_quan
    cof4_spin.current(0)
    cof4_spin.place(x=890,y=350)
    Label(fm,text='Frappe',bg='#C4C4C4',font=('Leelawadee', 12, 'bold')).place(x=887,y=310)

    Label(fm,image=img_cof5,bg='#C4C4C4').place(x=115,y=455)
    cof5_spin = ttk.Combobox(fm, justify=CENTER,font=('Leelawadee', 14, 'bold'), state='readonly', width=4)
    cof5_spin['values'] = list_quan
    cof5_spin.current(0)
    cof5_spin.place(x=218,y=490)
    Label(fm,text='Irish',bg='#C4C4C4',font=('Leelawadee', 12, 'bold')).place(x=229,y=450)

    Label(fm,image=img_cof6,bg='#C4C4C4').place(x=325,y=470)
    cof6_spin = ttk.Combobox(fm, justify=CENTER,font=('Leelawadee', 14, 'bold'), state='readonly', width=4)
    cof6_spin['values'] = list_quan
    cof6_spin.current(0)
    cof6_spin.place(x=438,y=490)
    Label(fm,text='Latte',bg='#C4C4C4',font=('Leelawadee', 12, 'bold')).place(x=450,y=450)

    Label(fm,image=img_cof7,bg='#C4C4C4').place(x=560,y=470)
    cof7_spin = ttk.Combobox(fm, justify=CENTER,font=('Leelawadee', 14, 'bold'), state='readonly', width=4)
    cof7_spin['values'] = list_quan
    cof7_spin.current(0)
    cof7_spin.place(x=678,y=490)
    Label(fm,text='Marocchino',bg='#C4C4C4',font=('Leelawadee', 12, 'bold')).place(x=665,y=450)

    Label(fm,image=img_cof8,bg='#C4C4C4').place(x=810,y=450)
    cof8_spin = ttk.Combobox(fm, justify=CENTER,font=('Leelawadee', 14, 'bold'), state='readonly', width=4)
    cof8_spin['values'] = list_quan
    cof8_spin.current(0)
    cof8_spin.place(x=890,y=490)
    Label(fm,text='Mocha',bg='#C4C4C4',font=('Leelawadee', 12, 'bold')).place(x=888,y=450)


    return fm


def orderhistory(parent) :
    conn = sqlite3.connect('final.db')
    cursor = conn.cursor()
    sql = 'select * from cashier where username=? '
    cursor.execute(sql,[userinfo.get()])
    info = cursor.fetchone()
    conn.close()

    fm = Frame(parent,width=1100,height=700,bg='#A2805D').place(x=0,y=0)
    Frame(fm,width=1100,height=100,bg='#C4C4C4').place(x=0,y=0)
    Label(fm,text='Chech orders history by Cashier  :     '+info[0],bg='#C4C4C4',font=('Leelawadee', 18, 'bold')).place(x=210,y=35)

    #Label(fm,bg='#65A8EA',fg='#FFFFFF').place(x=405,y=25)
    #Frame(fm,width=500,height=500,bg='#65A8EA').place(x=250,y=300)
    #Label(fm,bg='#A2805D').place(x=400,y=165)
    Label(fm,image=img_logo,bg='#A2805D').place(x=470,y=110)

    Button(fm,text='Exit Program',bg='#F9AABE',fg='#F97D7D',bd=1,command=quit).place(x=200,y=625)
    Button(fm,text='Back to menu',bg='#F2DEB1',fg='#E8B964',bd=1,command=lambda:mainfunc(parent)).place(x=500,y=625)
    Button(fm,text='Clear all data',bg='#F2DEB1',fg='#E8B964',bd=1).place(x=800,y=625)

    #Create TreeView Frame
    treeframe = Frame(fm)
    treeframe.place(x=200,y=300)
    #Create Scrollbar
    treebar = Scrollbar(treeframe)
    treebar.pack(side=RIGHT,fill=Y)
    #Create Treeview
    mytree = ttk.Treeview(treeframe,columns=("RANK","NAME","SCORE"),yscrollcommand=treebar.set)
    mytree.pack()
    #config scrollbar on the treeview
    treebar.config(command=mytree.yview)
    #create headings
    mytree.heading("#0",text="",anchor=W)
    mytree.heading("RANK",text="Name",anchor=CENTER)
    mytree.heading("NAME",text="Products",anchor=CENTER)
    mytree.heading("SCORE",text="Total",anchor=CENTER)
    #Format our columns
    mytree.column("#0",width=0,minwidth=0) #set minwidth=0 for disable the first column
    mytree.column("RANK",anchor=CENTER,width=150)
    mytree.column("NAME",anchor=CENTER,width=400)
    mytree.column("SCORE",anchor=CENTER,width=150)


def editproduct(parent) :
    conn = sqlite3.connect('final.db')
    cursor = conn.cursor()
    sql = 'select * from cashier where username=? '
    cursor.execute(sql,[userinfo.get()])
    info = cursor.fetchone()
    conn.close()

    fm = Frame(parent,width=1100,height=700,bg='#A2805D').place(x=0,y=0)
    Frame(fm,width=1100,height=100,bg='#C4C4C4').place(x=0,y=0)
    Label(fm,text='Edit Product by Cashier  :     '+info[0],bg='#C4C4C4',font=('Leelawadee', 18, 'bold')).place(x=210,y=35)

    #Label(fm,bg='#65A8EA',fg='#FFFFFF').place(x=405,y=25)
    #Frame(fm,width=500,height=500,bg='#65A8EA').place(x=250,y=300)
    #Label(fm,bg='#A2805D').place(x=400,y=165)
    Label(fm,image=img_logo,bg='#A2805D').place(x=470,y=110)

    Button(fm,text='Exit Program',bg='#F9AABE',fg='#F97D7D',bd=1,command=quit).place(x=200,y=625)
    Button(fm,text='Back to menu',bg='#F2DEB1',fg='#E8B964',bd=1,command=lambda:mainfunc(parent)).place(x=500,y=625)
    Button(fm,text='Clear all data',bg='#F2DEB1',fg='#E8B964',bd=1).place(x=800,y=625)

    #Create TreeView Frame
    treeframe = Frame(fm)
    treeframe.place(x=200,y=300)
    #Create Scrollbar
    treebar = Scrollbar(treeframe)
    treebar.pack(side=RIGHT,fill=Y)
    #Create Treeview
    mytree = ttk.Treeview(treeframe,columns=("ID","NAME","COST","QUANTITY"),yscrollcommand=treebar.set)
    mytree.pack()
    #config scrollbar on the treeview
    treebar.config(command=mytree.yview)
    #create headings
    mytree.heading("#0",text="",anchor=CENTER)
    mytree.heading("ID",text="ID",anchor=CENTER)
    mytree.heading("NAME",text="Products",anchor=CENTER)
    mytree.heading("COST",text="Cost",anchor=CENTER)
    mytree.heading("QUANTITY",text="Quantity",anchor=CENTER)
    #Format our columns
    mytree.column("#0",width=0,minwidth=0) #set minwidth=0 for disable the first column
    mytree.column("ID",anchor=CENTER,width=100)
    mytree.column("NAME",anchor=CENTER,width=350)
    mytree.column("COST",anchor=CENTER,width=100)
    mytree.column("QUANTITY",anchor=CENTER,width=100)



def login(parent) :
    global userentry, pwdentry

    fm = Frame(parent,width=1100,height=700,bg='#A2805D')
    Label(fm).place(x=0,y=0)

    Label(fm,image=img1,bg='#A2805D').place(x=280,y=150)
    #Label(fm,image=img_logo,bg='#C4C4C4').place(x=400,y=250)
    Label(fm,text='Mocca POS Admin Account Login',bg='#C4C4C4',fg='#121212').place(x=420,y=200)
    Label(fm,text='Username : ',bg='#C4C4C4',fg='#121212').place(x=380,y=280)
    Label(fm,text='Password : ',bg='#C4C4C4',fg='#121212').place(x=384,y=350)

    userentry = Entry(fm,width=20,textvariable=userinfo,bd=3,bg='#A2805D',fg='#FFFFFF')
    userentry.place(x=560,y=283)
    pwdentry = Entry(fm,width=20,textvariable=pwdinfo,show='*',bd=3,bg='#A2805D',fg='#FFFFFF')
    pwdentry.place(x=560,y=353)
    
    Button(fm,text='Exit',bg='#F9AABE',fg='#F97D7D',width=7,height=2,command=quit).place(x=420,y=450)
    Button(fm,text='Login',bg='#925946',fg='#C4C4C4',width=7,height=2,command=lambda:loginclick(parent)).place(x=620,y=450)

    return fm

def connection() :
    global conn,cursor
    conn = sqlite3.connect('final.db') #แก้ตรงที่อยู่ไฟล์ตรงนี้
    cursor = conn.cursor()

def loginclick(parent) :
    if userinfo.get() == ""  :
        messagebox.showwarning('Admin :','Enter username first')
    elif pwdinfo.get() == "" :
        messagebox.showwarning('Admin :','Enter password first')
    else :
        sql = 'SELECT * FROM cashier WHERE USERNAME=? AND PASSWORD=? '
        cursor.execute(sql,[userinfo.get(),pwdinfo.get()])
        result = cursor.fetchall()
        if result :
            messagebox.showinfo("Admin :","Login Successfully.")
            conn.close()
            mainfunc(parent)
        else :
            messagebox.showwarning('Admin :','Username or Password is invalid')

def submit(parent) :
    
    submit_frame = Toplevel(parent)
    submit_frame.geometry("500x300+200+200")
    submit_frame.title("Submit Order")
    submit_frame.config(bg='#121212')
    submit_frame.resizable(width=False, height=False)

    submit_frame_t = Label(submit_frame,text="List Of Product",font=('Leelawadee', 14, 'bold'),bg='#121212', fg='#B3B3B3')
    submit_frame_t.place(x=40,y=25)

    Label(submit_frame,text='Total Cost : ',font=('Leelawadee', 14, 'bold'),bg='#121212', fg='#B3B3B3').place(x=185,y=175)

    Label(submit_frame,text='Enter Discount Code :',bg='#C4C4C4').place(x=50,y=215)
    Entry(submit_frame,width=12,bd=2,textvariable=customname).place(x=260,y=215)

    Button(submit_frame,text='OK',bg='#F6EEE0',fg='black',font=('Leelawadee', 13, 'bold')).place(x=100,y=260)
    Button(submit_frame,text='Cancel',bg='#F6EEE0',fg='black',font=('Leelawadee', 13, 'bold')).place(x=300,y=260)

# UI
img0 = PhotoImage(file='ui/bg1.png')
img1 = PhotoImage(file='ui/Frame_1.png')
img2 = PhotoImage(file='ui/frame_left.png')
img3 = PhotoImage(file='ui/frame_bot.png')
img4 = PhotoImage(file='ui/but_white.png')
img5 = PhotoImage(file='ui/frame_top.png')
img6 = PhotoImage(file='ui/frame_right.png')

# Coffee + Logo
img_cof1 = PhotoImage(file='coffee/americano.png').subsample(6)
img_cof2 = PhotoImage(file='coffee/cappuccino.png').subsample(6)
img_cof3 = PhotoImage(file='coffee/cortado.png').subsample(6)
img_cof4 = PhotoImage(file='coffee/frappe.png').subsample(6)
img_cof5 = PhotoImage(file='coffee/irish.png').subsample(6)
img_cof6 = PhotoImage(file='coffee/latte.png').subsample(6)
img_cof7 = PhotoImage(file='coffee/marocchino.png').subsample(6)
img_cof8 = PhotoImage(file='coffee/mocha.png').subsample(6)
img_logo = PhotoImage(file='coffee/logo.png').subsample(3)

userinfo = StringVar()
pwdinfo = StringVar()
customname = StringVar()



connection()
home(window)
window.mainloop()