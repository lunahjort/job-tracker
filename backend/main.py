from fastapi import FastAPI
from pydantic import BaseModel

class Job(BaseModel):
    company: str
    role: str
    status: str

app = FastAPI()

# fake databas, endast lista
jobs = []

@app.get("/")
def root():
    return {"message": "API is running"}

# GET /jobs
@app.get("/jobs")
def get_jobs():
    return jobs

# POST /jobs
@app.post("/jobs")
def add_job (job: Job):
    jobs.append(job)
    return {"message": "Job added"}