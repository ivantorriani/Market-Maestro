import json
from datetime import datetime
#from p_1_ta import execute_p1
# initilizations - - - - - - - - - - - - - - - - - 

i = 0

j = 0
#date_key = datetime.now().strftime("%Y-%m-%d")
# experiments - - - - - - - - - - - - - - - - - - - - - - - - - - - -

data = [["['PSNY'] : 4", "['OPEN'] : 3", "['GEVO'] : 3", "['RR'] : 3", "['AITX'] : 2", "['MIRA'] : 2", "['LTNC'] : 2", "['MULN'] : 1", "['HYZN'] : 2", "['BRNE'] : 4", "['PWM'] : 4", "['BIEL'] : 3", "['TNXP'] : 2", "['CERO'] : 2", "['GRST'] : 3", "['MJNA'] : 2", "['ELAB'] : 1", "['HMBL'] : 2", "['DKSC'] : 3", "['ASST'] : 3", "['TSOI'] : 2", "['AHRO'] : 3", "['TCJH'] : 3", "['ADHC'] : 4", "['ABQQ'] : 4", "['FAMI'] : 2", "['VNUE'] : 2", "['RONN'] : 2", "['NDRA'] : 1", "['BLLB'] : 2"]]

print(data)


tickers = []

scores = []


def get_ticker():
    global i
    while (i < len(data[0][0])):
        ticker_holder = []
        for item in data[0][0][i]:
            if item.isupper():
                ticker_holder.append(item)
        ticker = ''.join(ticker_holder)
        tickers.append(ticker)
        i += 1
    return tickers


def get_scores():
    global j
    while (j < len(data[0][0])):
        score_holder = []
        for item in data[0][0][j]:
            if item.isdigit():
                score_holder.append(item)
        score = ''.join(score_holder)
        scores.append(score)
        j += 1

    return scores

scores = get_scores()

please = get_ticker()

print(please, scores)