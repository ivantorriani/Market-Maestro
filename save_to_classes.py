from a_break_and_volume import (

    detect_breakout,
    detect_high_volume,
    detect_cup_and_handle,
    detect_double_bottom,
    detect_ascending_triangle

)

from dataOrganizer import just_tags


# - - - - - - - - - - - - - - - - - -

list_of_tags = just_tags()

stock_list = {}

stock_gather = []

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

def fill_stock_dict():


    for item in list_of_tags:

        stock_list[str(item[0][0])] = Stock(

            str(item[0][0]),
            str(detect_breakout(item[0][0])),
            str(detect_high_volume(item[0][0])),
            str(detect_cup_and_handle(item[0][0])),
            str(detect_double_bottom(item[0][0])),
            str(detect_ascending_triangle(item[0][0]))

        )
        
    return stock_list




