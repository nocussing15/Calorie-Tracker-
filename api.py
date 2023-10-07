import requests
import json

api_key= 'FmmXHNTNLEh7p9oygtMvLEljvudBuQnt15cbqBgG'


_query = input()

_query.replace(' ','%20')


parameters = {
    'query' : _query,
    'dataType' : 'Survey (FNDDS)',
    'pageSize' : '1'
    }


response = requests.get(f'https://api.nal.usda.gov/fdc/v1/foods/search?api_key={api_key}',params = parameters)


#print(response.status_code)
food_query = response.json()
food_nutrients = food_query['foods'][0]['foodNutrients']

for nutrients in range(len(food_nutrients)): 
    if food_nutrients[nutrients]['nutrientId'] == 1008:
        print(food_nutrients[nutrients]['value'])

    
#print(response.url)    
