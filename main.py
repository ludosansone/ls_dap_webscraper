import extraction, transformation, loading

def main():
    """
        Fonction Principale
    """

    html = extraction.get_page("https://books.toscrape.com/catalogue/how-to-be-a-domestic-goddess-baking-and-the-art-of-comfort-cooking_470/index.html")
    if html:
        soup = extraction.get_soup(html)
        if soup:
            brut_datas_dict = extraction.get_book_brut_datas(soup)
            print(brut_datas_dict['upc'])
            print(brut_datas_dict['book_title'])
            print(brut_datas_dict['price_i'])
            print(brut_datas_dict['price_e'])
            print(brut_datas_dict['instock'])
            print(brut_datas_dict['product_description'])
            print(brut_datas_dict['category'])
            print(brut_datas_dict['img_url'])
            print(brut_datas_dict['rating'])
        else:
            print("Impossible de créer l'objet BeautifulSoup à partir de cette page HTML")
    else:
        print("Erreur: Impossible d'accéder à l'URL indiquée")
#

main()
