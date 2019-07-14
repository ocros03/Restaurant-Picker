from bs4 import BeautifulSoup
import requests


def main():
    ''' main function'''
    
    #name = "La Fontana Authentic Italian Restaurant"
    name = "https://www.hibachihutcharleston.com/"
    get_from_web(name)


def get_from_web(nm):
    ''' gets restaurant information from the internet'''

    url = nm
    print(url)
    
    r = requests.get(url)
    html_doc = r.text
    soup = BeautifulSoup(html_doc, 'lxml')
    #print(soup.prettify())

    script = soup.find('script')
    print(script)
    phone = script.text
    print(phone)


if __name__ == '__main__':
    main()
