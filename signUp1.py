from tkinter import *
from tkinter import font
from PIL import Image,ImageTk
import subprocess
from dataBase import DataBase
import re 
import os
from tools import *
current_path=os.getcwd()


#--------------------------------------#
#                                      #
#                                      #
#                                      #
#                                      #
#                                      #
# ------------------------------------ #
#___________________________Subprocess___________________________#

def button_suivant():
        v_generate_err=generate_err()
        v_regex_verification=regex_verification()
        if v_regex_verification and  v_generate_err  :
                db.insert_data_sign_up_phase1(field_nom.get(),prenom_field.get(),email_field.get(),phone_field.get(),regler_date(date_de_naissan_field.get()))
                window.destroy()      
                subprocess.run(["python",current_path+"\\signUp2.py"])
                print("travaille")
                



        
def go_to_luncher():
        window.destroy()      
        subprocess.run(["python",current_path+"\\Luncher.py"])


















#________________________________varaibel a utiliser___________________________________#

x_nom_entry=300+100+100
y_nom_entry=150

x_nom_Label=400+100+100
y_nom_Label=100

x_non_icon=350+100+100
y_non_icon=90

x_nom_etoile=600+100+100
y_nom_etoile=100


icon_size=50

#__________________________________________some function ___________________________________________#


#----------------------------placehoder----------------------------#


############################"event argument is to detect if I ckliked on the field or not#############################""""""
def focus_In(event):
        if date_de_naissan_field.get()=="YYYY-MM-DD":
                date_de_naissan_field.delete(0,END)
                date_de_naissan_field.configure(foreground="black")

def focus_out(event):
        if date_de_naissan_field.get()=="":
                date_de_naissan_field.insert(0,"YYYY-MM-DD")
                date_de_naissan_field.configure(foreground="gray",font=("Louis George Cafe Bold",15))


#--------place holder de l'email-----------------------------#
def focus_In_email(event):
        if email_field.get()=="school@service.com":
                email_field.delete(0,END)
                email_field.config(fg="black")

def focus_out_email(event):
        if email_field.get()=="":
                email_field.insert(0,"school@service.com")
                email_field.configure(foreground="gray",font=("Louis George Cafe Bold",15))


#--------place holder de l'email----------------------------#

def focus_In_phone(event):
        if phone_field.get()=="06******** | 07********":
                phone_field.delete(0,END)
                phone_field.config(fg="black")

def focus_out_phone(event):
        if phone_field.get()=="":
                phone_field.insert(0,"06******** | 07********")
                phone_field.configure(foreground="gray",font=("Louis George Cafe Bold",15))




#-----------------------create icon------------------------------#






#---------creation of a function that generate us a  error if it was the case------------#
def generate_err():
        ok=True
        if field_nom.get()=="":
                Label(window,text="****svp entrer le nom",fg="red",bg="white").place(x=x_nom_entry+350,y=y_nom_entry+40)
                ok=False
        else:
                Label(window,text="****svp entrer le nom",fg="white",bg="white").place(x=x_nom_entry+350,y=y_nom_entry+40)

        if prenom_field.get()=="":
                Label(window,text="****svp entrer le prenom",fg="red",bg="white").place(x=x_nom_entry+350,y=y_nom_entry+40+100)
                ok=False
        else:
                Label(window,text="****svp entrer le prenom",fg="white",bg="white").place(x=x_nom_entry+350,y=y_nom_entry+40+100)

        if email_field.get() in ["","school@service.com"]:
                Label(window,text="****svp entrer l' email",fg="red",bg="white").place(x=x_nom_entry+350,y=y_nom_entry+40+100*2)
                ok=False
        else: 
                Label(window,text="****svp entrer l' email",fg="white",bg="white").place(x=x_nom_entry+350,y=y_nom_entry+40+100*2)

        if phone_field.get() in  ["","06******** | 07********"]:
                Label(window,text="****svp entrer votre numero",fg="red",bg="white").place(x=x_nom_entry+350,y=y_nom_entry+30+100*3+40)
                ok=False
        else:
                Label(window,text="****svp entrer votre numero",fg="white",bg="white").place(x=x_nom_entry+350,y=y_nom_entry+30+100*3+40)

        if date_de_naissan_field.get()=="" or date_de_naissan_field.get()=="YYYY-MM-DD":
                Label(window,text="****svp entrer la date de naissance",fg="red",bg="white").place(x=x_nom_entry+250,y=y_nom_entry+40+100*4+85)
                ok=False
        else:
                Label(window,text="****svp entrer la date de naissance",fg="white",bg="white").place(x=x_nom_entry+250,y=y_nom_entry+40+100*4+85)

        return ok

#------verifier le syntaxx par les expresions regulieres-----------#

