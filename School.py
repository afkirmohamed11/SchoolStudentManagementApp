import subprocess
import os 
import mysql.connector as sqc


def connecter(user,bddn,passwd):

    # Define the MySQL connection parameters
    host = "localhost"
    user = user
    password = passwd
    database = bddn

    # Read the SQL script from file
    with open("script_des_bases_de_données.sql", "r", encoding="utf-8") as file:
        script = file.read()
    charset = "utf8mb4"

    # Construct the mysql command to execute the script
    command = f"mysql -h {host} -u {user} -p{password} --default-character-set={charset} {database}"

    # Run the command and pass the script as input
    subprocess.run(command, input=script.encode("utf-8"), shell=True)


file=open(r"config.properties","r")
var=file.read().split("=")[1].replace("\n","")
file.close()


cuurent_path =os.getcwd()
while True:
    try:
        if var=="0":
            username=input("S'il vous plait entrer le nom de votre utilisateur sur Mysql(généralement root): ")
            password=input("S'il vous plait entrer le mot de passe de cette utilisateur : ")
            db=input("S'il vous plait entrer le nom d'une base de données déja existe (généralement sys) : ")
            connecter(username,db,password)
            #--------gestion d'error au cas d'entrer des infos incorrect-----------
            db=sqc.connect(user=username,passwd=password,database="projet",host="localhost")
            print("connecter")
            crs=db.cursor()
            crs.execute("SELECT * FROM BentouhamiAfkirAkkouh;")
            print(crs.fetchone())

        subprocess.run(["python",cuurent_path+"\\Luncher.py"])
            

        with open(r"config.properties","w") as file:
            file.write("var=1")
        break
    except:
        print("Les informations sont incorrectes ,essayer une autre fois")