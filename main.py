#!/usr/bin/python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()

# Configuration
# Google form URL
url = ""
# XPath of Name
opt = ""
# Your Name
name = ""
# End Configuration


def name_select(url, xpath="", name=""):
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


def are_you_feeling_well_today():
    driver.find_element_by_xpath(
        "//*[@id=\"mG61Hd\"]/div/div/div[2]/div[2]/div/div[2]/div/span/div/div[1]/label/div/div[1]/div/div[3]/div").click()


def next_pg1():
    driver.find_element_by_xpath(
        "//*[@id=\"mG61Hd\"]/div/div/div[3]/div/div/div/span/span").click()


def next_pg2():
    driver.find_element_by_xpath(
        "//*[@id=\"mG61Hd\"]/div/div/div[3]/div/div/div[2]/span/span").click()


def submit():
    driver.find_element_by_xpath(
        "//*[@id=\"mG61Hd\"]/div/div/div[3]/div/div/div[2]/span/span").click()


def main():
    print("Started at ", time.strftime("%H:%M:%S", time.localtime()))
    driver.get(url)
    name_select(url, name=name)
    are_you_feeling_well_today()
    next_pg1()
    next_pg2()
    submit()
    driver.close()
    print("Stopped at ", time.strftime("%H:%M:%S", time.localtime()))


if __name__ == "__main__":
    main()
