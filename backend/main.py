from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from pydantic import BaseModel
from database import engine, SessionLocal
from models import Job as JobModel, Base

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

# databas (db session)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Job(BaseModel):
    company: str
    role: str
    status: str

@app.get("/")
def root():
    return {"message": "API is running"}

# GET /jobs
@app.get("/jobs")
def get_jobs(db: Session = Depends(get_db)):
    return db.query(JobModel).all()

# POST /jobs (skapa ID)
@app.post("/jobs")
def add_job (job: Job, db: Session = Depends(get_db)):
    db_job = JobModel(
        company=job.company,
        role=job.role,
        status=job.status
    )
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job

# DELETE /jobs
@app.delete("/jobs/{job_id}")
def delete_job(job_id: int, db: Session = Depends(get_db)):
    job = db.query(JobModel).filter(JobModel.id == job_id).first()
    if job:
        db.delete(job)
        db.commit()
        return {"message": "Job deleted"}
    return {"error": "Job not found"}

# UPDATE /jobs
@app.put("/jobs/{job_id}")
def update_job(job_id: int, updated_job: Job, db: Session = Depends(get_db)):
    job = db.query(JobModel).filter(JobModel.id == job_id).first()

    if job:
        job.company = updated_job.company
        job.role = updated_job.role
        job.status = updated_job.status

        db.commit()
        db.refresh(job)
        return job
    return {"error": "Job not found"}