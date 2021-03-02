from fastapi import FastAPI
import datetime

app = FastAPI()

wsb_dictionary={"SPY":0.1}
wise_dictionary={"SPY":0.2}
div2_dictionary={"SPY":-1}

def wsb_parser(symbol):
    initialize()
    try:	
        return wsb_dictionary[symbol]	
    except:	
        return -1	

def wise_parser(symbol):
    initialize()
    try:	
        return wise_dictionary[symbol]	
    except:	
        return -1

def div2_parser(symbol):	
    initialize_div2()
    try:	
        return div2_dictionary[symbol]	
    except:	
        return -1	

skills_dictionary={"WSB":wsb_parser, "WISE":wise_parser, "DIV2":div2_parser}	

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
                "datetime": "working"}	
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
def initialize_div2():
    try:
        # using data from periodic updates at https://www.spglobal.com/spdji/en/indices/equity/sp-500-dividend-points-index-annual/#overview
        with open('div2.csv') as fr:
            for line in fr:
                [symbol,new_div,old_div,change]=line.strip().split(',')
                div2_dictionary[symbol]=new_div
        return {
        "message": "Dividend file initialized"
        }
    except:
        return {
            "message": "Initialization failed"
        }
    
@app.get("/initialize")
def initialize():
    try:
        with open('wsb.csv') as fr:
            for line in fr:
                [symbol,mention]=line.strip().split(',')
                wsb_dictionary[symbol]=float(mention)
                wise_dictionary[symbol]=float(mention)
        return {
        "message": "Files initialized"
        }
    except:
        return {
            "message": "Initialization failed"
        }

@app.get("/")
def main():
    return {
        "message": "Hello, world!"
    }
