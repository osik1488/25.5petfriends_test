import pytest
from WebDriverWait import element_has_css_class
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Chrome('./chromedriver.exe')
   # Переходим на страницу авторизации
   pytest.driver.get('http://petfriends.skillfactory.ru/login')
   yield

   pytest.driver.quit()


def test_show_my_pets():
   # Вводим email

   pytest.driver.find_element(By.ID,'email').send_keys('jsuiai@mail.com')
   # Вводим пароль
   pytest.driver.find_element(By.ID,'pass').send_keys('1234')
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element(By.CSS_SELECTOR,'button[type="submit"]').click()



   pytest.driver.implicitly_wait(3)
   images = pytest.driver.find_elements(By.XPATH,'body/div[1]/div[1]/div[2]/div[7]/div[1]/img[1]')#СЮДА НУЖНО ПОСТАВИТЬ ОЖИДАЕМЫЕ РЕЗУЛЬТАТЫЪ
   pytest.driver.implicitly_wait(3)
   names = pytest.driver.find_elements(By.XPATH,'body/div[1]/div[1]/div[2]/div[7]/div[2]/h5[1]')
   pytest.driver.implicitly_wait(3)
   age = pytest.driver.find_elements(By.XPATH,'body/div[1]/div[1]/div[2]/div[7]/div[2]/p[1]')


   pytest.driver.find_element(By.CSS_SELECTOR, 'div#navbarNav > ul > li > a').click()
   WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, "html > body > div > div > div > h2")))
   pytest.driver.find_element(By.CSS_SELECTOR, "html > body > nav > div:nth-of-type(2) > button").click()

   for i in range(len(names)):
      assert images[i].get_attribute('src') != ''
      assert names[i].text != ''
      assert descriptions[i].text != ''
      assert ', ' in descriptions[i]
      parts = descriptions[i].text.split(", ")
      assert age[i].text != ''
      assert ', ' in age[i]
      assert len(parts[0]) > 0
      assert len(parts[1]) > 0
