from tkinter import *
from tkinter import messagebox
left1 = Tk()
left1.geometry("1600x800+0+0")
left1.title("Change Price")

label4 = Label(left1, font = ('arial',50,'bold'), text ="Change Price", fg = "black", bd = 10, anchor = 'w')
label4.grid(row = 0)

fries_inp_p = StringVar()
Sandwich_inp_p = StringVar()
burger_inp_p = StringVar()
drinks_inp_p = StringVar()
Pasta_inp_p = StringVar()
Tacos_inp_p = StringVar()
def update():
        if (fries_inp_p.get().isalpha()):
                messagebox.showinfo('Error','Incorrect Input')
                fries_inp_p.set("")
        #elif(fries_inp_p.get()==""):
            #fries_inp_p.set(a)
        if (Sandwich_inp_p.get().isalpha()):
                messagebox.showinfo('Error','Incorrect Input')
                Sandwich_inp_p.set("")
        #elif(Sandwich_inp_p.get()==""):
            #Sandwich_inp_p.set(b)
        if (burger_inp_p.get().isalpha()):
                messagebox.showinfo('Error','Incorrect Input')
                burger_inp_p.set("")
        #elif(burger_inp_p.get()==""):
            #burger_inp_p.set(c)
        if (drinks_inp_p.get().isalpha()):
                messagebox.showinfo('Error','Incorrect Input')
                drinks_inp_p.set("")
        #elif(drinks_inp_p.get()==""):
           # drinks_inp_p.set(d)
        
        if (Pasta_inp_p.get().isalpha()):
                messagebox.showinfo('Error','Incorrect Input')
                Pasta_inp_p.set("")
       # elif(Pasta_inp_p.get()==""):
            #Pasta_inp_p.set(e)
        if (Tacos_inp_p.get().isalpha()):
                messagebox.showinfo('Error','Incorrect Input')
                Tacos_inp_p.set("")   
        #elif(Tacos_inp_p.get()==""):
            #Tacos_inp_p.set(f)
        f1=open('value.txt','w')
        f1.write("{}\n{}\n{}\n{}\n{}\n{}".format(fries_inp_p.get(),Sandwich_inp_p.get(),burger_inp_p.get(),drinks_inp_p.get(),Pasta_inp_p.get(),Tacos_inp_p.get()))
        f1.close()
        messagebox.showinfo('YEAY','Updated Successfully')
def reset1():
	fries_inp_p.set("")
	Sandwich_inp_p.set("")
	burger_inp_p.set("")
	drinks_inp_p.set("")
	Pasta_inp_p.set("")
	Tacos_inp_p.set("")

def qexit1():
	left1.destroy()

def printfn():
        f1=open('value.txt','r')
        a=f1.readlines()
        print("UPDATED PRICE IS \n\n")
        for i in range(len(a)):
            
                if i==0 :
                    print('Fries=',a[i])
                elif i==1 :
                    print('Sandwich=',a[i])
                elif i==2 :
                    print('Burger=',a[i])
                elif i==3 :
                    print('Coffee=',a[i])
                elif i==4 :
                    print('Pasta=',a[i])
                else:
                    print('Tacos=',a[i])
        messagebox.showinfo('YEAY','Printed Successfully')
                    
        f1.close()
def backfn():
	left1.destroy()
	import question


fries = Label(left1, font=('arial',16,'bold'),text = "Fries", bd = 16, anchor = 'w' )
fries.grid(row=1,column=0,sticky = E)
txt_fries = Entry(left1,font=('arial',16,'bold'), textvariable=fries_inp_p, bd=10, insertwidth =4,bg = "purple", justify ='right')
txt_fries.grid(row=1,column=1)

Sandwich = Label(left1, font=('arial',16,'bold'),text = "Sandwich", bd = 16, anchor = 'w' )
Sandwich.grid(row=2,column=0,sticky = E)
txt_Sandwich = Entry(left1,font=('arial',16,'bold'), textvariable=Sandwich_inp_p, bd=10, insertwidth =4,bg = "green", justify ='right')
txt_Sandwich.grid(row=2,column=1)


burger = Label(left1, font=('arial',16,'bold'),text = "Burger", bd = 16, anchor = 'w' )
burger.grid(row=3,column=0,sticky = E)
txt_burger = Entry(left1,font=('arial',16,'bold'), textvariable=burger_inp_p, bd=10, insertwidth =4,bg = "orange", justify ='right')
txt_burger.grid(row=3,column=1)

drinks = Label(left1, font=('arial',16,'bold'),text = "Coffee", bd = 16, anchor = 'w' )
drinks.grid(row=4,column=0,sticky = E)
txt_drinks = Entry(left1,font=('arial',16,'bold'), textvariable=drinks_inp_p, bd=10, insertwidth =4,bg = "red", justify ='right')
txt_drinks.grid(row=4,column=1)

Pasta = Label(left1, font=('arial',16,'bold'),text = "Pasta", bd = 16, anchor = 'w' )
Pasta.grid(row=5,column=0,sticky = E)
txt_Pasta = Entry(left1,font=('arial',16,'bold'), textvariable=Pasta_inp_p, bd=10, insertwidth =4,bg = "yellow", justify ='right')
txt_Pasta.grid(row=5,column=1)

Tacos = Label(left1, font=('arial',16,'bold'),text = "Tacos", bd = 16, anchor = 'w' )
Tacos.grid(row=6,column=0,sticky = E)
txt_Tacos = Entry(left1,font=('arial',16,'bold'), textvariable=Tacos_inp_p, bd=10, insertwidth =4,bg = "blue", justify ='right')
txt_Tacos.grid(row=6,column=1)


btn_update = Button(left1, padx= 16, pady= 8, bd= 16, fg= "black", font=('arial',16,'bold'), width=10, text= "Update", bg= "yellow",command = update)
btn_update.grid(row=7, column= 1)

btn_reset1 = Button(left1, padx= 16, pady= 8, bd= 16, fg= "black", font=('arial',16,'bold'), width=10, text= "Reset", bg= "yellow",command = reset1)
btn_reset1.grid(row=7, column= 2)

btn_exit1 = Button(left1, padx= 16, pady= 8, bd= 16, fg= "black", font=('arial',16,'bold'), width=10, text= "Exit", bg= "yellow",command = qexit1)
btn_exit1.grid(row=7, column= 3)

btn_print = Button(left1, padx= 16, pady= 8, bd= 16, fg= "black", font=('arial',16,'bold'), width=10, text= "print", bg= "yellow",command = printfn)
btn_print.grid(row=7, column= 4)

btn_back = Button(left1, padx= 16, pady= 8, bd= 16, fg= "black", font=('arial',16,'bold'), width=10, text= "Back", bg= "yellow",command = backfn)
btn_back.grid(row=8, column= 3)



left1.mainloop()

