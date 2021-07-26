import bs4

def list_products(**kwargs):
    """Documentation here"""

    # Read html
    e_commerce_html = open('pages/content.html', 'r')
    
    # Parse html
    soup = bs4.BeautifulSoup(e_commerce_html.read(), 'html.parser')
    print(soup.find('span', {'class': 'a-badge-text'}).text)

    # This should return the list of products
    return []
