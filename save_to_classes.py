from technical_analysis import (

    detect_breakout,
    detect_high_volume,
    detect_cup_and_handle,
    detect_double_bottom,
    detect_ascending_triangle

)

from fundamental_analysis import (

    get_general_info,
    get_timely_info,
    get_financials,
    get_balance_sheet,
    get_cash_flow,
    get_earnings

)

from dataOrganizer import just_tags
from halo import Halo

# preliminary initializations - - - - - - - - - - - - - - - - - -

list_of_tags = just_tags()

tech_ana_dict = {}

fund_ana_dict = {}

first_spinner = Halo(text = 'Organizing T.A data into classes...', spinner = 'bouncingBar')

second_spinner = Halo(text = "Organizing F.A data into classes...", spinner = 'star')

# create classes - - - - - - - - - - - - - - - - - - 

class stock_ta:

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


class stock_fa:

    def __init__(
            
            self,
            symbol, 
            g_info,
            t_info,
            financials,
            balance_sheet,
            cash_flow
    ):
        self.symbol = symbol
        self.gen_info = g_info
        self.t_info = t_info
        self.financials = financials
        self.balance_sheet = balance_sheet
        self.cash_flow = cash_flow
    

# fill dictionaries - - - - - - - - - - - - - - - - - -

i = 0
def fill_ta_dict():
    global i 

    first_spinner.start()
    

#make sure it append to list

    while (i < len(list_of_tags[0])):

        tech_ana_dict[str(list_of_tags[0][i][0])] = stock_ta(

            str(list_of_tags[0][i][0]),
            str(detect_breakout(list_of_tags[0][i][0])),
            str(detect_high_volume(list_of_tags[0][i][0])),
            str(detect_cup_and_handle(list_of_tags[0][i][0])),
            str(detect_double_bottom(list_of_tags[0][i][0])),
            str(detect_ascending_triangle(list_of_tags[0][i][0]))
            

        )

        i += 1

    first_spinner.stop_and_persist(symbol='✔️', text='Done!')

        
    return tech_ana_dict




def fill_fa_dict():
    global i 

    second_spinner.start()

    while (i < len(list_of_tags[0])):
        fund_ana_dict[str(list_of_tags[0][i][0])] = stock_fa(

            str(list_of_tags[0][i][0]),
            str(get_general_info(list_of_tags[0][i][0])),
            str(get_timely_info(list_of_tags[0][i][0])),
            str(get_financials(list_of_tags[0][i][0])),
            str(get_cash_flow(list_of_tags[0][i][0])),
            str(get_earnings(list_of_tags[0][i][0]))
            

        )

        i += 1

    second_spinner.stop_and_persist(symbol='✔️', text='Done!')

        
    return fund_ana_dict