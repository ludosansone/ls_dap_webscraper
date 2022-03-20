import csv, os, requests, transformation

def load_category_datas(book_list, url_list):
    """
        On charge les données de tous les livres de la catégorie dans le fichier csv du même nom
    """

    file_name = book_list[0]['category'] + ".csv"
    file_path = "datas/csv_files/" + file_name
    url_index = 0

    try:
        os.mkdir('datas')
        os.mkdir('datas/csv_files')
    except:
        pass

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
        writer = csv.DictWriter(csvfile    , fieldnames = fieldnames, quoting = csv.QUOTE_NONNUMERIC)
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

def load_category_images(book_list):
    """
        On charge les images de tous les livres de la catégorie dans le dossier du même nom
    """

    dir_name = book_list[0]['category'] + "/"
    dir_path = "datas/images/" + dir_name

    try:
        os.mkdir('datas/images')
    except:
        pass
    os.mkdir('datas/images/' + dir_name)

    for book in book_list:
        book_title = transformation.get_valid_file_name(book['title'])

        jpgfile = open(dir_path + book_title + ".jpg", 'wb')
        file = requests.get(book['image_url'])
        jpgfile.write(file.content)
        jpgfile.close()
#
