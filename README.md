# Du WebScraping avec Python (encore!)

Un programme pour récupérer les informations du site web http://s736246878.onlinehome.fr/webludo/pages/jeux.php ; les données sont ensuite entrées dans un .csv pour traitement.

## Contenu du dossier

Deux fichiers Python ; un fichier avec les fonctions de récupération des données : start.py + un fichier main.py qui sera le fichier de lancement du programme.

### "Matos" requis

- Python 3
- L'installateur de modules Pip et Virtualenv ; infos : https://docs.python.org/fr/3/installing/index.html
- BeautifulSoup : https://www.crummy.com/software/BeautifulSoup/bs4/doc/
- Requests : https://www.w3schools.com/python/module_requests.asp

### Installation et démarrage (consignes adaptées pour utilisateurs/utilisatrices de Mac)

Etape 1: clonez le repo avec la commande ``git clone https://github.com/AlexandreKuzo/scraper_OC.git``

Etape 2: placez vous dans le repo ``cd scraper_OC`` et créez un environnement virtuel ``python3 -m venv env``

Etape 3: activez l'environnement virtuel ``source env/bin/activate``

Etape 4: une fois l'environnement virtuel activé, installez tous les packages requis en tapant la commande ``pip install requirements.txt``


## Executer le script

Vous pouvez lancer le script depuis le terminal avec la commande ``python3 main.py``, et voilà !


## Auteur
* **Alexandre Kuzo**  [@alexandrekuzo](https://github.com/AlexandreKuzo)
