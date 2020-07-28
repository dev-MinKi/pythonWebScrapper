import requests
from bs4 import BeautifulSoup


def extract_get_jobs(url):
  jobs=[]
  result = requests.get(url)
  soup = BeautifulSoup(result.text,"html.parser")
  logo = soup.find("div",{"class":"notice"}).find("span",{"class":"pacifico"}).text
  
  results = soup.find("div",{"class":"container"}).find('table',{"id":"jobsboard"})
  res = results.find_all("tr",{"class":"job"})
  for job_data in res:
    job_dt = job_data.find("td",{"class":"company"})
    link = job_dt.find("a",{"class":"preventLink"})["href"]
    company = job_dt.find("a",{"class":"companyLink"}).text
    title = job_dt.find("h2").text
    job={
      "title":title,
      "link":link,
      "company":company,
      "logo":logo
    }
    jobs.append(job)
  return jobs
    

def re_get_jobs(term):
  url = f"https://remoteok.io/remote-dev+{term}-jobs"
  jobs = extract_get_jobs(url)
  return jobs