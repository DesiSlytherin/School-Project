#Importing all the necessary libraries and modules
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import DateEntry
import mysql.connector
from PIL import ImageTk, Image
import smtplib

#code for the check command 
def check():
    
    db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '@fr@hT#b#ss#M',
    database = 'python_project'
    )

    cursor = db.cursor()

    
    query1 = "select * from checkin where Aadhar_no = '"+aadhar_entry.get()+"' and cname = '"+Name_entry.get()+"'"
    cursor.execute(query1)
    record = cursor.fetchall()
    y = ''

    for x in record:
        y = str(x) +'\n'

    if y == '':
        messagebox.showinfo("Record status","No records were found")
        aadhar_entry.delete(0,END)
        Name_entry.delete(0,END)
        
    else:
        aadhar_entry.delete(0,END)
        Name_entry.delete(0,END)
        label_record = Label(frame_rec, text = y, bg = 'white')
        label_record.pack()
            

    
    db.close()
    cursor.close()
    

#definition of function auth() - to double check the details of a customer(preventing fraud)
def auth():
    global bg3
    
    
    window2 = Toplevel()
    window2.title("Authentications")
    window2.geometry('600x400')
    

    #opening the image for the background
    bg3 = ImageTk.PhotoImage(Image.open(r"C:\Users\User\OneDrive\Pictures\background1.jpg"))

    #setting up the canvas
    canvas3 = Canvas(window2, height =400, width = 400, border = 0, highlightthickness = 0)
    canvas3.pack(fill = "both",expand = True)
    canvas3.create_image(0,0,image = bg3, anchor ="nw")

    #creating labels for the entry widgets
    canvas3.create_text(60,100,text = "Enter Name", font= ('Comic sans MS',15), fill = "white")
    canvas3.create_text(67,180,text = "Enter Aadhar", font= ('Comic sans MS',15), fill = "white")
    
    #creating entry widget for the aadhar no and Name
    global Name_entry
    Name_entry = Entry(window2, font = ('Comic sans MS',15), width = 15,fg = "#336d92",bg ="white", bd = 0)
    Name_window = canvas3.create_window(140,88,anchor ="nw", window = Name_entry)

    global aadhar_entry
    aadhar_entry = Entry(window2, font = ('Comic sans MS',15), width = 15,fg = "#336d92",bg ="white", bd = 0)
    aadhar_window = canvas3.create_window(140,168,anchor ="nw", window = aadhar_entry)

    #creating a button to check the database
    check_btn = Button(window2,text = "check", font = ('Comic sans MS',12),width = 20, bg = "white",fg = "#336d92",bd = 0, command = check)
    check_btnw = canvas3.create_window(160,280, window = check_btn)

    #creating a global frame
    global frame_rec
    frame_rec = LabelFrame(canvas3, bd = 5,bg = 'white',height = 350, width = 270, relief = RIDGE)
    frame_rec.pack(side = RIGHT, fill = "both", expand = False)

#functions defined for the buttons made below

def enter():
   
    a = code_entry.get()
    b = name_entry.get()
    c = str(Aadhar_entry.get())
    d = str(checkin_entry.get())
    e = str(checkout_entry.get())
    f = str(room_combo.get())
    g = str(roomno_entry.get())

    db = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '@fr@hT#b#ss#M',
        database = 'python_project'
        )

    cursor = db.cursor()

    if (a == "" or b == "" or c == "" or d == "" or e == "" or f == "" or g == ""):

        messagebox.showinfo("Record status","Please make sure all the fields and filled")

    else:
        query_enter = "insert into checkin values('"+ a +"','"+ b +"','"+ c +"','"+ d +"','"+ e +"','"+ g +"','"+ f +"')"
        cursor.execute(query_enter)
        db.commit()

        code_entry.delete(0, END)
        name_entry.delete(0, END)

        Aadhar_entry.delete(0, END)
        roomno_entry.delete(0, END)
        
        checkin_entry.set_date("1/1/2020")
        checkout_entry.set_date("1/1/2020")

        room_combo.delete(0,END)
        room_combo.insert(0,"Duplex")

        messagebox.showinfo("Record status",'Record entered succesfully')
        

    cursor.close()
    db.close()
                

