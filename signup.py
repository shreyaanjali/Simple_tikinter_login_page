from tkinter import *
from tkinter import messagebox
from PIL import ImageTk , Image
import pymysql


def clear():
    emailEntry.delete(0,END)
    usernameEntry.delete(0,END)
    passwordEntry.delete(0,END)
    confirmpasswordEntry.delete(0,END)
    check.set(0)


#function is declared here

def login_page():
    signup_window.destroy()
    import signing


def connect_database():
    if emailEntry.get() =='' or usernameEntry.get =='' or passwordEntry.get =='' or confirmpasswordEntry.get == '' :
        messagebox.showerror('Error', 'All fields are required')
    elif passwordEntry.get() != confirmpasswordEntry.get():
        messagebox.showerror('Error','password is not matching')

    elif check.get()==0:
        messagebox.showerror('Error','please accept the terms and conditions')
    

    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='Password123#')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Database connectivity issue , Please try again')
            return

        try:
           query='create database Userdata'
           mycursor.execute(query)
           query= 'use Userdata'
           mycursor.execute(query)
           query='create table data(id int auto_increment primary key not null, email varchar(50), username varchar(100),password varchar(20))'
           mycursor.execute(query)

        except:
             mycursor.execute('use Userdata')

        query='select * from data where username=%s'
        mycursor.execute(query,(usernameEntry.get()))

        row=mycursor.fetchone()
        if row !=None:
            messagebox.showerror('Error','Username alreday exits')

        else:
             query='insert into data (email,username,password) values(%s,%s,%s)'
             mycursor.execute(query,(emailEntry.get(),usernameEntry.get(),passwordEntry.get()))
             con.commit()
             con.close()
             messagebox.showinfo('Success','Registration is successful')
             clear()
             signup_window.destroy()
             import signing






signup_window=Tk()
signup_window.resizable(0,0)
signup_window.title('Signup page')
bgImage=ImageTk.PhotoImage(file='bg.jpg')
bgLable=Label(signup_window,image=bgImage)
bgLable.grid(row=0,column=0)

frame=Frame(signup_window,bg='white')
frame.place(x=554,y=100)

heading=Label(frame,text='CREATE AN ACCOUNT',font=('Microsoft Yahei UI Light',17,'bold'),bg='white',fg='firebrick1')
heading.grid(row=0,column=0,padx=10,pady=10)

emailLabel=Label(frame,text='Email',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
emailLabel.grid(row=1,column=0,sticky='w',padx=25,pady=(10,0))

emailEntry=Entry(frame,width=25,font=('Microsoft Yahei UI Light',10,'bold'),fg='white',bg='firebrick1')
emailEntry.grid(row=2,column=0,sticky='w',padx=25)




usernameLabel=Label(frame,text='Username',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
usernameLabel.grid(row=3,column=0,sticky='w',padx=25,pady=(10,0))

usernameEntry=Entry(frame,width=25,font=('Microsoft Yahei UI Light',10,'bold'),fg='white',bg='firebrick1')
usernameEntry.grid(row=4,column=0,sticky='w',padx=25)


passwordLabel=Label(frame,text='Password',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
passwordLabel.grid(row=5,column=0,sticky='w',padx=25,pady=(10,0))

passwordEntry=Entry(frame,width=25,font=('Microsoft Yahei UI Light',10,'bold'),fg='white',bg='firebrick1')
passwordEntry.grid(row=6,column=0,sticky='w',padx=25)



confirmpasswordLabel=Label(frame,text=' Confirm password',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
confirmpasswordLabel.grid(row=7,column=0,sticky='w',padx=25,pady=(10,0))

confirmpasswordEntry=Entry(frame,width=25,font=('Microsoft Yahei UI Light',10,'bold'),fg='white',bg='firebrick1')
confirmpasswordEntry.grid(row=8,column=0,sticky='w',padx=25)

check=IntVar()
termsandconditions=Checkbutton(frame,text='I Agree to the Terms and Conditions',font=('Microsoft Yahei UI Light',8,'bold'),
                               fg='firebrick1',bg='white',activebackground='white',activeforeground='firebrick1',cursor='hand2' ,variable=check)     
termsandconditions.grid(row=9 ,column=0,pady=10,padx=20)



signupButton=Button(frame,text='Signup',font=('Open Sans',15,'bold'),bd=0,bg='firebrick1',
                    fg='white',activebackground='firebrick1',activeforeground='white',width=15,command=connect_database)
signupButton.grid(row=10,column=0,pady=10)



alreadyaccount=Label(frame,text="Don't have an account?",font=('Open Sans',9,'bold'),fg='firebrick1',bg='white')
alreadyaccount.grid(row=11,column=0,sticky='w',padx=25,pady=10)


#--loginButton=Button(frame,text='Log in',font=('Open Sans', 15,'bold underline'),bd=0,
                   #bg='white',fg='blue',activebackground='white', activeforeground='firebrick1',cursor='hand2')

LoginButton=Button(frame,text='login',font=('Open Sans',9,'bold underline'),bd=0,bg='white',
                    fg='blue',activebackground='white',activeforeground='blue',width=4,command=login_page)

LoginButton.place(x=190,y=367)




signup_window.mainloop()
