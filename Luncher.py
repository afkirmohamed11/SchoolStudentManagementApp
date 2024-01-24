from tkinter import *
from PIL import ImageTk, Image
import subprocess
import mysql.connector 
import os
import webbrowser
from tools import *
from dataBase import DataBase

db=DataBase()
#---------------------------------------definition des commands des buttons------------------------
current_path=os.getcwd()
print(current_path)

def signup_button():
    window.destroy()
    subprocess.run(["python", current_path+"\\signUp1.py"])
def window_button():
    subprocess.run(["python", current_path+"\\window.py"])
    
def forgoten_pwd():
    window.destroy()
    subprocess.run(["python",current_path+"\\forgot_password1.py"])
    
def pass_account():
#----------------get info from name and password fields-------------------------------------
    cne_text=nomfield.get()
    password_text=passwordfield.get()
    
    result=db.get_passwd(cne_text)
#----------------------------------------------------------------------------------
    authentification=result[0][0] if result else None #since result of fetch is a tuple we have to selct first element to get the result
                                                   #i added that if in case the result of fetch was None to not give an error
    
    if authentification==password_text:
        print("script runned")
        fichier_log=open("fichierLog.txt",'w+')
        fichier_log.write(nomfield.get()+"\n")
        fichier_log.close()
        window.destroy()
        subprocess.run(["python",current_path+"\\Account.py"])
    else:
        erreur=Label(window,text="nom d'utilisateur ou mot de passe incorrect",font=("Arial",15),bg="white",fg="red")
        erreur.place(x=580,y=400)

    












# Create an instance of tkinter window----------------------------
window = Tk()
window.title("Lanceur")

# Define the geometry of the window (full screen)-------------------------------

window.geometry("1200x720")
#-------------define sceen color----------------------------------------------
window.config(bg="white")
#-------------import picture---------------------------------------------------
imagee=(Image.open(current_path+"\\icons\\school1.jpg"))
imagee=imagee.resize((430,800))
sidepicture = ImageTk.PhotoImage(imagee)
#----------------Create a Label Widget to display the  Image-----------------
label = Label(window, image = sidepicture,padx=0,pady=0, relief="flat")
label.grid(row=0,column=0)

#--------------------------------------------------------------------------------------------------------------#
# creating a leave button and changing its style                                                               #
# activebackground is color when to kpress on button ############ activeforegroud is color of text when press  #
# bg is color of background ##################################### fg is color of font                          #
#--------------------------------------------------------------------------------------------------------------#
lock_icon=create_icon(current_path+"\\icons\\lock_icon.png",(40, 40))
person_icon=create_icon(current_path+"\\icons\\person_icon.png",(50, 50))




#----------------------------welcome label--------------------------------------------------------------------
welcome=Label(window,text="ESPACE     ETUDIANT ",font=("LEMONMILK-Medium",54),bg="white")
welcome.place(x=435,y=0)

#---------------------------nom label and entry field-------------------------------------------------------
nom=Label(window,text="Nom d'utilisateur:",font=("Louis George Cafe Bold",35),bg="white",image=person_icon,compound="left")
nom.place(x=575,y=150)

nomfield=Entry(window,width=20,font=("Arial",30),relief="flat",bg="#e1f3ff",highlightcolor="#05bcfa",highlightthickness=3,highlightbackground='white')
nomfield.place(x=580,y=220)
#--------------------------password label and entry field-----------------------------------------------------
password=Label(window,text="Mot de passe:",font=("Louis George Cafe Bold",35),bg="white",image=lock_icon,compound="left")
password.place(x=580,y=280)

passwordfield=Entry(window,width=20,show="*", font=("Arial",30),relief="flat",bg="#e1f3ff",highlightcolor="#05bcfa",highlightthickness=3,highlightbackground='white')
passwordfield.place(x=580,y=340)
#-------------------confirm button---------------------------------------------------------------------------

confirm_button=Button(window,text="Confirmer",command=pass_account, bg="#258EF5",fg="white",activebackground="#258EF5", activeforeground="white",font=("Arial",20),padx=0,pady=0, relief="flat",width=27)
confirm_button.place(x=580,y=450)

#-------------------------forgot password --------------------------------------------------------------------


forgot_password=Button(window,text=("Mot de passe oublié?"),command=forgoten_pwd,bg="white",fg="#258EF5",activebackground="white", activeforeground="#258EF5",font=("Arial",14),padx=0,pady=0, relief="flat")
forgot_password.place(x=580,y=530)


#--------------------------sing up buttom-----------------------------------------------------------------------

signUp=Button(window,text=("S'inscrire"),command=signup_button,bg="white",fg="#258EF5",activebackground="white", activeforeground="#258EF5",font=("Arial",14),padx=0,pady=0, relief="flat")
signUp.place(x=940,y=530)

#--------------------------leave button--------------------------------------------------------------------------
leavebutton=Button(window,text="Quitter",command=window.quit,bg="#258EF5",fg="white",activebackground="#258EF5", activeforeground="white",font=("Arial",16),padx=0,pady=0, relief="flat")      #
leavebutton.place(x=1100, y=660)


#------------------------contact support --------------------------------------------------------------------------



framei = Frame(window, width=200, height=200,relief="ridge")
framei.place(x=460,y=640)
icon=PhotoImage(file=r""+current_path+"\\icons\\support.png")
button=Button(framei,image=icon,padx=0,pady=0,relief="flat",bg="white",command=open_email_client)
button.pack()




window.mainloop()