def delete():
    a = code_entry.get()
    
    db = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '@fr@hT#b#ss#M',
        database = 'python_project'
        )

    cursor = db.cursor()

    if a == "" :

        messagebox.showinfo("Record status","Please make sure the code is given")

    else:
        
        response = messagebox.askyesno("Record status","Are you sure you want to delete this record?\nThis action cannot be undone ")

        if response == 1:
            query_delete = "delete from checkin where ccode = '"+a+"'"
            cursor.execute(query_delete)
            db.commit()

            code_entry.delete(0,END)
            name_entry.delete(0, END)

            Aadhar_entry.delete(0, END)
            roomno_entry.delete(0, END)

            checkin_entry.set_date("1/1/2020")
            checkout_entry.set_date("1/1/2020")

            room_combo.delete(0,END)
            room_combo.insert(0,"Duplex")

            messagebox.showinfo("Record Status","The record has been deleted successfully")

    db.close()
    cursor.close()
 

def search():
    a = code_entry.get()
    
    db = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '@fr@hT#b#ss#M',
        database = 'python_project'
        )

    cursor = db.cursor()

    if a == "" :

        messagebox.showinfo("Record status","Please make sure the code is given")

    else:
        search_query = "select * from checkin where ccode = '"+a+"'"
        cursor.execute(search_query)
        result = cursor.fetchall()
        for row in result:

            name_entry.delete(0,END)
            name_entry.insert(0,str(row[1]))
    
            Aadhar_entry.delete(0,END)
            Aadhar_entry.insert(0,str(row[2]))

            checkin_entry.delete(0,END)
            checkin_entry.insert(0,str(row[3]))

            checkout_entry.delete(0,END)
            checkout_entry.insert(0,str(row[4]))

            room_combo.delete(0,END)
            room_combo.insert(0,str(row[6]))

            roomno_entry.delete(0,END)
            roomno_entry.insert(0,str(row[5]))

    cursor.close()
    db.close()


def clear():

    code_entry.delete(0,END)
    name_entry.delete(0,END)
    Aadhar_entry.delete(0,END)

    checkin_entry.set_date("1/1/2020")
    checkout_entry.set_date("1/1/2020")

    room_combo.delete(0,END)
    room_combo.insert(0,"Duplex")

    roomno_entry.delete(0,END)


