import csv
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup


request = requests.get(
    'http://s736246878.onlinehome.fr/webludo/pages/jeux.php?p=&SAI_recherche='
    )
page = request.content
soup = BeautifulSoup(request.text, "html.parser")


# récupération des url de chaque jeu pour une page de la bibliothèque
links = []


def game_links():
    game_links = (
        soup.find_all("td", {"width": "45px"})
    )
    for game_link in game_links:
        a = game_link.find("a")
        link_href = a["href"]
        base_url = "http://s736246878.onlinehome.fr/webludo/pages/jeux.php?"
        url_link = urljoin(base_url, link_href)
        links.append(url_link)


# récupération des 208 pages affichant les jeux de la ludothèque
site_pages = []
paginations = []


def get_pages():
    base_pagination = "http://s736246878.onlinehome.fr/webludo/pages/jeux.php?p="
    a = 1
    while a < 209:
        paginations.append(a)
        a += 1
    for pagination in paginations:
        pagination_url = base_pagination + "{}".format(pagination)
        site_pages.append(pagination_url)

# fonction d'écriture des données pour un jeu
def get_data_from_link():
    for link in links:
        request = requests.get(link)
        table = soup.find("table").find_all("td", {"align": "left"})
        table_lists = [elt.text.strip() for elt in table]
        with open('single_game.csv', 'a', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(table_lists)


# récupération des liens pour chaque jeu depuis la liste site_pages
all_games = []


def all_game_links():
    for site_page in site_pages:
        request = requests.get(site_page)
        page = request.content
        soup = BeautifulSoup(request.text, "html.parser")
        game_links = (
        soup.find_all("td", {"width": "45px"}))
        for game_link in game_links:
            a = game_link.find("a")
            link_href = a["href"]
            base_url = "http://s736246878.onlinehome.fr/webludo/pages/jeux.php?"
            url_link = urljoin(base_url, link_href)
            all_games.append(url_link)


# on exécute les fonctions pour que main.py utilise les listes
game_links()
get_pages()
all_game_links()
