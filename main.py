#!/usr/bin/python
from selenium import webdriver
import time
import schedule

# Configuration
# Google form URL
url = ""
# XPath of Name
opt = ""
# Your Name
name = ""
time_trigger = "00:00"
# End Configuration


def name_select(driver, url, xpath="", name=""):
    driver.find_element_by_class_name(
        "quantumWizMenuPaperselectOption").click()
    options = driver.find_element_by_class_name("exportSelectPopup")
    time.sleep(1)
    print("Options:", options)
    if len(xpath) > 0:
        options.find_element_by_xpath(xpath).click()
    else:
        contents = options.find_elements_by_tag_name('div')
        [i.click() for i in contents if i.text == name]


def are_you_feeling_well_today(driver):
    driver.find_element_by_xpath(
        "//*[@id=\"mG61Hd\"]/div/div/div[2]/div[2]/div/div[2]/div/span/div/div[1]/label/div/div[1]/div/div[3]/div").click()


def next_pg1(driver):
    driver.find_element_by_xpath(
        "//*[@id=\"mG61Hd\"]/div/div/div[3]/div/div/div/span/span").click()


def next_pg2(driver):
    driver.find_element_by_xpath(
        "//*[@id=\"mG61Hd\"]/div/div/div[3]/div/div/div[2]/span/span").click()


def submit(driver):
    driver.find_element_by_xpath(
        "//*[@id=\"mG61Hd\"]/div/div/div[3]/div/div/div[2]/span/span").click()


def main():
    print("Awaken")
    driver = webdriver.Chrome()
    driver.get(url)
    name_select(driver, url, name=name)
    are_you_feeling_well_today(driver)
    next_pg1(driver)
    next_pg2(driver)
    submit(driver)
    driver.close()
    print("End")


# Schedule to run main at a certain time
schedule.every().day.at(time_trigger).do(main)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        print("Waiting")
        print("Time now is: ", time.strftime("%H:%M:%S", time.localtime()))
        time.sleep(5)  # wait one minute