def checkin():

    wdw_checkin = Toplevel()
    wdw_checkin.title("Check in")
    wdw_checkin.resizable(width = False, height = False)
    wdw_checkin.geometry("630x500")
    wdw_checkin.config(bg = '#0d1e30')

    #creating the frames
    titleframe1 = LabelFrame(wdw_checkin, bg = "black", bd = 5, height = 50, width = 500, relief = RIDGE)
    titleframe1.pack(side = TOP, fill = "x")

    title_lbl_1 = Label(titleframe1, text = 'Customer Check in', font = ('Comic sans MS',12), fg = 'white', bg = 'black' )
    title_lbl_1.pack()

    #creating the labels 
    code_label = Label(wdw_checkin, text = 'Customer Code', font = ('Comic sans MS',15),fg = 'white', bg = '#0d1e30')
    code_label.place(x = 30,y = 90)

    name_label = Label(wdw_checkin, text = 'Customer Name', font = ('Comic sans MS',15),fg = 'white', bg = '#0d1e30')
    name_label.place(x = 30,y = 130)

    Aadhar_label = Label(wdw_checkin, text = 'Aadhar Number', font = ('Comic sans MS',15),fg = 'white', bg = '#0d1e30')
    Aadhar_label.place(x = 30,y = 170)

    checkin_label = Label(wdw_checkin, text = 'check-in date', font = ('Comic sans MS',15),fg = 'white', bg = '#0d1e30')
    checkin_label.place(x = 30,y = 210)

    checkout_label = Label(wdw_checkin, text = 'check-out date', font = ('Comic sans MS',15),fg = 'white', bg = '#0d1e30')
    checkout_label.place(x = 30,y = 250)

    roomtype_label = Label(wdw_checkin, text = 'Room type', font = ('Comic sans MS',15),fg = 'white',bg = '#0d1e30')
    roomtype_label.place(x = 30,y = 290)

    roomno_label = Label(wdw_checkin, text = 'Room Number', font = ('Comic sans MS',15),fg = 'white',bg = '#0d1e30')
    roomno_label.place(x = 30,y = 330)


    #creating the normal entry widgets
    global code_entry
    code_entry = Entry(wdw_checkin, font = ('Comic sans MS',15),fg = 'Black')
    code_entry.place (x= 200, y = 90)

    global name_entry
    name_entry = Entry(wdw_checkin, font = ('Comic sans MS',15),fg = 'Black')
    name_entry.place (x= 200, y =130)

    global Aadhar_entry
    Aadhar_entry = Entry(wdw_checkin, font = ('Comic sans MS',15),fg = 'Black')
    Aadhar_entry.place (x= 200, y = 170)

    global roomno_entry
    roomno_entry = Entry(wdw_checkin, font = ('Comic sans MS',15),fg = 'Black')
    roomno_entry.place (x= 200, y = 330)


    #Date-entry widgets for checkin and checkout
    global checkin_entry
    checkin_entry = DateEntry(wdw_checkin, width=40, year=2020, month=12, day=1, background = '#0d1e30', foreground='white', borderwidth=2)
    checkin_entry.place (x= 200, y = 220)
    checkin_entry.config(date_pattern = 'dd-mm-yyyy')

    global checkout_entry
    checkout_entry = DateEntry(wdw_checkin, width=40, year=2020, month=12, day=1, background = '#0d1e30', foreground='white', borderwidth=2)
    checkout_entry.place (x= 200, y = 260)
    checkout_entry.config(date_pattern = 'dd-mm-yyyy')
    
    #drop down combobox for room types
    room_options = ['Duplex', 'Cabana', 'lanai', 'Suite', 'Mini']
    global room_combo
    room_combo = ttk.Combobox(wdw_checkin, width = 40 ,value = room_options)
    room_combo.current(0)
    
    room_combo.place(x = 200, y = 300)

    #creating the enter details button
    enterdetails_btn = Button(wdw_checkin, width = 10, text = "Enter", font = ('Comic sans MS',15),fg = "black", command = enter, relief = RIDGE)
    enterdetails_btn.place(x = 30, y = 400)

    deletedetails_btn = Button(wdw_checkin, width =10, text = "Delete", font = ('Comic sans MS',15),fg = "black", command = delete, relief = RIDGE)
    deletedetails_btn.place(x = 180, y = 400)

    searchdetails_btn = Button(wdw_checkin, width = 10, text = "Search", font = ('Comic sans MS',15),fg = "black", command = search, relief = RIDGE)
    searchdetails_btn.place(x = 330, y = 400)

    cleardetails_btn = Button(wdw_checkin, width = 10, text = "Clear", font = ('Comic sans MS',15),fg = "black", command = clear, relief = RIDGE)
    cleardetails_btn.place(x = 480, y = 400)
   
def room_selected(event):

   indate = str(checkin_entry1.get())
   outdate = str(checkout_entry1.get())
   num1 = int(indate[0] + indate[1])
   num2 = int(outdate[0] + outdate[1])
   days = num2 - num1

   if roomtype.get() == 'Duplex':

       roomrent_entry.delete(0,END)
       roomserv_entry.delete(0,END)
       gst_entry.delete(0,END)
       totalbill_entry.delete(0,END)

       rent = days * 5000
       roomrent_entry.insert(0,str(rent))
       roomserv_entry.insert(0,"500.0")
       gst = 0.12 * (rent + 500)
       gst_entry.insert(0,str(gst))
       
       bill = str(rent + 500 + gst)

       totalbill_entry.insert(0,bill)

   if roomtype.get() == 'Cabana':

       roomrent_entry.delete(0,END)
       roomserv_entry.delete(0,END)
       gst_entry.delete(0,END)
       totalbill_entry.delete(0,END)
       
       rent = days * 4000
       roomrent_entry.insert(0,str(rent))
       roomserv_entry.insert(0,"500.0")
       gst = 0.12 * (rent + 500)
       gst_entry.insert(0,str(gst))
       
       bill = str(rent + 500 + gst)

       totalbill_entry.insert(0,bill)

   if roomtype.get() == 'Lanai':

       roomrent_entry.delete(0,END)
       roomserv_entry.delete(0,END)
       gst_entry.delete(0,END)
       totalbill_entry.delete(0,END)

       rent = days * 3000
       roomrent_entry.insert(0,str(rent))
       roomserv_entry.insert(0,"500.0")
       gst = 0.12 * (rent + 500)
       gst_entry.insert(0,str(gst))
       
       bill = str(rent + 500 + gst)

       totalbill_entry.insert(0,bill)

   if roomtype.get() == 'Suite':

       roomrent_entry.delete(0,END)
       roomserv_entry.delete(0,END)
       gst_entry.delete(0,END)
       totalbill_entry.delete(0,END)
       
       rent = days * 2000
       roomrent_entry.insert(0,str(rent))
       roomserv_entry.insert(0,"500.0")
       gst = 0.12 * (rent + 500)
       gst_entry.insert(0,str(gst))
       
       bill = str(rent + 500 + gst)

       totalbill_entry.insert(0,bill)

   if roomtype.get() == 'Mini':

       roomrent_entry.delete(0,END)
       roomserv_entry.delete(0,END)
       gst_entry.delete(0,END)
       totalbill_entry.delete(0,END)

       rent = days * 1000
       roomrent_entry.insert(0,str(rent))
       roomserv_entry.insert(0,"500.0")
       gst = 0.12 * (rent + 500)
       gst_entry.insert(0,str(gst))

       bill = str(rent + 500 + gst)

       totalbill_entry.insert(0,bill)

