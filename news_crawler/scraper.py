from lxml.etree import HTML
from requests import get
import csv

def silutesmuziejus_lt_scraper():
    url = "https://www.silutesmuziejus.lt/home/apie-muzieju/naujienu-archyvas/"
    response = get(url)

    if response.status_code == 200:
        data = HTML(response.text)

        # Išgauti naujienų pavadinimus, aprašymus, datas ir paveikslėlius
        pavadinimai = data.xpath("//div[contains(@class, 'news-content')]/div/h3[@class='news-title']/a")
        aprasymai = data.xpath("//div[contains(@class, 'news-short-content')]")
        datas = data.xpath("//div[@class='grid-date-post']/text()")
        paveikslėliai = data.xpath("//div[contains(@class, 'news-thumb')]/div/a/img/@src")

        if pavadinimai and aprasymai and datas and paveikslėliai:
            print("Duomenys sėkmingai gauti!")
            with open("duomenys.csv", "w", newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(["Data", "Pavadinimas", "Aprašymas", "Paveikslėlis"])

                for data, pavadinimas, aprasymas, paveikslėlis in zip(datas, pavadinimai, aprasymai, paveikslėliai):
                    writer.writerow([data.strip(), pavadinimas.text, aprasymas.text, paveikslėlis])
            print("Naujienos išsaugotos 'duomenys.csv' faile.")
        else:
            print("Nepavyko gauti duomenų.")

    else:
        print("Nepavyko prisijungti prie svetainės.")



#silutesmuziejus_lt_scraper()