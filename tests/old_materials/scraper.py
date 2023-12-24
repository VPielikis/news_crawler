from lxml.etree import HTML
from requests import get
import csv
import re

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
            with open("silutesmuziejus.csv", "w", newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(["Data", "Pavadinimas", "Aprašymas", "Paveikslėlis"])

                short_data = list(zip(datas, pavadinimai, aprasymai, paveikslėliai))[:10]
                for data, pavadinimas, aprasymas, paveikslėlis in short_data:
                    writer.writerow([data.strip(), pavadinimas.text, aprasymas.text, paveikslėlis])

            #data = list(zip(datas, pavadinimai, aprasymai, paveikslėliai))[:10]
            #for data, pavadinimas, aprasymas, paveikslėlis in data:
            #for data, pavadinimas, aprasymas, paveikslėlis in sujungti_duomenys:
               # for data, pavadinimas, aprasymas, paveikslėlis in zip(datas, pavadinimai, aprasymai, paveikslėliai):
                    #writer.writerow([data.strip(), pavadinimas.text, aprasymas.text, paveikslėlis])
            print("Naujienos išsaugotos 'silutesmuziejus.csv' faile.")
        else:
            print("Nepavyko gauti duomenų.")

    else:
        print("Nepavyko prisijungti prie svetainės.")

def pamarys_scraper():
    url = "http://www.pamarys.eu/category/aktualijos/"
    custom_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.5',
    }

    response = get(url, headers=custom_headers)

    if response.status_code == 200:
        data = HTML(response.text)

        pavadinimai = data.xpath("//h2[@class='post-title']/a/text()")
        aprasymai = data.xpath("//div[@class='postmeta']/span[@class='meta-author sep']/a/following-sibling::text()")
        datas = data.xpath("//span[@class='meta-date']/a/time/@datetime")
        paveikslėliai = re.findall(r'<img [^>]*src="([^"]+)', response.text)

        if pavadinimai and aprasymai and datas and paveikslėliai:
            with open("pamarys.csv", "w", newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(["Data", "Pavadinimas", "Aprašymas", "Paveikslėlis"])

                short_data = list(zip(datas, pavadinimai, aprasymai, paveikslėliai))[:10]
                for data, pavadinimas, aprasymas, paveikslėlis in short_data:
                    writer.writerow([data, pavadinimas, aprasymas, paveikslėlis])
            print("Naujienos išsaugotos 'pamarys.csv' faile.")
        else:
            print("Nepavyko gauti duomenų.")
    else:
        print("Nepavyko prisijungti prie puslapio. Status kodas:", response.status_code)

def silutes_naujienos():
    url = "https://www.silutesnaujienos.lt/lt/Temos/aktualijos/"
    custom_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.5',
    }

    response = get(url, headers=custom_headers)

    if response.status_code == 200:
        data = HTML(response.text)

        pavadinimai = data.xpath("//div[@class='p-header']/h3/a/text()")
        aprasymai = data.xpath("//p[@class='entry-summary']/text()")
        datas = data.xpath("//abbr[@class='date published']/@title")
        paveikslėliai = data.xpath("//span[@class='rb-iwrap']/img/@src")

        if pavadinimai and aprasymai and datas and paveikslėliai:
            with open("silutesnaujienos.csv", "w", newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(["Data", "Pavadinimas", "Aprašymas", "Paveikslėlis"])


                short_data = list(zip(datas, pavadinimai, aprasymai, paveikslėliai))[:10]
                for data, pavadinimas, aprasymas, paveikslėlis in short_data:
                    writer.writerow([data, pavadinimas, aprasymas, paveikslėlis])
            print("Naujienos išsaugotos 'silutesnaujienos.csv' faile.")
        else:
            print("Nepavyko gauti duomenų.")
    else:
        print("Nepavyko prisijungti prie puslapio. Status kodas:", response.status_code)

