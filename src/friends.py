
def get_name(person):
    return person['name']

def get_favourite_tv_show(person):
    return person['favourites']['tv_show']

def likes_to_eat(person,food):
    if food in person['favourites']['snacks']:
        return True
    return False

def add_friend(person,friend_name):
    person['friends'].append(friend_name)

def remove_friend(person,friend_name):
    person['friends'].remove(friend_name)

def total_money(people):
    total_money = 0
    for person in people:
        total_money += person['monies'] 
    return total_money

def lend_money(person1,person2,money):
    person1['monies']  -= money
    person2['monies']  += money

def all_favourite_foods(people):
    favorite_food = []
    for person in people:
        favorite_food += (person['favourites']['snacks'])
    return favorite_food

def find_no_friends(people):
    people_with_no_friends =[]
    for person in people:
        if person['friends'] == []:
            people_with_no_friends += [person]
    return people_with_no_friends

def unique_favourite_tv_shows(people):
    favorite_shows = []
    for person in people:
        favorite_shows.append(person['favourites']['tv_show'])
    favorite_shows = list(dict.fromkeys(favorite_shows))
    return favorite_shows




    
