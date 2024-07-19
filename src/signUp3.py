from tkinter import *
from tkinter import filedialog
from PIL import Image,ImageTk
import subprocess
from dataBase import DataBase
import os
import re


#------------button qui retour en arrière-------------#
def go_back():
        window.destroy()
        subprocess.run(["python",current_path+r"/signUp2.py"])

#----pour button valider-----

def valider():
        v_regex_verification=regex_verification()
        v_generate_err=generate_err()
        if v_regex_verification and v_generate_err:
                print("apply insertion function......")
                db.insert_data_sign_up_phase3(passwd_field.get(),filière_field.get())
                print("hello importaion des donnnées......")
                print(db.getrow())
                print("enregistrement.....")
                db.valide()
                window.destroy()
                subprocess.run(["python",current_path+"\\SignUp4.py"])

#____________________________creation of same util function__________________________________________#

def focus_In_filière(event):
        if filière_field.get()=="filière diponible:ID1/ID2/GI1/GI2(respecter la syntaxe)":
                filière_field.delete(0,END)
                filière_field.config(fg="black")

def focus_out_filière(event):
        if filière_field.get()=="":
                filière_field.insert(0,"filière diponible:ID1/ID2/GI1/GI2(respecter la syntaxe)")
                filière_field.configure(foreground="gray",font=("Louis George Cafe Bold",15)),
#--------------------create icon---------------------#
def create_icon(icon_path,tuple_size):
        image=Image.open(icon_path)
        image=image.resize(tuple_size,Image.ANTIALIAS)
        icon_image=ImageTk.PhotoImage(image)
        return icon_image




#---------fonction pour lagestion d'erreur------------#
def generate_err():
        ok=True
        
        if passwd_field.get()=="":
                Label(window,text="****svp entrer votre mot de passe",fg="red",bg="white").place(x=x_username_entry+350,y=y_username_entry+40)
                ok=False
        else:
                Label(window,text="****svp entrer votre mot de passe",fg="white",bg="white").place(x=x_username_entry+350,y=y_username_entry+40)
                
        if filière_field.get() in  ["","filière diponible:ID1/ID2/GI1/GI2(respecter la syntaxe)"]:
                Label(window,text="****svp entrer votre filière",fg="red",bg="white").place(x=x_username_entry+350,y=y_username_entry+200-10)
                ok=False
        
        else:
                Label(window,text="****svp entrer votre filière",fg="white",bg="white").place(x=x_username_entry+350,y=y_username_entry+200-10)
        return ok
def regex_verification():
        ok=True
        fil=re.match(r"^ID1|ID2|GI1|GI2$",filière_field.get())
        if  not bool(fil) and filière_field.get().strip()  not  in ("filière diponible:ID1/ID2/GI1/GI2(respecter la syntaxe)",""):
                ok=False
                Label(window,text="****invalide syntaxe",fg="red",bg="white").place(x=x_username_entry+50,y=y_username_entry+200-10)
                print("filière valider")
        else:
                Label(window,text="****invalide syntaxe",fg="white",bg="white").place(x=x_username_entry+50,y=y_username_entry+200-10)
                
                 
        return ok

#________________________________varaibel a utiliser___________________________________#

current_path=os.getcwd()


x_username_entry=300+100+100
y_username_entry=150

x_username_Label=400+100+100
y_username_Label=100

x_username_icon=350+100+100
y_username_icon=90

x_username_etoile=600+100+100
y_username_etoile=100


icon_size=50


#_____________________________________________creation de la fenêtre_________________________________________________#
window=Tk()
window.geometry("1200x720")
window.config(bg="white")
window.title("INSCRIPTION")




#-----------------se connecter tout d'abord à la base de donnée------------------#
db= DataBase()




#_______________________________________________________create the password widget __________________________________________________________#


                                                #----passwd Label-----#
