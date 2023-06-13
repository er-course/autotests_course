# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
sbis_site = 'https://sbis.ru/'
tensor_site = 'https://tensor.ru/about'
try:
    driver.maximize_window()
    driver.get(sbis_site)
    sleep(1)
    assert driver.current_url == sbis_site, 'Неверно открыт сайт'
    contacts = driver.find_element(By.CSS_SELECTOR, ".sbisru-Header__menu-link[href='/contacts']")
    contacts.click()
    sleep(2)

    tensor_logo = driver.find_element(By.CSS_SELECTOR, ".sbisru-Contacts__logo-tensor")
    tensor_logo.click()
    sleep(2)

    handles = driver.window_handles
    driver.switch_to.window(handles[1])
    sleep(1)

    people = driver.find_element(By.CSS_SELECTOR, ".tensor_ru-Index__block4-content " ".tensor_ru-Index__card-title")
    assert people.text == 'Сила в людях', 'Отсутствует блок с таким названием'
    driver.execute_script("return arguments[0].scrollIntoView(true);", people)
    sleep(2)

    about = driver.find_element(By.CSS_SELECTOR, ".tensor_ru-link[href='/about']")
    about.click()
    assert driver.current_url == tensor_site, "Переход по неверной ссылке"
    sleep(2)
finally:
    driver.quit()