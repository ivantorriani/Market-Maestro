from dataCollector import stockTags
from dataclasses import dataclass
from openai import OpenAI

#api key- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

api_key = 'peek'
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

ai_desc_1 = (
    "Your job is to look for keywords and find the associated value." + 
    " Only return the associated value, nothing else"

)

ai_desc_2 = (
     
     "Look through the data given to you. Only return" + 
     "the STOCK TICKER SYMBOL associated with the value 'Symbol'."
)


#list of instances- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
stocks = []
completeData = []
complete_tags = []




def aiFindInfo(keyword, listOfData, aiDesc):
    global ai_desc_1, ai_desc_2
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

def aiFindTicker(instructions, aidesc):
    directory = str(instructions)
    
        
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": aidesc},
            {"role": "user", "content": directory,}
        ]
    )


    data = completion.choices[0].message.content
    return data


#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

i = 0


def organize():
    global i
    while (i < len(stockTags)): #indiv Data resets every time, such that there is only one item in indivData at all times. 
        indivData = []
        for item in listOfKeywords:
                indivData.append(aiFindInfo(str(item), str(stockTags[i]), str(ai_desc_1)))                  
        completeData.append(indivData)

        return completeData

            

        i += 1

             
    
    return completeData
           
def just_tags():
     tag_ledger = []
     for item in stockTags:
          tag_ledger_i = []
          tag_ledger_i.append(aiFindTicker(str(item), str(ai_desc_2)))
          tag_ledger.append((tag_ledger_i))

     complete_tags.append(tag_ledger)

     return complete_tags

          
          
test = just_tags()

print(test)
# Only organize stock tags- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

    








text = str(stockTags[0])



    
    

