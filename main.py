#! /usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import json


options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)
urlList = []

def getCompany():
    print('Input Greenhouse.io job board page:')
    careerPage = input()
    if not re.match(r'https://boards.greenhouse.io/.*', careerPage):
        print("Invalid - Program takes only https://boards.greenhouse.io/XYZ formats.")
        return None
    else:
        return careerPage

def getOpenings(jobBoard):
    driver.get(jobBoard)
    jobLinks = driver.find_elements(By.TAG_NAME, 'a')
    for link in jobLinks:
        href = link.get_attribute('href')
        if href and 'job' in href:
            urlList.append(href)
    return urlList

def main(urlList):
    for job_link in urlList:
        driver.get(job_link)
        job_name = driver.find_element(By.XPATH, "//*[@id='header']/h1")
        job_name_text = job_name.text
        script_tag = driver.find_element(By.XPATH, "//script[@type='application/ld+json']")
        script_content = script_tag.get_attribute('innerHTML')
        json_data = json.loads(script_content)
        date_posted = json_data.get('datePosted')
        print(f'\n>>> {job_name_text}: --- posted: {date_posted} \n>>> {job_link}')
    driver.quit()

careerPage = getCompany()
getOpenings(careerPage)
main(urlList)
