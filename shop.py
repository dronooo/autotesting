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
time.sleep(1)
shop_btn = driver.find_element_by_css_selector("#menu-item-40>a").click()
time.sleep(1)
book_btn = driver.find_element_by_css_selector("a[href='http://practice.automationtesting.in/product/html5-forms/']").click()
time.sleep(1)
book_title = driver.find_element_by_css_selector("h1[itemprop='name']")
book_title_text = book_title.text
assert "HTML5 Forms" in book_title_text
driver.quit()


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
time.sleep(1)
shop_btn = driver.find_element_by_css_selector("#menu-item-40>a").click()
time.sleep(1)
html_btn = driver.find_element_by_css_selector("a[href='http://practice.automationtesting.in/product-category/html/']").click()
time.sleep(1)
element_number = driver.find_element_by_css_selector(".cat-item.cat-item-19.current-cat>.count")
element_number_text = element_number.text
assert "3" in element_number_text
driver.quit()


import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
from selenium.webdriver.support.select import Select
driver.get("http://practice.automationtesting.in/")
my_account_btn = driver.find_element_by_css_selector("a[href='http://practice.automationtesting.in/my-account/']").click()
time.sleep(1)
email = driver.find_element_by_css_selector("input#username")
email.send_keys("Andrew@andreeff.com")
password = driver.find_element_by_css_selector("input#password")
password.send_keys("Dron.kolpino")
login_btn = driver.find_element_by_css_selector("input[value='Login']").click()
time.sleep(1)
shop_btn = driver.find_element_by_css_selector("#menu-item-40>a").click()
time.sleep(1)
order_by = driver.find_element_by_css_selector("select.orderby>[value='menu_order']")
order_by_check = order_by.get_attribute("value")
assert order_by_check == "menu_order"
order_by1 = driver.find_element_by_css_selector("select.orderby").click()
order_by2 = driver.find_element_by_css_selector("select.orderby>[value='price-desc']").click
html_btn = driver.find_element_by_css_selector("a[href='http://practice.automationtesting.in/product-category/html/']").click()
time.sleep(1)
element_number = driver.find_element_by_css_selector(".cat-item.cat-item-19.current-cat>.count")
element_number_text = element_number.text
assert "3" in element_number_text
driver.quit()


import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver.get("http://practice.automationtesting.in/")
my_account_btn = driver.find_element_by_css_selector("a[href='http://practice.automationtesting.in/my-account/']").click()
time.sleep(1)
email = driver.find_element_by_css_selector("input#username")
email.send_keys("Andrew@andreeff.com")
password = driver.find_element_by_css_selector("input#password")
password.send_keys("Dron.kolpino")
login_btn = driver.find_element_by_css_selector("input[value='Login']").click()
time.sleep(1)
shop_btn = driver.find_element_by_css_selector("#menu-item-40>a").click()
time.sleep(1)
driver.quit()


import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver.get("http://practice.automationtesting.in/")
my_account_btn = driver.find_element_by_css_selector("a[href='http://practice.automationtesting.in/my-account/']").click()
time.sleep(1)
email = driver.find_element_by_css_selector("input#username")
email.send_keys("Andrew@andreeff.com")
password = driver.find_element_by_css_selector("input#password")
password.send_keys("Dron.kolpino")
login_btn = driver.find_element_by_css_selector("input[value='Login']").click()
time.sleep(1)
shop_btn = driver.find_element_by_css_selector("#menu-item-40>a").click()
time.sleep(1)
order_by = driver.find_element_by_css_selector("select.orderby>[value='menu_order']")
order_by_check = WebDriverWait(driver, 10).until(EC.element_to_be_selected(order_by))
order_by2 = driver.find_element_by_css_selector("select.orderby>[value='price-desc']").click()
order_by2 = driver.find_element_by_css_selector("select.orderby>[value='price-desc']")
order_by_check2 = WebDriverWait(driver, 10).until(EC.element_to_be_selected(order_by2))
driver.quit()


import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver.get("http://practice.automationtesting.in/")
my_account_btn = driver.find_element_by_css_selector("a[href='http://practice.automationtesting.in/my-account/']").click()
time.sleep(1)
email = driver.find_element_by_css_selector("input#username")
email.send_keys("Andrew@andreeff.com")
password = driver.find_element_by_css_selector("input#password")
password.send_keys("Dron.kolpino")
login_btn = driver.find_element_by_css_selector("input[value='Login']").click()
time.sleep(1)
shop_btn = driver.find_element_by_css_selector("#menu-item-40>a").click()
time.sleep(1)
android = driver.find_element_by_css_selector("a[href='http://practice.automationtesting.in/product/android-quick-start-guide/']>h3").click()
price1 = driver.find_element_by_css_selector("del>span.woocommerce-Price-amount.amount")
prise1_get_text = price1.text
assert prise1_get_text == "₹600.00"
price2 = driver.find_element_by_css_selector("ins>span.woocommerce-Price-amount.amount")
prise2_get_text = price2.text
assert prise2_get_text == "₹450.00"
driver.execute_script("window.scrollBy(0, 500);")
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".attachment-shop_single.size-shop_single.wp-post-image"))).click()
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "fullResImage")))
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a.pp_close"))).click()
driver.quit()

