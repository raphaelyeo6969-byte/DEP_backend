from fastapi import FastAPI, Header, HTTPException

app = FastAPI()

API_KEY = "test123"


@app.get("/")
def home():
    return {"status": "Nesso API is running"}


@app.post("/readings")
def receive_readings(data: dict, x_api_key: str = Header()):
    if x_api_key != API_KEY:
        raise HTTPException(
            status_code=401,
            detail="Invalid API key"
        )

    print(data)

    return {
        "status": "received"
    }