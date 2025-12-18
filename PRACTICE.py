import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
driver.get("https://shkola1sosnovka-r68.gosweb.gosuslugi.ru/")

try:

    #1
    cookie = driver.find_element(By.XPATH, "//*[text()='Я согласен']")
    cookie.click()
    time.sleep(2)

    #2
    more = driver.find_element(By.XPATH, "//*[text()='Подробнее']")
    more.click()
    time.sleep(2)

    #3
    scroll = driver.execute_script("""
                        window.scrollTo({
                                   top: 2500,
                                   behavior: 'smooth'
                                   });
    """)
    time.sleep(5)

    #4
    more1 = driver.find_element(By.XPATH, "//*[text()='Педагогический состав']")
    more1.click()
    time.sleep(2)

    #5
    scroll = driver.execute_script("""
                        window.scrollTo({
                                   top: 4000,
                                   behavior: 'smooth'
                                   });
    """)  
    time.sleep(5)

    #6
    scroll = driver.execute_script("""
                        window.scrollTo({
                                   top: -2000,
                                   behavior: 'smooth'
                                   });
    """)
    time.sleep(5)

    #7
    filtres = driver.find_element(By.XPATH, "//*[text()='Фильтры']")
    filtres.click()
    time.sleep(2)
    teacher = driver.find_element(By.CLASS_NAME, "search-field")
    teacher.click()
    time.sleep(2)
    teacher.send_keys("Иванов")
    time.sleep(2)
    teacher.send_keys(Keys.ENTER)
    time.sleep(5)

    #8
    scroll = driver.execute_script("""
                        window.scrollTo({
                                   top: 200,
                                   behavior: 'smooth'
                                   });
    """)

    time.sleep(5)
    driver.back()
    time.sleep(3)
    driver.back()
    time.sleep(1)
    driver.back()
    time.sleep(5)

    #9
    structure = driver.find_element(By.XPATH, "//*[text()='Структурные подразделения']")
    structure.click()
    time.sleep(3)

    #10
    management = driver.find_element(By.XPATH, "//*[text()='Руководство школы']")
    management.click()
    time.sleep(3)

    scroll = driver.execute_script("""
                        window.scrollTo({
                                   top: 6000,
                                   behavior: 'smooth'
                                   });
    """)  
    time.sleep(5)

    scroll = driver.execute_script("""
                        window.scrollTo({
                                   top: -3500,
                                   behavior: 'smooth'
                                   });
    """)  
    time.sleep(5)
    driver.back()
    time.sleep(5)

    #11
    scroll = driver.execute_script("""
                        window.scrollTo({
                                   top: 350,
                                   behavior: 'smooth'
                                   });
    """)  
    time.sleep(5)

    metodic = driver.find_element(By.XPATH, "//*[text()='Методический совет']")
    metodic.click()
    time.sleep(5)

    scroll = driver.execute_script("""
                        window.scrollTo({
                                   top: 6000,
                                   behavior: 'smooth'
                                   });
    """)  
    time.sleep(5)

    scroll = driver.execute_script("""
                        window.scrollTo({
                                   top: -6000,
                                   behavior: 'smooth'
                                   });
    """)  
    time.sleep(5)
    driver.back()
    time.sleep(5)

    #12

    pedagog = driver.find_element(By.XPATH, "//*[text()='Педагогический совет']")
    pedagog.click()
    time.sleep(3)

    scroll = driver.execute_script("""
                        window.scrollTo({
                                   top: 6000,
                                   behavior: 'smooth'
                                   });
    """)  
    time.sleep(5)

    scroll = driver.execute_script("""
                        window.scrollTo({
                                   top: -6000,
                                   behavior: 'smooth'
                                   });
    """)  
    time.sleep(5)
    driver.back()
    time.sleep(5)

    #13

    shoolsovet = driver.find_element(By.XPATH, "//*[text()='Управляющий совет школы']")
    shoolsovet.click()
    time.sleep(3)

    scroll = driver.execute_script("""
                        window.scrollTo({
                                   top: 6000,
                                   behavior: 'smooth'
                                   });
    """)  
    time.sleep(5)

    scroll = driver.execute_script("""
                        window.scrollTo({
                                   top: -6000,
                                   behavior: 'smooth'
                                   });
    """)  
    time.sleep(5)
    driver.back()
    time.sleep(5)
    driver.back()
    time.sleep(5)

    #14

    scroll = driver.execute_script("""
                        window.scrollTo({
                                   top: 1000,
                                   behavior: 'smooth'
                                   });
    """)  
    time.sleep(5)


    swipe = driver.find_element(By.CLASS_NAME, "swiper-button-next")
    swipe.click()
    time.sleep(5)

    swipe1 = driver.find_element(By.CLASS_NAME, "swiper-button-prev")
    swipe1.click()
    time.sleep(5)

    #15

    scroll = driver.execute_script("""
                        window.scrollTo({
                                   top: -4000,
                                   behavior: 'smooth'
                                   });
    """)  
    time.sleep(3)

    #16
    driver.back()
    time.sleep(4)

    scroll = driver.execute_script("""
                        window.scrollTo({
                                   top: 12000,
                                   behavior: 'smooth'
                                   });
    """)  
    time.sleep(3)

    studues = driver.find_element(By.XPATH, "//*[text()='Независимая оценка качества условий образовательной деятельности']")
    studues.click()
    time.sleep(3)

    #17
    scroll = driver.execute_script("""
                        window.scrollTo({
                                   top: 1300,
                                   behavior: 'smooth'
                                   });
    """)  
    time.sleep(3)

    weekdays = driver.find_element(By.XPATH, "//*[text()='Каникулы']")
    weekdays.click()
    time.sleep(3)

    #18

    driver.back()
    time.sleep(3)
    dnevnik = driver.find_element(By.XPATH, "//*[text()='Дневник']")
    dnevnik.click()
    time.sleep(3)

    scroll = driver.execute_script("""
                        window.scrollTo({
                                   top: 100,
                                   behavior: 'smooth'
                                   });
    """)  
    time.sleep(2)

    scroll = driver.execute_script("""
                        window.scrollTo({
                                   top: -100,
                                   behavior: 'smooth'
                                   });
    """)
    time.sleep(2)
    driver.back()
    time.sleep(3)
    #19

    works = driver.find_element(By.XPATH, "//*[text()='Деятель']")
    works.click()
    time.sleep(3)

    scroll = driver.execute_script("""
                        window.scrollTo({
                                   top: 100,
                                   behavior: 'smooth'
                                   });
    """)  
    time.sleep(2)

    scroll = driver.execute_script("""
                        window.scrollTo({
                                   top: -100,
                                   behavior: 'smooth'
                                   });
    """)
    time.sleep(2)
    driver.back()




finally:

    time.sleep(5)
    driver.quit()
