from tkinter import *
import mysql.connector 
import subprocess
from PIL import Image,ImageTk
import os
from io import BytesIO
from dataBase import DataBase
from tools import *

db=DataBase()

def emploi():
    db.get_schedule()
    
current_path=os.getcwd()
account=Tk()
account.title("INFORMATION PERSONNELLES")
account.geometry("1200x720")
account.config(bg="white")
iconsbarr=Frame(account,width=155,height=1440,bg="#15b4ea")
iconsbarr.place(x=0,y=0)
def username():
    logfile=open("fichierlog.txt",'r')
    users=logfile.read().split("\n")
    print(users)
    username=users[0]
    return username

def personel():
    personel=Tk()
    personel.geometry=("1200x720")
    personel.config(bg="white")
def get_user_second_name():
    cursorr.execute("SELECT prenom from Etudiant where Cne='"+username()+"';")
    result=cursorr.fetchone()
    return result[0]
def log_out():
    account.destroy()
    subprocess.run(["python",current_path+"\\Luncher.py"])
def get_user_first_name():
    cursorr.execute("SELECT nom from Etudiant where Cne='"+username()+"';")
    result=cursorr.fetchone()
    return result[0]
def get_filiere():
    cursorr.execute("SELECT filière from Etudiant where Cne='"+username()+"';")
    result=cursorr.fetchone()
    return result[0]

def get_user_CNE():
    cursorr.execute("SELECT CNE from Etudiant where Cne='"+username()+"';")
    result=cursorr.fetchone()
    cne=result[0]
    return cne

def get_user_picture():
    print(username())

    cursorr.execute("SELECT image from Etudiant where Cne='"+username()+"';")
    result=cursorr.fetchone()
    photo_path=result[0]
    return BytesIO(photo_path)
def get_user_CNE():
    cursorr.execute("SELECT CNE from Etudiant where Cne='"+username()+"';")
    result=cursorr.fetchone()
    cne=result[0]
    return cne

def get_user_CIN():
    cursorr.execute("SELECT CIN from Etudiant where Cne='"+username()+"';")
    result=cursorr.fetchone()
    cin=result[0]
    return cin
def get_password():
    cursorr.execute("SELECT mot_de_passe from Etudiant where cne='"+username()+"';")
    result=cursorr.fetchone()
    mot_de_passe=result[0]
    return mot_de_passe
def get_téléphone():
    cursorr.execute("SELECT téléphone from Etudiant where cne='"+username()+"';")
    result=cursorr.fetchone()
    téléphone=result[0]
    return téléphone

def get_email():
    cursorr.execute("SELECT email from Etudiant where cne='"+username()+"';")
    result=cursorr.fetchone()
    email=result[0]
    return email

def get_date_de_naissance():
    cursorr.execute("SELECT date_de_naissance from Etudiant where cne='"+username()+"';")
    result=cursorr.fetchone()
    date_de_naissance=result[0]
    return date_de_naissance
def get_adress():
    cursorr.execute("SELECT id from Etudiant where cne='"+username()+"';")
    id=cursorr.fetchone()
    print(id)
    cursorr.execute("SELECT num, rue, ville from adress where id_Etud='"+str(id[0])+"';")
    result =cursorr.fetchone()
    adress=str(result[0])+"-"+result[1]+"-"+result[2]
    return adress
    

def imporicon(path,size_tuple):
    icon=Image.open(path)
    icon=icon.resize(size_tuple, Image.ANTIALIAS)
    icon=ImageTk.PhotoImage(icon)
    return icon


def description_filière():
    account.destroy()
    subprocess.run(["python",os.getcwd()+"\\Description_filière.py"])
#-------------------------subprocesses-------------------------------------
def person():
    account.destroy()
    subprocess.run(["python", current_path+"\\info_pers.py"])
def description():
    account.destroy()
    subprocess.run(["python", current_path+"\\Description_filière.py"])
def accueil():
    account.destroy()
    subprocess.run(["python", current_path+"\\Account.py"])
def cours():
    account.destroy()
    subprocess.run(["python", current_path+"\\Cours.py"])

#------------------------------------------partie SQL-------------------------------------------------------------------------------------------------------#

#------------------------connect to the database ETUDIANT------------------------------------    
database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root", 
    database="projet")
#------------------------create cursor---------------------------------------------
cursorr=database.cursor()


#-----------------------------import icons----------------------------------------

