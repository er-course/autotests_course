# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from time import sleep

site = 'http://fix-online.sbis.ru/'
user_login, user_password = 'selenium_test', 'Selenium_test123'
person = 'Селениум'
text = 'Привет!'
driver = webdriver.Chrome()
driver.maximize_window()
try:

    driver.get(site)
    sleep(2)
    login = driver.find_element(By.NAME, "Login")
    login.send_keys(user_login, Keys.ENTER)
    assert login.get_attribute('value') == user_login, "Введен неверный логин"
    password = driver.find_element(By.NAME, "Password")
    password.send_keys(user_password, Keys.ENTER)
    assert password.get_attribute('value') == user_password,  "Введен неверный пароль"
    sleep(5)

    contacts = driver.find_element(By.CSS_SELECTOR, '.NavigationPanels-Accordion__title')
    contacts.click()
    sleep(2)
    contact_btn = driver.find_element(By.CSS_SELECTOR, '.NavigationPanels-SubMenu__headTitle')
    contact_btn.click()
    sleep(2)
    plus_btn = driver.find_element(By.CSS_SELECTOR, '.icon-RoundPlus')
    plus_btn.click()
    sleep(2)

    search = driver.find_element(By.CLASS_NAME, 'controls-Search__nativeField_caretEmpty')
    sleep(2)
    search.send_keys(person, Keys.ENTER)
    sleep(2)
    receiver = driver.find_element(By.CSS_SELECTOR, '[data-qa="person-Information__fio"]')
    receiver.click()
    sleep(1)

    msg_box = driver.find_element(By.CSS_SELECTOR, '.textEditor_Viewer__Paragraph')
    sleep(2)
    msg_box.send_keys(text)
    sleep(2)
    msg_box = driver.find_element(By.CSS_SELECTOR, '.icon-BtArrow')
    msg_box.click()
    sleep(2)
    message = driver.find_element(By.CSS_SELECTOR, '.msg-entity-text')
    assert message.text == text, 'Не удалось найти отправленное сообщения'

    action_chains = ActionChains(driver)
    action_chains.move_to_element(message)
    action_chains.context_click(message)
    action_chains.perform()
    sleep(2)
    delete_msg = driver.find_element(By.CSS_SELECTOR, '[title="Перенести в удаленные"]')
    delete_msg.click()
    sleep(1)

    assert driver.find_elements(By.CSS_SELECTOR, '.msg-dialogs-item__content-inner') != message, 'Сообщение не удалено!'
    sleep(2)
finally:
    driver.quit()
