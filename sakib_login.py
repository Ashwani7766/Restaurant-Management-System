from tkinter import *
from tkinter import messagebox
#from PIL import Image,ImageTk

root=Tk()
root.geometry("860x600")
root.title("login page")
root.configure(bg='#ECC30F')
cc=StringVar()
ccc=StringVar()
#Frames
top = Frame(root,bg='#EE960F')
top.pack(side=TOP)

left = Frame(root,bg='#EE960F')
left.pack(side=LEFT,padx=10)

right = Frame(root,bg='#BA4606')
right.pack(side=RIGHT,padx=10)

def enter():
	if cc.get() == "abcd" and ccc.get() == "123456":
		root.destroy()
		import question
	else:
		tkinter.messagebox.showinfo('Error','Authentication Failed')
		cc.set("")
		ccc.set("")	

#image

'''i=Image.open(r"pizza.jpg")
i1=ImageTk.PhotoImage(i)
label=Label(left,image=i1)
label.pack()
'''
#labels
L0=Label(top,text='WELCOME TO CAFETERIA MANAGAEMENT SYSTEM',font=('Bauhaus 93',25),bg='#ECC30F',fg='#EC270F',pady=30)
L0.pack()
L=Label(top,text='Golden Chef',font=('Bauhaus 93',30),bg='#ECC30F',fg='#EC270F',pady=30)
L.pack(padx=30)

L1=Label(right,text='Login',bg='#BA4606',fg='#060923',font=('Bauhaus 93',30))
L1.grid(row=0,column=0)
L2=Label(right,text='_________________',bg='#BA4606')
L2.grid(row=1,column=0)
L3=Label(right,text='Username',bg='#BA4606',fg='#060923',font=('Times New Roman',13))
L3.grid(row=2,column=0)
L4=Label(right,text='Password',bg='#BA4606',fg='#060923',font=('Times New Roman',13))
L4.grid(row=3,column=0)

#button
B1=Button(right,text='Continue',bg='#F31E14',fg='white',font=('Times New Roman',13),command=enter)
##command pending
B1.grid(row=4,column=1,sticky=E,padx=32,pady=10)

#Entry
E1=Entry(right,bd=2,width=20,textvariable=cc).grid(row=2,column=1,padx=30,pady=40)
E2=Entry(right,bd=2,width=20,show="*",textvariable=ccc).grid(row=3,column=1,padx=30,pady=40)

    
    
root.mainloop()
