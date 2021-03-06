import extraction, loading

def main():
    """
        Ce programme visite le site books.toscrape.com, et extrait les informations de tous les livres du catalogue
    """

    total_book_number = 0
    
    loading.create_directories()
    WEBSITE_URL = "https://books.toscrape.com/index.html"
    HTML_WEBSITE = extraction.get_page(WEBSITE_URL)
    if HTML_WEBSITE:
        soup_website = extraction.get_soup(HTML_WEBSITE )
        category_urls = extraction.get_all_categories(soup_website)
        print(f"{len(category_urls)} catégories trouvées")
        for category_url in category_urls:
            html_category = extraction.get_page(category_url)
            if html_category:
                soup_category = extraction.get_soup(html_category)
                url_list = extraction.get_urls_category(soup_category, category_url)
                book_number = len(url_list)
                book_list = []
                print(f"{book_number} livres en cours de récupération...")
                for url in url_list:
                    html_book = extraction.get_page(url)
                    if html_book:
                        soup_book = extraction.get_soup(html_book)
                        if soup_book:
                            datas_dict = extraction.get_book_datas(soup_book)
                            print(f"{datas_dict['title']} (données extraites)")
                            book_image = extraction.get_book_image(datas_dict['image_url'])
                            if book_image:
                                print("Image extraite")
                                loading.load_book_image(book_image, datas_dict['title'], datas_dict['category'])
                                print("Image enregistrée")
                            else:
                                print("Image Introuvable")
                            book_list.append(datas_dict)
                            total_book_number += 1
                            
                        else:
                            print("Impossible de créer l'objet BeautifulSoup à partir de cette page HTML")
                    else:
                        print("Erreur: Impossible d'accéder à l'URL indiquée")
                file_path = loading.load_category_datas(book_list, url_list)
                print(f"Les données de cette catégorie ont été chargées dans : {file_path}")
            else:
                print("Erreur: Impossible d'accéder à l'URL indiquée")
        print(f"Vous avez extré les données de {total_book_number} livres")
    else:
        print("Erreur: Impossible d'accéder à l'URL indiquée")

main()
