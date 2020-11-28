import requests
from bs4 import BeautifulSoup

URL = 'http://pythonjobs.github.io/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='main')
#print(results.prettify())

job_elems = results.find_all('div', class_='job')
for job_elem in job_elems:
     #print(job_elem)
     title_elem = job_elem.find('h1')
     location_elem = job_elem.find('span', class_='info')

     if None in (title_elem, company_elem, location_elem):
         continue
     print(title_elem.text.strip())
     print(location_elem.text.strip())
     print()

filter_jobs = results.find_all('h1',string=lambda text: "developer" in text.lower())

for f_job in filter_jobs:
    link = URL + f_job.find('a')['href']
    print(f_job.text.strip())
    print(f"Apply here: {link}\n")
