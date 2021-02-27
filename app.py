from fastapi import FastAPI
import datetime

app = FastAPI()
wsb_dictionary={"SPY":0.1}
wise_dictionary={"SPY":0.2}

def wsb_parser(symbol):
    try:
        return wsb_dictionary[symbol]
    except
        return 0

def wise_parser(symbol):
    try:
        return wise_dictionary[symbol]
    except
        return 0
    
skills_dictionary={"WSB":wsb_parser, "WISE":wise_parser}

def dispatch_skill_parser(skill, symbol):
    try:
        return skills_dictionary[skill](symbol)
    except:
        return 0

@app.get("/initialize/{key}")
def initialize(key: str):
    if key == "TheAnswerIs42":
        wsb_dictionary={"SPY":0.1}
        wise_dictionary={"SPY":0.2}
        return {"initialize":"success"}
    else
        wsb_dictionary={}
        wise_dictionary={}
        return {"initialize":"fail"}

@app.get("/")
def main():
    return {
        "message": "Hello, world!"
    }
