from calorie_tracker import check_date_input,check_food_input,check_meal_input,get_food_nutrients

def test_check_date():
    assert check_date_input('10/01/2023') == True 
    assert check_date_input('123/01/2023') == False
    assert check_date_input('ten/ten/2023') == False
    assert check_date_input('10-01/2023') == False
    assert check_date_input('3333') == False
    assert check_date_input('') == False
def test_meal_input():
    assert check_meal_input('breakfast') == True
    assert check_meal_input('BrEaKfAst') == True
    assert check_meal_input('BREAKFAST') == True
    assert check_meal_input('Lunch') == True
    assert check_meal_input('LUNCH') == True
    assert check_meal_input('lUnCh') == True
    assert check_meal_input('3333') == False
    assert check_meal_input('') == False

def test_food_input():
    assert check_food_input('Egg') == True
    assert check_food_input('3a2f') == False
    assert check_food_input('3232') == False
    assert check_food_input('') == False
    assert check_food_input('Egg, Chicken, Coffee') == True
    
def test_calorie_count():
    assert get_food_nutrients('chicken') == 164
    assert get_food_nutrients('coffee') == 1.0
    assert get_food_nutrients('Iced Oat Milk Latte') == 418 
    assert get_food_nutrients(' ') == None
    assert get_food_nutrients('asdf') == None
    assert get_food_nutrients('3d32sa') == None 