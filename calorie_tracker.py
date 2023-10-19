import PySimpleGUI as sg
import pandas as pd
import re
import sys
import requests
import csv

#add some color to your gui
sg.theme('DarkAmber')
# GUI INPUT MENU 
def main():
      menu()
      show()
      

#function that will be used to check if the value inputed is correct or not
def check_date_input(date):
                 #date check
                if re.search(r"^(0[1-9]|1[012])[-/.](0[1-9]|[12][0-9]|3[01])[-/.]\d{4}$", date):
                       return True
                else:
                       return False 
def check_meal_input(meal):               
                #meal check
                meal_input_options = ['breakfast','lunch','dinner','snack']
                if meal.lower().strip() in meal_input_options:
                      return True
                else: 
                      return False
def check_food_input(food):                    
                #calorie check 
                if re.search(r"[a-zA-Z]+", food):
                      return True
                else:
                       return False

dates_list=[]
meals_list=[]
      

def menu():
    #Step 1, always define a layout
    layout = [
        [sg.Text('Please enter todays date (ex:01/01/2023)'),sg.Input(key='-DATE-') ],
        [sg.Text('Please enter your Meal (ex:Breakfast, Lunch, Dinner, Snack)'), sg.Input(key='-MEAL-')],
        [sg.Text('Please enter your Food(ex:Egg, Chicken, Coffee)'), sg.Input(key='-FOOD-')], 
        [sg.Submit(), sg.Button('Clear'), sg.Button('Show Current Entries'),sg.Exit()]
    ]


    #Step 2, actually create the window
    window= sg.Window('Calorie Tracker Input Menu', layout)
    # will clear away values 
    def clear_input():
        for key in values:
            window[key]('')
        return None

    #Step 3, event loop to process 'events'
    while True:
        event, values = window.read()
        if event == 'Clear':
            clear_input()
        # For Exit Button
        if event in (sg.WIN_CLOSED,'Exit'):
            break   
        #Will check the logic for submission and store input into lists
        if event == 'Submit':
           if not check_date_input(values['-DATE-']):
            sg.popup('Your Date was Incorrect')
            window['-DATE-'].update(window['-DATE-'](''))
           elif not check_meal_input(values['-MEAL-']):
            sg.popup('Please Select a meal again')
            window['-MEAL-'].update(window['-MEAL-'](''))
           elif not check_food_input(values['-FOOD-']):
            sg.popup('Please enter in food in food format')
            window['-FOOD-'].update(window['-FOOD-'](''))
           else:
                food_list=[]  
                food_list.append((values['-FOOD-']))
                food_list=food_list[0].split(',')
                calories_list=[]
                print(food_list)
                for food in food_list:
                    #strip() here will account for spaces in the food name
                    calories_food = get_food_nutrients(food.strip())
                    calories_list.append(calories_food)
                    print(calories_list)
                calories_food=sum(calories_list)
                    
                tracker_calorie(values['-DATE-'],values['-MEAL-'],values['-FOOD-'],calories_food)
                clear_input()
                sg.popup('Data Saved!')
            
        if event == 'Show Current Entries':
            show_current_entries()
              
                  
    window.close()


#used to display current entries in pysimplegui
def show_current_entries():
    sg.theme('DarkBlue1')
    filename = 'calorie.csv'
    with open(filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        try:
            header_list = next(reader)
            data=list(reader)
        except:
            sg.popup_error('Error Reading CSV File')
            return None
    sg.set_options(element_padding=(0,0))
    
    Layout = [[sg.Table(values=data,
                        headings=header_list,
                        auto_size_columns=True,
                        justification='center'
                        )]]
    window = sg.Window('Table', Layout, grab_anywhere= False)
    
    window.read()
    
    window.close()
        
        
        
# find out the calorie amount for a specific food 
#api key for food data central 
api_key = 'FmmXHNTNLEh7p9oygtMvLEljvudBuQnt15cbqBgG'
def get_food_nutrients(food):
    # Replace spaces with '%20' in the food name
    _query = food.replace(' ', '%20')

    parameters = {
        'query': _query,
        'dataType': 'Survey (FNDDS)',
        'pageSize': '1',
    }

    response = requests.get(f'https://api.nal.usda.gov/fdc/v1/foods/search?api_key={api_key}', params=parameters)
    # does the food that we query exist?
    if response.status_code == 200:
        food_query = response.json()
        if 'foods' in food_query and len(food_query['foods']) > 0:
            food_nutrients = food_query['foods'][0]['foodNutrients']
            for nutrients in range(len(food_nutrients)): 
                if food_nutrients[nutrients]['nutrientId'] == 1008:
                    return food_nutrients[nutrients]['value']

        else:
            return None
    else:
        print(f"Failed to retrieve data for {food}. Status code: {response.status_code}")
        return None
    





def tracker_calorie(day_input, meal_input, food_input, calorie_input):
    # Used to create the columns for the CSV file
    fieldnames=['date','meal','food','calories']
    while True:
        try:
            with open('calorie.csv','x') as file:
                writer = csv.DictWriter(file, lineterminator='\n', fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow({'date':day_input,'meal':meal_input,'food':food_input, 'calories':calorie_input})
                break
        except FileExistsError:
            with open('calorie.csv','a') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writerow({'date':day_input,'meal':meal_input,'food':food_input,'calories':calorie_input})
                break
        except FileNotFoundError:
            sys.exit('File not Found')
        except UnboundLocalError:
            sys.exit('Something is wrong')



'''#convert dataframe to csv
def df_csv(dataframe):
      try:
        dfs= dataframe
        dfs.to_csv('calories.csv', sep=',',encoding='utf-8',index=False)
      except FileNotFoundError:
            sys.exit('Dataframe not Found')
      
#take inputs from gui and create a dataframe
def dataframe():
      df=pd.DataFrame()
      #creates a dataframe
      try:
           if df.empty: 
            d = {'dates': dates_list, 'meals':meals_list,'food':food_list}
            df = pd.DataFrame(data=d)
            
            
            food_index = df['food']
            #add the calories column to the index
            df['Calores'] = [get_food_nutrients(food) for food in food_index]
            #add the calories of the food per date to desired row
      except:


        df_csv(df)




'''




def show():
      try:
        calorie_table = pd.read_csv('calorie.csv')
        print(calorie_table)
      except FileNotFoundError:
            sys.exit('csv not found')
        
#every time i open up the menu I want to store the data into the excel sheet

#def store_data():

#


if __name__ == "__main__":
    main()
#possibly create a class for multiple accounts?
# lets try to create 1 account for now via pandas DF and input via the GUI


