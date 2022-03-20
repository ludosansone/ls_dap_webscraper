def get_number_available(data):
    """
        On extrait la valeur numérique de la donnée brute
    """

    substrings = data.split()
    for substring in substrings:
        substring = substring.replace('(', '')
        if (substring.isnumeric()):
            return substring
    return 0
#

def get_star_number(data):
    """
        On transforme le nombre d'étoile écrit en toutes lettres, en valeur numérique
    """

    rating_dict = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }

    return rating_dict[data]
#

def get_image_url(relative_url):
    """
        On crée l'url absolut de l'image, à partir de son url relative
    """

    image_url = relative_url.replace('/../..', '')
    image_url = "https://books.toscrape.com/" + relative_url

    return image_url
#

def get_book_url(relative_url):
    """
        On crée l'url absolut du livre, , à partir de son url relative
    """

    url = relative_url.replace('../../../', '')
    url = "https://books.toscrape.com/catalogue/" + url

    return url
#

def get_category_url(relative_url):
    """
        On crée l'url absolut de la catégorie, à partir de son url relative
    """

    url = "https://books.toscrape.com/" + relative_url

    return url
#

def get_valid_file_name(name):
    valid_name = name.replace(' ', '_')\
    .replace(':', '')\
    .replace(',', '')\
    .replace('/', '')\
    .replace('?', '')\
    .replace('"', '')\
    .replace('&', '')\
    .replace('*', '')

    return valid_name
#
