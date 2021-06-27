from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
for i in range(1,3):
    driver.get("https://my-subs.co/versions-2086-%s-23-south-park-subtitles" % i)
    assert "South Park" in driver.title
    driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div[2]/div[2]/a').click()



driver.close()
