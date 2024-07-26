from dataCollector import stockTags
from dataclasses import dataclass
from openai import OpenAI

#api key- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

api_key = 'bleep!'
client = OpenAI(api_key=api_key)


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

#list of instances- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
stocks = []
completeData = []

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
i = 0


def organize():
    global i
    while (i < len(stockTags)):
        indivData = []
        for item in listOfKeywords:
            indivData.append(aiFind(str(item), str(stockTags[i])))
        completeData.append(indivData)
        i += 1
    
    return completeData
           

  
dataList = organize()


    








text = str(stockTags[0])



    
    

