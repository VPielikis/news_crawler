import requests

def main_test(urls, custom_headers): #Pridedame custom_headers parametra
    for url in urls:
        try:
            response = requests.get(url, headers=custom_headers)
            response.raise_for_status()
            print(f"Pavyko sėkmingai prisijungti prie: {url} svetainės!")
        except requests.exceptions.RequestException as e: # Gaudo bet kokias klaidas
            print(f"Nepavyko prisijungti prie: {url}: {e}")
def test_urls():
    urls = [
        "https://rekvizitai.vz.lt/imones/",


    ]

    custom_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.5',

    }

    main_test(urls, custom_headers)