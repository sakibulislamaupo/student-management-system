import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pymysql


lms = tk.Tk()
lms.geometry("1350x800+0+0")
lms.title("Library Management System")
lms.config(background="#B2B2B2")

# Title....

title_label = tk.Label(lms, text="Library Management System", font=("Arial", 30, "bold"), border=12, relief=tk.GROOVE, background="#B2B2B2", foreground="black")
title_label.pack(side=tk.TOP, fill=tk.X)

# Detail....

detail_frame = tk.LabelFrame(lms, border=10, relief=tk.GROOVE, background="#B2B2B2", foreground="white")
detail_frame.place(x=30, y=120, width=470, height=600)

data_frame = tk.LabelFrame(lms, border=10, relief=tk.GROOVE, bg="#B2B2B2")
data_frame.place(x=500, y=120, width=800, height=575)

# Variables....

name = tk.StringVar()
id_val = tk.StringVar()
phone = tk.StringVar()
address = tk.StringVar()
bookid = tk.StringVar()
booktitle = tk.StringVar()
borrowdate = tk.StringVar()
duedate = tk.StringVar()
fine = tk.StringVar()

# Entry....

name_label = tk.Label(detail_frame, text="Name", background="#B2B2B2", font=("Arial", 18), foreground="black")
name_label.grid(row=0, column=0, padx=8, pady=8, sticky=tk.W)
name_entry = tk.Entry(detail_frame, background="white", font=("Arial",18), textvariable=name)
name_entry.grid(row=0, column=1, padx=8, pady=8)


id_label = tk.Label(detail_frame, text="ID", background="#B2B2B2", font=("Arial", 18), foreground="black")
id_label.grid(row=1, column=0, padx=8, pady=8, sticky=tk.W)
id_entry = tk.Entry(detail_frame, background="white", font=("Arial",18), textvariable=id_val)
id_entry.grid(row=1, column=1, padx=8, pady=8)


phone_label = tk.Label(detail_frame, text="Phone", background="#B2B2B2", font=("Arial", 18), foreground="black")
phone_label.grid(row=2, column=0, padx=8, pady=8, sticky=tk.W)
phone_entry = tk.Entry(detail_frame, background="white", font=("Arial",18), textvariable=phone)
phone_entry.grid(row=2, column=1, padx=8, pady=8)


address_label = tk.Label(detail_frame, text="Addredss", background="#B2B2B2", font=("Arial", 18), foreground="black")
address_label.grid(row=3, column=0, padx=8, pady=8, sticky=tk.W)
address_entry = tk.Entry(detail_frame, background="white", font=("Arial",18), textvariable=address)
address_entry.grid(row=3, column=1, padx=8, pady=8)


bookid_label = tk.Label(detail_frame, text="Book ID", background="#B2B2B2", font=("Arial", 18), foreground="black")
bookid_label.grid(row=4, column=0, padx=8, pady=8, sticky=tk.W)
bookid_entry = tk.Entry(detail_frame, background="white", font=("Arial",18), textvariable=bookid)
bookid_entry.grid(row=4, column=1, padx=8, pady=8)


booktitle_label = tk.Label(detail_frame, text="Book Title", background="#B2B2B2", font=("Arial", 18), foreground="black")
booktitle_label.grid(row=5, column=0, padx=8, pady=8, sticky=tk.W)
booktitle_entry = tk.Entry(detail_frame, background="white", font=("Arial",18), textvariable=booktitle)
booktitle_entry.grid(row=5, column=1, padx=8, pady=8)


borrowdate_label = tk.Label(detail_frame, text="Borrow Date", background="#B2B2B2", font=("Arial", 18), foreground="black")
borrowdate_label.grid(row=6, column=0, padx=8, pady=8, sticky=tk.W)
borrowdate_entry = tk.Entry(detail_frame, background="white", font=("Arial",18), textvariable=borrowdate)
borrowdate_entry.grid(row=6, column=1, padx=8, pady=8)


duedate_label = tk.Label(detail_frame, text="Due Date", background="#B2B2B2", font=("Arial", 18), foreground="black")
duedate_label.grid(row=7, column=0, padx=8, pady=8, sticky=tk.W)
duedate_entry = tk.Entry(detail_frame, background="white", font=("Arial",18), textvariable=duedate)
duedate_entry.grid(row=7, column=1, padx=8, pady=8)


fine_label = tk.Label(detail_frame, text="Fine", background="#B2B2B2", font=("Arial", 18), foreground="black")
fine_label.grid(row=8, column=0, padx=8, pady=8, sticky=tk.W)
fine_entry = tk.Entry(detail_frame, background="white", font=("Arial",18), textvariable=fine)
fine_entry.grid(row=8, column=1, padx=8, pady=8)



# Functions....

def connect_data():
    conn = pymysql.connect(host="localhost", user="root", password="", database="student management system")
    curr = conn.cursor()
    curr.execute("Select * from main")
    rows = curr.fetchall()
    if len(rows) != 0:
        monitor.delete(*monitor.get_children())
        for row in rows:
            monitor.insert('', tk.END, values=row)
        conn.commit()
    conn.close()