def enter_out():

    db = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '@fr@hT#b#ss#M',
        database = 'python_project'
        )

    cursor = db.cursor()

    if (outcode_entry.get() == "" or outname_entry.get() == ""):
        messagebox.showinfo("Record Status","Please make sure the fields are filled")

    else:

        h = outcode_entry.get()
        i = outname_entry.get()
        j = checkin_entry1.get()
        k = checkout_entry1.get()
        l = roomtype.get()
        m = roomrent_entry.get()
        n = roomserv_entry.get()
        o = gst_entry.get()
        p = totalbill_entry.get()

        query_entryout = "insert into checkout values('"+ h +"','"+ i +"','"+ j +"','"+ k +"','"+ l +"','"+ m +"','"+ n +"','"+ o +"','"+ p +"')"
        cursor.execute(query_entryout)
        db.commit()

        outcode_entry.delete(0,END)
        outname_entry.delete(0,END)
        
        checkin_entry1.set_date("1/1/2020")
        checkout_entry1.set_date("1/1/2020")

        roomrent_entry.delete(0,END)
        roomserv_entry.delete(0,END)

        gst_entry.delete(0,END)
        totalbill_entry.delete(0,END)

        outcode_entry.delete(0,END)
        outcode_entry.delete(0,END)

        roomtype.delete(0,END)
        roomtype.insert(0,"Duplex")
        
        messagebox.showinfo("Record Status","The record has been entered successfully")

    cursor.close()
    db.close()

def delete_out():

        db = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '@fr@hT#b#ss#M',
        database = 'python_project'
        )

        cursor = db.cursor()

        answer = messagebox.askyesno("Record status","Are you sure you want to delete this record?\nThis action cannot be undone ")

        if answer == 1:

            code_delete = outcode_entry.get()
            query_delete1 = "delete from checkout where ccode = '"+code_delete+"'"
            cursor.execute(query_delete1)
            db.commit()

            outcode_entry.delete(0,END)
            outname_entry.delete(0,END)
            
            checkin_entry1.set_date("1/1/2020")
            checkout_entry1.set_date("1/1/2020")

            roomrent_entry.delete(0,END)
            roomserv_entry.delete(0,END)

            gst_entry.delete(0,END)
            totalbill_entry.delete(0,END)

            outcode_entry.delete(0,END)
            outcode_entry.delete(0,END)

            roomtype.delete(0,END)
            roomtype.insert(0,"Duplex")
            
            messagebox.showinfo("Record Status","The record has been deleted successfully")

        db.close()
        cursor.close()

