###################################   Registration_login: регистрация аккаунта   ########################################
import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://practice.automationtesting.in/")
my_account_btn = driver.find_element_by_css_selector("a[href='http://practice.automationtesting.in/my-account/']").click()
time.sleep(1)
email = driver.find_element_by_css_selector("input#reg_email")
email.send_keys("Andrew@andreeff.com")
password = driver.find_element_by_css_selector("input#reg_password")
password.send_keys("Dron.kolpino")
register_btn = driver.find_element_by_css_selector("input[value='Register']").click()
time.sleep(3)
driver.quit()

######################################   Registration_login: логин в систему  #####################################
import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://practice.automationtesting.in/")
my_account_btn = driver.find_element_by_css_selector("a[href='http://practice.automationtesting.in/my-account/']").click()
time.sleep(1)
email = driver.find_element_by_css_selector("input#username")
email.send_keys("Andrew@andreeff.com")
password = driver.find_element_by_css_selector("input#password")
password.send_keys("Dron.kolpino")
login_btn = driver.find_element_by_css_selector("input[value='Login']").click()
logout_title = driver.find_element_by_css_selector("a[href='http://practice.automationtesting.in/my-account/customer-logout/']")
logout_title_text = logout_title.text
assert "Logout" in logout_title_text
time.sleep(3)
driver.quit()