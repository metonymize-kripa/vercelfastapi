from fastapi import FastAPI
import datetime

app = FastAPI()

wsb_dictionary={"SPY":0.1}
wise_dictionary={"SPY":0.2}
div2_dictionary={}
dive_dictionary={}

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

def dive_parser(symbol):	
    try:	
        return dive_dictionary[symbol]	
    except:
        initialize_dive()
        try:
            return dive_dictionary[symbol]
        except:
            return {}	

skills_dictionary={"WSB":wsb_parser, "WISE":wise_parser, "DIV2":div2_parser, "DIVE":dive_parser}	

def dispatch_skill_parser(skill, symbol):
    try:	
        return skills_dictionary[skill](symbol)	
    except:	
        return 0
    
@app.get("/parse/{parameter}")
def parse(parameter: str):
    parsed_parameter_list = parameter.strip().split('%20')
    num_parameters_parsed = len(parsed_parameter_list)
    
    #return {"Output":parsed_parameter_list}

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
                "datetime": datetime.date.today()}#datetime.now().time()}	
    except:	
        return {"symbol": "no symbol",	
                "skill": "no skill",	
                "skill_output": "no output",	
                "datetime": "no time"}	           

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
    
def initialize_dive():
    try:
        # using data from dividend.com downloaded Mar 2, 2021
        # Symbol,Status,NextPayDate,DivYield,NextEstPayout,AnnualDividend
        with open('dive-mar2-2021.csv') as fr:
            for line in fr:
                split_line = line.strip().split(',')
                if len(split_line) == 6:
                    [Symbol,Status,NextPayDate,DivYield,NextEstPayout,AnnualDividend,ExDiv]=split_line
                    dive_dictionary[Symbol]={"symbol":Symbol,
                                             "status":Status,
                                             "nextpaydate":NextPayDate,
                                             "divyield":DivYield,
                                             "nextestpayout":NextEstPayout,
                                             "annualdividend":AnnualDividend,
                                            "exdiv":ExDiv}
        return {
        "message": "DIVE file initialized"
        }
    except:
        return {
            "message": "DIVE Initialization failed"
        }
    
@app.get("/initialize")
def initialize():
    initialize_dive()
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
