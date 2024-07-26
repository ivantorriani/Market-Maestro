from dataCollector import stockTags
from dataclasses import dataclass
from openai import OpenAI

#api key- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

api_key = 'urdad'
client = OpenAI(api_key=api_key)

#stock class - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

class Stock:
    tag = str
    name = str
    lastPrice = float
    changePrice = float
    changePercent = float
    volume = float

#keyword list - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

listOfKeywords = [
    "Symbol",
    "Company Name",
    "Last Price",
    "Change",
    "% Change",
    "Volume"
]


#AI desc- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

aiDesc = (
    "Your job is to look for keywords and find the associated value." + 
    " Only return the associated value."

)

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 



def aiFind(keyword, listOfData):
    global aiDesc
    directory = str("Keyword" + keyword + "in" + listOfData)
    
        
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": aiDesc},
            {"role": "user", "content": directory,}
        ]
    )


    data = completion.choices[0].message.content
    return data



#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 






text = str(stockTags[0])



    
    

