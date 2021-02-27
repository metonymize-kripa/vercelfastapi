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
    
@app.get("/parse/{parameter}")
def parse(parameter: str):
    parsed_parameter_list = parameter.strip().split()
    num_parameters_parsed = len(parsed_parameter_list)
    
    if  num_parameters_parsed == 2:
        parsed_symbol = parsed_parameter_list[0].upper()
        parsed_skill = parsed_parameter_list[1].upper()
        skill_returned_value = dispatch_skill_parser(parsed_skill, parsed_symbol)
    else:
        return {"symbol": "no symbol",
                "skill": "no skill",
                "skill_output": "no output",
                "datetime": "no time"}
        
    try:
        return {"symbol": parsed_symbol,
                "skill": parsed_skill,
                "skill_output": skill_returned_value,
                "datetime": datetime.datetime.now().time()}
    except:
        return {"symbol": "no symbol",
                "skill": "no skill",
                "skill_output": "no output",
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
