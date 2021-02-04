"""Restaurant rating lister."""
import random
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

def add_rest_rating(dictionary):
    while True:
        try: 
            restaurant = input("What is the restaurant name? ").rstrip()
            restaurant_score = int(input("What is the restaurant score? ").rstrip())

            if 1 <= restaurant_score <= 5:
                dictionary[restaurant] = restaurant_score
                break 
            else:
                print("Rating must be 1-5. Try again.")
            
        except ValueError:
            print ("Rating must be an integer! Try again.")
    return dictionary

restaurant_ratings = create_dict_ratings("scores.txt")
while True:
    command = int(input("What would you like to do? Enter 1 to see all the restaurant ratings, 2 to add a new restaurant rating, 3 to update a random restaurant and 4 to quit: "))
    if command == 1:
        for restaurant, rating in sort_alpha(restaurant_ratings):
            print(f"{restaurant} is rated at {rating}.")
    elif command == 2:
        restaurant_ratings = add_rest_rating(restaurant_ratings)
    elif command == 3:
        restaurant = random.choice(list(restaurant_ratings.keys()))
        rating = int(input(f'what would you like to rate {restaurant}? '))
        restaurant_ratings[restaurant] = rating
    elif command == 4:
        break
    else:
        print("Not a valid command. Try again.")
