from idlelib.pyshell import usage_msg
from tkinter import *
from tkinter import filedialog,messagebox
from PIL import Image,ImageTk
import os
from stegano import lsb

win =Tk()
win.geometry('900x480')
win.config(bg='black')
#button Function
def open_img():
    global open_file
    open_file=filedialog.askopenfilename(initialdir=os.getcwd(),
                                         title='select file type',
                                         filetypes=(('png file','*.png'),('JPG file','*.jpg'),
                                                    ('all file','*.txt')))
    img = Image.open(open_file)
    img = ImageTk.PhotoImage(img)
    lf1.configure(image=img)
    lf1.image=img
def hide():
    global hide_msg
    password = code.get()
    if password =='256651':
        msg =text1.get(1.0,END)
        hide_msg = lsb.hide(str(open_file),msg)
        messagebox.showinfo('success','your message is sucessfully hiden in a image , please save your image')
    elif password =='':
        messagebox.showerror('Error','please enter secret key')
    else:
        messagebox.showerror('error','Wrong secret key')
        code.set('')
    msg=text1.get(1.0,END)
    hide_msg=lsb.hide(str(open_file),msg)
    def hide():
        global hide_msg
        msg=text1.get(1.0,END)
        hide_msg=lsb.hide(str(open_file),msg)
def save_img():
    hide_msg.save('secret file.png')
    messagebox.showinfo('saved','Image has been successfully saved')

def show():
    password = code.get()
    if password =='256651':
         show_msg=lsb.reveal(open_file)
         text1.delete(1.0,END)
         text1.insert(END,show_msg)
    elif password =='':
        messagebox.showerror('Error','please enter secret key')
    else:
        messagebox.showerror('error','Wrong secret key')
        code.set('')

#logo
logo = PhotoImage(file='logo.png')
Label(win,image=logo,bd=0).place(x=0,y=0)
#Heading
Label(win,text='steganography',font='impack 30 bold',bg='black',fg='red').place(x=950,y=20)
#image
Label(win,text='Image',font='impack 30 bold',bg='black',fg='red').place(x=900,y=300)
#Text
Label(win,text='Text',font='impack 30 bold',bg='black',fg='red').place(x=1170,y=300)
#Frame 1
f1 = Frame(win,width=250,height=220,bd=5,bg='Grey')
f1.place(x=830,y=80)
lf1 = Label(f1,bg='grey')
lf1.place(x=0,y=0)
#frame 2
f2 = Frame(win,width=250,height=220,bd=5,bg='white')
f2.place(x=1100,y=80)
text1=Text(f2,font='ariel 15 bold',wrap=WORD)
text1.place(x=0,y=0,width=310,height=210)
#Label for secret key
Label(win,text='Enter secret key',font='10',bg='black',fg='green').place(x=1040,y=330)
#entry widget for secret key
code=StringVar()
e=Entry(win,textvariable=code,bd=2,font='impact 10 bold',show='*')
e.place(x=1020,y=360)
#Buttons
open_button=Button(win,text='open Image',bg='grey',fg='red',font='ariel 12 bold',cursor='hand2',command=open_img)
open_button.place(x=850,y=417)

save_button=Button(win,text='save Image',bg='grey',fg='red',font='ariel 12 bold',cursor='hand2',command=save_img)
save_button.place(x=970,y=417)

hide_button=Button(win,text='Hide Data',bg='grey',fg='red',font='ariel 12 bold',cursor='hand2',command=hide)
hide_button.place(x=1150,y=417)

show_button=Button(win,text='Show Data',bg='grey',fg='red',font='ariel 12 bold',cursor='hand2',command=show)
show_button.place(x=1250,y=417)

mainloop()