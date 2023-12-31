from lxml.etree import HTML
from requests import get
import re

def silutesmuziejusd_test():
    data = get("https://www.silutesmuziejus.lt/home/apie-muzieju/naujienu-archyvas/").text
    data = HTML(data)

    # Išgauti duomenis
    pavadinimai = data.xpath("//div[contains(@class, 'news-content')]/div/h3[@class='news-title']/a")
    aprasymai = data.xpath("//div[contains(@class, 'news-short-content')]")
    datos = data.xpath("//div[@class='grid-date-post']/text()")
    paveikslėliai = data.xpath("//div[contains(@class, 'news-thumb')]/div/a/img/@src")

    # Patikrinti ir spausdinti ataskaitą
    print("Duomenys is silutesmuziejus.lt:")
    print("Pavadinimai:", "Gauta" if pavadinimai else "Nepavyko gauti")
    print("Aprašymai:", "Gauta" if aprasymai else "Nepavyko gauti")
    print("Paveikslėliai:", "Gauta" if paveikslėliai else "Nepavyko gauti")
    print("Data:", "Gauta" if datos else "Nepavyko gauti")

def pamarys_test():
        url = "http://www.pamarys.eu/category/aktualijos/"

        # Nustatome pasirinktines antraštes
        custom_headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept-Language': 'en-US,en;q=0.5',
        }

        response = get(url, headers=custom_headers)

        if response.status_code == 200:
            data = HTML(response.text)

            # Išgauti duomenis
            pavadinimai = data.xpath("//h2[@class='post-title']/a/text()")
            aprasymai = data.xpath(
                "//div[@class='postmeta']/span[@class='meta-author sep']/a/following-sibling::text()")
            datas = data.xpath("//span[@class='meta-date']/a/time/@datetime")

            # Išgauname paveikslėlius naudojant reguliariąją išraišką
            paveikslėliai = re.findall(r'<img [^>]*src="([^"]+)', response.text)

            # Patikrinti ir spausdinti ataskaitą
            print("Duomenys iš pamarys.eu:")
            print("Pavadinimai:", "Gauta" if pavadinimai else "Nepavyko gauti")
            print("Aprašymai:", "Gauta" if aprasymai else "Nepavyko gauti")
            print("Data:", "Gauta" if datas else "Nepavyko gauti")
            print("Paveikslėliai:", "Gauta" if paveikslėliai else "Nepavyko gauti")
        else:
            print("Nepavyko prisijungti prie puslapio. Status kodas:", response.status_code)


def silutesnaujienos_test():
    url = "https://www.silutesnaujienos.lt/lt/Temos/aktualijos/"

    # Nustatome pasirinktines antraštes
    custom_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.5',
    }

    response = get(url, headers=custom_headers)

    if response.status_code == 200:
        data = HTML(response.text)

        # Išgauti duomenis
        pavadinimai = data.xpath("//div[@class='p-header']/h3/a/text()")
        aprasymai = data.xpath("//p[@class='entry-summary']/text()")
        datas = data.xpath("//abbr[@class='date published']/@title")
        paveikslėliai = data.xpath("//span[@class='rb-iwrap']/img/@src")

        # Patikrinti ir spausdinti ataskaitą
        print("Duomenys iš silutesnaujienos.lt:")
        print("Pavadinimai:", "Gauta" if pavadinimai else "Nepavyko gauti")
        print("Aprašymai:", "Gauta" if aprasymai else "Nepavyko gauti")
        print("Data:", "Gauta" if datas else "Nepavyko gauti")
        print("Paveikslėliai:", "Gauta" if paveikslėliai else "Nepavyko gauti")
    else:
        print("Nepavyko prisijungti prie puslapio. Status kodas:", response.status_code)







