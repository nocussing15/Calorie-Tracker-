# Calorie-Tracker-
#### Video Demo: <>
#### Description: 
Hello! My final project for CS50P will be a Calorie-Tracker. I decieded on making a Calorie-Tracker after using the calorie-tracker function on the application known as Ganbaru. My Calorie-Tracker uses various modules such as PySimpleGui, Pandas, Sys, Requests, and CSV. When I first created the calorie-tracker, it was more of a simple data entry journal, where the terminal would ask the user what was the date, what meal, what kind of food, and how many calories were consumed. One of the new challenges I faced was creating a GUI for a user to use. After researching about how to implent a gui in python, I decided to go with the pysimplegui module because of it's straightforward documentation. The GUI takes in several inputs from the User, and will even display a window to see current food entries. Next, in the original Calorie-Tracker, a user also had to manually input the amount of calories they had consumed. Now the calorie data, given the user's input of food, is pulled from the U.S Department of Agriculture's FoodData Central. Using the requests libray, we can interact with the FoodData Central's API, allowing us to get the calorie data from their database. 




#### Modules:
There are a couple of modules that will need to be installed to run the calorie-tracker:
| Modules |
|-----|
|Pysimplegui|               
|Pandas|              
|RE|
|sys|
|requests|
|csv|



#### Running the Program:
- The Program uses an API key generated by FoodData Central. To run the tracker, you will have to obtain your own API key here : https://fdc.nal.usda.gov/api-key-signup.html
- After obtaining your API key, create a config.py file and type in api_key="YOUR API KEY". Save the config file in the same folder you are running the program. The program will automatically call for you config.py.


#### How the Program Works:
1. The Program will ask for:
    - a date (ex:01/01/2023)
    - your meal (ex: Breakfast, Lunch, Dinner,Snack)
    - what food did you eat? (ex: Egg, chicken, coffee, beans, rice)
2. Please make sure to enter in the information following the examples format per input
3. When you open the program you will notice a note, all the food quantity is measured by 100g. So if you enter chicken, the calories calculated will be for 100g of chicken.
4. Once your food is entered, if there is an error in how the amount of calories showing up, there is the option to edit your entries. Simply click on the row you wish to edit, then hit the edit button. Reinput the correct values and hit save.

#### Future: 
In the future, i'd like to come back to this project to update the GUI and expand upon how the tracker's ability to display food information. One of the many concepts that can be added to expand about tihs project is the use of classes, and creating user accounts, so that multiple users can have thier own calorie tracker. Then users can save their own calorie tracker into some database and make pull and push requests to that database. 
  