import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver.get("http://practice.automationtesting.in/")
my_account_btn = driver.find_element_by_css_selector("a[href='http://practice.automationtesting.in/my-account/']").click()
time.sleep(1)
email = driver.find_element_by_css_selector("input#username")
email.send_keys("Andrew@andreeff.com")
password = driver.find_element_by_css_selector("input#password")
password.send_keys("Dron.kolpino")
login_btn = driver.find_element_by_css_selector("input[value='Login']").click()
time.sleep(1)
driver.execute_script("window.scrollBy(0, 500);")
shop_btn = driver.find_element_by_css_selector("#menu-item-40>a").click()
time.sleep(1)
atb = driver.find_element_by_css_selector("a[data-product_id='182']").click()
time.sleep(2)
item = driver.find_element_by_css_selector("span.cartcontents")
item_text = item.text
assert item_text == "1 Item"
amount = driver.find_element_by_css_selector("a>span.amount")
amount_text = amount.text
assert amount_text == "₹180.00"
basket = driver.find_element_by_css_selector(".wpmenucart-icon-shopping-cart-0").click()
wait = WebDriverWait(driver, 10)
wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "td[data-title='Subtotal']>.woocommerce-Price-amount"), "180.00"))
wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "strong>.woocommerce-Price-amount"), "189.00"))
driver.quit()

import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver.get("http://practice.automationtesting.in/")
my_account_btn = driver.find_element_by_css_selector("a[href='http://practice.automationtesting.in/my-account/']").click()
time.sleep(1)
email = driver.find_element_by_css_selector("input#username")
email.send_keys("Andrew@andreeff.com")
password = driver.find_element_by_css_selector("input#password")
password.send_keys("Dron.kolpino")
login_btn = driver.find_element_by_css_selector("input[value='Login']").click()
time.sleep(1)
shop_btn = driver.find_element_by_css_selector("#menu-item-40>a").click()
time.sleep(1)
driver.execute_script("window.scrollBy(0, 300);")
atb1 = driver.find_element_by_css_selector("a[data-product_id='182']").click()
time.sleep(1)
atb2 = driver.find_element_by_css_selector("a[data-product_id='180']").click()
time.sleep(3)
basket = driver.find_element_by_css_selector(".wpmenucart-icon-shopping-cart-0").click()
time.sleep(3)
del1 = driver.find_element_by_css_selector("a.remove").click()
undo = driver.find_element_by_partial_link_text("Undo?").click()
inp = driver.find_element_by_css_selector("[name='cart[045117b0e0a11a242b9765e79cbf113f][qty]']").clear()
time.sleep(1)
inp = driver.find_element_by_css_selector("[name='cart[045117b0e0a11a242b9765e79cbf113f][qty]']")
inp.send_keys("3")
update_basket = driver.find_element_by_css_selector("input[value='Update Basket']").click()
value1 = inp.get_attribute("value")
time.sleep(1)
assert value1 == "3"
time.sleep(1)
apply_coupon = driver.find_element_by_css_selector("input[name='apply_coupon']").click()
time.sleep(1)
send = driver.find_element_by_css_selector("ul.woocommerce-error>li")
send_text = send.text
assert send_text == "Please enter a coupon code."
driver.quit()


import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver.get("http://practice.automationtesting.in/")
shop_btn = driver.find_element_by_css_selector("#menu-item-40>a").click()
time.sleep(1)
driver.execute_script("window.scrollBy(0, 300);")
atb1 = driver.find_element_by_css_selector("a[data-product_id='182']").click()
time.sleep(1)
basket = driver.find_element_by_css_selector(".wpmenucart-icon-shopping-cart-0").click()
time.sleep(2)
wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".wc-proceed-to-checkout>a"))).click()
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#billing_first_name"))).send_keys("ANDREW")
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#billing_last_name"))).send_keys("ANDREEFF")
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#billing_email"))).send_keys("ANDREW@ANDREEFF.COM")
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#billing_phone"))).send_keys("+70000000000")
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#billing_address_1"))).send_keys("Nevsky pr.")
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#billing_city"))).send_keys("Saint-Petersburg")
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#billing_state"))).send_keys("Saint-Petersburg")
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#billing_postcode"))).send_keys("198000")
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#select2-chosen-1"))).click()
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#s2id_autogen1_search"))).send_keys("Russia")
time.sleep(1)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span.select2-match"))).click()
driver.execute_script("window.scrollBy(0, 600);")
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#payment_method_cheque"))).click()
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#place_order"))).click()
wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "tfoot>tr:nth-child(3)>td"), "Check Payments"))
driver.quit()
