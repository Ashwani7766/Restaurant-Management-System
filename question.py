from tkinter import*

newroot = Tk()
newroot.geometry("600x500")
newroot.title("Menu")
newroot.configure(bg='#ECC30F')



def enter1():
	newroot.destroy()
	import restaurant_management_system

def enter2():
	newroot.destroy()
	import price_new

#Frames
top=Frame(newroot,height=50,relief=SUNKEN)
top.pack()
bottom=Frame(newroot,relief=SUNKEN,bg='#BA4606')
bottom.pack(pady=20)


heading = Label(top, text="WELCOME TO BILLING SYSTEM ",font=('Bauhaus 93',25),fg='blue',pady=30)
heading.pack()


bill = Label(bottom, text="Bill",bg='#BA4606',fg='#060923',font=('Times New Roman',17))
bill.grid(row=0,column=0,sticky=W)

bill_btn = Button(bottom, text="Press Here ",command= enter1, fg="white" , bg="black")
bill_btn.grid(row=0,column=1,padx=60,pady=20)


change_price = Label(bottom, text="Change Price",bg='#BA4606',fg='#060923',font=('Times New Roman',17))        
change_price.grid(row=1,column=0,sticky=W)

change_price_btn = Button(bottom, text="Press Here",  command= enter2, fg="white" , bg="black")
change_price_btn.grid(row=1,column=1,padx=60,pady=20)

newroot.mainloop()
