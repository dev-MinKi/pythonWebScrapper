import csv

def save_to_file(job_list):
  file = open("jobs.csv",mode="w")
  writer = csv.writer(file)
  writer.writerow(["title","link","company","logo"])
  for jobs in job_list:
    for job in jobs:
      writer.writerow(list(job.values()))
  return