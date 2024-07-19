from tkinter import *
import mysql.connector 
import subprocess
from PIL import Image,ImageTk
import os
import webbrowser
from tkinter import messagebox
from dataBase import DataBase
from tools import *

db=DataBase()


    
current_path=os.getcwd()
account=Tk()
account.title("LES COURS")
account.geometry("1200x720")
account.config(bg="white")
iconsbarr=Frame(account,width=170,height=1440,bg="#15b4ea",)
iconsbarr.place(x=0,y=0)






#-----------------------------import icons----------------------------------------

person_icon=create_icon(current_path+"\\icons\\person_icon1.png",(80,80))
person_button=Button(iconsbarr,text="PROFIL",command=lambda account=account: person(account), image=person_icon,compound="top" ,font=("Louis George Cafe",20),padx=0,pady=0,relief="flat",bg="#15b4ea",activebackground="#15b4ea",fg="white",activeforeground="white",highlightcolor="white")
person_button.place(x=18,y=0)


school_icon=create_icon(current_path+"\\icons\\school.png",(80,80))
school_icon_button=Button(iconsbarr,image=school_icon,padx=0,pady=0, command=lambda account=account :accueil(account),relief="flat",bg="#15b4ea",activebackground="#15b4ea",compound="top" ,font=("Louis George Cafe",20),text="ACCUEIL",fg="white",activeforeground="white")
school_icon_button.place(x=10,y=115)

paper=create_icon(current_path+"\\icons\\paper1.png",(70,70))
paper_button=Button(iconsbarr,bg="#15b4ea",padx=0,pady=0,command=lambda account=account :description(account), relief="flat",image=paper,activebackground="#15b4ea",compound="top" ,font=("Louis George Cafe",20),text="DESCRIPT°",fg="white",activeforeground="white")
paper_button.place(x=0,y=230)

book_icon=create_icon(current_path+"\\icons\\book.png",(70,70))
book_icon_button=Button(iconsbarr,bg="#15b4ea",padx=0,pady=0,command=lambda account=account :cours(account), relief="flat",image=book_icon,activebackground="#15b4ea",compound="top" ,font=("Louis George Cafe",18),text="COURS",fg="white",activeforeground="white")
book_icon_button.place(x=25,y=335)


agenda_icon=create_icon(current_path+"\\icons\\agenda.png",(60,60))
agenda_icon_button=Button(iconsbarr,bg="#15b4ea",padx=0,pady=0, relief="flat",command=db.get_schedule, image=agenda_icon,activebackground="#15b4ea",compound="top" ,font=("Louis George Cafe",15),text="EMPLOI DU \n DU TEMPS",fg="white",activeforeground="white")
agenda_icon_button.place(x=10,y=460)
support_icon=create_icon(current_path+"\\icons\\support.png",(70,70))
def open_email_client():
    webbrowser.open('mailto:equipetechniquestkinter@gmail.com')

button = Button(iconsbarr, command=open_email_client, image=support_icon, relief="flat", bg="#15b4ea",activebackground="#15b4ea")
button.place(x=30,y=630)

#--------------------------leave button-------------------------------------------
leavebutton=Button(account,text="Quitter",command=account.quit,bg="#258EF5",fg="white",activebackground="#258EF5", activeforeground="white",font=("Arial",16),padx=0,pady=0, relief="flat")      #
leavebutton.place(x=1100, y=675)
#--------------------------logout button--------------------------------------------
logout=Button(account,text="Partir",command=lambda win=account: log_out(win),bg="#258EF5",fg="white",activebackground="#258EF5", activeforeground="white",font=("Arial",16),padx=0,pady=0, relief="flat")      #
logout.place(x=180, y=675)
#----------------------Les cours----------------------------------




#----------------------Les cours----------------------------------

body_frame=Frame(account,bg="#B5EFFF", width=940,height=640,relief="flat")
body_frame.place(x=200,y=30)


re1=db.get_modules()
re2=db.get_modules_links()
re1 = [elem[0].replace('(', '').replace(')', '').replace(',', '') for elem in re1]
re2=[elem[0].replace('(', '').replace(')', '').replace(',', '') if elem[0] is not None else None for elem in re2]
dy=20
for i in range(0, len(re1)):
    if re2[i] is None or re2[i].lower() == 'none':
        l1=Label(body_frame,text=str(re1[i])+": ",bg="#B5EFFF",fg="#0073e6",font=("Arila",20))
        l1.place(x=40,y=dy) 
        l2=Label(body_frame, text='Pas de cours',bg="#B5EFFF",fg="#BC5294",font=("Arila",20))
        l2.place(x=735,y=dy)
    else:
        l1=Label(body_frame,text=re1[i]+": ",bg="#B5EFFF",fg="#0073e6",font=("Arila",20))
        l1.place(x=40,y=dy)
        cours_lien=Button(body_frame,bg="#15b4ea",padx=0,pady=0, relief="flat",command=lambda i=i:db.cours_acces(i),activebackground="#15b4ea",compound="top" ,font=("Louis George Cafe",15,"underline","bold"),text="Clique ici",fg="#F9F871",activeforeground="white")
        cours_lien.place(x=735,y=dy)
    dy=dy+47



account.mainloop()


