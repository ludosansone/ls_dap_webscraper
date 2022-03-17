import requests
from bs4 import BeautifulSoup as bs

def get_page(url):
    """
        On récupère le contenu de la page dont l'URL est placé en argument
    """

    try:
        response = requests.get(url)
        return response.text
    except:
        return False
#

def get_soup(html_page):
    """
        On converti la page html en un objet BeautifulSoup
        Par ici la bonne soupe
    """

    try:
        soup = bs(html_page, 'html.parser')
        return soup
    except:
        return False
#

