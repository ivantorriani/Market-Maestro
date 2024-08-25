from a_break_and_volume import (

    detect_breakout,
    detect_high_volume,
    detect_cup_and_handle,
    detect_double_bottom,
    detect_ascending_triangle

)

from dataOrganizer import just_tags
from halo import Halo

# - - - - - - - - - - - - - - - - - -

list_of_tags = just_tags()

stock_list = {}

stock_gather = []

loading_spinner = Halo(text = 'Loading', spinner = 'dots')
# - - - - - - - - - - - - - - - - - -

class Stock:

    def __init__(
            
            self,
            symbol,
            breakout_status,
            high_volume_status,
            cup_and_handle_status,
            double_bottom_status,
            ascending_triangle_status
            
    ):
        self.symbol = symbol
        self.breakout_status = breakout_status
        self.high_volume_status = high_volume_status
        self.cup_and_handle_status = cup_and_handle_status
        self.double_bottom_status = double_bottom_status
        self.ascending_triangle_status = ascending_triangle_status

# fill dictionary - - - - - - - - - - - - - - - - - -
i = 0
def fill_stock_dict():
    global i 

    loading_spinner.start()
    

#make sure it append to list

    while (i < len(list_of_tags[0])):

        stock_list[str(list_of_tags[0][i][0])] = Stock(

            str(list_of_tags[0][i][0]),
            str(detect_breakout(list_of_tags[0][i][0])),
            str(detect_high_volume(list_of_tags[0][i][0])),
            str(detect_cup_and_handle(list_of_tags[0][i][0])),
            str(detect_double_bottom(list_of_tags[0][i][0])),
            str(detect_ascending_triangle(list_of_tags[0][i][0]))
            

        )

        i += 1

    loading_spinner.stop_and_persist(symbol='✔️', text='Done!')

        
    return stock_list