passwd_Label=Label(window,text="Entrer votre mot de passe :",font=("Helvetica",15,"bold"),bg="white")
passwd_Label.place(x=x_username_Label-10,y=y_username_Label)



#--------creation de l'etoile---------#

passwd_etoile=Label(window, text="*", font=("Arial",15),fg="red",bg="white")
passwd_etoile.place(x=x_username_etoile+60,y=y_username_etoile)


#---------creation du l'icon
passwd_icon=create_icon(current_path+"\\icons\\passwd_icon.jpg",(45,45))
image_label=Label(window, image=passwd_icon,padx=0,pady=0,relief="flat",bg="white")
image_label.place(x=x_username_icon-15,y=y_username_icon)
image_label.config(highlightthickness=0)

passwd_txt=StringVar()
passwd_field=Entry(window,show="*", textvariable=passwd_txt,bd=0,width=45,font=("Arial",15),highlightcolor="#05bcfa",highlightthickness=3,highlightbackground='white',bg="#e1f3ff")
passwd_field.place(x=x_username_entry,y=y_username_entry)



# ________________________________________creation du champ filière___________________________________________________#

    
    
#--------------creation du label-------------------#
filière_Label=Label(window, text="Entrer votre filière :",font=("Halvetica",15,"bold"),bg="white")
filière_Label.place(x=x_username_Label-10,y=y_username_Label+120+30)



#--------------creation du entry of filière------------#

filière_txt=StringVar()
filière_field=Entry(window,textvariable=filière_txt,font=("Avial",15), width=45,bd=0,highlightcolor="#05bcfa",highlightthickness=3,highlightbackground='white',bg="#e1f3ff",fg="black")
filière_field.place(x=x_username_entry,y=y_username_entry+120+30)
filière_field.insert(0,"filière diponible:ID1/ID2/GI1/GI2(respecter la syntaxe)")
filière_field.configure(fg="gray")
filière_field.bind("<FocusIn>",focus_In_filière)
filière_field.bind("<FocusOut>",focus_out_filière)

#------------creation de l'étoile--------------#
filière_etoile=Label(window, text="*",font=("Halvetica",15,"bold"),fg="red",bg="white")
filière_etoile.place(x=x_username_etoile-20,y=y_username_etoile+120+30)

#---------------craetion de l'icon ----------#
filière_icon=create_icon("icons/filière_icon.png",(icon_size-10,icon_size-10))
icon_label=Label(window,image=filière_icon,bd=0,bg="white")
icon_label.place(x=x_username_icon-20,y=y_username_icon+120+30)







#______________________________________________________creation d'un frame/background___________________________________________________#



frame_title =Frame(window,bg="white" )
frame_title.place(x=290,y=0,width=3500,height=60)

frame=Frame(window,bg="blue")
frame.place(x=0,y=0,width=290+100,height=7000)


school_image=create_icon(current_path+"\\icons\\school1.jpg",(300+100,740))
picture_label=Label(frame,image=school_image)
picture_label.pack()

#--------creation du titre--------#


espace_etudiant=Label(frame_title,text="ESPACE      ETUDIANT", font=("Arial",40),bg="white")
espace_etudiant.place(x=150,y=5)



#___________________________________________creation des button_________________________________________#


#----------creation du boutton valider-----------#
button_valider=Button(window, text="valider",fg="white",bg="#258EF5",width=20,activebackground="#15b4ea",activeforeground="blue",font=("Avial",10,"bold"),command=valider)
button_valider.place(x=1000,y=680)

#-----------creartion du button go back----------#
# go_back_icon=create_icon(current_path+"\\icons\\go_back.jpg",(45,15))
go_back_button=Button(window, text="Précedent",width=20,foreground="white" ,compound="left",bg="#258EF5",font=("Avial",10,"bold"),activebackground="#15b4ea",activeforeground="blue",command=go_back)
go_back_button.place(x=300+100,y=680)

window.mainloop()