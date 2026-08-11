from fastapi import FastAPI
app = FastAPI(title="Document Service")
@app.get("/")
def root():
    return {"service": "document-service"}