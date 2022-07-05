################ ОТОБРАЖЕНИЕ СТРАНИЦЫ ТОВАРА #################3
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
'''
1. Откройте http://practice.automationtesting.in/
2. Залогиньтесь
3. Нажмите на вкладку "Shop"
4. Откройте книгу "HTML 5 Forms"
5. Добавьте тест, что заголовок книги назвается: "HTML5 Forms"
'''
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(6)
driver.maximize_window()

# Залогиньтесь
# Нажмите на вкладку "My Account Menu"
my_account = driver.find_element_by_id("menu-item-50").click()
# В разделе "Login", введите email для логина
username = driver.find_element_by_id("username")
username.send_keys("test123123test@mail.ru")
# В разделе "Login", введите пароль для логина
password = driver.find_element_by_id("password")
password.send_keys("!!11@22@76##Tq1")
# Нажмите на кнопку "Login"
login = driver.find_element_by_css_selector('input[value="Login"]').click()
# Нажмите на вкладку "Shop"
#shop = driver.find_element_by_link_text("Shop").click()
shop = driver.find_element_by_id("menu-item-40").click()
#driver.execute_script("window.scrollBy(0, 200);")
# Откройте книгу "HTML 5 Forms"
ht = driver.find_element_by_css_selector('.post-181 h3').click()
# Добавьте тест, что заголовок книги назвается: "HTML5 Forms"
h1 = driver.find_element_by_tag_name('h1')
h1_text = h1.text
assert h1_text == "HTML5 Forms"



################ КОЛИЧЕСТВО ТОВАРОВ В КАТЕГОРИИ ################

'''
1. Откройте http://practice.automationtesting.in/
2. Залогиньтесь
3. Нажмите на вкладку "Shop"
4. Откройте категорию "HTML"
5. Добавьте тест, что отображается три товара
'''

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
# Откройте http://practice.automationtesting.in/
driver.get("http://practice.automationtesting.in/")
wait = driver.implicitly_wait(5)

# Залогиньтесь
# Нажмите на вкладку "My Account Menu"
my_account = driver.find_element_by_id("menu-item-50").click()
# В разделе "Login", введите email для логина
username = driver.find_element_by_id("username")
username.send_keys("test123123test@mail.ru")
# В разделе "Login", введите пароль для логина
password = driver.find_element_by_id("password")
password.send_keys("!!11@22@76##Tq1")
# Нажмите на кнопку "Login"
login = driver.find_element_by_css_selector('input[value="Login"]').click()
# Нажмите на вкладку "Shop"
shop = driver.find_element_by_link_text("Shop").click()
driver.execute_script("window.scrollBy(0, 200);")
# Откройте категорию "HTML"
html = driver.find_element_by_css_selector(".product-categories li:nth-child(2)").click()
# Добавьте тест, что отображается три товара
count = driver.find_elements_by_css_selector('.products li')
if len(count) == 3:
    print("3 товара")
else:
    print("Ошибка. Количество товаров: " + str(len(count)))


############## СОРТИРОВКА ТОВАРОВ ####################
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)
# Откройте http://practice.automationtesting.in/
driver.get("http://practice.automationtesting.in/")
#wait = driver.implicitly_wait(5)
# Залогиньтесь
# Нажмите на вкладку "My Account Menu"
my_account = driver.find_element_by_id("menu-item-50").click()
# В разделе "Login", введите email для логина
username = driver.find_element_by_id("username")
username.send_keys("test123123test@mail.ru")
# В разделе "Login", введите пароль для логина
password = driver.find_element_by_id("password")
password.send_keys("!!11@22@76##Tq1")
# Нажмите на кнопку "Login"
login = driver.find_element_by_css_selector('input[value="Login"]').click()
# Нажмите на вкладку "Shop"
shop = driver.find_element_by_partial_link_text("Shop").click()
#driver.execute_script("window.scrollBy(0, 200);")
# Добавьте тест, что в селекторе выбран вариант сортировки по умолчанию
default_sorting = driver.find_element_by_css_selector('option[value="menu_order"]')
# Отсортируйте товары по цене от большей к меньшей
field = driver.find_element_by_class_name(".woocommerce-ordering")
select = Select(field)
select.select_by_value("price")



###################### ОТОБРАЖЕНИЕ, СКИДКА ТОВАРА ########################

import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)


