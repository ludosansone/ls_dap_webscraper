import extraction, loading

def main():
    """
        Fonction Principale
    """

    url_category = "https://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html"
    html_category = extraction.get_page(url_category)
    if html_category:
        soup_category = extraction.get_soup(html_category)
        url_list = extraction.get_urls_category(soup_category, url_category)
        book_number = len(url_list)
        book_list = []
        print(str(book_number) + " livres en cours de récupération...")
        for url in url_list:
            html_book = extraction.get_page(url)
            if html_book:
                soup_book = extraction.get_soup(html_book)
                if soup_book:
                    datas_dict = extraction.get_book_datas(soup_book)
                    book_list.append(datas_dict)
                    print(datas_dict['title'] + " récupéré...")
                else:
                    print("Impossible de créer l'objet BeautifulSoup à partir de cette page HTML")
            else:
                print("Erreur: Impossible d'accéder à l'URL indiquée")
        file_path = loading.load_new_category(book_list)
        print("Toutes les données se trouvent dans : " + file_path)
    else:
        print("Erreur: Impossible d'accéder à l'URL indiquée")
#

main()
