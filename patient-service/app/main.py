from fastapi import FastAPI
app = FastAPI(title="Patient Service")
@app.get("/")
def root():
    return {"service": "patient-service"}