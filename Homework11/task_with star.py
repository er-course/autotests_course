# Перейти на  https://sbis.ru/
# В Footer'e найти "Скачать СБИС"
# Перейти по ней
# Скачать СБИС Плагин для вашей ОС в папку с данным тестом
# Убедиться, что плагин скачался
# Вывести на печать размер скачанного файла в мегабайтах
# Для сдачи задания пришлите код и запись с экрана прохождения теста
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import os

site = 'https://sbis.ru'

options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {"download.default_directory": r"C:\autotests_course\Homework11",
                                          "safebrowsing.enabled": True})
driver = webdriver.Chrome(options=options)
try:
    driver.maximize_window()
    driver.get(site)
    sleep(3)
    footer = driver.find_element(By.CSS_SELECTOR, '.sbisru-Footer__container')
    driver.execute_script("return arguments[0].scrollIntoView(true);", footer)
    sleep(2)
    download_link = driver.find_element(By.XPATH, "//a[contains(@class, 'sbisru-Footer__link') and "
                                                  "contains(text(), 'Скачать СБИС')]")
    download_link.click()
    sleep(3)
    plugin_link = driver.find_element(By.CSS_SELECTOR, '[data-id="plugin"]')
    plugin_link.click()
    sleep(1)
    download_plugin = driver.find_element(By.CSS_SELECTOR, '[data-for="plugin"] .sbis_ru-DownloadNew-loadLink')
    download_plugin.click()
    sleep(3)
    setup_file = 'sbisplugin-setup-web.exe'
    assert Path(setup_file).exists(), 'Файл не загружен'
    print(f' Размер скачанного файла {round(os.path.getsize(setup_file) / 1048576, 2)} мб')
finally:
    driver.quit()
