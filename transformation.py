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

def get_image_url(data):
    image_url = "https://books.toscrape.com/" + data
    image_url = image_url.replace('/../..', '')

    return image_url
#
