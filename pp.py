import tkinter as tk
import mysql.connector


# iski place pr hum import tkinter * kr skte the but nhi krenge kyuki * me ttk module nhi aata
win=tk.Tk()
 
win.geometry('500x500')
win.title('Registration form')

Fullname=tk.StringVar()
Age=tk.IntVar()
Email=tk.StringVar()
c=tk.StringVar()
var=tk.IntVar()

def database():
    name1 = Fullname.get()
    age = Age.get()
    mail = Email.get()
    gender = var.get()
    city = c.get()
    conn =mysql.connector.connect(host='localhost',user='root', password='',database='form')

    cursor1=conn.cursor()
    cursor1.execute("CREATE TABLE IF NOT EXISTS student (Fullname VARCHAR(20) ,Age INTEGER(10),Email VARCHAR(30), Gender VARCHAR(10), city VARCHAR(20)) ")
    cursor1.execute("INSERT INTO student (Fullname,Age,Email,Gender,city) VALUES(%s,%s,%s,%s,%s)",(name1,age,mail,gender,city))
    conn.commit()



# Creating labels
heading_label = tk.Label(win, text="Register", width= 20, font=("bold,20"))
heading_label.place(x=130, y=70)

Name_label= tk.Label(win, text='Enter your name : ', width=20,font=('bold',10))
Name_label.place(x=80,y=130)

Name_entry=tk.Entry(win,textvar=Fullname)
Name_entry.place(x=240,y=130)

Age_label= tk.Label(win, text='Enter your age : ',width=20, font=('bold',10))
Age_label.place(x=80,y=166)

Age_entry=tk.Entry(win,textvar=Age)
Age_entry.place(x=240,y=166)

Email_label= tk.Label(win, text='Enter mail : ',width=20, font=('bold',10))
Email_label.place(x=70,y=200)

Email_entry = tk.Entry(win,textvar=Email)
Email_entry.place(x=240,y=200)

Gender_label= tk.Label(win, text='Enetr your gender : ',width=20, font=('bold',10))
Gender_label.place(x=68,y=230)

tk.Radiobutton(win, text='Male', padx=5, variable=var, value=1).place(x=235,y=230)
tk.Radiobutton(win, text='Female', padx=20,variable=var, value=2).place(x=290,y=230)

City_lable= tk.Label(win, text="City :", width=20, font=('bold',10))
City_lable.place(x=100,y=270)
list1=['Ahemdabad','Banglore','Delhi','Indore','Mumbai','pune']

droplist=tk.OptionMenu(win,c, *list1)
# tk.OptionMenu()
droplist.config(width=15)
c.set("select youe city")
droplist.place(x=240,y=265)

tk.Button(win,text='ADD', width=20, bg='brown', fg='white',command=database).place(x=170,y=340)


win.mainloop()