def regex_verification():
        ok=True
        email=re.match(r"^\w+\.?\w*@\w+\.\w{2,}$",email_field.get())
        if  not bool(email) and email_field.get().strip()  not  in ('school@service.com',""):
                ok=False
                Label(window,text="****invalide syntaxe",fg="red",bg="white").place(x=x_nom_entry+30,y=y_nom_entry+40+100*2)
                print("email valider")
        else:
                Label(window,text="****invalide syntaxe",fg="white",bg="white").place(x=x_nom_entry+30,y=y_nom_entry+40+100*2)
                

        phone=re.match(r"^0(6|7)\d{8}$",phone_field.get())
        if not bool(phone) and phone_field.get().strip() not in ("06******** | 07********",""):
                ok=False
                Label(window,text="****invalide syntaxe",fg="red",bg="white").place(x=x_nom_entry+30,y=y_nom_entry+30+100*3+40)
                print("phone valider")
        else:
                Label(window,text="****invalide syntaxe",fg="white",bg="white").place(x=x_nom_entry+30,y=y_nom_entry+30+100*3+40)

        
        date=re.match(r"^[1-2]\d{3}-(0?[1-9]|1[0-2])-((0?[1-9])|[1-2]?\d|3[0-1])$",date_de_naissan_field.get())
        if not bool(date) and date_de_naissan_field.get().strip() not in ("YYYY-MM-DD",""):
                ok=False
                Label(window,text="****invalide syntxe",fg="red",bg="white",bd=1).place(x=x_nom_entry+90,y=y_nom_entry+40+100*4+85)
        else:
                Label(window,text="****invalide syntxe",fg="white",bg="white",bd=1).place(x=x_nom_entry+90,y=y_nom_entry+40+100*4+85)

        return ok




#_____________________________________________creation de la fenêtre_________________________________________________#
window=Tk()
window.geometry("1200x720")
window.config(bg="white")
window.title("INSCRIPTION")

#--------------------creation de la conenection avec la base de donee------------------
db=DataBase()













#______________________________________________create the non widget______________________________________#



#-----enter the Entry name field------#
name_txt=StringVar()

field_nom=Entry(window, textvariable=name_txt, width=45,bd=0,font=("Arial",15),highlightcolor="#05bcfa",highlightthickness=3,highlightbackground='white',bg="#e1f3ff")
field_nom.place(x=x_nom_entry,y=y_nom_entry)



#-----enter the name Label------#
nom=Label(window,text="Entrer votre nom  : ",fg="black",font=("Helvetica",15,"bold"),bg="white" ,highlightthickness=0)
nom.place(x=x_nom_Label,y=y_nom_Label)

necessary_point=Label (window, text="*", fg="red",font=("Arial",15),bg="white" ,highlightthickness=0)
necessary_point.place(x=x_nom_etoile,y=y_nom_etoile)


#--------------association of icon picture to the Entry-------------------#

personel_icon=create_icon(current_path+"\\icons\\person_icon.png",(45,45))
image_label=Label(window, image=personel_icon,padx=0,pady=0,relief="flat",bg="white")
image_label.place(x=x_non_icon,y=y_non_icon)
image_label.config(highlightthickness=0)



#_______________________________________________________create a prenom widget __________________________________________________________#


                                                #----prenom Label-----#
prenom_Label=Label(window,text="Entrer votre Prenom :",font=("Helvetica",15,"bold"),bg="white")
prenom_Label.place(x=x_nom_Label,y=y_nom_Label+100)



#--------creation de l'etoile---------#

prenom_etoile=Label(window, text="*", font=("Arial",15),fg="red",bg="white")
prenom_etoile.place(x=x_nom_etoile+10,y=y_nom_etoile+100)


prenom_txt=StringVar()
prenom_field=Entry(window, textvariable=prenom_txt,bd=0,width=45,font=("Arial",15),highlightcolor="#05bcfa",highlightthickness=3,highlightbackground='white',bg="#e1f3ff")
prenom_field.place(x=x_nom_entry,y=y_nom_entry+100)



#--------------creation de l'icon de prenom-------------------#

prenom_icon=create_icon(current_path+"\\icons\\person_icon.png",(45,45))

image_label=Label(window, image=prenom_icon,padx=0,pady=0,relief="flat",bg="white")
image_label.place(x=x_non_icon,y=y_non_icon+100)
image_label.config(highlightthickness=0)








# ________________________________________creation du champ email___________________________________________________#

    
    
#--------------creation du label-------------------#
email_Label=Label(window, text="Entrer votre email :",font=("Halvetica",15,"bold"),bg="white")
email_Label.place(x=x_nom_Label,y=y_nom_Label+200)



#--------------creation du entry of email------------#

email_txt=StringVar()
email_field=Entry(window,textvariable=email_txt,font=("Louis George Cafe Bold",15), width=45,bd=0,highlightcolor="#05bcfa",highlightthickness=3,highlightbackground='white',bg="#e1f3ff",fg="black")
email_field.place(x=x_nom_entry,y=y_nom_entry+200)
email_field.insert(0,"school@service.com")
email_field.configure(fg="gray")
email_field.bind("<FocusIn>",focus_In_email)
email_field.bind("<FocusOut>",focus_out_email)


