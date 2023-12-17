import requests
def test(urls):
    for url in urls:
        try:
            response = requests.get(url)
            response.raise_for_status()
            print(f"Pavyko prisijungti prie: {url}!")
        except requests.exceptions.RequestException as e: # Gaudo bet kokias klaidas
            print(f"Nepavyko prisijungti prie: {url}: {e}")
def test_urls():
    urls = [
        "https://www.silute.lt/naujienos/1091",
        "https://www.silutesmuziejus.lt/home/apie-muzieju/naujienu-archyvas/",
        "https://lkca.lt/naujienos/",
        "http://www.pamarys.eu/category/aktualijos/"
    ]
    test(urls)