# python module for one-timepad
#import onetimepad
# python module to create GUI
import smtplib
from tkinter import *
import sqlite3,sys
def connection():
    try:
        conn=sqlite3.connect("student.db")
    except:
        print("cannot connect to the database")
    return conn


def verifier():
    a=b=c=d=e=f=0
    if not student_name.get():
        t1.insert(END,"<>Student name is required<>\n")
        a=1
    if not roll_no.get():
        t1.insert(END,"<>Roll no is required<>\n")
        b=1
    if not branch.get():
        t1.insert(END,"<>Branch is required<>\n")
        c=1
    if not phone.get():
        t1.insert(END,"<>Phone number is requrired<>\n")
        d=1
    if not email.get():
        t1.insert(END,"<>email name is required<>\n")
        e=1
    if not address.get():
        t1.insert(END,"<>Address is Required<>\n")
        f=1
    if a==1 or b==1 or c==1 or d==1 or e==1 or f==1:
        return 1
    else:
        return 0


def add_student():
    ret = verifier()
    if ret == 0:
        conn = connection()
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS STUDENTS(NAME TEXT,ROLL_NO INTEGER,BRANCH TEXT,PHONE_NO INTEGER,FATHER TEXT,ADDRESS TEXT)")
        cur.execute("insert into STUDENTS values(?,?,?,?,?,?)", (
        student_name.get(), int(roll_no.get()), branch.get(), int(phone.get()), email.get(), address.get()))
        conn.commit()
        conn.close()
        t1.insert(END, "Stundent Registration  Successfully Check Your Register Email ID\n")

def view_student():
    conn=connection()
    cur=conn.cursor()
    cur.execute("select * from STUDENTS")
    data=cur.fetchall()
    conn.close()
    for i in data:
        t1.insert(END,str(i)+"\n")


def delete_student():
    ret=verifier()
    if ret==0:
        conn=connection()
        cur=conn.cursor()
        cur.execute("DELETE FROM STUDENTS WHERE ROLL_NO=?",(int(roll_no.get()),))
        conn.commit()
        conn.close()
        t1.insert(END,"Student Profile Successfully Deleted\n")

def update_student():
    ret=verifier()
    if ret==0:
        conn=connection()
        cur=conn.cursor()
        cur.execute("UPDATE STUDENTS SET NAME=?,ROLL_NO=?,BRANCH=?,PHONE_NO=?,FATHER=?,ADDRESS=? where ROLL_NO=?",(student_name.get(),int(roll_no.get()),branch.get(),int(phone.get()),email.get(),address.get(),int(roll_no.get())))
        conn.commit()
        conn.close()
        t1.insert(END,"Student Profile  Updated Successfully\n")


def clse():
    sys.exit()


if __name__ == "__main__":
    student_root = Tk()
    student_root.geometry("1366x800")
    student_root.title("Student Management System")
    title = Label(student_root, text="Seva Sadan Student Management System", font=("Arial",30, "bold"),bg="black", fg="#1aff1a")
    title.pack(side=TOP, fill=X)

    student_name = StringVar()
    roll_no = StringVar()
    branch = StringVar()
    phone = StringVar()
    email = StringVar()
    address = StringVar()
    gmail=email
    # -----main1 frame-------------------

    main1_frame = Frame(student_root, bd=4, relief=RIDGE, bg="black")
    main1_frame.place(x=35, y=70, width=650, height=300)



    main1_title = Label(main1_frame, text="Student Panel", font=("Arial", 20, "bold"), fg="#1aff1a", bg="black")
    main1_title.grid(row=0, column=1, pady=0, padx=0)


    label1 = Label(main1_frame, text="Student Name. : ", font=("Arial", 15, "bold"), fg="#1aff1a", bg="black")
    label1.grid(row=1, column=0, pady=0, padx=20)

    label2 = Label(main1_frame, text="Student Enroll. : ", font=("Arial", 15, "bold"), fg="#1aff1a", bg="black")
    label2.grid(row=2, column=0, pady=0, padx=20)

    label3 = Label(main1_frame, text="Student Branch : ", font=("Arial", 15, "bold"), fg="#1aff1a", bg="black")
    label3.grid(row=3, column=0, pady=0, padx=20)

    label4 = Label(main1_frame, text="Student Phone : ", font=("Arial", 15, "bold"), fg="#1aff1a", bg="black")
    label4.grid(row=4, column=0, pady=0, padx=20)

    label5 = Label(main1_frame, text="Student Email : ", font=("Arial", 15, "bold"), fg="#1aff1a", bg="black")
    label5.grid(row=5, column=0, pady=0, padx=20)
    label6 = Label(main1_frame, text="Student Address : ", font=("Arial", 15, "bold"), fg="#1aff1a", bg="black")
    label6.grid(row=6, column=0, pady=0, padx=20)

    e1 = Entry(main1_frame, textvariable=student_name,width=30)
    e1.grid(row=1, column=1, pady=0, padx=10)

    e2 = Entry(main1_frame, textvariable=roll_no,width=30)
    e2.grid(row=2, column=1, pady=0, padx=10)

    e3 = Entry(main1_frame, textvariable=branch,width=30)
    e3.grid(row=3, column=1, pady=0, padx=10)

    e4 = Entry(main1_frame, textvariable=phone,width=30)
    e4.grid(row=4, column=1, pady=0, padx=10)

    e5 = Entry(main1_frame, textvariable=email,width=30)
    e5.grid(row=5, column=1, pady=0, padx=10)

    e6 = Entry(main1_frame, textvariable=address,width=30)
    e6.grid(row=6, column=1, pady=0, padx=10)



    # -----main2 frame-------------------
    main2_frame = Frame(student_root, bd=4, relief=RIDGE, bg="black")
    main2_frame.place(x=680, y=70, width=650, height=300)

    main2_title = Label(main2_frame, text="Control Panel", font=("Arial", 20, "bold"), fg="#1aff1a", bg="black")
    main2_title.place(x=200, y=0)

    b1 = Button(main1_frame, command=add_student, width=30, text="Add Student", bg="black", fg="#1aff1a",
                font=("comicsanses", 10, "normal"))
    b1.place(x=110, y=230)

    b2 = Button(main2_frame, text="View All Student", width=30, command=view_student, bg="black", fg="#1aff1a",
                font=("comicsanses", 10, "normal"))
    b2.place(x=180, y=50)


    b4 = Button(main2_frame, text="Update Profile", width=30, command=update_student, bg="black", fg="#1aff1a",
                font=("comicsanses", 10, "normal"))
    b4.place(x=180, y=100)

    b3 = Button(main2_frame, text="Delete Profile", width=30, command=delete_student, bg="black", fg="#1aff1a",
                font=("comicsanses", 10, "normal"))
    b3.place(x=180, y=150)

    b5 = Button(main2_frame, text="Exit", width=30, command=clse, bg="black", fg="#1aff1a",
                font=("comicsanses", 10, "normal"))
    b5.place(x=180, y=200)

    b6=Label(main2_frame,text="Developed By:| Ashish Patil | Dipak Mahajan | Ruchee Chouhan |",bg="black", fg="#1aff1a")
    b6.place(x=100,y=260)
    # -----main3 frame-------------------
    main3_frame = Frame(student_root, bd=4, relief=RIDGE, bg="black")
    main3_frame.place(x=0, y=400, width=1366, height=300)

    # -----------Table data frame----------------
    t1 = Text(main3_frame, width=1300, height=250,fg='#1aff1a',bg="black",font=("Arial",10,'bold'))
    t1.grid(row=2, column=1)

    # --------data search--------------

student_root=Tk()
student_root.mainloop()