# Откройте http://practice.automationtesting.in/
driver.get("http://practice.automationtesting.in/")
# Залогиньтесь
# Нажмите на вкладку "My Account Menu"
my_account = driver.find_element_by_id("menu-item-50").click()
# В разделе "Login", введите email для логина
username = driver.find_element_by_id("username")
username.send_keys("test123123test@mail.ru")
# В разделе "Login", введите пароль для логина
password = driver.find_element_by_id("password")
password.send_keys("!!11@22@76##Tq1")
# Нажмите на кнопку "Login"
login = driver.find_element_by_name('login')
login.click()
# Нажмите на вкладку "Shop"
#shop = driver.find_element_by_link_text("Shop").click()
shop = driver.find_element_by_id('menu-item-40')
shop.click()
driver.execute_script("window.scrollBy(0, 200);")
# Откройте книгу "Android Quick Start Guide"
android = driver.find_element_by_css_selector('.post-169 h3').click()
# Добавьте тест, что содержимое старой цены = "₹600.00"
price_600 = driver.find_element_by_css_selector(".price del")
price_600_text = price_600.text
assert price_600_text == "₹600.00"
# Добавьте тест, что содержимое новой цены = "₹450.00"
price_450 = driver.find_element_by_css_selector(".price ins")
price_450_text = price_450.text
assert price_450_text == '₹450.00'
# Добавьте явное ожидание и нажмите на обложку книги
book_cover = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
(By.CSS_SELECTOR, ".images")))
book_cover.click()
# Добавьте явное ожидание и закройте предпросмотр нажав на крестик (кнопка вверху справа)
book_close = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
(By.CLASS_NAME, ".pp_close")))
book_close.click()

###################### ПРОВЕРКА ЦЕНЫ В КОРЗИНЕ #######################
'''
1. Откройте http://practice.automationtesting.in/ # в этом тесте логиниться не нужно
2. Нажмите на вкладку "Shop"
3. Добавьте в корзину книгу "HTML5 WebApp Development" # см. комментарии в самом низу
4. Добавьте тест, что возле коризны(вверху справа) количество товаров = "1 Item", а стоимость = "₹180.00"
• Используйте для проверки assert
5. Перейдите в корзину
6. Используя явное ожидание, проверьте что в Subtotal отобразилась стоимость
7. Используя явное ожидание, проверьте что в Total отобразилась стоимость

# если эта книга будет out of stock - тогда вместо неё добавьте книгу HTML5 Forms и выполните тесты по аналогии
# если все книги будут out of stock - тогда пропустите это и следующие два задания
'''

import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)

# Откройте http://practice.automationtesting.in/
driver.get("http://practice.automationtesting.in/shop/")

# Нажмите на вкладку "Shop"
#shop = driver.find_element_by_link_text("Shop").click()
shop = driver.find_element_by_id('menu-item-40')
shop.click()
#driver.execute_script("window.scrollBy(0, 400);")
# Добавьте в корзину книгу "HTML5 WebApp Development"
add_to_basket = driver.find_element_by_css_selector(".post-182 a:nth-child(2)")
add_to_basket.click()
# Добавьте тест, что возле коризны(вверху справа) количество товаров = "1 Item", а стоимость = "₹180.00"
Item = driver.find_element_by_class_name("cartcontents")
Item_text = Item.text
assert Item_text == "1 Item"

price = driver.find_element_by_css_selector("amount")
price_text = price.text
assert price_text == "₹180.00"
# Перейдите в корзину
basket = driver.find_element_by_css_selector(".main-nav li:nth-child(6)").click()
#basket = driver.find_element_by_class_name("wpmenucart-icon-shopping-cart-0")
# Используя явное ожидание, проверьте что в Subtotal отобразилась стоимость
price_subtotal = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
(By.CSS_SELECTOR, ".cart-subtotal td")))
# Используя явное ожидание, проверьте что в Total отобразилась стоимость
price_total = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
(By.CSS_SELECTOR, ".order-total td")))

################### Shop: работа в корзине ########################
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

# Нажмите на вкладку "Shop"
shop = driver.find_element_by_id('menu-item-40')
shop.click()
driver.execute_script("window.scrollBy(0, 500);")
# Добавьте в корзину книги "HTML5 WebApp Development" и "JS Data Structures and Algorithm"
html_5 = driver.find_element_by_css_selector(".post-182 a:nth-child(2)")
html_5.click()
time.sleep(3)
driver.execute_script("window.scrollBy(400, 650);")
JS_Data_Structures = driver.find_element_by_css_selector(".post-180 a:nth-child(2)")
JS_Data_Structures.click()

