from  tkinter import *
from tkinter import messagebox
from PIL import ImageTk , Image
import pymysql

#Functionality Part




def forget_pass():
    def change_password():
        if user_entry.get()=='' or newpass_entry.get()=='' or confirmpass_entry.get()=='':
            messagebox.showerror('Error','All fields are required',parent=window)
        elif newpass_entry.get() !=  confirmpass_entry.get():
            messagebox.showerror('Erropr','passord and confirm password is not matching',parent=window)
        else:
                con = pymysql.connect(host='localhost', user='root', password='Password123#',database='Userdata')
                mycursor = con.cursor()
                query = 'select * from data  where username=%s'
                mycursor.execute(query, (user_entry.get()))
                row=mycursor.fetchone()
                if  row==None:
                    messagebox.showerror('Error','Incorrect Username ',parent=window)
                else:
                    query='update data set password=%s where username=%s'
                    mycursor.execute(query,(newpass_entry.get(),user_entry.get()))
                con.commit()
                con.close()
                messagebox.showinfo('Sucess','Password changed successfully',parent=window)
                window.destroy()



    window = Toplevel()
    window.title('Change Password')
    bgPic = ImageTk.PhotoImage(file='background.jpg')
    bglabel = Label(window, image=bgPic)
    bglabel.grid(row=0, column=0)

    heading_label = Label(window,text='RESET PASSWORD',font=('arial','18','bold'),
                          bg='white',fg='magenta2')
    heading_label.place(x=480, y=60)

    userLabel = Label(window,text='Username', font=('arial',12,'bold'),
                      bg='white',fg='orchid1')
    userLabel.place(x=470,y=130)

    user_entry = Entry(window, width=25, fg='magenta2',font=('arial',11,'bold'),bd=0, highlightthickness=0)
    user_entry.configure(bg='white')

    user_entry.place(x=470,y=160)

    Frame(window, width=225, height=2 , bg='orchid').place(x=459,y=180)

    passwordLabel = Label(window, text=' New Password', font=('arial', 12, 'bold'),
                      bg='white', fg='orchid1')
    passwordLabel.place(x=470, y=210)

    newpass_entry = Entry(window, width=25, fg='magenta2', font=('arial', 11, 'bold'),bd=0, highlightthickness=0)
    newpass_entry.configure(bg='white')
    newpass_entry.place(x=470, y=240)

    Frame(window, width=250, height=2, bg='orchid').place(x=470, y=260)

    confirmpassLabel = Label(window, text=' Confirm Password', font=('arial', 12, 'bold'),
                          bg='white', fg='orchid1')
    confirmpassLabel.place(x=470, y=290)

    confirmpass_entry = Entry(window, width=25, fg='magenta2', font=('arial', 11, 'bold'), bd=0,highlightthickness=0)
    confirmpass_entry.configure(bg='white')
    confirmpass_entry.place(x=470, y=320)

    Frame(window, width=250, height=2, bg='orchid').place(x=470, y=340)

    submitButton = Button(window, text='Submit', font=('Open Sans', 15, 'bold'), bd=0, bg='magenta2',
                          fg='white', activebackground='magenta2', activeforeground='white', width=15,
                          cursor='hand2',command=change_password)
    submitButton.place(x=470,y=390)



    window.mainloop()

def login_user():
    if usernameEntry.get()== '' or PasswordEntry.get()=='':
         messagebox.showerror('Error','All Fields Are Required')

    else:
        try:
           con=pymysql.connect(host='localhost', user='root', password='Password123#')
           mycursor=con.cursor()

        except:
            messagebox.showerror('Error','Connection is not established please try again')
            return
        query ='use Userdata'
        mycursor.execute(query)
        query='select * from data where username=%s and password=%s'
        mycursor.execute(query,(usernameEntry.get(),PasswordEntry.get()))
        row=mycursor.fetchone()
        if row==None:
            messagebox.showerror('Error','Invalid username or password')
        else:
            messagebox.showerror('Succes','login  is sccessfull')


