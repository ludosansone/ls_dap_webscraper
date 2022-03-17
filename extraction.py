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

def get_book_brut_datas(soup):
    """
        On extrait les données brutes à partir de l'objet BeautifulSoup placé en paramètre
    """

    brut_datas_dict = dict()

    table_divisions = soup.find_all('td')
    brut_datas_dict['category'] = soup.find_all('li')[2].text.strip()
    brut_datas_dict['book_title'] = soup.h1.text
    brut_datas_dict['product_description'] = soup.find_all('p')[3].text
    brut_datas_dict['price_e'] = table_divisions[2].text.replace('Â£', '')
    brut_datas_dict['price_i'] = table_divisions[3].text.replace('Â£', '')
    brut_datas_dict['instock'] = table_divisions[5].text
    brut_datas_dict['upc'] = table_divisions[0].text
    img_url = "https://books.toscrape.com/" + soup.img['src']
    brut_datas_dict['img_url'] = img_url.replace('/../..', '')
    brut_datas_dict['rating'] = soup.find_all('p')[2]['class'][1]

    return brut_datas_dict
#
