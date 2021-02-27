from fastapi import FastAPI
import datetime

app = FastAPI()

@app.get("/example/{parameter}")
def example(parameter: str):
    parsed_parameter_list = parameter.strip().split()
    num_parameters_parsed = len(parsed_parameter_list)
    
    if  num_parameters_parsed == 2:
        parsed_symbol = parsed_parameter_list[0].upper()
        parsed_skill = parsed_parameter_list[1].upper()
    else:
        return {"symbol": "no symbol",
                "skill": "no skill",
                "datetime": "no time"}
        
    try:
        return {"symbol": parsed_symbol,
                "skill": parsed_skill,
                "datetime": datetime.datetime.now().time()}
    except:
        return {"symbol": "no symbol",
                "skill": "no skill",
                "datetime": "no time"}
    """
    return {
        "parameter": parameter,
        "datetime": datetime.datetime.now().time()
    }
    """

@app.get("/")
def main():
    return {
        "message": "Hello, world!"
    }
