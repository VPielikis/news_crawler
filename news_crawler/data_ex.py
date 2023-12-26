import requests
from lxml import html

# Čia yra jūsų kategorijų sąrašas
categories = [
    "akmens_gaminiai"]


def extract_data(category, page_number):
    url = f"https://rekvizitai.vz.lt/imones/{category}/{page_number}/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.5',
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return None

    return html.fromstring(response.content)

def print_data(tree):
    if tree is None:
        return False

    titles = tree.xpath('//a[contains(@class, "company-title d-block")]/text()')
    if not titles:
        return False

    subtitles = tree.xpath('//a[contains(@class, "company-subtitle d-block")]/text()')
    addresses = tree.xpath('//div[contains(@class, "address")]/text()')
    activities = tree.xpath('//div[contains(@class, "activities")]/text()')
    descriptions = tree.xpath('//div[contains(@class, "description")]/text()')
    contact_info = tree.xpath('//div[contains(@class, "see-info")]/a/@href')

    for i in range(len(titles)):
        print(f"Įmonės pavadinimas: {titles[i]}")
        print(f"Subtitras: {subtitles[i] if i < len(subtitles) else 'N/A'}")
        print(f"Adresas: {addresses[i] if i < len(addresses) else 'N/A'}")
        print(f"Veiklos sritis: {activities[i] if i < len(activities) else 'N/A'}")
        print(f"Aprašymas: {descriptions[i] if i < len(descriptions) else 'N/A'}")
        print(f"Kontaktinė informacija: {contact_info[i] if i < len(contact_info) else 'N/A'}")
        print("\n")

    return True

def run_data_ex():
# Iteruojama per kiekvieną kategoriją ir puslapius
    for category in categories:
        page_number = 1
        while print_data(extract_data(category, page_number)):
            page_number += 1
