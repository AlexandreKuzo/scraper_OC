import csv
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from start import site_pages, links, all_games

# on définit et écrit les titres des colonnes du fichier .csv
headers = ['numero', 'nom', 'editeur', 'prix_location', 'nombre_joueurs', 'age', 'resume', 'contenu', 'image']
with open('jeux.csv', 'a', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(headers)

# récupération des liens pour chaque jeu depuis la liste site_pages
def main():
    for all_game in all_games:
            request = requests.get(all_game)
            page = request.content
            soup = BeautifulSoup(request.text, "html.parser")
            table = soup.find("table").find_all("td", {"align":"left"})
            table_lists = [elt.text.strip() for elt in table]
            with open('jeux.csv', 'a', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(table_lists)


if __name__ == '__main__':
    main()
