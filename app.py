from fastapi import FastAPI

app = FastAPI(title="AWS DevOps Project")


@app.get("/")
def home():
    return {
        "message": "AWS DevOps Project is running!"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
 
