from dataOrganizer import dataList
from dataclasses import dataclass

# class init and readability- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
print(dataList)
class Stock:
    def __init__(self, tag, name, lastPrice, changePrice, changePercent, volume):
        self.tag = str(tag)
        self.name = str(name)
        self.lastPrice = (lastPrice)
        self.changePrice = (changePrice)
        self.changePercent = (changePercent)
        self.volume = (volume)

    '''def __str__(self):
        return (
        f"Stock Summary: \n"
        f"Tag: {self.tag}\n"
        f"Name: {self.name}\n"
        f"Last Price: {self.lastPrice:.2f}\n"  # limit the amount of float points
        f"Change of Price: {self.changePrice:.2f}\n"
        f"Change of Percent: {self.changePercent:.2f}\n"
        f"Volume: {self.volume:.2f}\n"
    )'''



#list of instances- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
instances =  []
def getStockInstances():
    #for i in range (len(dataList)):
    for item in dataList[0]:
        stock = Stock(
            tag = (dataList[0]),
            name = (dataList[1]),
            lastPrice = (dataList[2]),
            changePrice = (dataList[3]),
            changePercent = (dataList[4]),
            volume = (dataList[5])
        
        )
        return stock

