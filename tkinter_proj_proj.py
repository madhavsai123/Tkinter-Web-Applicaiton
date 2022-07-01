from tkinter import *
from tkinter import messagebox
import os

root=Tk()

root.title("Login Page for Tkinter")

root.geometry("900x600+300+100")

root.minsize(100,100)
root.maxsize(1600,1400)





def save():
 
    a=var_u.get()
    b=var_p.get()

    f=open('record1.txt','a')
    f.write('\t'+a)
    f.close()
    f1=open('record2','a')
    f1.write('\t'+b)
    f1.close()
    messagebox.showinfo("you have been regerstered in the database")
     







Label(root,text="Username: ", bg="red", fg="white",font=("Times New Roman", 20, "bold")).place(x=45,y=45)
var_u=StringVar(); Entry(root,textvariable=var_u,font=("Times New Roman", 20, "bold"),bg="red",fg="white",width=13).place(x=200,y=45)

Label(root,text="Password: ",bg="red", fg="white", font=("Times New Roman", 20, "bold")).place(x=45, y=100)
var_p=StringVar(); Entry(root,textvariable=var_p,font=("Times New Roman", 20, "bold"), bg="red", fg="white", width=13,show='*').place(x=200,y=95)


def login():



        
    a=var_u.get()
    b=var_p.get()

    with open("record1.txt") as f:
        v=f.read() 
        if a in v:
            file=open("record2",'r')
            v=file.read()
            messagebox.showinfo("Username sucesfull")
            if b in v:
                messagebox.showinfo("Sucesfully loged in")
    
    







Button(root,text="Save Details",bg="green", fg="blue",  activebackground="orange", command=save, activeforeground="pink", font=("Times New Roman", 20, "bold"),bd=10,relief=RAISED).place(x=150,y=400)
Button(root,text="Login In",bg="green", fg="blue",  activebackground="pink", command=login, activeforeground="orange", font=("Times New Roman", 20, "bold"),bd=10,relief=RAISED).place(x=200,y=450)

root.mainloop()

