import requests
from bs4 import BeautifulSoup


def get_last_page(url):
  result = requests.get(url)
  soup = BeautifulSoup(result.text, "html.parser")
  s_pagination = soup.find("div",{"class":"s-pagination"})
  links=s_pagination.find_all("a")
  pages=[]
  for link in links[:-1]:
    pages.append(int(link.find("span").string))
  max_page=pages[-1]
  return max_page

def extract_get_jobs(last_page,url):
  jobs=[]
  res = requests.get(url)
  sop = BeautifulSoup(res.text,"html.parser")
  logo = sop.find("div",{"class":"-main"}).find("a",{"class":"-logo"}).find("span").text
  for page in range(last_page):
    result = requests.get(f"{url}&pg={page+1}")
    print(f"Scrapping page {page}")
    soup = BeautifulSoup(result.text,"html.parser")
    results=soup.find("div",{"class":"listResults"})
    result = results.find_all("div",{"class":"grid--cell"})
    for job_data in result:
      job = job_data.find("a",{"class":"s-link"})
      if job==None:
        continue;
      title = job["title"]
      link = job["href"]
      company = job_data.find("h3",{"class":"fc-black-700"}).find("span").text
      
      data={
        "title":title,
        "link":link,
        "company":company,
        "logo":logo
      }
      jobs.append(data)
  return jobs

def st_get_jobs(term):
  url = f"https://stackoverflow.com/jobs?r=true&q={term}"
  last_page=get_last_page(url)
  jobs = extract_get_jobs(last_page,url)
  return jobs
