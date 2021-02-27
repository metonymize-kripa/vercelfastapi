from fastapi import FastAPI
import datetime

app = FastAPI()

wsb_dictionary={"SPY":0.1}
wise_dictionary={"SPY":0.2}
    
@app.get("/parse/{parameter}")
def parse(parameter: str):
    parsed_parameter_list = parameter.strip().split()
    num_parameters_parsed = len(parsed_parameter_list)
    
    return {
        "parameter": parameter,
        "datetime": datetime.datetime.now().time()
    }

@app.get("/")
def main():
    return {
        "message": "Hello, world!"
    }
