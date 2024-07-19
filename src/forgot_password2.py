import tkinter as tk
import mysql.connector
from PIL import Image,ImageTk
import os
from dataBase import DataBase
from tools import *
current_path=os.getcwd()
# from forgot_password1 import get_cne_value
# cne_value = get_cne_value # cette valeur de cne saisie par user sera utilisée lorsqu'on veut modifier le mot de passe dasn la base de données


# -----------------------------Function to open the password reset GUI--------------------------------------------
click_count=0

cne=DataBase.get_cne_user_connecter()
def update_password():
    global click_count
    global cne
    mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="root", 
        database="projet"
    )
    mycursor = mydb.cursor()
    # Retrieve password input from entry fields
    new_password = entry1.get()
    confirm_password = entry2.get()
    click_count += 1
    new_password = entry1.get()
    confirm_password = entry2.get()

    if new_password == confirm_password:
        # Update password in database
        sql = "UPDATE etudiant SET mot_de_passe = %s WHERE cne = %s"
        val = (new_password, cne)  # replace passwd with the actual passwd of the user
        mycursor.execute(sql, val)
        mydb.commit()
        error_label = tk.Label(reset_root, text="Error")
        error_label.config(text="Mise à jour du mot de passe réussie!",font=("Louis George Cafe Bold", 15, "bold"), fg="green",bg="white",relief="flat")
        error_label.place(x=580, y=560)
        error_label.after(3000, error_label.destroy)
        reset_root.after(3000,lambda win=reset_root :log_out(win))
        

    else:
        message_label=tk.Label(reset_root, text="Error")
        message_label.config(text="Les mots de passe ne correspondent pas!", font=("Louis George Cafe Bold", 18, "bold"), fg="red",bg="white")
        message_label.place(x=600, y=560)
        message_label.after(2500, message_label.destroy)
      
    if click_count >= 5:
          # Destroy the window after 5 clicks if passwords do not match
          reset_root.destroy()





reset_root = tk.Tk()
reset_root.config(bg="white")
imagee=(Image.open(current_path+"\\icons\\password2.jpg"))
imagee=imagee.resize((430,800))
sidepicture = ImageTk.PhotoImage(imagee)
#----------------Create a Label Widget to display the  Image-----------------
label = tk.Label(reset_root, image = sidepicture,padx=0,pady=0, relief="flat")
label.grid(row=0,column=0)
reset_root.title("Réinitialisation du mot de passe")
reset_root.geometry("1200x720")
welcome=tk.Label(reset_root,text="ESPACE     ETUDIANT ",font=("LEMONMILK-Medium",54),bg="white")
welcome.place(x=435,y=0)


# Add labels, entry fields, and buttons

label1 = tk.Label(reset_root, text="Entrez un mot de passe:", font=("Louis George Cafe Bold",35),bg="white")
label1.place(x=580,y=170)

entry1 = tk.Entry(reset_root,width=20,show="*",font=("Louis George Cafe Bold",35),relief="flat",bg="#e9eaef",highlightcolor="#041777",highlightthickness=3,highlightbackground='white')
entry1.place(x=580,y=250)




label2 = tk.Label(reset_root, text="Confirmer le mot de passe:", font=("Louis George Cafe Bold",35),bg="white")
label2.place(x=580,y=320)

entry2 = tk.Entry(reset_root,width=20,show="*",font=("Louis George Cafe Bold",35),relief="flat",bg="#e9eaef",highlightcolor="#041777",highlightthickness=3,highlightbackground='white')
entry2.place(x=580,y=400)
verify_button = tk.Button(reset_root,text="Vérifiez",bg="#32a2cd",fg="white",activebackground="#32a2cd", activeforeground="white",font=("Louis George Cafe Bold",20),padx=0,pady=0, relief="flat",width=33,command=update_password)
verify_button.place(x=580, y=500)

#--------------------------leave button--------------------------------------------------------------------------
leavebutton=tk.Button(reset_root,text="Quitter",command=reset_root.quit,bg="#258EF5",fg="white",activebackground="#258EF5", activeforeground="white",font=("Louis George Cafe Bold",16),padx=0,pady=0, relief="flat")      #
leavebutton.place(x=1100, y=660)

# Main GUI window loop
reset_root.mainloop()

