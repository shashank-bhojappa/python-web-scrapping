import requests
from bs4 import BeautifulSoup

URL = 'https://au.indeed.com/jobs?q=developer&l=Brisbane%20QLD'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='resultsCol')
#print(results.prettify())

job_elems = results.find_all('div', class_='jobsearch-SerpJobCard unifiedRow row result')
for job_elem in job_elems:
     #print(job_elem)
     title_elem = job_elem.find('h2', class_='title')
     company_elem = job_elem.find('span', class_='company')
     location_elem = job_elem.find('span', class_='location accessible-contrast-color-location')

     if None in (title_elem, company_elem, location_elem):
         continue
     print(title_elem.text.strip())
     print(company_elem.text.strip())
     print(location_elem.text.strip())
     print()

filter_jobs = results.find_all('h2',class_='title')

for f_job in filter_jobs:
    link = URL + f_job.find('a')['href']
    print(f_job.text.strip())
    print(f"Apply here: {link}\n")
