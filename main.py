import extraction, transformation, loading

def main():
    """
        Fonction Principale
    """

    html = extraction.get_page("https://books.toscrape.com/catalogue/how-to-be-a-domestic-goddess-baking-and-the-art-of-comfort-cooking_470/index.html")
    if html:
        soup = extraction.get_soup(html)
        if soup:
            datas_dict = extraction.get_book_datas(soup)
            print(datas_dict['universal_product_code'])
            print(datas_dict['title'])
            print(datas_dict['price_including_tax'])
            print(datas_dict['price_excluding_tax'])
            print(datas_dict['number_available'])
            print(datas_dict['product_description'])
            print(datas_dict['category'])
            print(datas_dict['review_rating'])
            print(datas_dict['image_url'])
            
        else:
            print("Impossible de créer l'objet BeautifulSoup à partir de cette page HTML")
    else:
        print("Erreur: Impossible d'accéder à l'URL indiquée")
#

main()
