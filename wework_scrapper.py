import requests
from bs4 import BeautifulSoup


def extract_get_jobs(url):
  jobs=[]
  result = requests.get(url)
  soup = BeautifulSoup(result.text,"html.parser")
  logo =soup.find("header",{"id":"main-header"}).find("h1").text
  results = soup.find("section",{"id":"category-2"}).find("article")
  result = results.find("ul")
  res = result.find_all("li")
  for job_data in res[:-1]:
    link = job_data.find("a")["href"]
    company = job_data.find("span",{"class":"company"}).text
    title = job_data.find("span",{"class":"title"}).text
    job={
      "title":title,
      "link":link,
      "company":company,
      "logo":logo
    }
    jobs.append(job)
  return jobs

def ww_get_jobs(term):
  url = f"https://weworkremotely.com/remote-jobs/search?term={term}"
  jobs = extract_get_jobs(url)
  return jobs