from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

# зайти на лабиринт
driver.get("https://www.labirint.ru/")

# принять куки
button_cookie = driver.find_element(By.XPATH, '//*[@id="minwidth"]/div[4]/div[2]/button')
button_cookie.click()

# найти книги по слову Python
search_input = driver.find_element(By.CSS_SELECTOR, "#search-field")
search_input.send_keys("Python", Keys.RETURN)

# собрать все карточки товаров
books = driver.find_elements(By.CSS_SELECTOR, "div.product-card")
print('Страница №1.')
print(len(books))

#вывести в консоль инфо: название + автор + цена
for book in books:
    title = book.find_element(By.CSS_SELECTOR, "a.product-card__name").text
    author = book.find_element(By.CSS_SELECTOR, "div.product-card__author").text
    price = book.find_element(By.CSS_SELECTOR, "div.product-card__price-current").text
    print(title +'\t' + author + '\t' +  price)

# Перейти на следующую страницу
button_next = driver.find_element(By.CSS_SELECTOR, "div[class='pagination-next']")
time.sleep(2)
button_next.click()
# собрать все карточки товаров
books1 = driver.find_elements(By.CSS_SELECTOR, "div.product-card")
print('Страница №2.')
print(len(books1))

#вывести в консоль инфо: название + автор + цена
for book1 in books1:
    title1 = ''
    author1 =''
    # price1 = ''
    try:
        title1 = book1.find_element(By.CSS_SELECTOR, "a.product-card__name").text
    except:
        title1 = 'Нет названия'
    try:
        author1 = book1.find_element(By.CSS_SELECTOR, "div.product-card__author").text
    except:
        author1 = 'Нет автора'
    try:
        price1 = book1.find_element(By.CSS_SELECTOR, "div.product-card__price-current").text
    except:
        price1 = "Нет в продаже"
    print(title1 +'\t' + author1 + '\t' +  price1)

sleep(30)