def signup_page():
    login_window.destroy()
    import signup


def hide():
    openeye.configure(file='closeye.png')
    PasswordEntry.configure(show='*')
    eyeButton.configure(command=show)


def show():
    openeye.configure(file='openeye.png')
    PasswordEntry.configure(show='')
    eyeButton.configure(command=hide)
    

def user_enter(argue):
    if usernameEntry.get()=='Username' :
        usernameEntry.delete(0,END)


def password_enter(argue):
    if PasswordEntry.get()=='Password' :
        PasswordEntry.delete(0,END)
    

#GUI Part
login_window = Tk()
login_window.resizable(0,0)
login_window.title('Login Page')
bgImage=ImageTk.PhotoImage(file='bg.jpg')
bgLabel=Label(login_window,image=bgImage)
bgLabel.grid(row=0,column=0)

heading=Label(login_window,text='USER LOGIN',font=('Microsoft Yahei UI Light',23,'bold'),bg='white',fg='firebrick1')
heading.place(x=605,y=120)
usernameEntry=Entry(login_window,width=25,font=('Microsoft Yahei UI Light',11,'bold'),bd=0,fg='firebrick1')
usernameEntry.place(x=580,y=200)
usernameEntry.insert(0,'Username')
usernameEntry.bind('<FocusIn>',user_enter)

Frame(login_window,width=250,height=2,bg='firebrick1').place(x=580,y=222)


PasswordEntry=Entry(login_window,width=25,font=('Microsoft Yahei UI Light',11,'bold'),bd=0,fg='firebrick1')
PasswordEntry.place(x=580,y=260)
PasswordEntry.insert(0,'Password')
PasswordEntry.bind('<FocusIn>',password_enter)

Frame(login_window,width=250,height=2,bg='firebrick1').place(x=580,y=282)

openeye=PhotoImage(file='openeye.png')
eyeButton=Button(login_window,image=openeye,bd=0,bg='white',activebackground='white',cursor='hand2',command=hide)
eyeButton.place(x=800,y=255)

forgetButton=Button(login_window,text='Forgot Password ?',bd=0,bg='white',activebackground='white',cursor='hand2',font=('Microsoft Yahei UI Light',8,'bold'),fg='firebrick1',activeforeground='firebrick1',command=forget_pass)
forgetButton.place(x=706,y=290)

loginButton=Button(login_window,text='Login',font=('Open Sans', 16,'bold'),fg='white',bg='firebrick1',activeforeground='white',activebackground='firebrick1',cursor='hand2',bd=0,width=13,command=login_user)
loginButton.place(x=590,y=350)

orLabel=Label(login_window,text='------------------------OR-------------------------',font=('Open Sans',11),fg='firebrick1',bg='white')
orLabel.place(x=570,y=390)

facebook_logo=PhotoImage(file='facebook.png')
fbLabel=Label(login_window, image=facebook_logo,bg='white')
fbLabel.place(x=640,y=440)

google_logo=PhotoImage(file='google.png')
googleLabel=Label(login_window, image=google_logo,bg='white')
googleLabel.place(x=690,y=440)

twitter_logo=PhotoImage(file='twitter.png')
twitterLabel=Label(login_window, image=twitter_logo,bg='white')
twitterLabel.place(x=750,y=440)

SignupLabel=Label(login_window,text='Dont have account?',font=('Open Sans',9,'bold'),fg='firebrick1',bg='white')
SignupLabel.place(x=590,y=500)

newaccountButton=Button(login_window,text='Create new one',font=('Open Sans', 7,'bold underline'),
                        fg='blue',bg='white',activeforeground='blue',activebackground='firebrick1',cursor='hand2',bd=0,command=signup_page)
newaccountButton.place(x=741,y=500)


login_window.mainloop()
