from fastapi import FastAPI
import datetime

app = FastAPI()
wsb_dictionary={"SPY":0.1}
wise_dictionary={"SPY":0.2}


@app.get("/")
def main():
    return {
        "message": "Hello, world!"
    }