# Перейдите в корзину
#view_basket = driver.find_element_by_css_selector("a[title='View Basket']").click()
basket = driver.find_element_by_css_selector(".main-nav li:nth-child(6)").click()
#basket_2 = driver.find_element_by_css_selector("[title='View your shopping cart']").click()
time.sleep(3)
# Удалите первую книгу
time.sleep(3)
delete_first_book = driver.find_element_by_css_selector(".cart_item .product-remove [data-product_id='181']").click()
# Нажмите на Undo (отмена удаления)
undo = driver.find_element_by_css_selector(".woocommerce-message a").click()
# В Quantity увеличьте количесто товара до 3 шт для "JS Data Structures and Algorithm“
quantity = driver.find_element_by_css_selector(".quantity [max='9631']")
quantity.clear()
quantity.send_keys("3")
# Нажмите на кнопку "UPDATE BASKET"
update_basket = driver.find_element_by_css_selector("input[value='Update Basket']").click()
# Добавьте тест, что value элемента quantity для "JS Data Structures and Algorithm" равно 3 # используйте assert
value_quantity = driver.find_element_by_css_selector(".quantity [max='9631']")
value_quantity_3 = value_quantity.get_attribute("value")
assert value_quantity_3 == "3"
time.sleep(3)
# Нажмите на кнопку "APPLY COUPON"
apply_coupon = driver.find_element_by_name("apply_coupon").click()
# Добавьте тест, что возникло сообщение: "Please enter a coupon code."
coupon = driver.find_element_by_css_selector(".woocommerce-error li")
coupon_text = coupon.text
assert coupon_text == "Please enter a coupon code."

############### Shop: покупка товара ##########################
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(5)
driver.maximize_window()
# Нажмите на вкладку "Shop"
shop = driver.find_element_by_id('menu-item-40')
shop.click()
driver.execute_script("window.scrollBy(0, 300);")
# Добавьте в корзину книги "HTML5 WebApp Development"
html_5 = driver.find_element_by_css_selector(".post-182 a:nth-child(2)")
html_5.click()
# Перейдите в корзину
#view_basket = driver.find_element_by_css_selector("a[title='View Basket']").click()
#basket = driver.find_element_by_css_selector(".main-nav li:nth-child(6)").click()
basket_2 = driver.find_element_by_css_selector("[title='View your shopping cart']")
basket_2.click()
# Нажмите "PROCEED TO CHECKOUT"
#proceed_to_checkout = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
#(By.CSS_SELECTOR, ".wc-proceed-to-checkout a")))
proceed_to_checkout = driver.find_element_by_css_selector(".wc-proceed-to-checkout a").click()
proceed_to_checkout.click()
# Заполните все обязательные поля
first_name = driver.find_element_by_id("billing_first_name")
#first_name_visible = WebDriverWait(driver, 10).until_not(
#EC.visibility_of_element_located(first_name))
# Заполнение обязательных полей
first_name.send_keys("Anna")
last_name = driver.find_element_by_id("billing_last_name")
last_name.send_keys("Di")
email = driver.find_element_by_name("billing_email")
email.send_keys("test@mail.ru")
phone = driver.find_element_by_name("billing_phone")
phone.send_keys("+79999999999")
country = driver.find_element_by_css_selector('.select2-search input')
country.send_keys("Finland")
select = Select(country)
select.select_by_value("FI")
address = driver.find_element_by_name('billing_address_1')
address.send_keys("Avenue 1")
address_2 = driver.find_element_by_name('billing_address_2')
address_2.send_keys("33")
postcode = driver.find_element_by_name('billing_postcode')
postcode.send_keys("102103")
town = driver.find_element_by_class_name('billing_city')
town.send_keys("Finland")
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(3)
# Выберите способ оплаты "Check Payments"
check_payment = driver.find_element_by_id("payment_method_cheque").click()
#Нажмите Place Order
place_order = driver.find_element_by_id("place_order").click()
# Используя явное ожидание, проверьте что отображается надпись "Thank you. Your order has been received."
#text_after_odrer = driver.find_element_by_class_name("woocommerce-thankyou-order-received")
text_after_odrer = WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-thankyou-order-received"), "Thank you. Your order has been received"))
# Используя явное ожидание, проверьте что в Payment Method отображается текст "Check Payments"
#payment_method = driver.find_element_by_css_selector(".method strong")
payment_method = WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".method strong"), "Check Payments"))
