"""
BBC Software Engineering Graduate Trainee Scheme: Technical Task
Create a Game of Life, following Conway's rules
This was written for Python3 by Dan Helyer
"""

#Import random function to allow for randomly generated starting grid
import random

#Determine what alive and dead cells will look like for user
alive = 'Y' #Looks like a tree
dead = '.' #Looks like a seed

#Create function to print a nested array as a 2D grid
def print_array(x_array):
    for row in x_array:
        for cell in row:
            print(cell, end=" ")
        print()
    print()

#Create function to count the neighbours of a particular cell
def count_neighbours(y, x):
    neighbours = 0

    #Set default range to capture neighbours
    y_min = -1
    y_max = 2
    x_min = -1
    x_max = 2

    #Use if statements to stop counting at edges of the grid
    if y == 0:
        y_min = 0
    if y == y_axis - 1:
        y_max = 1
    if x == 0:
        x_min = 0
    if x == x_axis - 1:
        x_max = 1

    #Use for loops to cycle through all neighbouring cells
    for i in range(y+y_min, y+y_max):
        for j in range(x+x_min, x+x_max):
            if array[i][j] == alive:
                neighbours += 1

    #Remove cell itself from counted neighbours
    if array[y][x] == alive:
        neighbours -= 1

    return neighbours

#Create function to determine if a cell lives or dies in next iteration
def life_or_death(y, x):
    neighbours = count_neighbours(y, x)

    if array[y][x] == alive:
        if not 2 <= neighbours <= 3:
            return dead #A living cell without 2 or 3 neighbours becomes dead
        else:
            return alive #A living cell with 2 or 3 neighbours remains alive
    else:
        if neighbours == 3:
            return alive #A dead cell with exactly 3 neighbours becomes alive
        else:
            return dead #A dead cell without exactly 3 neighbours remains dead

#Create functions checking for Game Over conditions
def game_over_extinction():
    #Check if life remains in the grid
    for i in range(y_axis):
        for j in range(x_axis):
            if next_array[i][j] == alive:
                return False #Life remains, keep playing
    print_array(next_array)
    print('Game over, no life remains.')
    return True

def game_over_static():
    #Check if next iteration matches current one, meaning life is static
    for i in range(y_axis):
        for j in range(x_axis):
            if next_array[i][j] != array[i][j]:
                return False #Life is fluid, keep playing
    print_array(next_array)
    print('You win, life is static!')
    return True

def game_over_cyclical():
    #Check if next iteration matches previous iteration, meaning life is cyclical
    for i in range(y_axis):
        for j in range(x_axis):
            if next_array[i][j] != last_array[i][j]:
                return False #Life is fluid, keep playing
    print_array(next_array)
    print('You win, life is cyclical!')
    return True

#Welcome message signifying start of the program
print("Welcome to Conway's Game of Life, as coded by Dan Helyer")
print("For our purposes '{}' represents life and '{}' represents death".format(str(alive), str(dead)))
print("First we need to determine the size of our game grid.")

#Ask user to determine the x- and y-axis
while True: #x-axis
    try:
        x_axis = int(input('How many columns do you want? '))
        if x_axis > 0:
            break
        print('Please choose a number greater than 0.')
    except ValueError:
        print('Please use numericals (0–9) to type a whole number.')

while True: #y-axis
    try:
        y_axis = int(input('How many rows do you want? '))
        if y_axis > 0:
            break
        print('Please choose a number greater than 0.')
    except ValueError:
        print('Please use numericals (0–9) to type a whole number.')

#Generate blank 2D arrays to act as past, present, and future game grids
array = [[dead for i in range(x_axis)] for j in range(y_axis)]
next_array = [[dead for i in range(x_axis)] for j in range(y_axis)]
last_array = [[dead for i in range(x_axis)] for j in range(y_axis)] #Used to detect cyclical loops

#Fill the grid with random life
for i in range(y_axis):
    for j in range(x_axis):
        array[i][j] = random.choice([alive, dead])

#Let the game begin
Game_Over = False

#While loop is used to continue game until Game Over is reached
while not Game_Over:
    print()
    print_array(array)
    input('Press enter to continue to the next iteration...')

    #Cycle through each cell to determine life or death in the next iteration
    for i in range(y_axis):
        for j in range(x_axis):
            next_array[i][j] = life_or_death(i, j) #Store results in next_array

    #Check for game over conditions
    if game_over_extinction():
        Game_Over = True
    elif game_over_static():
        Game_Over = True
    elif game_over_cyclical():
        Game_Over = True

    #Replace last_array with current array
    last_array = [cell[:] for cell in array]
    #Replace current array with next_array
    array = [cell[:] for cell in next_array]
