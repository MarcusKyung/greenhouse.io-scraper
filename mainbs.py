import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import time
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
    response = requests.get(jobBoard)
    soup = BeautifulSoup(response.text, 'html.parser')
    jobLinks = soup.select('div.opening a')
    for link in jobLinks:
        href = 'https://boards.greenhouse.io' + link['href']
        urlList.append(href)
    return urlList

def main(urlList):
    try:
        # Iterate through urlList, extract text and datePosted from JSON
        for job_link in urlList:
            response = requests.get(job_link)
            soup = BeautifulSoup(response.text, 'html.parser')
            job_name = soup.select_one("div#header h1").text
            job_location = soup.select_one("div.location").text.strip()
            try:
                script_content = soup.find("script", {"type": "application/ld+json"}).string
                json_data = json.loads(script_content)
                date_posted = json_data.get('datePosted')
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
                print(f'\n>>> {job_name}: --- posted: {color_code}{date_posted}{color.END} \n>>> Location: {job_location} \n>>> {job_link}')
            except AttributeError: 
                print(f'\n>>> {job_name}: --- posted: {color.RED}No Post Date Available{color.END} \n>>> Location: {job_location} \n>>> {job_link}')
    finally:
        print('------------------------')

careerPage = getCompany()
start_bs = time.time()
getOpenings(careerPage)
main(urlList)
end_bs = time.time()
bs_time = end_bs - start_bs
print(f'Beautiful Soup Script took {bs_time} seconds to execute.')
