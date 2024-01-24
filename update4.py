from tkinter import *
from PIL import Image, ImageTk
import os
import subprocess

current_path=os.getcwd()

window=Tk()
window.geometry("1200x720")
window.config(bg="white")

def create_icon(icon_path,tuple_size):
        image=Image.open(icon_path)
        image=image.resize(tuple_size,Image.ANTIALIAS)
        icon_image=ImageTk.PhotoImage(image)
        return icon_image

def Accueil():
        window.destroy()
        subprocess.run(["python",current_path+"\\Account.py"])

def Connect():
        window.destroy()
        subprocess.run(["python",current_path+"\\Luncher.py"])
#---------creation du l'icon
passwd_icon=create_icon(current_path+"\\icons\\success_icon.png",(200,200))
image_label=Label(window,compound="top", text="Les modificaions saisies sont\n enregistrées avec succès",image=passwd_icon,padx=0,pady=0,relief="flat",bg="white",activebackground="green",font=("Louis George Cafe",15,"bold"),fg="#0fb61d")
image_label.place(x=500,y=150)
image_label.config(highlightthickness=0)



#----------creation du boutton valider-----------#
button_valider=Button(window, command=Accueil,text="Accueil",fg="white",bg="#258EF5",width=20,activebackground="#15b4ea",activeforeground="blue",font=("Avial",13,"bold"))
button_valider.place(x=950,y=650)

#-----------creartion du button go back----------#
# go_back_icon=create_icon(current_path+"\\icons\\go_back.jpg",(45,15))
go_back_button=Button(window,command=Connect, text="Connecter",width=20,foreground="white" ,compound="left",bg="#258EF5",font=("Avial",13,"bold"),activebackground="#15b4ea",activeforeground="blue")
go_back_button.place(x=30,y=650)

window.mainloop()
