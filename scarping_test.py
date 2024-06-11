from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.onlinejobs.ph/jobseekers/jobsearch').text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('div', class_ = 'jobpost-cat-box latest-job-post card-hover-default')
for job in jobs:
    jobT = job.find('h4', class_ = 'fs-16 fw-700').text.replace(' ','')
    type = job.find('span', class_ = 'badge full-time mt-md-0').text.replace(' ','')

    print(f'''
    CompanyJob: {jobT}
    JobType: {type}
    ''')