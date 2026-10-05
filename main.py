from bs4 import BeautifulSoup
import requests
import pandas as pd

def fetch_link(url):
   res = requests.get(url, timeout=10)
   res.raise_for_status()
   return BeautifulSoup(res.text, 'html.parser')
   

def get_text(parent, selector):
    element = parent.select_one(selector)
    return element.text.strip() if element else None

def get_attribute(parent, selector, attribute):
    element = parent.select_one(selector)
    return element[attribute] if element and attribute in element.attrs else None

def extract_jobs(soup):
  jobs = []

  for element in soup.find_all('div', class_='card-content'):
    title = get_text(element, 'h2.title')
    company = get_text(element, 'h3.company')
    location = get_text(element, 'p.location')
    learn_link = get_attribute(element, 'a.card-footer-item', 'href')
    jobs.append({
        'title': title,
        'company': company,
        'location': location,
        'learn_link': learn_link
    })
  return jobs


if __name__ == '__main__':
   link = 'https://realpython.github.io/fake-jobs/'
   soup = fetch_link(link)
   jobs = extract_jobs(soup)
   if not jobs:
       print("No jobs found.")
   else:
         df = pd.DataFrame(jobs)
         df.to_csv('jobs.csv', index=False)
         print("Jobs data saved to jobs.csv")