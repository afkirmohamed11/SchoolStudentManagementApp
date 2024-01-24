from tkinter import *
import subprocess
import os
from dataBase import DataBase
from tools import *



db=DataBase()


    

current_path=os.getcwd()
account=Tk()
account.geometry("1200x720")
account.config(bg="white")
account.title("ACCUEIL")
iconsbarr=Frame(account,width=155,height=1440,bg="#15b4ea",)
iconsbarr.place(x=0,y=0)

def personel():
    personel=Tk()
    personel.geometry=("1200x720")
    personel.config(bg="white")
def log_out():
    account.destroy()
    subprocess.run(["python",current_path+"\\Luncher.py"])

#--------------subprocesses-------------------------------------




person_icon=create_icon(current_path+"\\icons\\person_icon1.png",(80,80))
person_button=Button(iconsbarr,text="PROFIL",image=person_icon,command=lambda account=account: person(account),compound="top" ,font=("Louis George Cafe",20),padx=0,pady=0,relief="flat",bg="#15b4ea",activebackground="#15b4ea",fg="white",activeforeground="white",highlightcolor="white")
person_button.place(x=18,y=0)


school_icon=create_icon(current_path+"\\icons\\school.png",(80,80))
school_icon_button=Button(iconsbarr,image=school_icon,padx=0,pady=0,command=lambda account=account :accueil(account),relief="flat",bg="#15b4ea",activebackground="#15b4ea",compound="top" ,font=("Louis George Cafe",20),text="ACCUEIL",fg="white",activeforeground="white")
school_icon_button.place(x=10,y=115)

paper=create_icon(current_path+"\\icons\\paper1.png",(70,70))
paper_button=Button(iconsbarr,bg="#15b4ea",padx=0,pady=0, relief="flat",command=lambda account=account :description(account),image=paper,activebackground="#15b4ea",compound="top" ,font=("Louis George Cafe",20),text="DESCRIPT°",fg="white",activeforeground="white")
paper_button.place(x=0,y=230)

book_icon=create_icon(current_path+"\\icons\\book.png",(70,70))
book_icon_button=Button(iconsbarr,bg="#15b4ea",padx=0,pady=0, relief="flat",command=lambda account=account :cours(account),image=book_icon,activebackground="#15b4ea",compound="top" ,font=("Louis George Cafe",18),text="COURS",fg="white",activeforeground="white")
book_icon_button.place(x=25,y=335)


agenda_icon=create_icon(current_path+"\\icons\\agenda.png",(60,60))
agenda_icon_button=Button(iconsbarr,bg="#15b4ea",padx=0,pady=0, relief="flat",command=db.get_schedule, image=agenda_icon,activebackground="#15b4ea",compound="top" ,font=("Louis George Cafe",15),text="EMPLOI DU \n DU TEMPS",fg="white",activeforeground="white")
agenda_icon_button.place(x=10,y=460)

support_icon=create_icon(current_path+"\\icons\\support.png",(70,70))


button = Button(iconsbarr, command=open_email_client, image=support_icon, relief="flat", bg="#15b4ea",activebackground="#15b4ea")
button.place(x=30,y=630)


#-------------------------------body----------------------------------------------------------------------------

#------------------------------personal data frame------------------------------------------------------------------
body_frame=Frame(account,bg="#B5EFFF",width=1000,height=530,relief="flat")
body_frame.place(x=180,y=70)
#-------------------- personal picture import ----------------------------------------------------------
photo=db.get_user_picture()
photo_label=Label(body_frame,image=photo)
photo_label.place(x=0,y=0)
#----------------------show other data ----------------------------------------------------------------------
minus=50
firstName_label=Label(body_frame,text="NOM:",bg="#B5EFFF",fg="#0073e6",font=("Arila",35))
firstName_label.place(x=220,y=100)
firstName_label2=Label(body_frame,text=db.get_user_first_name(),bg="#B5EFFF",fg="#A92B6F",font=("Arila",35))
firstName_label2.place(x=700,y=150-minus)

second_Name_label=Label(body_frame,text="PRENOM:",bg="#B5EFFF",fg="#0073e6",font=("Arila",35))
second_Name_label.place(x=220,y=200)
second_Name_label2=Label(body_frame,text=db.get_user_second_name(),bg="#B5EFFF",fg="#A92B6F",font=("Arila",35))
second_Name_label2.place(x=700,y=250-minus)

CNE_label=Label(body_frame,text="CNE:",bg="#B5EFFF",fg="#0073e6",font=("Arila",35))
CNE_label.place(x=220,y=300)
CNE_label2=Label(body_frame,text=db.get_user_CNE(),bg="#B5EFFF",fg="#A92B6F",font=("Arila",35))
CNE_label2.place(x=700,y=350-minus)

filier_label=Label(body_frame,text="FILIERE:",bg="#B5EFFF",fg="#0073e6",font=("Arila",35))
filier_label.place(x=220,y=400)
filier_label2=Label(body_frame,text=db.get_filiere(),bg="#B5EFFF",fg="#A92B6F",font=("Arila",35))
filier_label2.place(x=700,y=450-minus)

#--------------------------leave button-------------------------------------------
leavebutton=Button(account,text="Quitter",command=account.quit,bg="#258EF5",fg="white",activebackground="#258EF5", activeforeground="white",font=("Arial",16),padx=0,pady=0, relief="flat")      #
leavebutton.place(x=1100, y=660)
#--------------------------logout button--------------------------------------------
logout=Button(account,text="Partir",command=log_out,bg="#258EF5",fg="white",activebackground="#258EF5", activeforeground="white",font=("Arial",16),padx=0,pady=0, relief="flat")      #
logout.place(x=200, y=660)
account.mainloop()