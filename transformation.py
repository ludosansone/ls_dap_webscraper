def get_number_available(data):
    substrings = data.split()
    for substring in substrings:
        substring = substring.replace('(', '')
        if (substring.isnumeric()):
            return substring
    return 0
#

def get_star_number(data):
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
    image_url = relative_url.replace('/../..', '')
    image_url = "https://books.toscrape.com/" + relative_url

    return image_url
#

def get_book_url(relative_url):
    url = relative_url.replace('../../../', '')
    url = "https://books.toscrape.com/catalogue/" + url

    return url
#

def get_category_url(relative_url):
    url = "https://books.toscrape.com/" + relative_url

    return url
#
