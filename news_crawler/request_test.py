import requests
def main_test(urls, custom_headers): #Pridedame custom_headers parametra
    for url in urls:
        try:
            response = requests.get(url, headers=custom_headers)
            response.raise_for_status()
            print(f"Pavyko prisijungti prie: {url}!")
        except requests.exceptions.RequestException as e: # Gaudo bet kokias klaidas
            print(f"Nepavyko prisijungti prie: {url}: {e}")
def test_urls():
    urls = [
        "https://www.silute.lt/naujienos/1091",
        "https://www.silutesmuziejus.lt/home/apie-muzieju/naujienu-archyvas/",
        "https://lkca.lt/naujienos/",
        "http://www.pamarys.eu/category/aktualijos/",
        "https://www.silutesnaujienos.lt/lt/Temos/aktualijos/"
    ]


    custom_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.5',
        # Add other headers as needed
    }

    main_test(urls, custom_headers)
