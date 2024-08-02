import requests
from bs4 import BeautifulSoup
import csv

# Lire l'URL depuis le fichier url.txt
with open('url.txt', 'r', encoding='utf-8') as file:
    url = file.readline().strip()  # Lire la première ligne et supprimer les espaces autour

# Effectuer une requête HTTP pour obtenir le contenu de la page
response = requests.get(url)
response.raise_for_status()  # Assurer que la requête a réussi

# Analyser le contenu HTML de la page
soup = BeautifulSoup(response.text, 'html.parser')

# Trouver tous les éléments <tr> contenant les données souhaitées
rows = soup.find_all('tr')

# Préparer une liste pour stocker les conventions collectives
conventions = []

# Extraire les données de chaque ligne
for row in rows:
    # Extraire les colonnes dans chaque ligne
    cols = row.find_all('td')
    if len(cols) == 2:
        # Extraire les valeurs de chaque colonne
        code = cols[0].get_text(strip=True)
        description = cols[1].get_text(strip=True)
        conventions.append({'code': code, 'description': description})

# Définir le nom du fichier CSV
csv_filename = 'conventions_collectives.csv'

# Écrire les données dans le fichier CSV
with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['code', 'description'])
    writer.writeheader()  # Écrire les en-têtes
    writer.writerows(conventions)  # Écrire les lignes de données

print(f"Les données ont été enregistrées dans le fichier {csv_filename}.")