def add_function():
    if name.get() == " " or id_entry.get() == " " or phone.get() == " " or address.get() == " " or bookid.get() == " " or booktitle.get() == " " or borrowdate.get() == " " or duedate.get() == " " or fine.get() == " ":
        messagebox.showerror("Error!", "Please Fill All Inputs!")
    else:
        conn = pymysql.connect(host="localhost", user="root", password="", database="student management system")
        curr = conn.cursor()
        curr.execute("Insert into main values(%s,%s,%s,%s,%s,%s,%s,%s,%s)", (name.get(),
                                                                             id_val.get(),
                                                                             phone.get(),
                                                                             address.get(),
                                                                             bookid.get(),
                                                                             booktitle.get(),
                                                                             borrowdate.get(),
                                                                             duedate.get(),
                                                                             fine.get()))
        conn.commit()
        conn.close()
        connect_data()

def fetch_data(event):

    cursor_row = monitor.focus()
    content = monitor.item(cursor_row)
    row = content['values']

    name.set(row[0])
    id_val.set(row[1])
    phone.set(row[2])
    address.set(row[3])
    bookid.set(row[4])
    booktitle.set(row[5])
    borrowdate.set(row[6])
    duedate.set(row[7])
    fine.set(row[8])

def clear_function():

    name.set("")
    id_val.set("")
    phone.set("")
    address.set("")
    bookid.set("")
    booktitle.set("")
    borrowdate.set("")
    duedate.set("")
    fine.set("")

def update_function():

    conn = pymysql.connect(host="localhost", user="root", password="", database="student management system")
    curr = conn.cursor()
    curr.execute("Update main data set name=%s, phone=%s, address=%s, bookid=%s, booktitle=%s, borrowdate=%s, duedate=%s, fine=%s where id=%s", (name.get(), phone.get(),address.get(),bookid.get(),booktitle.get(),borrowdate.get(),duedate.get(),fine.get(),id_val.get()))
    conn.commit()
    connect_main()
    conn.close()

def delete_function():
    conn = pymysql.connect(host="localhost", user="root", password="", database="student management system")
    curr = conn.cursor()
    curr.execute("Delete from main where id=%s", (id_val.get()))
    conn.commit()
    connect_data()
    conn.close()


# Button....

button_frame = tk.Frame(detail_frame, background="lightgrey")
button_frame.place(x=65, y=450, width=288, height=135)

add_button = tk.Button(button_frame, text="Add", font=("Arial", 18, "bold"), background="lightgrey", border=5, width=8, command=add_function)
add_button.grid(row=0, column=0, padx=2, pady=2)

update_button = tk.Button(button_frame, text="Update", font=("Arial", 18, "bold"), background="lightgrey", border=5, width=8, command=update_function)
update_button.grid(row=0, column=1, padx=2, pady=2)

delete_button = tk.Button(button_frame, text="Delete", font=("Arial", 18, "bold"), background="lightgrey", border=5, width=8, command=delete_function)
delete_button.grid(row=1, column=0, padx=5, pady=15)

clear_button = tk.Button(button_frame, text="Clear", font=("Arial", 18, "bold"), background="lightgrey", border=5, width=8, command=clear_function)
clear_button.grid(row=1, column=1, padx=2, pady=15)

# Search....

search_frame = tk.Frame(data_frame, background="lightgrey", border=10, relief=tk.GROOVE)
search_frame.pack(side=tk.TOP, fill=tk.X)

search_label = tk.Label(search_frame, text="Main Monitor", background="lightgrey", font=("Arial", 25, "bold"))
search_label.grid(row=0, column=0, padx=8, pady=8
                  )


# Frame....

main_frame = tk.Frame(data_frame, background="lightgrey", border=10, relief=tk.GROOVE)
main_frame.pack(fill=tk.BOTH, expand=1)

y_scroll = tk.Scrollbar(main_frame, orient=tk.VERTICAL)
x_scroll = tk.Scrollbar(main_frame, orient=tk.HORIZONTAL)

monitor = ttk.Treeview(main_frame, columns=("name", "id", "phone", "address","bookid","booktitle","borrowdate","duedate","fine"), yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)

y_scroll.config(command=monitor.yview)
y_scroll.pack(side=tk.RIGHT, fill=tk.Y)

x_scroll.config(command=monitor.xview)
x_scroll.pack(side=tk.BOTTOM, fill=tk.X)

monitor.heading("name", text="Name")
monitor.heading("id", text="ID")
monitor.heading("phone", text="Phone")
monitor.heading("address", text="Address")
monitor.heading("bookid", text="BookID")
monitor.heading("booktitle", text="Book Title")
monitor.heading("borrowdate", text="Borrow Date")
monitor.heading("duedate", text="Due Date")
monitor.heading("fine", text="Fine")
monitor['show'] = 'headings'

monitor.pack(fill=tk.BOTH, expand=1)

connect_data()
monitor.bind("<ButtonRelease-1>", fetch_data)

lms.mainloop()