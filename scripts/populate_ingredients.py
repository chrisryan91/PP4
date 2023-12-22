with open('FOOD_DES.txt', 'r') as file:
    lines = file.readlines()

ingredient_names = [line.split('~')[2] for line in lines]