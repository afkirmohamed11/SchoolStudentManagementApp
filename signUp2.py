from tkinter import *
from tkinter import font,filedialog
from PIL import Image,ImageTk
import subprocess
from dataBase import DataBase
import  re
import os
#____________________________creation of same util function__________________________________________#


#--------------------create icon---------------------#
def create_icon(icon_path,tuple_size):
        image=Image.open(icon_path)
        image=image.resize(tuple_size,Image.ANTIALIAS)
        icon_image=ImageTk.PhotoImage(image)
        return icon_image


#------------button qui retour en arrière-------------#
def go_back():
        window.destroy()
        subprocess.run(["python",current_path+r"/signUp1.py"])
def suivant():
       v_generate_err=generate_err()
       v_regex_verification=regex_verification()
       if v_generate_err and v_regex_verification:
              cne=CNE_field.get()
              db.insert_data_sign_up_phase2(field_adress.get(),cne,CIN_field.get(),photo_field.get())
              window.destroy()
              with open(r"fichierLog.txt","w+") as file:
                      file.write(cne+"\n")
                      
              subprocess.run(["python",current_path+r"/signUp3.py"])


#-----------la fonction qui permet de parcourir les lien pour recuperer l'image désirer---------#
last_msg=[]
def parcourir_lien():
        print("debut")
        try:
               des=last_msg[len(last_msg)-1]
        except:
               pass
        err_mes=Label(window,text="",fg="red",font=("Arial",10,"bold"),bg="white")
        last_msg.append(err_mes)
        photo_path=filedialog.askopenfile() #avoir le path apres le parcour
        

       
        while ".png" not in  str(photo_path) and ".jpg" not in str(photo_path):
            err_mes.place(x=x_adress_entry+70,y=y_adress_entry+440)
            err_mes.config(text="**svp la photo doit être d'extesion 'png' ou 'jpg'")
            photo_path=filedialog.askopenfile()
            photo_field.delete(0,END)
            photo_field.insert(0,photo_path)

        print("sort")
        
        err_mes.destroy()
        try:
            des.destroy()
        except:
               pass
        photo_field.delete(0,END)
        photo_field.insert(0,photo_path)





#---------creation of a function that generate us a  error if it was the case------------#

def generate_err():
       ok=True
       if field_adress.get() in["", "N°-rue-ville"] :
                Label(window,text="****svp entrer votre adresse",fg="red",bg="white").place(x=x_adress_entry+350,y=y_adress_entry+40)
                ok=False
       else:
                Label(window,text="****svp entrer votre adresse",fg="white",bg="white").place(x=x_adress_entry+350,y=y_adress_entry+40)

       if CNE_field.get()=="":
                Label(window,text="****svp entrer votre CNE",fg="red",bg="white").place(x=x_adress_entry+350,y=y_adress_entry+40+100+20)
                ok=False
       else:
                Label(window,text="****svp entrer votre CNE",fg="white",bg="white").place(x=x_adress_entry+350,y=y_adress_entry+40+100+20)

       if CIN_field.get()=="":
                Label(window,text="****svp entrer votre CIN",fg="red",bg="white").place(x=x_adress_entry+350,y=y_adress_entry+40+100*2+50)
                ok=False
       else: 
                Label(window,text="****svp entrer votre photo",fg="white",bg="white").place(x=x_adress_entry+350,y=y_adress_entry+40+100*2+50)

       if photo_field.get()=="":
                Label(window,text="****svp entrer votre photo",fg="red",bg="white").place(x=x_adress_entry+350,y=y_adress_entry+30+100*3+40)
                ok=False
       else:
                Label(window,text="****svp entrer votre numero",fg="white",bg="white").place(x=x_adress_entry+350,y=y_adress_entry+30+100*3+40)
       return ok
       

