import re
import requests
import csv
import os
from bs4 import BeautifulSoup


# Création de la fonction pour récupérer toutes les pages du site
def get_all_pages():
    urls = []
    page_number = 1
    for i in range(4):
        url = f"https://emploi.afrikinterim.com/?page={page_number}"
        page_number += 1
        urls.append(url)
    return urls


# Fonction pour extraire les offres d'une page spécifique
def parse_job(url, csv_writer):
    r = requests.get(url)
    r.encoding = "utf-8"  # Forcer l'encodage en UTF-8
    soup = BeautifulSoup(r.text, "html.parser")  # Utiliser r.text pour respecter l'encodage
    jobs = soup.find_all("div", class_="main")

    for job in jobs:
        titre = job.find("h3").text.strip() if job.find("h3") else "Non précisé"
        date = job.find("div", class_="text-date").text.strip() if job.find("div",
                                                                            class_="text-date") else "Non précisé"
        lieu = job.find("div", class_="text-info truncate").text.strip() if job.find("div",
                                                                                     class_="text-info truncate") else "Non précisé"

        # Écrire les données dans le fichier CSV
        csv_writer.writerow([titre, date, lieu])


# Fonction principale pour scraper toutes les pages et écrire les résultats dans un fichier CSV
def parse_all_job():
    # Chemin du fichier CSV
    chemin = os.path.join(os.getcwd(), "jobfair.csv")

    # Écriture dans le fichier CSV avec l'en-tête
    with open(chemin, mode="w", newline="",
              encoding="utf-8-sig") as file:  # Utilisation de utf-8-sig pour gérer les accents
        csv_writer = csv.writer(file)
        csv_writer.writerow(["Titre", "Date", "Lieu"])  # En-tête

        pages = get_all_pages()
        for page in pages:
            print(f"Scraping {page}...")
            parse_job(url=page, csv_writer=csv_writer)

    print(f"Les données ont été enregistrées dans {chemin}")


# Lancer le scraping
parse_all_job()
