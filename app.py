from fastapi import FastAPI
from fastapi.responses import JSONResponse
from main import run_analysis

app = FastAPI()

@app.get("/analyze")
def analyze():
    results = run_analysis()
    return JSONResponse(content=results, media_type="application/json; charset=utf-8")