def regex_verification():
        ok=True
        adress=re.match(r"^\d{1,}-\w+\s?\w+\s?\w+-\w+\s?\w+$",field_adress.get())
        if  not bool(adress) and field_adress.get().strip()  not  in ("N°-rue-ville",""):
                ok=False
                Label(window,text="****invalide syntaxe",fg="red",bg="white").place(x=x_adress_entry+50,y=y_adress_entry+40)
                print("adress valider")
        else:
                Label(window,text="****invalide syntaxe",fg="white",bg="white").place(x=x_adress_entry+50,y=y_adress_entry+40)
                

        CNE=re.match(r"^[A-Z]\d{9}|[A-Z]{2}\d{7}\d?\d?$",CNE_field.get())
        if not bool(CNE) and CNE_field.get().strip() not in ("L**********",""):
                ok=False
                Label(window,text="****invalide syntaxe",fg="red",bg="white").place(x=x_adress_entry+50,y=y_adress_entry+40+100+20)
                print("CNE valider")
        else:
                Label(window,text="****invalide syntaxe",fg="white",bg="white").place(x=x_adress_entry+50,y=y_adress_entry+40+100+20)

        
        CIN=re.match(r"^[A-Z]\d{6}|[A-Z]{2}\d{5}\d?$",CIN_field.get())
        if not bool(CIN) and CIN_field.get().strip() not in (""):
                ok=False
                Label(window,text="****invalide syntxe",fg="red",bg="white",bd=1).place(x=x_adress_entry+50,y=y_adress_entry+40+100*2+50)
        else:
                Label(window,text="****invalide syntxe",fg="white",bg="white",bd=1).place(x=x_adress_entry+50,y=y_adress_entry+40+100*2+50)

        return ok


def focus_In_adress(event):
        if field_adress.get()=="N°-rue-ville":
                field_adress.delete(0,END)
                field_adress.config(fg="black")

def focus_out_adress(event):
        if field_adress.get()=="":
                field_adress.insert(0,"N°-rue-ville")
                field_adress.configure(foreground="gray",font=("Louis George Cafe Bold",15))
#________________________________varaibel a utiliser___________________________________#

current_path=current_path=os.getcwd()



x_adress_entry=300+100+100
y_adress_entry=150+10

x_adress_Label=400+100+100
y_adress_Label=100+10

x_adress_icon=350+100+100
y_adress_icon=90+10

x_adress_etoile=600+100+100
y_adress_etoile=100+10


icon_size=50

#_____________________________________________creation de la fenêtre_________________________________________________#
window=Tk()
window.geometry("1200x720")
window.config(bg="white")
window.title("INSCRIPTION")

#-----------------se connecter tout d'abord à la base de donnée------------------#
db= DataBase()


#______________________________________________create the adress widget______________________________________#


                

#--------------association of icon picture to the Entry-------------------#

adress_icon=create_icon("icons/adress_icon.jpg",(45,45))

image_label=Label(window, image=adress_icon,padx=0,pady=0,relief="flat")
image_label.place(x=x_adress_icon-15,y=y_adress_icon)
image_label.config(highlightthickness=0,bd=0)



#-----enter the Entry name field------#
name_txt=StringVar()

field_adress=Entry(window, textvariable=name_txt, width=45,bd=0,font=("Arial",15),highlightcolor="#05bcfa",highlightthickness=3,highlightbackground='white',bg="#e1f3ff")
field_adress.place(x=x_adress_entry,y=y_adress_entry)
field_adress.insert(0,"N°-rue-ville")
field_adress.config(fg="gray")
field_adress.bind("<FocusIn>",focus_In_adress)
field_adress.bind("<FocusOut>",focus_out_adress)


#-----enter the name Label------#
adress=Label(window,text="Entrer votre adress  : ",fg="black",font=("Helvetica",15,"bold"),bg="white" ,highlightthickness=0)
adress.place(x=x_adress_Label-10,y=y_adress_Label)

necessary_point=Label (window, text="*", fg="red",font=("Arial",15),bg="white" ,highlightthickness=0)
necessary_point.place(x=x_adress_etoile,y=y_adress_etoile)



#_______________________________________________________create the CNE widget __________________________________________________________#


                                                #----CNE Label-----#
CNE_Label=Label(window,text="Entrer votre CNE :",font=("Helvetica",15,"bold"),bg="white")
CNE_Label.place(x=x_adress_Label-10,y=y_adress_Label+120)



#--------creation de l'etoile---------#

CNE_etoile=Label(window, text="*", font=("Arial",15),fg="red",bg="white")
CNE_etoile.place(x=x_adress_etoile-30,y=y_adress_etoile+120)


#---------creation du l'icon
CNE_icon=create_icon("icons/CNE_icon.jpg",(45,45))

image_label=Label(window, image=CNE_icon,padx=0,pady=0,relief="flat",bg="white")
image_label.place(x=x_adress_icon-10,y=y_adress_icon+120)
image_label.config(highlightthickness=0)