#------------creation de l'étoile--------------#
email_etoile=Label(window, text="*",font=("Halvetica",15,"bold"),fg="red",bg="white")
email_etoile.place(x=x_nom_etoile-15,y=y_nom_etoile+200)

#---------------craetion de l'icon ----------#
email_icon=create_icon(current_path+"\\icons\\email_icon.png",(icon_size-10,icon_size-10))
icon_label=Label(window,image=email_icon,bd=0,bg="white")
icon_label.place(x=x_non_icon,y=y_non_icon+206)








#_______________________________creation du numero de telephone______________________________________#


#--------------creation du label-------------------#
phone_Label=Label(window, text="Entrer votre phone  :",font=("Halvetica",15,"bold"),bg="white")
phone_Label.place(x=x_nom_Label,y=y_nom_Label+330)


#--------------creation du entry of phone------------#
phone_txt=StringVar()
phone_field=Entry(window,textvariable=phone_txt,font=("Louis George Cafe Bold",15), width=45,bd=0,highlightcolor="#05bcfa",highlightthickness=3,highlightbackground='white',bg="#e1f3ff")
phone_field.place(x=x_nom_entry,y=y_nom_entry+330)
phone_field.insert(0,"06******** | 07********")
phone_field.configure(fg="gray")
phone_field.bind("<FocusIn>",focus_In_phone)
phone_field.bind("<FocusOut>",focus_out_phone)


#------------creation de l'étoile--------------#
phone_etoile=Label(window, text="*",font=("Halvetica",15,"bold"),fg="red",bg="white")
phone_etoile.place(x=x_nom_etoile,y=y_nom_etoile+330)

#---------------craetion de l'icon ----------#
phone_icon=create_icon(current_path+"\\icons\\phone_icon.png",(icon_size-10,icon_size-10))
icon_label=Label(window,image=phone_icon,bd=0,bg="white",fg="white")
icon_label.place(x=x_non_icon,y=y_non_icon+336)






#______________________________________________creation de date de naissance_________________________________________________________________#


#--------------creation du label-------------------#
date_de_naissan_Label=Label(window, text="Entrer la date de naissance  :",font=("Louis George Cafe Bold",15,"bold"),bg="white")
date_de_naissan_Label.place(x=x_nom_Label,y=y_nom_Label+430+50)



#--------------creation du entry of date_de_naissan------------#
date_de_naissan_txt=StringVar()
date_de_naissan_field=Entry(window,textvariable=date_de_naissan_txt,font=("Louis George Cafe Bold",15), width=45,bd=0,highlightcolor="#05bcfa",highlightthickness=3,highlightbackground='white',bg="#e1f3ff",fg="black")
date_de_naissan_field.place(x=x_nom_entry,y=y_nom_entry+430+50)

date_de_naissan_field.insert(0,"YYYY-MM-DD")
date_de_naissan_field.configure(fg="gray")
date_de_naissan_field.bind("<FocusIn>",focus_In)
date_de_naissan_field.bind("<FocusOut>",focus_out)

#-------------------creation de l'étoile-----------------#
date_de_naissan_etoile=Label(window, text="*",font=("Halvetica",15,"bold"),fg="red",bg="white")
date_de_naissan_etoile.place(x=x_nom_etoile+100,y=y_nom_etoile+430+50)

#---------------craetion de l'icon ----------#
date_de_naissan_icon=create_icon(current_path+"\\icons\\date_de_naissance_icon.png",(icon_size-15,icon_size-15))
icon_label=Label(window,image=date_de_naissan_icon,bd=0,bg="white")
icon_label.place(x=x_non_icon,y=y_non_icon+430+50)




#___________________________________________creation des button_________________________________________#


#----------creation du boutton suivant-----------#
button_suivant=Button(window, text="suivant",fg="white",bg="#258EF5",width=20,activebackground="#258EF5",activeforeground="blue",font=("Louis George Cafe Bold",10,"bold"),command=button_suivant)
button_suivant.place(x=1000,y=680)

#-----------creartion du button go back----------#
go_back_icon=create_icon(current_path+"\\icons\\go_back.jpg",(45,15))
go_back_button=Button(window, text="Précedent",width=20,foreground="white" ,compound="left",bg="#258EF5",font=("Louis George Cafe Bold",10,"bold"),activebackground="#15b4ea",activeforeground="blue",command=go_to_luncher)
go_back_button.place(x=300+100,y=680)
















#______________________________________________________creation d'un frame___________________________________________________#




frame=Frame(window,bg="blue")
frame.place(x=0,y=0,width=290+100,height=7000)


school_image=create_icon(current_path+"\\icons\\school1.jpg",(300+100,740))
picture_label=Label(frame,image=school_image)
picture_label.pack()

#--------creation du titre--------#


espace_etudiant=Label(window,text="ESPACE      ETUDIANT", font=("Arial",52),bg="white")
espace_etudiant.place(x=435,y=0)
                                                                                                                                                                                        








window.mainloop()