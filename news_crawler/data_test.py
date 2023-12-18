from lxml.etree import HTML
from requests import get

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

