import requests, transformation
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

def get_book_datas(soup):
    """
        On extrait les données à partir de l'objet BeautifulSoup placé en paramètre, en opérant une transformation si nécessaire
    """

    datas_dict = dict()

    # Extraction brute, ou presque
    table_divisions = soup.find_all('td')
    datas_dict['universal_product_code'] = table_divisions[0].text
    datas_dict['title'] = soup.h1.text
    datas_dict['price_including_tax'] = table_divisions[3].text.replace('Â£', '')
    datas_dict['price_excluding_tax'] = table_divisions[2].text.replace('Â£', '')
    datas_dict['number_available'] = table_divisions[5].text
    datas_dict['product_description'] = soup.find_all('p')[3].text
    datas_dict['category'] = soup.find_all('li')[2].text.strip()
    datas_dict['review_rating'] = soup.find_all('p')[2]['class'][1]
    datas_dict['image_url'] = soup.img['src']

    # Transformation si nécessaire
    datas_dict['number_available'] = transformation.get_number_available(datas_dict['number_available'])
    datas_dict['review_rating'] = transformation.get_star_number(datas_dict['review_rating'])
    datas_dict['image_url'] = transformation.get_image_url(datas_dict['image_url'])

    return datas_dict
#
