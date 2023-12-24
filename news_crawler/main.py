from category_crawler import *

kategorijos = kategoriju_crawler()
print("Gautos kategorijos:")
for kategorija in kategorijos:
    print(kategorija)
irasyti_i_csv(kategorijos)
