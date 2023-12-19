from request_test import *
from data_test import *
def test_data():
    silutesmuziejusd_test()
    silutesnaujienos_test()
    pamarys_test()

def test_rq():
    test_urls()


def testas():
    user_d = ''
    while user_d != 'n':
        user_d = input("Patikrinti duomenų gavimą iš xPath? (Įveskite Y arba N): ").lower()

        if user_d == 'y':
            test_data()
            break
        elif user_d == 'n':
            break
        else:
            print("Neteisinga įvestis. Prašome įvesti Y arba N.")

    user_d = ''
    while user_d != 'n':
        user_d = input("Patikrinti ar pavyksta prisijungti? (Įveskite Y arba N): ").lower()

        if user_d == 'y':
            test_rq()
            break
        elif user_d == 'n':
            break
        else:
            print("Neteisinga įvestis. Prašome įvesti Y arba N.")