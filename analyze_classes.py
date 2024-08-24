from dataOrganizer import just_tags
from openai import OpenAI

# - - - - - - - - - - - - - - - - - -

api_key = 'a-boo!'
client = OpenAI(api_key=api_key)

list_of_tags = just_tags()

# Example  - - - - - - - - - - - - - - - - - -

#apple_stock = stocks["AAPL"]
#print(apple_stock.price)  # Output: 175.20

# - - - - - - - - - - - - - - - - - - -