def search_out():

    db = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '@fr@hT#b#ss#M',
        database = 'python_project'
        )

    cursor = db.cursor()

    a1 = outcode_entry.get()

    if a1 == "":
        messagebox.showerror("Record status","Code field not filled out")

    else:
        query_searchout = "select * from checkout where ccode = '"+ a1 +"'"
        cursor.execute(query_searchout)
        result_out = cursor.fetchall()

        count = 0

        for string in result_out:

            count+=1

            outname_entry.delete(0,END)
            outname_entry.insert(0,str(string[1]))

            checkin_entry1.delete(0,END)
            checkin_entry1.insert(0,str(string[2]))

            checkout_entry1.delete(0,END)
            checkout_entry1.insert(0,str(string[3]))

            roomtype.delete(0,END)
            roomtype.insert(0,str(string[4]))

            roomrent_entry.delete(0,END)
            roomrent_entry.insert(0,str(string[5]))

            roomserv_entry.delete(0,END)
            roomserv_entry.insert(0,str(string[6]))

            gst_entry.delete(0,END)
            gst_entry.insert(0,str(string[7]))

            totalbill_entry.delete(0,END)
            totalbill_entry.insert(0,str(string[8]))

    if count == 0:

        messagebox.showinfo("Record status","No record found")
    
    db.close()
    cursor.close()

def clear_out():

    outcode_entry.delete(0,END)
    outname_entry.delete(0,END)

    roomrent_entry.delete(0,END)
    roomserv_entry.delete(0,END)

    gst_entry.delete(0,END)
    totalbill_entry.delete(0,END)

    #Setting to default values 
    checkin_entry1.set_date("1/1/2020")
    checkout_entry1.set_date("1/1/2020")

    roomtype.delete(0,END)
    roomtype.insert(0,"Duplex")


def checkout():

    wdw_checkout = Toplevel()
    wdw_checkout.title("Check out")
    wdw_checkout.resizable(width = False, height = False)
    wdw_checkout.geometry("630x550")
    wdw_checkout.config(bg = '#0d1e30')

    #Title frames
    titleframe3 = LabelFrame(wdw_checkout, bg = "black", bd = 5, height = 50, width = 500, relief = RIDGE)
    titleframe3.pack(side = TOP, fill = "x")

    title_lbl_3 = Label(titleframe3, text = 'Customer Check-out', font = ('Comic sans MS',15), fg = 'white', bg = 'black' )
    title_lbl_3.pack()

    #Creating the labels
    outcode_label = Label(wdw_checkout, text = 'Customer code', font = ('Comic sans MS',15), fg = 'white', bg = '#0d1e30')
    outcode_label.place(x = 30,y = 90)

    outname_label = Label(wdw_checkout, text = 'Customer Name', font = ('Comic sans MS',15), fg = 'white', bg = '#0d1e30')
    outname_label.place(x = 30,y = 130)

    checkindate_label = Label(wdw_checkout, text = 'Check in-date', font = ('Comic sans MS',15), fg = 'white', bg = '#0d1e30')
    checkindate_label.place(x = 30,y = 170)

    checkoutdate_label = Label(wdw_checkout, text = 'Check out-date', font = ('Comic sans MS',15), fg = 'white', bg = '#0d1e30')
    checkoutdate_label.place(x = 30,y = 210)

    outroomtype_label = Label(wdw_checkout, text = 'Room Type', font = ('Comic sans MS',15), fg = 'white', bg = '#0d1e30')
    outroomtype_label.place(x = 30,y = 250)
    
    roomrent_label = Label(wdw_checkout, text = 'Room Rent',font = ('Comic sans MS',15), fg = 'white', bg = '#0d1e30')
    roomrent_label.place(x = 30, y = 290)

    roomserv_label = Label(wdw_checkout, text = 'Room service', font = ('Comic sans MS',15), fg = 'white', bg = '#0d1e30')
    roomserv_label.place(x = 30,y = 330)

    gst_label = Label(wdw_checkout, text = 'GST Tax', font = ('Comic sans MS',15), fg = 'white', bg = '#0d1e30')
    gst_label.place(x = 30,y = 370)

    totalbill_label = Label(wdw_checkout, text = 'Total Bill', font = ('Comic sans MS',15), fg = 'white',bg = '#0d1e30')
    totalbill_label.place(x = 30,y = 410)

    #entry widgets for the labels above
    global outcode_entry
    outcode_entry = Entry(wdw_checkout,font = ('Comic sans MS',15), fg = 'black')
    outcode_entry.place(x = 200, y = 90)

    global outname_entry
    outname_entry = Entry(wdw_checkout,font = ('Comic sans MS',15), fg = 'black')
    outname_entry.place(x = 200, y = 130)

    #dropdown calendar for date entry
    global checkin_entry1
    checkin_entry1 = DateEntry(wdw_checkout, width=40, year=2020, month=12, day=1, background = 'Black', foreground='white', borderwidth=2)
    checkin_entry1.place(x= 200, y = 170)
    checkin_entry1.config(date_pattern = 'dd-mm-yyyy')

    global checkout_entry1
    checkout_entry1 = DateEntry(wdw_checkout, width=40, year=2020, month=12, day=1, background = 'Black', foreground='white', borderwidth=2)
    checkout_entry1.place(x= 200, y = 210)
    checkout_entry1.config(date_pattern = 'dd-mm-yyyy')


    #dropdown combobox for roomtype
    room1_options = ['Duplex', 'Cabana', 'Lanai', 'Suite', 'Mini']

    global roomtype
    roomtype = ttk.Combobox(wdw_checkout, width = 40 ,value = room1_options)
    roomtype.current(0)
    roomtype.bind('<<ComboboxSelected>>',room_selected)
    roomtype.place(x = 200, y = 250)

    global roomrent_entry
    roomrent_entry = Entry(wdw_checkout,font = ('Comic sans MS',15), fg = 'black')
    roomrent_entry.place(x = 200, y = 290)

    global roomserv_entry
    roomserv_entry = Entry(wdw_checkout,font = ('Comic sans MS',15), fg = 'black')
    roomserv_entry.place(x = 200, y = 330)

    global gst_entry
    gst_entry = Entry(wdw_checkout,font = ('Comic sans MS',15), fg = 'black')
    gst_entry.place(x = 200, y = 370)

    global totalbill_entry
    totalbill_entry = Entry(wdw_checkout,font = ('Comic sans MS',15), fg = 'black')
    totalbill_entry.place(x = 200, y = 410)

    #creating the buttons for entering and deleting
    enterdetails_btn = Button(wdw_checkout, width = 10, text = "Enter", font = ('Comic sans MS',15),fg = "black", command = enter_out, relief = RIDGE)
    enterdetails_btn.place(x = 30, y = 480)

    deletedetails_btn = Button(wdw_checkout, width =10, text = "Delete", font = ('Comic sans MS',15),fg = "black", command = delete_out, relief = RIDGE)
    deletedetails_btn.place(x = 180, y = 480)

    searchdetails_btn = Button(wdw_checkout, width = 10, text = "Search", font = ('Comic sans MS',15),fg = "black", command = search_out, relief = RIDGE)
    searchdetails_btn.place(x = 330, y = 480)

    cleardetails_btn = Button(wdw_checkout, width = 10, text = "Clear", font = ('Comic sans MS',15),fg = "black", command = clear_out, relief = RIDGE)
    cleardetails_btn.place(x = 480, y = 480)

