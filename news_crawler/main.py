from testai import *
from scraper import *

def paleisti_scrapers():
    try:
        silutesmuziejus_lt_scraper()
        pamarys_scraper()
        silutes_naujienos()
    except Exception as e:
        print(f"Įvyko klaida: {e}")
        testas()

def paklausti_vartotojo():
    while True:
        atsakymas = input("Ar norite gauti duomenis iš silutesmuziejus.lt, pamarys.lt, silutesnaujienos.lt? (Y/N): ").upper()
        if atsakymas == 'Y':
            paleisti_scrapers()
            break
        elif atsakymas == 'N':
            print("Programa baigia darbą.")
            break
        else:
            print("Įvestas netinkamas simbolis. Prašome įvesti 'Y' arba 'N'.")

if __name__ == "__main__":
    paklausti_vartotojo()
