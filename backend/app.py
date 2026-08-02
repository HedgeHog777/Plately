"""
Commit #1

If you're reading this,
we actually started.
"""
from fastapi import FastAPI

app = FastAPI(
    title="Plately API",
    version="0.0.1"
)

@app.get("/")
def root():
    return {
        "project": "Plately",
        "status": "Building..."
    }
