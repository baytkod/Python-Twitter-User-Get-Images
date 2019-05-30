from urllib.request import urlretrieve  # Python 3
import random
from selenium import webdriver
import time
from selenium.webdriver.remote.webelement import WebElement

browser = webdriver.Firefox(executable_path=r'C:\Users\Muhammed\Desktop\geckodriver.exe')

def scroll():
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)

def image():
    count = 0
    for user in browser.find_elements_by_xpath("//div[starts-with(@id,'stream-item-user-')]/div[1]/div[1]/a[1]/img[1]"):
        count += 1
        src = user.get_attribute('src').split('bigger')
        kod = user.get_attribute('src').split('/')
        img = str(src[0])+str('400x400')+str(src[1])
        print(str(count)+" "+str(src[0])+str('400x400')+str(src[1]))
        urlretrieve(img, str('uploads/')+str(random.randint(1,100))+str(kod[5]))
        if int(count) == 100:
            time.sleep(1)
            image()

browser.get('https://www.twitter.com/login')
time.sleep(2)

username = browser.find_element_by_class_name("js-username-field")
password = browser.find_element_by_class_name("js-password-field")

username.send_keys("mamMmia_")
password.send_keys("xxxxxxxx")

time.sleep(1)
login_btn = browser.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/div[2]/button')
login_btn.click()
time.sleep(2)

users = [
    "Ayşe",
    "Özlem",
    "Ahsen",
    "Ahu",
    "Gül",
    "Asude",
    "Begüm",
    "Bade",
    "Bahar",
    "Balın",
    "Banu",
    "Başak",
    "Behin",
    "Belgi",
    "Belgin",
    "Belkıs",
    "Belma",
    "Belur",
    "Benan",
    "Bennur",
    "Bengi",
    "Bengisu",
    "Beren",
    "Berfu",
    "Beril",
    "Belen",
    "Berrak",
    "Berna",
    "Beste",
    "Betül",
    "Beyza",
    "Büşra",
    "Burçin",
]

for user in users:
    search_text = browser.find_element_by_class_name('search-input')
    search_text.clear()
    time.sleep(1)
    search_text.send_keys(user)

    search_btn = browser.find_element_by_xpath('//*[@id="global-nav-search"]/span/button')
    search_btn.click()
    time.sleep(4)

    kisiler_btn = browser.find_element_by_xpath('//*[@id="page-container"]/div[1]/div[2]/div/ul/li[3]/a')
    kisiler_btn.click()
    time.sleep(3)

    for x in range(0, 30):
        scroll()
        print(x)
        time.sleep(1)
        if x == 6:
            image()
            break