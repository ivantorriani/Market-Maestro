from dataOrganizer import just_tags
from openai import OpenAI
from ai_descs import otto_fu
from save_to_classes import fill_stock_dict
from halo import Halo

# - - - - - - - - - - - - - - - - - -

api_key = 'kleep'

client = OpenAI(api_key=api_key)

list_of_tags = just_tags()

stock_dict = fill_stock_dict()

ias_ledger = []


loading_spinner = Halo(text = 'Loading', spinner = 'dots')

i = 0
# Example  - - - - - - - - - - - - - - - - - -



# - - - - - - - - - - - - - - - - - - -



#while (i < len(list_of_tags[0])):
#    print(list_of_tags[0][i][0])
#    i += 1




def analyze():
    global otto_fu, stock_dict, i

    temp_ledger = []

    while (i < len(list_of_tags[0])):

        

        loading_spinner.start

        stock = stock_dict[str(list_of_tags[0][i][0])]

        symbol = stock.symbol
        breakout_st = stock.breakout_status
        high_volume_st = stock.high_volume_status
        cup_and_handle_st = stock.cup_and_handle_status
        double_bottom_st = stock.double_bottom_status
        ascending_tri_st = stock.ascending_triangle_status

        directory = (
            "Here is information from the technical analyst: "
            "Symbol: " + str(symbol) +
            "Breakout Status: " + str(breakout_st) +
            "High Volume Check: " + str(high_volume_st) +
            "Cup and Handle Check:" + str(cup_and_handle_st) +
            "Double Bottom Check: " + str(double_bottom_st) + 
            "Ascending Triangle Check: " + str(ascending_tri_st)

        )
        
        completion = client.chat.completions.create(
            model="gpt-4",
            messages = [

                {"role": "system", "content": str(otto_fu)},

                {"role": "user", "content": directory,}
            ]
        )

        score = completion.choices[0].message.content
        temp_ledger.append(str(list_of_tags[0][i]) + " : " +  str(score))
        i += 1
    
    ias_ledger.append(temp_ledger)
    loading_spinner.stop_and_persist(symbol='✔️', text='Done!')


    return ias_ledger

test = analyze()

print(test)