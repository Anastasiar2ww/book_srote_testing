
############ РЕГИСТРАЦИЯ АККАУНТА ###############
'''
1. Откройте http://practice.automationtesting.in/
2. Нажмите на вкладку "My Account Menu"
3. В разделе "Register", введите email для регистрации
4. В разделе "Register", введите пароль для регистрации
• составьте такой пароль, чтобы отобразилось "Medium" или "Strong", иначе регистрация не выполнится
• почту и пароль сохраните, потребуюутся в дальнейшем
5. Нажмите на кнопку "Register"
'''

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(6)
driver.maximize_window()

# Нажмите на вкладку "My Account Menu"
my_account = driver.find_element_by_id("menu-item-50").click()
# В разделе "Register", введите email для регистрации
email_register = driver.find_element_by_id("reg_email")
email_register.send_keys("test123123test@mail.ru")
#В разделе "Register", введите пароль для регистрации
password_register = driver.find_element_by_id("reg_password")
password_register.send_keys("!!11@22@76##Tq1")
time.sleep(15)
#Нажмите на кнопку Register
register = driver.find_element_by_css_selector('input[value="Register"]').click()


################### ЛОГИН В СИСТЕМУ #######################

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

'''
1. Откройте http://practice.automationtesting.in/
2. Нажмите на вкладку "My Account Menu"
3. В разделе "Login", введите email для логина # данные можно взять из предыдущего теста
4. В разделе "Login", введите пароль для логина # данные можно взять из предыдущего теста
5. Нажмите на кнопку "Login"
6. Добавьте проверку, что на странице есть элемент "Logout"
'''

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(6)
driver.maximize_window()

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
# Добавьте проверку, что на странице есть элемент "Logout"
#logout = driver.find_element_by_css_selector(".woocommerce li:nth-child(6)")
logout_visible = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
(By.CSS_SELECTOR, ".woocommerce li:nth-child(6)")))