CNE_txt=StringVar()
CNE_field=Entry(window, textvariable=CNE_txt,bd=0,width=45,font=("Arial",15),highlightcolor="#05bcfa",highlightthickness=3,highlightbackground='white',bg="#e1f3ff")
CNE_field.place(x=x_adress_entry,y=y_adress_entry+120)







# ________________________________________creation du champ CIN___________________________________________________#

    
    
#--------------creation du label-------------------#
CIN_Label=Label(window, text="Entrer votre CIN :",font=("Halvetica",15,"bold"),bg="white")
CIN_Label.place(x=x_adress_Label,y=y_adress_Label+250)



#--------------creation du entry of CIN------------#

CIN_txt=StringVar()
CIN_field=Entry(window,textvariable=CIN_txt,font=("Avial",15), width=45,bd=0,highlightcolor="#05bcfa",highlightthickness=3,highlightbackground='white',bg="#e1f3ff")
CIN_field.place(x=x_adress_entry,y=y_adress_entry+250)


#------------creation de l'étoile--------------#

CIN_etoile=Label(window, text="*",font=("Halvetica",15,"bold"),fg="red",bg="white")
CIN_etoile.place(x=x_adress_etoile-25,y=y_adress_etoile+250)

#---------------craetion de l'icon ----------#
CIN_icon=create_icon("icons/CIN_icon.jpg",(icon_size-15,icon_size-10))
icon_label=Label(window,image=CIN_icon,bd=0,bg="white")
icon_label.place(x=x_adress_icon,y=y_adress_icon+256)













# ________________________________________creation du champ du photo___________________________________________________#

    
    
#--------------creation du label-------------------#
photo_Label=Label(window, text="Entrer votre photo :",font=("Halvetica",15,"bold"),bg="white")
photo_Label.place(x=x_adress_Label,y=y_adress_Label+280+120)


#------------creation de l'étoile--------------#
photo_etoile=Label(window, text="*",font=("Halvetica",15,"bold"),fg="red",bg="white")
photo_etoile.place(x=x_adress_etoile-10,y=y_adress_etoile+280+120)

#--------------creation du entry of photo------------------#
photo_txt=StringVar()
photo_field=Entry(window,textvariable=photo_txt,font=("Avial",15), width=35,bd=2,highlightcolor="#05bcfa",highlightthickness=3,highlightbackground='white',bg="#e1f3ff")
photo_field.place(x=x_adress_entry,y=y_adress_entry+280+120)


#-------------------craetion de l'icon --------------------#
photo_icon=create_icon("icons/photo_icon.png",(icon_size-15,icon_size-15))
icon_label=Label(window,image=photo_icon,bd=0,bg="white",fg="white")
icon_label.place(x=x_adress_icon,y=y_adress_icon+286+120)

# ----------------creation du boutton parcourir-------------#
parcourir=Button(window,text="Parcourir",width=15,bg="green",fg="white",highlightbackground="violet",highlightcolor="blue",font=("Avial",10,"bold"),command=parcourir_lien)
parcourir.place(x=x_adress_icon+350,y=y_adress_entry+405)











#______________________________________________________creation d'un frame/background___________________________________________________#



frame_title =Frame(window,bg="white" )
frame_title.place(x=290,y=0,width=3500,height=70)

frame=Frame(window,bg="blue")
frame.place(x=0,y=0,width=290+100,height=7000)


school_image=create_icon("icons/school1.jpg",(300+100,740))
picture_label=Label(frame,image=school_image)
picture_label.pack()

#--------creation du titre--------#


espace_etudiant=Label(frame_title,text="ESPACE      ETUDIANT", font=("Arial",50),bg="white")
espace_etudiant.place(x=150,y=5)





#___________________________________________creation des button_________________________________________#


#----------creation du boutton suivant-----------#
button_suivant=Button(window, text="suivant",fg="white",bg="#258EF5",width=20,activebackground="#15b4ea",activeforeground="blue",font=("Avial",10,"bold"),command=suivant)
button_suivant.place(x=1000,y=680)

#-----------creartion du button go back----------#
# go_back_icon=create_icon("icons/go_back.jpg",(45,15))
go_back_button=Button(window, text="Précedent",width=20,foreground="white" ,compound="left",bg="#258EF5",font=("Avial",10,"bold"),activebackground="#15b4ea",activeforeground="blue",command=go_back)
go_back_button.place(x=300+100,y=680)


window.mainloop()