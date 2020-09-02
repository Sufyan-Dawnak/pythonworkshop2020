from tkinter import *
from PIL import Image,ImageTk   
import csv
main = Tk()
main.title("REGISTRATION FORM")
main.geometry("400x475")
p1 = ImageTk.PhotoImage(file = 'b.jpg') ''' ImageTk to deal with a picture in jpeg format '''
main.iconphoto(FALSE,p1) ''' for making icon '''


l = Label(main, text="REGISTRATION FORM",font=("bold", 10),bg='ivory3',fg='black')
l.place(x=120,y=15)

l1 = Label(main, text="USER NAME",font=("bold", 10),bg='ivory3',fg='black')
l1.place(x=40,y=70)
e1 = Entry(main, bd = 8)
e1.place(x=180,y=70)

l2 = Label(main, text="DATE OF BIRTH",font=("bold", 10) ,bg='ivory3',fg='black')
l2.place(x=40,y=140)
e2 = Entry(main, bd = 8)
e2.place(x=180,y=140)

l3 = Label(main, text="ACCOUNT NO.",font=("bold", 10),bg='ivory3',fg='black')
l3.place(x=40,y=210)
e3 = Entry(main, bd = 8)
e3.place(x=180,y=210)

l4 = Label(main, text="CARD NO.",font=("bold", 10),bg='ivory3',fg='black')
l4.place(x=40,y=280)
e4 = Entry(main, bd = 8)
e4.place(x=180,y=280)

l5 = Label(main, text="PIN CODE",font=("bold", 10),bg='ivory3',fg='black')
l5.place(x=40,y=350)
e5 = Entry(main, bd = 8)
e5.place(x=180,y=350)


def save():''' a fuction to save the user entered data in a csv file'''
    with open('acc.csv','r',newline = '') as file:
        entry = csv.reader(file) 
        rows=list(entry)
        total=len(rows)
        b = total - 1 +1 
        with open('acc.csv','a',newline = '') as file:
            writer = csv.writer(file)
            p = int(e5.get())
            if(p!=0):
                name=e1.get()
                dob=e2.get()
                acc=e3.get()
                card=e4.get()
                pin=e5.get()
                bal = 0
                chn = 3
                stat = 'active'
                print("\n")
                writer.writerow([b,name,dob,acc,card,pin,bal,chn,stat])
                print('____ENTRIES DONE SUCCESSFULLY____')
                print("REGISTERED NUMBER OF ENTRIES ARE : ", b)
            else:
                print("___NO ENTRIES___")
         
       


b = Button(main,text='SUBMIT',width=5,bg='green',fg='black',command = save)
b.place(x=90,y=420)


def clear():'''a function to clear entry fields'''
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)

b = Button(main,text='CLEAR',width=5,bg='red',fg='black',command = clear)
b.place(x=180,y=420)

def exit():
    sys.exit()

b = Button(main,text='EXIT',width=5,bg='red',fg='black',command = exit)
b.place(x=270,y=420)
main.configure(background='ghost white')
main.mainloop()

