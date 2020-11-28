import requests
from bs4 import BeautifulSoup

URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
#print(soup)

#Find Elements by ID
results = soup.find(id='SearchResults')
#print(results.prettify())
job_elems = results.find_all('section', class_='card-content')
for job_elem in job_elems:
    title_elem = job_elem.find('h2', class_='title')
    company_elem = job_elem.find('div', class_='company')
    location_elem = job_elem.find('div', class_='location')
    if None in (title_elem, company_elem, location_elem):
        continue
    print(title_elem.text.strip())
    print(company_elem.text.strip())
    print(location_elem.text.strip())
    print()

#Find Elements by Class Name and Text Content
#python_jobs = results.find_all('h2', string='Python Developer')

#Pass a Function to a Beautiful Soup Method
filter_jobs = results.find_all('h2',string=lambda text: "manager" in text.lower())

for f_job in filter_jobs:
    link = f_job.find('a')['href']
    print(f_job.text.strip())
    print(f"Apply here: {link}\n")
