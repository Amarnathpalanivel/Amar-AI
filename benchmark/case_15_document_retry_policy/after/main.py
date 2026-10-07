from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()

def retry_delay(attempt: int, base: float = 0.25):
    attempt = max(attempt, 0)
    # Cap exponential backoff so a transient failure does not delay work indefinitely.
    return min(base * (2 ** attempt), 8.0)

@app.get("/jobs/{job_id}/retry-delay")
def job_retry_delay(job_id: str, attempt: int = 0):
    job = job_repository.get(job_id)
    if job is None:
        raise HTTPException(status_code=404, detail="Job not found")
    return {"delay": retry_delay(attempt)}

def schedule_retry(job_id: str, attempt: int):
    return queue.enqueue(job_id, delay=retry_delay(attempt))

def job_status(job_id: str):
    return job_repository.status(job_id)

def ready():
    return {"ready": True}
