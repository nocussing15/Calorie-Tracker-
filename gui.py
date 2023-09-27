import PySimpleGUI as sg
import pandas as pd
import re
import sys

#add some color to your gui
sg.theme('DarkAmber')
# GUI INPUT MENU 
def main():
      menu()
      dataframe()
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
food_list=[]        

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
        if event in (sg.WIN_CLOSED,'Exit'):
            break   
        
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
                dates_list.append(values['-DATE-'])
                meals_list.append(values['-MEAL-'])
                food_list.append(values['-FOOD-'])
                clear_input()
                sg.popup('Data Saved!')
            
    window.close()


#convert dataframe to csv
def df_csv(dataframe):
      try:
        dfs= dataframe
        dfs.to_csv('calories.csv', sep=',',encoding='utf-8',index=False)
      except FileNotFoundError:
            sys.exit('Dataframe not Found')
      
#take inputs from gui and create a dataframe
def dataframe():
      d = {'dates': dates_list, 'meals':meals_list,'food':food_list}

      df = pd.DataFrame(data=d)
      
      df_csv(df)

def show():
      try:
        calorie_table = pd.read_csv('calories.csv')
        print(calorie_table)
      except FileNotFoundError:
            sys.exit('csv not found')
        
#every time i open up the menu I want to store the data into the excel sheet

#def store_data():




if __name__ == "__main__":
    main()
#possibly create a class for multiple accounts?
# lets try to create 1 account for now via pandas DF and input via the GUI