#definition of cus_man() function - for customer management
def cus_man():
    global bg2

    window3 = Toplevel()
    window3.title("Customer Management")

    #opening the image for the canvas
    bg2 = ImageTk.PhotoImage(Image.open(r"C:\Users\User\OneDrive\Pictures\background1.jpg"))

    #setting the background as the image
    canvas2 = Canvas(window3, height =400, width = 300, border = 0, highlightthickness = 0)
    canvas2.pack(fill = "both",expand = True)
    canvas2.create_image(0,0,image = bg2, anchor ="nw")
    
    #creating buttons for this window
    checkin_btn = Button(window3, text = "CHECK IN", font = ("Comic Sans MS", 10),width = 20, bg = "white", fg = "#336d92", bd = 0, command = checkin)
    checkin_btnw = canvas2.create_window(150, 130, window = checkin_btn)

    checkout_btn = Button(window3, text = "CHECK OUT", font = ("Comic Sans MS", 10),width = 20, bg = "white", fg = "#336d92", bd = 0, command = checkout)
    checkout_btnw = canvas2.create_window(150, 230, window = checkout_btn) 

#functions for the buttons in the email() module 
def bill():

    db = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '@fr@hT#b#ss#M',
        database = 'python_project'
        )

    cursor = db.cursor()

    bill_name = Name1_entry.get()
    query = "select * from checkout where cname = '"+bill_name+"'"
    cursor.execute(query)
    global result_bill
    result_bill = cursor.fetchall()
    global row
    for row in result_bill:

        Code = str(row[0])
        label_code = Label(frame_bill, text = ('Customer Code =',Code), bg = 'White')
        label_code.pack()

        Name = str(row[1])
        label_name = Label(frame_bill, text = ('Customer Name =',Name), bg = 'White')
        label_name.pack()

        checkindate = row[2]
        label_checkin = Label(frame_bill, text = ('Check-in =',checkindate), bg = 'White')
        label_checkin.pack()

        checkoutdate = row[3]
        label_checkout = Label(frame_bill, text = ('Check-out =',checkoutdate), bg = 'White')
        label_checkout.pack()

        roomtype = row[4]
        label_room = Label(frame_bill, text = ('Room-Type =',roomtype), bg = 'White')
        label_checkout.pack()

        roomrent = row[5]
        label_roomrent = Label(frame_bill, text = ('Room-Rent =',roomrent), bg = 'White')
        label_roomrent.pack()

        roomserv = row[6]
        label_roomserv = Label(frame_bill, text = ('Room-service =',roomserv), bg = 'White')
        label_roomserv.pack()

        gst = row[7]
        label_gst = Label(frame_bill, text = ('GST Tax =',gst), bg = 'White')
        label_gst.pack()

        totalbill = row[8]
        label_totalbill = Label(frame_bill, text = ('Total Bill =',totalbill), bg = 'White')
        label_totalbill.pack()

        

    db.close()
    cursor.close()

