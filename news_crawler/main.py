from category_crawler import kategoriju_crawler
from category_crawler import irasyti_i_csv
from data_ex import run_data_ex
from data_ex import clear_file
from data_ex import print_csv_file

def logika(msg):
    while True:
        atsakymas = input(msg).upper()
        if atsakymas in ["Y", "N"]:
            return atsakymas
        print("Prašome įvesti 'Y' arba 'N'.")

atsakymas = logika("Ar norite pradėti kategorijų gavimą iš tinklapio? (Y/N): ")
if atsakymas == "Y":
    kategorijos = kategoriju_crawler()
    print("Gautos kategorijos:")
    for kategorija in kategorijos:
        print(kategorija)

    atsakymas = logika("Ar norite įrašyti gautas kategorijas į CSV failą? (Y/N): ")
    if atsakymas == "Y":
        irasyti_i_csv(kategorijos)


atsakymas = logika("Ar norite pradėti duomenų išgavimą iš pasirinktų kategorijų ? (Y/N): ")
if atsakymas == "Y":
        run_data_ex()

atsakymas = logika("Ar norite įrašyti duomenis į csv failą ? (Y/N): ")
if atsakymas == "Y":
        clear_file()
        print_csv_file()
        print("Duomenys sėkmingai gauti ir įrašyti į data.csv failą !")

