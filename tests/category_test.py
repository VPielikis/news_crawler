from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def kategoriju_crawler():
    url = "https://rekvizitai.vz.lt/imones/"
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(url)

    driver.implicitly_wait(2)

    try:
        accept_button = driver.find_element(By.ID, "cookiescript_accept")
        accept_button.click()
    except Exception as e:
        print("Slapukų sutikimo langas nerastas arba nepavyko uždaryti: ", e)

    categories_elements = driver.find_elements(By.XPATH, "//div[@class='input-wr']//div[@class='choices__item choices__item--choice choices__item--selectable' and @data-value!='']")
    categories = [element.get_attribute('data-value') for element in categories_elements if element.get_attribute('data-value')]

    driver.quit()

    # Atspausdinti kategorijas
    for category in categories:
        print(category)
