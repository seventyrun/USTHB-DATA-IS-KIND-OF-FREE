from bs4 import BeautifulSoup
import pandas as pd
import requests

#read data from an xlsx file
data = pd.read_excel (r'Classeur1.xlsx')
list_eleve=data['numero'].tolist()

#for each matricule in the list go to the url and send it then get an html page response and extract data from it by using soup
#and print in on the screen

for i in list_eleve:
    try:
        print(i)
        url = 'https://ent.usthb.dz/index.php/Verifications_renseignements_L1/chercher_mat'
        data_send = {"mat": i, "valider": "Valider"}
        response=requests.post(url,data_send)

        soup = BeautifulSoup(response.text, 'lxml')
        nom = soup.find("input", {"name": "nom"})['value']
        prenom = soup.find("input", {"name": "prennom"})['value']
        date_nes = soup.find("input", {"name": "date_naiss"})['value']
        lieu_naiss = soup.find("input", {"name": "lieu_naiss"})['value']
        mail_usthb = soup.find("input", {"name": "mail_usthb"})['value']
        mail = soup.find("input", {"name": "mail_alter"})['value']
        domaine = soup.find("input", {"name": "domaine"})['value']
        section = soup.find("input", {"name": "section"})['value']
        groupe = soup.find("input", {"name": "groupe"})['value']
        print(nom,prenom,date_nes,lieu_naiss,mail_usthb,mail,domaine,section,groupe)
#if matricule not dound in data base witch can be possible 
    except TypeError:
        print("not in the data base")

        


