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

# uppdaterad POST /jobs (skapa ID)
@app.post("/jobs")
def add_job (job: Job):
    new_job = job.model_dump()
    new_job["id"] = len(jobs) + 1
    jobs.append(new_job)
    return {"message": "Job added"}

# DELETE /jobs
@app.delete("/jobs/{job_id}")
def delete_job(job_id: int):
    for job in jobs:
        if job["id"] == job_id:
            jobs.remove(job)
            return {"message": "Job deleted"}
    return {"error": "Job not found"}

# UPDATE /jobs kommer här nedan