from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# fake databas, endast lista
jobs = []

class Job(BaseModel):
    company: str
    role: str
    status: str

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

# UPDATE /jobs
@app.put("/jobs/{job_id}")
def update_job(job_id: int, updated_job: Job):
    for job in jobs:
        if job["id"] == job_id:
            job["company"] = updated_job.company
            job["role"] = updated_job.role
            job["status"] = updated_job.status
            return job
    return {"error": "Job not found"}