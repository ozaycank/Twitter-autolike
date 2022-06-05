from selenium.webdriver.common.keys import Keys
from selenium import webdriver

import time

browser = webdriver.Firefox()

browser.get("https://twitter.com/")

time.sleep(3)

log_in = browser.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div/span/span")

log_in.click()

time.sleep(3)

username = browser.find_element_by_xpath("//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")

Next = browser.find_element_by_xpath("/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div/span/span")
username.send_keys("YOUR_USERNAME")

time.sleep(2)

Next.click()

time.sleep(2)

password = browser.find_element_by_xpath("/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
logging = browser.find_element_by_xpath("/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div")


time.sleep(2)

password.send_keys("#YOUR_PASSWORD")

time.sleep(2)

logging.click()

time.sleep(2)

search_area = browser.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/label/div[2]/div/input")

search_area.send_keys("#galatasaray")

time.sleep(2)

search_area.send_keys(Keys.ENTER)


time.sleep(5)

#search_button = browser.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/label/div[1]/button")

lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match=False
while(match==False):
    lastCount = lenOfPage
    time.sleep(3)
    lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    if lastCount == lenOfPage:
        match=True


time.sleep(5)

elements = browser.find_elements_by_css_selector(".r-4qtqp9.r-yyyyoo.r-1xvli5t.r-dnmrzs.r-bnwqim.r-1plcrui.r-lrvibr.r-1hdv0qi")


for element in elements:
    try:
        element.click()
        time.sleep(2)
    except Exception:
        print("An Error Occur...")


browser.close()