person_icon=imporicon(current_path+"\\icons\\person_icon1.png",(80,80))
person_button=Button(iconsbarr,command=person,text="PROFIL",image=person_icon,compound="top" ,font=("Louis George Cafe",20),padx=0,pady=0,relief="flat",bg="#15b4ea",activebackground="#15b4ea",fg="white",activeforeground="white",highlightcolor="white")
person_button.place(x=18,y=0)


school_icon=imporicon(current_path+"\\icons\\school.png",(80,80))
school_icon_button=Button(iconsbarr,image=school_icon,padx=0,pady=0,relief="flat",bg="#15b4ea",activebackground="#15b4ea",compound="top" ,font=("Louis George Cafe",20),text="ACCUEIL",fg="white",activeforeground="white",command=accueil)
school_icon_button.place(x=10,y=115)

paper=imporicon(current_path+"\\icons\\paper1.png",(70,70))
paper_button=Button(iconsbarr,command=description,bg="#15b4ea",padx=0,pady=0, relief="flat",image=paper,activebackground="#15b4ea",compound="top" ,font=("Louis George Cafe",20),text="DESCRIPT°",fg="white",activeforeground="white")
paper_button.place(x=0,y=230)

book_icon=imporicon(current_path+"\\icons\\book.png",(70,70))
book_icon_button=Button(iconsbarr,command=cours,bg="#15b4ea",padx=0,pady=0, relief="flat",image=book_icon,activebackground="#15b4ea",compound="top" ,font=("Louis George Cafe",18),text="COURS",fg="white",activeforeground="white")
book_icon_button.place(x=25,y=335)


agenda_icon=imporicon(current_path+"\\icons\\agenda.png",(60,60))
agenda_icon_button=Button(iconsbarr,bg="#15b4ea",padx=0,pady=0, relief="flat",command=emploi, image=agenda_icon,activebackground="#15b4ea",compound="top" ,font=("Louis George Cafe",15),text="EMPLOI DU \n DU TEMPS",fg="white",activeforeground="white")
agenda_icon_button.place(x=10,y=460)

support_icon=imporicon(current_path+"\\icons\\support.png",(70,70))
button=Button(iconsbarr,command=open_email_client,image=support_icon,padx=0,pady=0,relief="flat",bg="#15b4ea",activebackground="#15b4ea")
button.place(x=30,y=630)


#-------------------------------body----------------------------------------------------------------------------
# hello=Label(text="HELLO\t"+get_user_second_name(),font=("Arial",30),fg="#258EF5",bg="white")
# hello.place(x=700,y=30)
#------------------------------personal data frame------------------------------------------------------------------
body_frame=Frame(account,bg="#B5EFFF",width=1000,height=550,relief="flat")
body_frame.place(x=180,y=50)
#-------------------- personal picture import ----------------------------------------------------------
photo=imporicon(get_user_picture(),(200,200))
photo_label=Label(body_frame,image=photo)
photo_label.place(x=0,y=0)
#----------------------show other data ----------------------------------------------------------------------


firstName_label=Label(body_frame,text="NOM:",bg="#B5EFFF",fg="#0073e6",font=("Arila",20))
firstName_label.place(x=210,y=30)
firstName_label2=Label(body_frame,text=get_user_first_name(),bg="#B5EFFF",fg="#A92B6F",font=("Arila",20))
firstName_label2.place(x=600,y=30)

second_Name_label=Label(body_frame,text="PRENOM:",bg="#B5EFFF",fg="#0073e6",font=("Arila",20))
second_Name_label.place(x=210,y=80)
second_Name_label2=Label(body_frame,text=get_user_second_name(),bg="#B5EFFF",fg="#A92B6F",font=("Arila",20))
second_Name_label2.place(x=600,y=80)

CNE_label=Label(body_frame,text="CNE:",bg="#B5EFFF",fg="#0073e6",font=("Arila",20))
CNE_label.place(x=210,y=130)
CNE_label2=Label(body_frame,text=get_user_CNE(),bg="#B5EFFF",fg="#A92B6F",font=("Arila",20))
CNE_label2.place(x=600,y=130)


CIN_label=Label(body_frame,text="CIN:",bg="#B5EFFF",fg="#0073e6",font=("Arila",20))
CIN_label.place(x=210,y=180)
CIN_label2=Label(body_frame,text=get_user_CIN(),bg="#B5EFFF",fg="#A92B6F",font=("Arila",20))
CIN_label2.place(x=600,y=180)


