import csv, os, transformation

def create_directories():
    """
        Création des dossiers de base
    """

    try:
        os.mkdir('datas')
    except:
        pass
    
    try:
        os.mkdir('datas/csv_files')
    except:
        pass
    try:
        os.mkdir('datas/images')
    except:
        pass
#

def load_category_datas(book_list, url_list):
    """
        On charge les données de tous les livres de la catégorie dans le fichier csv du même nom
    """

    file_path = "datas/csv_files/" + book_list[0]['category'] + ".csv"
    url_index = 0

    with open(file_path, 'w', newline = '', encoding = 'utf-8') as csvfile:
        fieldnames = [
            'product_page_url',
            'universal_product_code',
            'title',
            'price_including_tax',
            'price_excluding_tax',
            'number_available',
            'product_description',
            'category',
            'review_rating',
            'image_url'
        ]
        writer = csv.DictWriter(csvfile, fieldnames = fieldnames, quoting = csv.QUOTE_NONNUMERIC)
        writer.writeheader()
        for book in book_list:
            book['product_description']  = book['product_description'].replace('"', '')

            writer.writerow({
                'product_page_url': url_list[url_index],
                'universal_product_code': book['universal_product_code'],
                'title': book['title'],
                'price_including_tax': book['price_including_tax'],
                'price_excluding_tax': book['price_excluding_tax'],
                'number_available': book['number_available'],
                'product_description': book['product_description'],
                'category': book['category'],
                'review_rating': book['review_rating'],
                'image_url': book['image_url'],
            })
            url_index += 1
    return file_path
#

def load_book_image(book_image, book_title, book_category):
    """
        On charge l'image du livre dans un fichier portant le nom du livre, dans un dossier portant le nom de sa catégorie
    """

    dir_path = "datas/images/" + book_category + "/"

    try:
        os.mkdir('datas/images/' + book_category)
    except:
        pass

    book_title = transformation.get_valid_file_name(book_title)
    with open(dir_path + book_title + ".jpg", 'wb') as jpgfile:
        jpgfile.write(book_image.content)
#
