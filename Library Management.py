import tkinter 
import mysql.connector
import datetime
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from mysql.connector import cursor

class LibraryManagement:
    def __init__(self,root): 
        self.root=root #initialising self 
        #for fullscreen=root.overrideredirect(True)
        root.title("Library Management")
        root.geometry("1920x1080+0+0")#Whatever your screen resolution is

        #========================= Variable =========================#
        self.member_var=StringVar()
        self.id_var=StringVar()
        self.studname_var=StringVar()
        self.division_var=StringVar()
        self.mobile_var=StringVar()
        self.address_var=StringVar()
        self.bookid_var=StringVar()
        self.bookname_var=StringVar()
        self.dateissue_var=StringVar()
        self.datedue_var=StringVar()
        self.latefine_var=StringVar()
        self.actualprice_var=StringVar()#Remember to make exact same variables in table db

        lbltitle= Label(self.root, text="Library Management", bg="#000B4F", fg="white", bd=8, relief=RIDGE, font=("sans seriff", 40, "bold"))
        lbltitle.pack(side=TOP, fill=X)
        
        frame= Frame(self.root, bd=10,  relief=RIDGE, padx=1, pady=2, bg="#6D6D6D")
        frame.place(x=0, y=75, width=1280, height=268)
        
        #========================= Dataframe Left =========================#
        DataFrameLeft=LabelFrame(frame, text="Library Membership Info", bg="#20368F", fg="white", bd=6, relief=RIDGE, font=("sans seriff", 15, "bold", "underline"))
        DataFrameLeft.place(x=0, y=0, width=710, height=245)

        lblMember=Label(DataFrameLeft, bg="#20368F", fg="white", text="Member type", font=("sans seriff", 12, "bold"), padx=2, pady=6)
        lblMember.grid(row=0, column=0, sticky=W)

        comMember=ttk.Combobox(DataFrameLeft, textvariable=self.member_var, font=("sans seriff", 12, "bold"), width=24, state="readonly")
        comMember["values"]=("Admin Staff", "Student", "Lecturer")
        comMember.grid(row=0, column=1)
 
        lblStudentID=Label(DataFrameLeft, bg="#20368F", fg="white", text="Student ID", font=("sans seriff", 12, "bold"), padx=2, pady=6)
        lblStudentID.grid(row=1, column=0, sticky=W)
        txtStudentID=Entry(DataFrameLeft, font=("sans seriff", 12), textvariable=self.id_var, width=26)
        txtStudentID.grid(row=1, column=1,)

        lblStudName=Label(DataFrameLeft, bg="#20368F", fg="white", text="Student Name", font=("sans seriff", 12, "bold"), padx=2, pady=6)
        lblStudName.grid(row=2, column=0, sticky=W) 
        txtStudName=Entry(DataFrameLeft, font=("sans seriff", 12), textvariable=self.studname_var, width=26)
        txtStudName.grid(row=2, column=1,)
        
        lblDivision=Label(DataFrameLeft, bg="#20368F", fg="white", text="Division", font=("sans seriff", 12, "bold"), padx=2, pady=6)
        lblDivision.grid(row=3, column=0, sticky=W)
        comDivision=ttk.Combobox(DataFrameLeft, textvariable=self.division_var, font=("sans seriff", 12, "bold"), width=24, state="readonly")
        comDivision["values"]=("A","B","C","D","E","F")
        comDivision.grid(row=3, column=1)

        lblMobile=Label(DataFrameLeft, bg="#20368F", fg="white", text="Mobile", font=("sans seriff", 12, "bold"), padx=2, pady=6)
        lblMobile.grid(row=4, column=0, sticky=W)
        txtMobile=Entry(DataFrameLeft, font=("sans seriff",12), textvariable=self.mobile_var, width=26)
        txtMobile.grid(row=4, column=1)

        lblAddress=Label(DataFrameLeft, bg="#20368F", fg="white", text="Address", font=("sans seriff", 12, "bold"), padx=2, pady=6)
        lblAddress.grid(row=5, column=0, sticky=W)
        txtAddress=Entry(DataFrameLeft, font=("sans seriff", 12), textvariable=self.address_var, width=26)
        txtAddress.grid(row=5, column=1)

        lblBookID=Label(DataFrameLeft, bg="#20368F", fg="white", text="Book ID", font=("sans seriff", 12, "bold"), padx=2, pady=6)
        lblBookID.grid(row=0, column=3, sticky=W)
        txtBookID=Entry(DataFrameLeft, font=("sans seriff", 12), textvariable=self.bookid_var, width=26)
        txtBookID.grid(row=0, column=4)

        lblBookName=Label(DataFrameLeft, bg="#20368F", fg="white", text="Book Name", font=("sans seriff", 12, "bold"), padx=2, pady=6)
        lblBookName.grid(row=1, column=3, sticky=W)
        txtBookName=Entry(DataFrameLeft, font=("sans seriff", 12), textvariable=self.bookname_var, width=26)
        txtBookName.grid(row=1, column=4)

        lblDateIssued=Label(DataFrameLeft, bg="#20368F", fg="white", text="Date Issued", font=("sans seriff", 12, "bold"), padx=2, pady=6)
        lblDateIssued.grid(row=2, column=3, sticky=W)
        txtDateIssued=Entry(DataFrameLeft, font=("sans seriff", 12), textvariable=self.dateissue_var, width=26)
        txtDateIssued.grid(row=2, column=4)

        lblDateDue=Label(DataFrameLeft, bg="#20368F", fg="white", text="Date Due", font=("sans seriff", 12, "bold"), padx=2, pady=6)
        lblDateDue.grid(row=3, column=3, sticky=W)
        txtDateDue=Entry(DataFrameLeft, font=("sans seriff", 12), textvariable=self.datedue_var, width=26)
        txtDateDue.grid(row=3, column=4)

        lblLateRT=Label(DataFrameLeft, bg="#20368F", fg="white", text="Late Fine", font=("sans seriff", 12, "bold"), padx=2, pady=6)
        lblLateRT.grid(row=4, column=3, sticky=W)
        txtLateRT=Entry(DataFrameLeft, font=("sans seriff", 12), textvariable=self.latefine_var, width=26)
        txtLateRT.grid(row=4, column=4)

        lblActualPrice=Label(DataFrameLeft, bg="#20368F", fg="white", text="Actual Price", font=("sans seriff", 12, "bold"), padx=2, pady=6)
        lblActualPrice.grid(row=5, column=3, sticky=W)
        txtActualPrice=Entry(DataFrameLeft, font=("sans seriff", 12), textvariable=self.actualprice_var, width=26)
        txtActualPrice.grid(row=5, column=4)

        #========================= Dataframe Right =========================#
        DataFrameRight=LabelFrame(frame, text="Book details", bg="#20368F", fg="white", bd=6, relief=RIDGE, font=("sans seriff", 15, "bold", "underline"), padx=4)
        DataFrameRight.place(x=710, y=0, width=545, height=245)

        self.txtBox=Text(DataFrameRight, font=("sans seriff", 13), width=33, height=11)
        self.txtBox.grid(row=0, column=2, padx=1, pady=0)
        
        list0Scrollbar=Scrollbar(DataFrameRight)
        list0Scrollbar.grid(row=0, column=3, sticky="ns")
        txtBox=Listbox(DataFrameRight, font=("sans seriff", 12), width=18, height=10)
        txtBox.grid(row=0, column=0, padx=1, pady=0)
        list0Scrollbar.config(command=txtBox.yview)

        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0, column=1, sticky="ns")

        listbooks=['Book 1','Book 2','Book 3','Book 4',
                    'Book 5','Book 6','Book 7','Book 8','Book 9','Book 10',
                    'Book 11','Book 12','Book 13','Book 14','Book 15','Book 16',
                    'Book 17','Book 18','Book 19','Book 20'
                    ]

        def SelectBook(event=""):
            value=str(listBox.get(listBox.curselection()))
            x=value
            if (x=="Book 1"):
                self.bookid_var.set("BKID1")
                self.bookname_var.set("Book Title")  
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateissue_var.set(d1)
                self.datedue_var.set(d3)
                self.latefine_var.set("1$") 
                self.actualprice_var.set("10$")

            elif (x=="Book 2"):
                self.bookid_var.set("BKID2")
                self.bookname_var.set("Book Title 2")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateissue_var.set(d1)
                self.datedue_var.set(d3)
                self.latefine_var.set("1.5$") 
                self.actualprice_var.set("20$")
        
        listBox=Listbox(DataFrameRight,font=("sans seriff", 12), width=20, height=11)
        listBox.bind("<<ListboxSelect>>",SelectBook)
        listBox.grid(row=0, column=0, padx=0, pady=0)
        listScrollbar.config(command=listBox.yview)

        for item in listbooks:
            listBox.insert(END,item)
     
        #========================= Buttons Frame =========================#
        Framebutton= Frame(self.root, bd=10, relief=RIDGE, padx=2, bg="#829CD0")
        Framebutton.place(x=0, y=340, width=1280, height=74)

        btnAddData=Button(Framebutton, command=self.add_data, text="ADD DATA", font=("sans seriff", 12, "bold"), bg="#EBEBEB", fg="black", width=18, height=2)
        btnAddData.grid(row=0, column=0, padx=9)

        btnAddData=Button(Framebutton, command=self.showData, text="SHOW DATA", font=("sans seriff", 12, "bold"), bg="#EBEBEB", fg="black", width=18, height=2)
        btnAddData.grid(row=0, column=1, padx=10)

        btnAddData=Button(Framebutton, command=self.update, text="UPDATE", font=("sans seriff", 12, "bold"), bg="#EBEBEB", fg="black", width=18, height=2)
        btnAddData.grid(row=0, column=2, padx=10)

        btnAddData=Button(Framebutton, command=self.delete, text="DELETE", font=("sans seriff", 12, "bold"), bg="#EBEBEB", fg="black", width=18, height=2)
        btnAddData.grid(row=0, column=3, padx=10)

        btnAddData=Button(Framebutton, command=self.reset, text="RESET", font=("sans seriff", 12, "bold"), bg="#EBEBEB", fg="black", width=18, height=2)
        btnAddData.grid(row=0, column=4, padx=10)

        btnAddData=Button(Framebutton, command=self.iexit, text="EXIT", font=("sans seriff", 12, "bold"), bg="#EBEBEB", fg="black", width=18, height=2)
        btnAddData.grid(row=0, column=5, padx=10)

        #========================= Info Frame =========================#
        FrameDetails= Frame(self.root, bd=10, relief=RIDGE, padx=1, bg="#323232")
        FrameDetails.place(x=0, y=410, width=1280, height=250)

        Table_frame=Frame(FrameDetails, bd=6, relief=RIDGE, bg="#323232")
        Table_frame.place(x=0, y=2, width=1256, height=228)

        xscroll=ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame, orient=VERTICAL)

        self.library_table=ttk.Treeview(Table_frame,column=("Member type", "StudentID", "Student Name", "Division",
                                                            "Mobile", "Address", "Book ID", "Book Name", "Date Issued",
                                                            "Date Due", "Late fine", "Actual Price" ),xscrollcommand=xscroll.set,
                                                            yscrollcommand=yscroll.set)

        xscroll.pack(side=BOTTOM, fill=X)
        yscroll.pack(side=RIGHT, fill=Y)
        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)    
        
        
        self.library_table.heading("Member type", text="Member type")
        self.library_table.heading("StudentID", text="StudentID")
        self.library_table.heading("Student Name", text="Student Name")
        self.library_table.heading("Division", text="Division")
        self.library_table.heading("Mobile", text="Mobile")
        self.library_table.heading("Address", text="Address")
        self.library_table.heading("Book ID", text="Book ID")
        self.library_table.heading("Book Name", text="Book Name")
        self.library_table.heading("Date Issued", text="Date Issued")
        self.library_table.heading("Date Due", text="Date Due")
        self.library_table.heading("Late fine", text="Late fine")
        self.library_table.heading("Actual Price", text="Actual Price")

        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH, expand=1)
        self.library_table.column("Member type", width=105)
        self.library_table.column("StudentID", width=105)
        self.library_table.column("Student Name", width=105)
        self.library_table.column("Division", width=105)
        self.library_table.column("Mobile", width=105)
        self.library_table.column("Address", width=105)
        self.library_table.column("Book ID", width=105)
        self.library_table.column("Book Name", width=105)
        self.library_table.column("Date Issued", width=105)
        self.library_table.column("Date Due", width=105)
        self.library_table.column("Late fine", width=105)
        self.library_table.column("Actual Price", width=105)

        self.fetch_data()
        self.library_table.bind("<ButtonRelease-1>", self.get_cursor)

    def add_data(self):
        conn=mysql.connector.connect(host="localhost", username="root", password="root", database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                            self.member_var.get(),
                            self.id_var.get(),
                            self.studname_var.get(),
                            self.division_var.get(),
                            self.mobile_var.get(),
                            self.address_var.get(),
                            self.bookid_var.get(),
                            self.bookname_var.get(),
                            self.dateissue_var.get(),
                            self.datedue_var.get(),
                            self.latefine_var.get(),
                            self.actualprice_var.get(),
        ))
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Success", "Member has been inserted successfully")

    def update(self):
        conn=mysql.connector.connect(host="localhost", username="root", password="root", database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("update library set Member=%s, StudName=%s, Division=%s, Mobile=%s, Address=%s, BookID=%s, BookName=%s, DateIssue=%s, DateDue=%s, Latefine=%s, ActualPrice=%s where ID=%s", (
                            self.member_var.get(),
                            self.studname_var.get(),
                            self.division_var.get(),
                            self.mobile_var.get(),
                            self.address_var.get(),
                            self.bookid_var.get(),
                            self.bookname_var.get(),
                            self.dateissue_var.get(),
                            self.datedue_var.get(),
                            self.latefine_var.get(),
                            self.actualprice_var.get(),
                            self.id_var.get()
        ))
        conn.commit()
        self.fetch_data()
        self.reset()
        conn.close()
        messagebox.showinfo("Success", "Member has been updated")

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost", username="root", password="root", database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from library")
        rows=my_cursor.fetchall()

        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.library_table.focus()
        content=self.library_table.item(cursor_row)
        row=content['values']
        self.member_var.set(row[0]),
        self.id_var.set(row[1]),
        self.studname_var.set(row[2]),
        self.division_var.set(row[3]),
        self.mobile_var.set(row[4]),
        self.address_var.set(row[5]),
        self.bookid_var.set(row[6]),
        self.bookname_var.set(row[7]),
        self.dateissue_var.set(row[8]),
        self.datedue_var.set(row[9]),
        self.latefine_var.set(row[10]),
        self.actualprice_var.set(row[11]) 

    def showData(self):
        self.txtBox.insert(END,"Member Type\t\t"+self.member_var.get() + "\n")
        self.txtBox.insert(END,"Student ID\t\t"+self.id_var.get() + "\n")
        self.txtBox.insert(END,"Student Name\t\t"+self.studname_var.get() + "\n")
        self.txtBox.insert(END,"Division\t\t"+self.division_var.get() + "\n")
        self.txtBox.insert(END,"Mobile\t\t"+self.mobile_var.get() + "\n")
        self.txtBox.insert(END,"Address\t\t"+self.address_var.get() + "\n")
        self.txtBox.insert(END,"Book ID\t\t"+self.bookid_var.get() + "\n")
        self.txtBox.insert(END,"Book Name\t\t"+self.bookname_var.get() + "\n")
        self.txtBox.insert(END,"Date Issue\t\t"+self.dateissue_var.get() + "\n")
        self.txtBox.insert(END,"Date Due\t\t"+self.datedue_var.get() + "\n")
        self.txtBox.insert(END,"Late Fine\t\t"+self.latefine_var.get() + "\n")
        self.txtBox.insert(END,"Actual Price\t\t"+self.actualprice_var.get() + "\n")

    def iexit(self):
        iexit=tkinter.messagebox.askyesno("Library Management System", "Do you want to exit?")
        if iexit>0:
            self.root.destroy()
            return()

    def reset(self):
        self.member_var.set("")
        self.id_var.set("")
        self.studname_var.set("")
        self.division_var.set("")
        self.mobile_var.set("")
        self.address_var.set("")
        self.bookid_var.set("")
        self.bookname_var.set("")
        self.dateissue_var.set("")
        self.datedue_var.set("")
        self.latefine_var.set("")
        self.actualprice_var.set("")
        self.txtBox.delete("1.0",END)
        
    def delete(self):
        if self.id_var.get()=="" or self.studname_var.get()=="":
            messagebox.showerror("Error", "First select the Member")
        else:
            conn=mysql.connector.connect(host="localhost", username="root", password="root", database="mydata")
            my_cursor=conn.cursor()
            query="DELETE from library where ID=%s"
            value=(self.id_var.get(),)
            my_cursor.execute(query,value)
            
            conn.commit()
            self.fetch_data()
            self.reset()
            conn.close()
            
            messagebox.showinfo("Success", "Member has been deleted")    

if __name__=="__main__":
    root=Tk()
    obj=LibraryManagement(root) #root=name of the window
    root.mainloop() #if mainloop not used the window will automatically closed
