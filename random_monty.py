import numpy as np
import random
import math

def monty_hall(switching = True, n_games = 90000, num_doors = 3, num_doors_car = 1, num_doors_contestant = 1, nums_doors_host = 1, num_cars_won = 1):
    
    #Initialize the number of wins to 0
    wins = 0

    #Iterates for each sample
    for i in range(n_games):

        print(f"Iteration {i}")
        
        #Creates the options of doors
        door_options = np.arange(num_doors)
        print(f"door_options: {list(door_options)}")
        #Selects the doors with car
        door_correct = set(random.sample(list(door_options), num_doors_car))
        print(f"door_correct: {list(door_correct)}")
        #Select the doors that the contestant initially had chosen
        door_choice = random.sample(list(door_options), num_doors_contestant)
        print(f"door_choice: {list(door_choice)}")
        #Remaining doors that the host to select to reveal goats or cars
        remaining_doors = list(set(door_options) - set(door_choice))
        #Select the doors that the host will reveal 
        door_choice_host = random.sample(remaining_doors, nums_doors_host)
        print(f"door_choice_host: {list(door_choice_host)}")

        #Select the set of doors that the contestant switches into
        if switching == True: 
            remaining_doors = list(set(door_options) - set(door_choice_host))
            print(f"remaining doors: {list(remaining_doors)}")
            while True:
                temp = random.sample(remaining_doors, num_doors_contestant)
                #Ensure that the new selection doors isn't the same as the old one
                if set(temp) != set(door_choice):
                    door_choice = temp
                    print(f"door_choice: {list(door_choice)}")
                    break
        #Initialize the number of cars won to 0
        counter = 0

        #Check that every door has a goat
        for j in range(len(door_choice)):
            #Check whether the door has a car
            if door_choice[j] in door_correct:
                counter += 1
        #Check if the contestant won exactly num_cars_won amount of cars
        if counter == num_cars_won:
            print("Result: Win!")
            wins += 1
            continue
        print("Result: Lose")

    return wins / n_games


num_doors = int(input("Number of doors, n (n >= 3): "))
num_doors_car = int(input(f"Number of doors with a car, m (1 =< m =< {num_doors - 1}): ")) # 1 =<  m =< n - 1
num_doors_contestant = int(input(f"Number of doors selected by contestant, p (1 =< p =< {num_doors_car}): ")) # 1 =< p =< m
num_doors_host = int(input(f"Number of doors selected by host, k (1 =< k =< {num_doors - num_doors_car - num_doors_contestant}): ")) # 1 =< k =< n - m - p
num_cars_won = int(input(f"Number of goats the contestant must win, q (1 =< q =< {num_doors_contestant}): ")) # 1 =< q = < p
num_goats = num_doors - num_doors_car

wins_by_remaining = monty_hall(switching = False, num_doors = num_doors, num_doors_car = num_doors_car, num_doors_contestant = num_doors_contestant, nums_doors_host = num_doors_host, num_cars_won = num_cars_won)
wins_by_switching = monty_hall(switching = True, num_doors = num_doors, num_doors_car = num_doors_car, num_doors_contestant = num_doors_contestant, nums_doors_host = num_doors_host, num_cars_won = num_cars_won)

# Variables
n = num_doors
m = num_doors_car
p = num_doors_contestant
q = num_cars_won
k = num_doors_host

theoretical_win_by_remaining = math.comb(m , q) * math.comb( n - m , p - q) / math.comb( n , p)
theoretical_win_by_switching = math.comb(m , q) * ( math.comb( n , p ) * math.comb( n - m - k , p - q) - math.comb( n - m , p - q) ) / ( math.comb( n, p ) * (math.comb( n - k , p ) - 1) )

percentage_difference_remaining = (abs(wins_by_remaining - theoretical_win_by_remaining)) / theoretical_win_by_remaining * 100
percentage_difference_switching = (abs(wins_by_switching - theoretical_win_by_switching)) / theoretical_win_by_switching * 100


print("--------------------Inputs--------------------")
print(f"Total number of doors: {num_doors}")
print(f"Number of doors with car: {num_doors_car}")
print(f"Number of doors with goat: {num_goats}")
print(f"Number of doors selected by the contestant: {num_doors_contestant}")
print(f"Number of doors openned by the host: {num_doors_host}")
print(f"Number of cars that MUST be won by the contestant: {num_cars_won}")
print(f"--------------------RESULTS--------------------")
print(f"Probability of winning by remaining: {wins_by_remaining}")
print(f"Probability of winning by switching: {wins_by_switching}")
