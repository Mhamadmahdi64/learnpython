#This imports all the classes, functions, and constants from the Tkinter module, allowing us to use them in our code.
from tkinter import *
#This imports the datetime module, which provides classes to work with dates and times.
import datetime
#This imports the openpyxl module, which allows us to work with Excel files.
import openpyxl
from openpyxl import Workbook
root = Tk()
root.geometry("950x552")
root.iconbitmap('img/icon.ico')
root.title('Market tools for buildings')
#=====[Creating a Frame:]======
F1 = Frame(root,bg='silver',width=600,height=550)
F1.place(x=1,y=1) 
#=====[loading images]=====for sure replace your own images with your own ones

img_menu1 = PhotoImage(file='img/1.png')
img_menu2 = PhotoImage(file='img/2.png')
img_menu3 = PhotoImage(file='img/3.png')
img_menu4 = PhotoImage(file='img/4.png')
img_menu5 = PhotoImage(file='img/5.png')
img_menu6 = PhotoImage(file='img/6.png')

#Creating Labels and Buttons:
title = Label(F1,text='projects for sale building tools',font=('times new roman',20,'bold'),fg='white',bg='#5F7161')
title.place(x=0,y=0)

menu1 = Button(F1,width=88,bg='#EFEAD8',bd=1,relief=SOLID,cursor='hand2',height = 85 ,image=img_menu1,text='wrench',compound=TOP) 
menu1.place(x=30,y=45)

menu2 = Button(F1,width=88,bg='#EFEAD8',bd=1,relief=SOLID,cursor='hand2',height = 85 ,image=img_menu2,text='keys',compound=TOP) 
menu2.place(x=170,y=45)
menu3 = Button(F1,width=88,bg='#EFEAD8',bd=1,relief=SOLID,cursor='hand2',height = 85 ,image=img_menu3,text='screwdriver',compound=TOP) 
menu3.place(x=310,y=45)
menu4 = Button(F1,width=88,bg='#EFEAD8',bd=1,relief=SOLID,cursor='hand2',height = 85 ,image=img_menu4,text='screwdriver',compound=TOP) 
menu4.place(x=30,y=150)
menu5 = Button(F1,width=88,bg='#EFEAD8',bd=1,relief=SOLID,cursor='hand2',height = 85 ,image=img_menu5,text='screwdriver',compound=TOP) 
menu5.place(x=170,y=150)
menu6 = Button(F1,width=88,bg='#EFEAD8',bd=1,relief=SOLID,cursor='hand2',height = 85 ,image=img_menu6,text='screwdriver',compound=TOP) 
menu6.place(x=310,y=150)
#Running the Application:
root.mainloop()


