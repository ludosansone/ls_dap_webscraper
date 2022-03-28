# ls_dap_webscraper

Ce Programme visite le site 'books.toscrape.com', extrait les données de chaque livre, et télécharge sa couverture.


## Installation de l'environnement virtuel

Afin de garentir le bon fonctionnement de ce script, vous devez l'exécuter dans le même environnement virtuel que le développeur. Pour se faire, suivez les instructions d'installation ci-dessous.
Attention, nous partons du principe que les paquets pip et venv sont bien installés sur votre ordinateur. Si tel n'est pas le cas, veuillez vous référer à leur documentation respective pour procéder à leur installation.


### Installation sous Windows

1- Ouvrez l'invite de commandes

2- Déplacez-vous à la racine du dossier ls_dap_webscraper, à l'aide de la commande cd

3- Pour créer l'environnement virtuel, saisissez la commande : python -m venv env

4- Pour démarrer ce dernier, saisissez la commande : env\Scripts\activate

5- Pour y installer les paquets nécessaires à la bonne exécution du script, saisissez la commande : pip install -r requierments.txt


### Installation sous Linux ou MacOSX

1- Ouvrez un terminal

2- Déplacez-vous à la racine du dossier ls_dap_webscraper, à l'aide de la commande cd

3- Pour créer l'environnement virtuel, saisissez la commande : python -m venv env

4- Pour démarrer ce dernier, saisissez la commande : source env/bin/activate

5- Pour y installer les paquets nécessaires à la bonne exécution du script, saisissez la commande : pip install -r requierments.txt


## Exécution du script

Une fois l'environnement virtuel installé et démarré, vous pouvez exécuter le script avec la commande : python main.py

## Résultats

Une fois l'exécution terminée, vous pourrez trouver tous les résultats dans le dossier datas.
