import extraction, loading

def main():
    """
        Fonction Principale
    """

    website_url = "https://books.toscrape.com/index.html"
    html_website = extraction.get_page(website_url)
    if html_website:
        soup_website = extraction.get_soup(html_website)
        category_urls = extraction.get_all_categories(soup_website)
        print(str(len(category_urls)) + " catégories trouvées")
        for category_url in category_urls:
            html_category = extraction.get_page(category_url)
            if html_category:
                soup_category = extraction.get_soup(html_category)
                url_list = extraction.get_urls_category(soup_category, category_url)
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
                            print(datas_dict['title'] + " (données extraites)")
                        else:
                            print("Impossible de créer l'objet BeautifulSoup à partir de cette page HTML")
                    else:
                        print("Erreur: Impossible d'accéder à l'URL indiquée")
                file_path = loading.load_category_datas(book_list, url_list)
                loading.load_category_images(book_list)
                print("Les données de cette catégorie ont été chargées dans : " + file_path)
                

            else:
                print("Erreur: Impossible d'accéder à l'URL indiquée")
    else:
        print("Erreur: Impossible d'accéder à l'URL indiquée")
#

main()
