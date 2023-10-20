import requests
import bs4
Req_headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36'}

def FindLast(url):
    
    response=requests.get(url, headers=Req_headers) #runna il link
       
    response.raise_for_status()  

    soup=bs4.BeautifulSoup(response.text, "html.parser")
    
    annuncio=soup.find('div', class_="items__item item-card item-card--small")
    
    for link in annuncio('a', href=True):
        link=link['href']

    annuncio_nome=annuncio.find('h2')
    
    name=str(annuncio_nome.text.strip())
    annuncio_prezzo=annuncio.find('p')
    price=str(annuncio_prezzo.text.strip())

    return name,price,link