filiere_label=Label(body_frame,text="FILIERE:",bg="#B5EFFF",fg="#0073e6",font=("Arila",20))
filiere_label.place(x=210,y=220)
filiere_label2=Label(body_frame,text=get_filiere(),bg="#B5EFFF",fg="#A92B6F",font=("Arila",20))
filiere_label2.place(x=600,y=220)



EMAIL_label=Label(body_frame,text="EMAIL:",bg="#B5EFFF",fg="#0073e6",font=("Arila",20))
EMAIL_label.place(x=210,y=270)
EMAIL_label2=Label(body_frame,text=get_email(),bg="#B5EFFF",fg="#A92B6F",font=("Arila",20))
EMAIL_label2.place(x=600,y=270)

add=0
TELEPHONE_label=Label(body_frame,text="TELEPHONE:",bg="#B5EFFF",fg="#0073e6",font=("Arila",20))
TELEPHONE_label.place(x=210,y=320+add)
TELEPHONE_label2=Label(body_frame,text=get_téléphone(),bg="#B5EFFF",fg="#A92B6F",font=("Arila",20))
TELEPHONE_label2.place(x=600,y=320+add)


DATE_DE_NAISSANCE_label=Label(body_frame,text="DATE DE NAISSANCE:",bg="#B5EFFF",fg="#0073e6",font=("Arila",20))
DATE_DE_NAISSANCE_label.place(x=210,y=370+add)
DATE_DE_NAISSANCE_label2=Label(body_frame,text=get_date_de_naissance(),bg="#B5EFFF",fg="#A92B6F",font=("Arila",20))
DATE_DE_NAISSANCE_label2.place(x=600,y=370+add)


ADRESSE_label=Label(body_frame,text="ADRESSE:",bg="#B5EFFF",fg="#0073e6",font=("Arila",20))
ADRESSE_label.place(x=210,y=420+add)
ADRESSE_labe2=Label(body_frame,text=get_adress(),bg="#B5EFFF",fg="#A92B6F",font=("Arila",20))
ADRESSE_labe2.place(x=600,y=420+add)

#---------------------------- masquer le mot de passe----------------------

def show_password(event):
    """Cette fonction est appelée lorsque l'utilisateur clique sur le Label du mot de passe."""
    password_label.config(show="")
    password_label.unbind("<Button-1>")
    password_label.bind("<Button-1>", hide_password)

def hide_password(event):
    """Cette fonction est appelée lorsque l'utilisateur clique à nouveau sur le Label du mot de passe."""
    password_label.config(show="*")
    password_label.unbind("<Button-1>")
    password_label.bind("<Button-1>", show_password)

# Création du champ de mot de passe sécurisé
password_label = Label(body_frame, text=get_password(), bg="#B5EFFF", fg="#A92B6F", font=("Arial", 20))
password_label.place(x=600, y=470)

# Ajout d'un événement de clic au Label pour afficher/masquer le mot de passe
password_label.bind("<Button-1>", show_password)


MOT_DE_PASSE_label=Label(body_frame,text="MOT DE PASSE:",bg="#B5EFFF",fg="#0073e6",font=("Arila",20))
MOT_DE_PASSE_label.place(x=210,y=470)

#------------------modification button: go to script singUP1 of Rida----------------------------

#-----------subprocess-----------
def go_there():
    account.destroy()
    subprocess.run(["python", current_path+"\\Update1.py"])

verify_button = Button(body_frame, text="Modifier!", bg="blue", fg="white", font=("Arial", 18), command=go_there,relief="flat")
verify_button.place(x=870, y=490)

verify_button = Button(body_frame, text="Délibération!", bg="blue",relief="flat", fg="white", font=("Arial", 18), command=db.get_deliberatin)
verify_button.place(x=10, y=490)

#--------------------------leave button-------------------------------------------
leavebutton=Button(account,text="Quitter",command=account.quit,bg="#258EF5",fg="white",activebackground="#258EF5", activeforeground="white",font=("Arial",16),padx=0,pady=0, relief="flat")      #
leavebutton.place(x=1100, y=660)
#--------------------------logout button--------------------------------------------
logout=Button(account,text="Partir",command=log_out,bg="#258EF5",fg="white",activebackground="#258EF5", activeforeground="white",font=("Arial",16),padx=0,pady=0, relief="flat")      #
logout.place(x=200, y=660)
account.mainloop()



