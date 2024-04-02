#! /usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta
import re
import json

class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)
urlList = []

def getCompany():
    while True:
        print('Input Greenhouse.io job board page:')
        careerPage = input()
        if re.match(r'https://boards.greenhouse.io/.*', careerPage):
            return careerPage
        else:
            print("Invalid - Program takes only https://boards.greenhouse.io/XYZ formats.")

def getOpenings(jobBoard):
    driver.get(jobBoard)
    jobLinks = driver.find_elements(By.TAG_NAME, 'a')
    for link in jobLinks:
        href = link.get_attribute('href')
        if href and 'job' in href:
            urlList.append(href)
    return urlList

def main(urlList):
    try:
        # Iterate through urlList, extract text and datePosted from JSON
        for job_link in urlList:
            driver.get(job_link)
            job_name = driver.find_element(By.XPATH, "//*[@id='header']/h1")
            job_name_text = job_name.text
            job_location = driver.find_element(By.XPATH, "//*[@id='header']/div")
            job_location_text = job_location.text
            script_tag = driver.find_element(By.XPATH, "//script[@type='application/ld+json']")
            script_content = script_tag.get_attribute('innerHTML')
            json_data = json.loads(script_content)
            date_posted = json_data.get('datePosted')

            # Color Coding
            current_date = datetime.now().date()
            difference = current_date - datetime.strptime(date_posted, "%Y-%m-%d").date()
            one_week = timedelta(weeks=1)
            two_weeks = timedelta(weeks=2)
            if difference <= one_week:
                color_code = color.GREEN
            elif difference <= two_weeks:
                color_code = color.YELLOW
            else:
                color_code = color.RED

            # Print Results
            print(f'\n>>> {job_name_text}: --- posted: {color_code}{date_posted}{color.END} \n>>> Location: {job_location_text} \n>>> {job_link}')
    except Exception as e:
        print("Error:", e)
    finally:
        print('------------------------')
        driver.quit()

careerPage = getCompany()
getOpenings(careerPage)
main(urlList)
