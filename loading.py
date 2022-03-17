import csv, os

def load_new_category(book_list):
    file_name = book_list[0]['category'] + ".csv"
    file_path = "datas/" + file_name

    try:
        os.mkdir('datas')
    except:
        pass

    with open(file_path, 'w', newline = '', encoding = 'utf-8') as csvfile:
        fieldnames = [
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
            writer.writerow({
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
    return file_path
#