def send():
    try:
        with smtplib.SMTP("smtp.gmail.com","587") as SMTP:
            SMTP.ehlo()
            SMTP.starttls()
            SMTP.ehlo()

            SMTP.login("afrahpythonproject@gmail.com","pythonproject")

            subject = "We hope you had a comfortable stay at our hotel!\nHere is your bill for the stay"
            rec = email_entry.get() 
            body = row[0:8]
            msg = f"subject: {subject}\n\n{body}"
            SMTP.sendmail("afrahpythonproject@gmail.com",rec,msg)
            messagebox.showinfo("Email status","The email has been sent succesfully")

    except:
        messagebox.showinfo("Email status","There was some issue sending the mail\nPlease try again later")
        

def reset():

    Name1_entry.delete(0,END)
    aadhar1_entry.delete(0,END)
    email_entry.delete(0,END)

#definition of email() function - for sending the bill to the customers via email 
def email():
    
    window_em = Toplevel()
    window_em.title("Emails")
    window_em.geometry('800x400')
    

    #opening the image for the background
    global bg_em
    bg_em = ImageTk.PhotoImage(Image.open(r"C:\Users\User\OneDrive\Pictures\background1.jpg"))

    #setting up the canvas
    canvas_em = Canvas(window_em, height =400, width = 400, border = 0, highlightthickness = 0)
    canvas_em.pack(fill = "both",expand = True)
    canvas_em.create_image(0,0,image = bg_em, anchor ="nw")

    #creating labels for the entry widgets
    canvas_em.create_text(60,50,text = "Name", font= ('Comic sans MS',15), fill = "white")
    canvas_em.create_text(67,130,text = "Aadhar", font= ('Comic sans MS',15), fill = "white")
    canvas_em.create_text(67,210,text = "Email", font= ('Comic sans MS',15), fill = "white") 

    #creating entry widget for the aadhar no and Name
    global Name1_entry
    Name1_entry = Entry(window_em, font = ('Comic sans MS',15), width = 20,fg = "#336d92",bg ="white", bd = 0)
    Name1_window = canvas_em.create_window(110,40,anchor ="nw", window = Name1_entry)

    global aadhar1_entry
    aadhar1_entry = Entry(window_em, font = ('Comic sans MS',15), width = 20,fg = "#336d92",bg ="white", bd = 0)
    aadhar1_window = canvas_em.create_window(110,120,anchor ="nw", window = aadhar1_entry)

    global email_entry
    email_entry = Entry(window_em, font = ('Comic sans MS',15), width = 25,fg = "#336d92",bg ="white", bd = 0)
    email_window = canvas_em.create_window(110,200,anchor ="nw", window = email_entry)

    #creating a button to check the database
    bill_btn = Button(window_em,text = "Bill", font = ('Comic sans MS',12),width = 10, bg = "white",fg = "#336d92",bd = 0,relief = RIDGE, command = bill)
    bill_btnw = canvas_em.create_window(70,300, window = bill_btn)

    send_btn = Button(window_em,text = "Send", font = ('Comic sans MS',12),width = 10, bg = "white",fg = "#336d92",bd = 0,relief = RIDGE, command = send)
    send_btnw = canvas_em.create_window(180,300, window = send_btn)

    reset_btn = Button(window_em,text = "reset", font = ('Comic sans MS',12),width = 10, bg = "white",fg = "#336d92",bd = 0,relief = RIDGE, command = reset)
    reset_btnw = canvas_em.create_window(290,300, window = reset_btn)

    global frame_bill
    frame_bill = LabelFrame(canvas_em, bd = 5,bg = 'white',height = 350, width = 270, relief = RIDGE)
    frame_bill.pack(side = RIGHT, fill = "both", expand = False)

