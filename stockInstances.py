from dataOrganizer import dataList
from dataclasses import dataclass

# class init - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

class Stock:
    tag = str
    name = str
    lastPrice = float
    changePrice = float
    changePercent = float
    volume = float

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

print(dataList)
