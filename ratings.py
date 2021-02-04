"""Restaurant rating lister."""
file = open('scores.txt')
rest_ratings = {}

for line in file:
    line = line.rstrip()
    rest_ratings[line[:-2]]=line[-1]

def sort_alpha(dictionary):
    sorted_list = sorted(dictionary.items())
    return sorted_list 

while True:
    try: 
        restaurant = input("What is the restaurant name? ").rstrip()
        restaurant_score = int(input("What is the restaurant score? "))

        if 1 <= restaurant_score <= 5:
            rest_ratings[restaurant] = restaurant_score
            break 
        else:
            print ("Rating must be 1-5. Try again.")
        
    except ValueError:
        print ("Rating must be an integer! Try again.")

for word in sort_alpha(rest_ratings):
    print(f"{word[0]} is rated at {word[1]}.")