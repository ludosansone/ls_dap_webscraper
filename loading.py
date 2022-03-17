import csv

def load_new_book(book_dict):
    with open('book.csv', 'w', newline = '') as csvfile:
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
        writer.writerow({
            'universal_product_code': book_dict['universal_product_code'],
            'title': book_dict['title'],
            'price_including_tax': book_dict['price_including_tax'],
            'price_excluding_tax': book_dict['price_excluding_tax'],
            'number_available': book_dict['number_available'],
            'product_description': book_dict['product_description'],
            'category': book_dict['category'],
            'review_rating': book_dict['review_rating'],
            'image_url': book_dict['image_url'],
        })

#


    return 0

