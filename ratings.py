"""Restaurant rating lister."""
import random
import os
def create_dict_ratings(file_name):
    file = open(file_name)
    rest_ratings = {}
    for line in file:
        line = line.rstrip()
        rest_ratings[line[:-2]]=line[-1]
    return rest_ratings

def sort_alpha(dictionary):
    sorted_list = sorted(dictionary.items())
    return sorted_list 

def add_rest_rating(restaurant, dictionary):
    while True:
        try: 
            restaurant_score = int(input(f"What is {restaurant}'s score? ").rstrip())

            if 1 <= restaurant_score <= 5:
                dictionary[restaurant] = restaurant_score
                break 
            else:
                print("Rating must be 1-5. Try again.")
            
        except ValueError:
            print ("Rating must be an integer! Try again.")
    return dictionary
def update_rest_rating(dictionary):
    while True:
        try: 
            restaurant = input("What is the restaurant name? ").rstrip()
            if restaurant in dictionary:
                update = input(f'{restaurant} has already been rated a {dictionary[restaurant]}. Would you like to update the rating? Y for yes and N for no. ')
                if update.lower == 'y':
                    restaurant_score = int(input(f"What is {restaurant}'s new score? ").rstrip())
                elif update.lower == 'n':
                    break
                else:
                    print("Not a valid entry. try again.")
            elif restaurant not in dictionary:
                restaurant_score = int(input(f"{restaurant} has not been rated yet. What is {restaurant}'s score? ").rstrip())

            if 1 <= restaurant_score <= 5:
                dictionary[restaurant] = restaurant_score
                break 
            else:
                print("Rating must be 1-5. Try again.")
            
        except ValueError:
            print ("Rating must be an integer! Try again.")
    return dictionary


txt_files = []
for file_dir in os.listdir("."):
    if file_dir.endswith('.txt'):
        txt_files.append(file_dir)
while True:
    print(f'txt_files in current directory: {txt_files} ')
    file = input('Which file would you like use?')
    if os.path.isfile(file):
        restaurant_ratings = create_dict_ratings(file)
        break
    else:
        print("Not a valid file name. Try again. ")
while True:
    command = int(input("What would you like to do? Enter 1 to see all the restaurant ratings, 2 to add or update a new restaurant rating, and 3 to quit: "))
    if command == 1:
        for restaurant, rating in sort_alpha(restaurant_ratings):
            print(f"{restaurant} is rated at {rating}.")
    elif command == 2:
        while True:
            restaurant = input("What is the restaurant's name? ").rstrip()
            if restaurant in restaurant_ratings:
                update = input(f'{restaurant} has already been rated a {restaurant_ratings[restaurant]}. Would you like to update the rating? Y for yes and N for no. ')
                if update.lower() == 'y':
                    restaurant_ratings = add_rest_rating(restaurant, restaurant_ratings)
                    break
                elif update.lower() == 'n':
                    break
                else:
                    print("Not a valid command. Try again.")
            elif restaurant not in restaurant_ratings:
                restaurant_ratings = add_rest_rating(restaurant, restaurant_ratings)
                break
    elif command == 3:
        break
    else:
        print("Not a valid command. Try again.")
