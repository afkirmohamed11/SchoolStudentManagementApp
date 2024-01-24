import re
import webbrowser
from PIL import Image,ImageTk
import os
import subprocess

def regler_date(date):
        date_list=date.split("-")
        if bool(re.match(r"^\d{4}-\d-\d$",date)):
                date_list[1]="0"+date_list[1]
                date_list[2]="0"+date_list[2]
        elif bool(re.match(r"^\d{4}-\d\d-\d$",date)): 
                date_list[2]="0"+date_list[2]
        elif bool(re.match(r"^\d{4}-\d-\d\d$",date)):
                date_list[1]="0"+date_list[1]
        date="-".join(date_list)
        
        return date

def open_email_client():
    webbrowser.open('mailto:equipetechniquestkinter@gmail.com')

#-----------------------create icon------------------------------#
def create_icon(icon_path,tuple_size):
        image=Image.open(icon_path)
        image=image.resize(tuple_size,Image.ANTIALIAS)
        icon_image=ImageTk.PhotoImage(image)
        return icon_image
    
    
current_path=os.getcwd()

def person(account):
    
    account.destroy()
    subprocess.run(["python", current_path+"\\info_pers.py"])

def description(account):
    account.destroy()
    subprocess.run(["python", current_path+"\\Description_filière.py"])

def accueil(account):
    account.destroy()
    subprocess.run(["python", current_path+"\\Account.py"])
def cours(account):
    account.destroy()
    subprocess.run(["python", current_path+"\\Cours.py"])

def log_out(account):
    account.destroy()
    subprocess.run(["python",current_path+"\\Luncher.py"])