#defining the main menu window
def mm_window():
    global bg1
    window1 = Toplevel()
    window1.title("Main Menu")
    window1.resizable(width = False, height = False)

    #reading data from the image needed for the background    
    bg1 = ImageTk.PhotoImage(Image.open(r"C:\Users\User\OneDrive\Pictures\treespython.jpg"))

    #setting the background as the image
    canvas1 = Canvas(window1,height =400, width = 300,border = 0, highlightthickness = 0)
    canvas1.pack(fill = "both",expand = True)
    canvas1.create_image(0,0,image = bg1, anchor ="nw")
    
    #creating the buttons  
    auth_btn = Button(window1, text= "AUTHENTICATION", font = ("Comic sans ms", 10),width = 24, bg = "white", fg = "#336d92", bd = 0, command = auth)
    auth_btnw = canvas1.create_window(150, 100, window = auth_btn)

    empman_btn = Button(window1, text= "SEND EMAILS", font = ("comic sans ms", 10),width = 24, bg = "white", fg = "#336d92", bd = 0, command = email)
    empman_btnw = canvas1.create_window(150, 300,window = empman_btn)

    cusman_btn = Button(window1, text= "CUSTOMER MANAGEMENT", font = ("comic sans ms", 10),width = 24, bg = "white", fg = "#336d92", bd = 0, command = cus_man)
    cusman_btnw = canvas1.create_window(150, 200, window = cusman_btn)

    
#definition of the login() function, checks the password
def login():
    
    if (pass_entry.get() == "" and user_entry.get() == '') or (pass_entry.get() == "ataliya" and user_entry.get() == "A Taliya"):
        pass_entry.delete(0, END)
        user_entry.delete(0, END)
        mm_window()
    else:
        messagebox.showerror("Wrong password","Password or Username is incorrect\nTry again")
        pass_entry.delete(0, END)
        user_entry.delete(0, END)

#Main code for the Login window
main = Tk()
main.geometry("480x550")
main.title("Login Page")
main.resizable(width = False, height = False)

#opening the image for the canvas of the login window
bg = ImageTk.PhotoImage(Image.open(r"C:\Users\User\OneDrive\Pictures\background1.jpg"))

#creating the canvas for the login window 
canvas = Canvas(main, width = 640, height = 550, border = 0, highlightthickness = 0)
canvas.pack(fill = "both",expand = True)
canvas.create_image(0,0,image = bg, anchor ="nw")
canvas.create_text(240,30,text ="Please enter the following details to login", font = ("Comic Sans MS", 18), fill = "white")
canvas.create_text(80,130,text = "username",font = ("Comic Sans MS", 18),fill = "white")
canvas.create_text(80,200, text ='password ', font =("Comic Sans MS", 18), fill = "white")

#Entry widget for the username and password
pass_entry = Entry(main, font=("Comic sans MS",15), width = 15,fg = "#336d92",bg ="white", bd = 0)
pass_entry.config(show = "•")
pass_window = canvas.create_window(160,188,anchor ="nw", window = pass_entry)

user_entry = Entry(main, font = ("Comic sans MS",15),width = 15,fg = "#336d92",bg ="white", bd = 0)
user_window = canvas.create_window(160,122, anchor ="nw", window = user_entry)

#Making the button for logging in
login_btn = Button(main, text= "Login", font=("Arial",15), width = 15, bg = "white", fg= "#336d92", bd = 0, command = login)
login_btnw = canvas.create_window(160,280, anchor = "nw", window = login_btn)


main.mainloop()










