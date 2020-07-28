from flask import Flask, render_template, request, redirect, send_file
from stack_scrapper import st_get_jobs
from wework_scrapper import ww_get_jobs
from remote_scrapper import re_get_jobs
from exporter import save_to_file
app=Flask("LastProject")

db={}
@app.route("/")
def home():
  return render_template("home.html")
term=""
@app.route("/search")
def search():
  job_list=[]
  result_total_job=0
  term = request.args.get("term")
  if term:
    term = term.lower()
    existingJobs = db.get(term)
    if existingJobs:
      job_db = existingJobs
      for job_ in job_db:
        length=len(job_)
        result_total_job=result_total_job+length
    else:
      jobs=st_get_jobs(term)
      st_total_job = len(jobs)
      job_list.append(jobs)
      job_data=ww_get_jobs(term)
      ww_total_job = len(job_data)
      job_list.append(job_data)
      re_job = re_get_jobs(term)
      job_list.append(re_job)
      re_total_job = len(re_job)
      job_db=job_list
      db[term]=job_db
      result_total_job = st_total_job+ww_total_job+re_total_job
  else:
    return redirect("/")
  return render_template("search.html",
  result_total_job=result_total_job,
  job_list=job_db,
  term=term)
@app.route("/export")
def export():
  try:
    word = request.args.get("term")
    word = word.lower()
    if not word:
      raise Exception()
    jobs = db.get(word)
    if not jobs:
      raise Exception()
    save_to_file(jobs)
    return send_file("jobs.csv")
  except:
    return redirect("/")


app.run(host="0.0.0.0")