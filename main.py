from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()

@app.get("/")
def home():
    return {"status": "running"}

@app.get("/pay")
def pay(pa: str, pn: str, am: int):
    upi_url = f"upi://pay?pa={pa}&pn={pn}&am={am}&cu=INR"
    return RedirectResponse(url=upi_url)