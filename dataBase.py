import mysql.connector as sc
from tkinter import messagebox
import webbrowser
from io import BytesIO
from tools import *


class DataBase:
    def __init__(self):
        self.mydata={}
        self.database=sc.connect(
            user="root",
            passwd="root",
            host="localhost",
            database="projet"

        )
        # print("connected")

        self.cursor=self.database.cursor()
        self.target_attribute=10

   #----------------------pour le script 1(collecter les données dans le fichier text data.txt)--------------------#
    def insert_data_sign_up_phase1(self,nom,prenom,email,téléphone,date_de_naissance):
        args=[("nom",nom),("prenom",prenom),("email",email),("téléphone",téléphone),("date_de_naissance",date_de_naissance)]
        file=open("data.txt","a+")
        for key,value in args:
            file.write(key+f":::{value}\n")
        file.close()


   #----------------------pour le script 2 (collecter les données dans le fichier text data.txt)--------------------#
    def insert_data_sign_up_phase2(self,adress,cne,cin,image):
        args=[("cne",cne),("cin",cin),("adress",adress),("image",image)]
        file=open("data.txt","a+")
        for key,value in args:
            file.write(key+f":::{value}\n")
        file.close()
    
    #----------------------pour le script 3 (collecter les données dans le fichier text data.txt)--------------------#
    def insert_data_sign_up_phase3(self,passwd,filière):
        args=[("passwd",passwd),("filière",filière)]
        for key,value in args:
            file=open("data.txt","a+")
            file.write(key+f":::{value}\n")
        file.close()



    #------------------------selection les données depuis le fichier data.txt puis les stocker dans une list pour les enregister sur la base des donneés------------    
    def getrow(self):
        file=open("data.txt","r")
        data=file.read().split("\n")
        data.remove("")
        print(data)
        for line in data:
            items=line.split(":::")
            self.mydata[items[0]]=items[1]
        return self.mydata

    #-------------une method static qui permet de convertir une phote en forme binaire-------------------------------------------------------------------------
    @staticmethod
    def convertToBinary(image_path):
        with open(image_path,"rb") as image :
            db= image.read()
        return db
    

    
    def get_image_link(self):
        Myimage_path=self.mydata["image"].split(" ")
        print(Myimage_path)
        if "png" in Myimage_path[2] or "jpg"in Myimage_path[2]:
            
            Myimage_path =Myimage_path[1].split("=")[1].replace("'","")+" "+Myimage_path[2].replace("'","")
        else:
            Myimage_path=Myimage_path[1].split("=")[1].replace("'","")

        print(Myimage_path)
        return Myimage_path
    #-----------------enregistrement des données dans a base des données--------------

    def valide(self):
        #-----definition d'image path 
        image_path=self.get_image_link()
        #------insertion des données (sans l'adress)--------#
        try:
            requeste="INSERT INTO ETUDIANT (mot_de_passe,nom,prenom,filière,email,téléphone,cne,cin,date_de_naissance,image) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            data=(self.mydata["passwd"],self.mydata["nom"],self.mydata["prenom"],self.mydata["filière"],
                  self.mydata["email"],self.mydata["téléphone"],self.mydata["cne"],self.mydata["cin"],self.mydata["date_de_naissance"],DataBase.convertToBinary(image_path))
            self.cursor.execute(requeste,data)
            self.database.commit()
            print("saved data without adress ")
        except:
            messagebox.showwarning("Warning","Etudiant déja existe, retour à a la page précédente pour corriger le CNE")
            raise "cne déja existe, recommencez la (ré)insription"
        

           
        

        #--------fetch the id of the student------
        self.cursor.execute("SELECT id from Etudiant order by id desc")
        valide_id=self.cursor.fetchall()
        v_valide_id=valide_id[0][0]
        print(v_valide_id)
        #----------insertion de l'adress----------
        adress=self.mydata["adress"].split("-")
        requeste="INSERT INTO Adress VALUES (%s,%s,%s,%s);"
        data=(v_valide_id,adress[0],adress[1],adress[2])
        self.cursor.execute(requeste,data)


        self.database.commit()
        print("saved adress data")

        #-----supprisseion du contenu de fichier pour une autre operation------#
        with open("data.txt","w") as file:
            file.write("")
        return
            
    #-----get name and prenom d'étudiant
    def getStudent(self):
        with open(r"fichierLog.txt","r") as fL:
            cne=fL.readlines()[0].replace("\n","")
        requete="SELECT NOM,PRENOM,filière FROM ETUDIANT WHERE CNE=%s"
        self.cursor.execute(requete,(cne,))
        nom_prenom_fil=self.cursor.fetchall()
        if nom_prenom_fil[0][2]=="ID1":
            filiere="ingénieurie des données 1"
        elif nom_prenom_fil[0][2]=="ID2":
            filiere="ingénieurie des données 2"
        elif nom_prenom_fil[0][2]=="GI1":
            filiere="génie informatique 1"
        else:
            filiere="génie informatique 2"

        return nom_prenom_fil[0][0],nom_prenom_fil[0][1],filiere
    
    #---------recuperation du cne d'utilisateur connecter--------------
    @staticmethod
    def get_cne_user_connecter():
        with open(r"fichierLog.txt","r") as fL:
            cne=fL.readlines()[0].replace("\n","")
            return cne

    # ----------recuperation des modules  et leur professeurs------------
    def get_Modules_Profs(self):
        
        requete ="SELECT module,professeur from modules where filière=(SELECT filière from etudiant where cne=%s)"
        data=(DataBase.get_cne_user_connecter(),)
        self.cursor.execute(requete,data)
        return  self.cursor.fetchall()
    
    #------------fonction pour modifier les données
    def update(self):

        requete="Update Etudiant set mot_de_passe=%s,nom=%s,prenom=%s,filière=%s,email=%s,téléphone=%s,date_de_naissance=%s"
        data=(self.mydata["passwd"],self.mydata["nom"],self.mydata["prenom"],self.mydata["filière"],
                  self.mydata["email"],self.mydata["téléphone"],self.mydata["date_de_naissance"])
        if self.mydata["image"]!="":
            requete=requete+",image=%s"
            data=data+(DataBase.convertToBinary(self.get_image_link()),)  
        requete=requete+"where cne='"+DataBase.get_cne_user_connecter()+"'"
        self.cursor.execute(requete,data)
        self.database.commit()

        requete="Update Etudiant set mot_de_passe=%s,nom=%s,prenom=%s,filière=%s,email=%s,téléphone=%s,date_de_naissance=%s"


        #--------fetch the id of the student------
        self.cursor.execute("SELECT id from Etudiant where cne=%s",(DataBase.get_cne_user_connecter(),))
        valide_id=self.cursor.fetchall()
        v_valide_id=valide_id[0][0]
        print(v_valide_id)
        #----------insertion de l'adress----------
        adress=self.mydata["adress"].split("-")
        requeste="update adress set num=%s,rue=%s,ville=%s where id_Etud=%s;"
        data=(adress[0],adress[1],adress[2],v_valide_id)
        self.cursor.execute(requeste,data)

        print("update avec succssés")

        # -------get Schedule--------

    def get_schedule(self):
        requete="SELECT filière from Etudiant where cne=%s"
        data=(DataBase.get_cne_user_connecter(),)
        self.cursor.execute(requete,data)
        filiere=self.cursor.fetchone()[0]
        requete="SELECT link from emploidutemps where filier=%s"
        data=(filiere,)
        self.cursor.execute(requete,data)
        link=self.cursor.fetchone()[0]
        webbrowser.open_new_tab(link)


    def get_user_first_name(self):
        self.cursor.execute("SELECT nom from Etudiant where Cne='"+DataBase.get_cne_user_connecter()+"';")
        result=self.cursor.fetchall()
        return result[0][0]
    
    def get_user_second_name(self):
        self.cursor.execute("SELECT prenom from Etudiant where Cne='"+DataBase.get_cne_user_connecter()+"';")
        result=self.cursor.fetchall()
        return result[0][0]
    
    def get_filiere(self):
        self.cursor.execute("SELECT filière from Etudiant where Cne='"+DataBase.get_cne_user_connecter()+"';")
        result=self.cursor.fetchall()
        return result[0][0]

    def get_user_picture(self):
        self.cursor.execute("SELECT image from Etudiant where Cne='"+DataBase.get_cne_user_connecter()+"';")
        result=self.cursor.fetchall()
        photo_in_byte=result[0][0]
        picture=create_icon(BytesIO(photo_in_byte),(200,200))
        return picture

    def get_user_CNE(self):
        self.cursor.execute("SELECT CNE from Etudiant where Cne='"+DataBase.get_cne_user_connecter()+"';")
        result=self.cursor.fetchall()
        cne=result[0][0]
        return cne

    def get_user_CIN(self):
        self.cursor.execute("SELECT CIN from Etudiant where Cne='"+DataBase.get_cne_user_connecter()+"';")
        result=self.cursor.fetchall()
        cin=result[0][0]
        return cin

    
    def cours_acces(self,i):
        self.cursor.execute("SELECT link from modules where filière='"+self.get_filiere()+"';")
        url =self.cursor.fetchall() 
        link=url[i][0]
        webbrowser.open_new_tab(link)
        
    
    def get_modules(self):
        self.cursor.execute("select module from modules where filière = '"+self.get_filiere()+"';")
        return self.cursor.fetchall()
    
    
    def get_modules_links(self):
        self.cursor.execute("select link from modules where filière = '"+self.get_filiere()+"';")
        return self.cursor.fetchall()
    
    def get_passwd(self,cne_text):
        self.cursor.execute("SELECT mot_de_passe from Etudiant where cne='"+cne_text+"';")
        passwd=self.cursor.fetchall()
        return passwd
    
    def get_cne_cin_ddn(self,cne, cin, ddn):
            self.cursor.execute("SELECT * FROM etudiant WHERE cne=%s AND cin=%s AND date_de_naissance=%s", (cne, cin, ddn))
            result = self.cursor.fetchone()
            return result

    def get_deliberatin(self):
            self.cursor.execute("SELECT link FROM deliberation WHERE filière=%s", (self.get_filiere(),))
            result = self.cursor.fetchone()
            webbrowser.open_new_tab(result[0])
