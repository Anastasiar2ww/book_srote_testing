#######################ДОБАВЛЕНИЕ КОММЕНТАРИЯ#######################
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(6)
driver.maximize_window()

# Проскролльте страницу вниз на 600 пикселей
driver.execute_script("window.scrollBy(0, 600);")
# Нажмите на название книги "Selenium Ruby" или на кнопку "READ MORE"
Selenium_ruby = driver.find_element_by_css_selector('.post-160 h3').click()
# Нажмите на вкладку "REVIEWS"
reviews = driver.find_element_by_css_selector(".tabs.wc-tabs li:nth-child(2)").click()
# Поставьте 5 звёзд
#stars = driver.find_element_by_class_name("star-5").click()
stars = driver.find_element_by_css_selector(".stars a:nth-child(5)").click()
# Заполните поле "Review" сообщением: "Nice book!"
your_rewier = driver.find_element_by_id("comment")
your_rewier.send_keys("Nice book!")
# Заполните поле "Name"
name = driver.find_element_by_id("author")
name.send_keys("Anna")
# Заполните "Email"
email = driver.find_element_by_id("email")
email.send_keys("test@mail.ru")
# Нажмите на кнопку "SUBMIT"
submit = driver.find_element_by_name("submit").click()

################################################################################




