import random
while True:
        try:
            random.seed(int(input('Please enter a seed: ')))
            break
        except ValueError:
            print('Error! That is not a valid input!')
        print()
print()


yesWins = 0
noWins = 0
keepChoice = 0
changeChoice = 0

# create function that will allow the user to play one instance of the Monty Hall problem
def play():
    global keepChoice
    global changeChoice
    global yesWins
    global noWins                                       # ensure the variables will be affected by the results of the simulation
    print()
    print("""There are three doors, each concealing a prize.
Two of those are laundry detergent, but one is $10,000.
Which door will you choose: 1, 2, or 3?""")

    doors = [1, 2, 3]
    prize_door = random.choice(doors)                  
    revealed_door = 0                                   # create variables for the door with detergent that will be revealed
    new_choice = 0                                      # and the door the user will be given the option to switch to
    while True:
        try:
            chosen_door = int(input('Please enter your choice: '))
            while chosen_door not in range(1, 4):
                chosen_door = int(input('Invalid input, please choose a number provided: '))
            break
        except ValueError:
            print('Input not recognized.')              # get user's chosen door
   
    for i in doors:                                     # for loop goes through door options and finds a door that
        if i != prize_door and i != chosen_door:        # hasn't been chosen and isn't the door with 10k
            revealed_door = i                           # this door will be revealed to the user
  
    for i in doors:                                     # same process with previous door but now we search for a door that
        if i != chosen_door and i != revealed_door:     # hasn't been chosen and isn't the door we revealed
            new_choice = i                              # the user will be given the option to switch to this door

    print()
    print(f"""Before door {chosen_door}'s contents are revealed...
I'd like to show you that behind door {revealed_door} is laundry detergent.
Now, it's not too late to change doors.""")
    print()
    print(f'Would you like to switch from door {chosen_door} to door {new_choice}?')
    print()
    choice = input("Enter 'Y' to switch doors, or 'N' to stick with your first choice: ")
    options = ['y', 'n']
    while choice.lower() not in options:
        choice = input("Invalid input, please enter 'Y' or 'N': ")
    if choice.lower() == 'y':
        chosen_door = new_choice
        changeChoice += 1
    elif choice.lower() == 'n':
        chosen_door = chosen_door
        keepChoice += 1                                 # record if decision was to change or to keep the user's choice
    print()
    
    print(f'You chose door {chosen_door}.')             
    if chosen_door == prize_door:
        print('Congratulations! You have won the $10,000!')
        if choice.lower() == 'y':
            yesWins += 1
        elif choice.lower() == 'n':
            noWins += 1                                 # record if decision led to a win or a loss
    elif chosen_door != prize_door:
        print(f'How unfortunate, the cash prize was behind door {prize_door}.\nPlease enjoy the laundry detergent.')
    print()
    main_menu()


# create function that will simulate multiple games at once
def sim():
    global yesWins
    global noWins
    global keepChoice
    global changeChoice                                 # ensure the variables will be affected by the result of this game as well
    print()
    while True:
        try:
            repetitions = int(input('How many games should be simulated?: '))
            while repetitions <= 0:
                repetitions = int(input('Invalid input, please enter a positive integer: '))
            break
        except ValueError:
            print('Input not recognized.')
    doors = [1, 2, 3]
    for i in range(repetitions):                        # create loop to repeat the simulation n times as tasked by user
        prize_door = random.choice(doors)                   # assign a random number from 1-3 to be the door with 10k
        chosen_door = random.choice(doors)                  # simulate the user choosing a door
        revealed_door = 0                               
        new_choice = 0                                  
       
        for i in doors:                                     # relies on prize door and user's choice to find
            if i != prize_door and i != chosen_door:        # a door to reveal to user
                revealed_door = i                           
       
        for i in doors:                                     # relies on user's choice and revealed door to find
            if i != chosen_door and i != revealed_door:     # a door to give the user an option to switch to
                new_choice = i                              
       
        decision = random.choice([True, False])         # simulate user decision (either keeping or changing the choice)
        if decision == True:                            
            chosen_door = new_choice                    
            changeChoice += 1                                
        elif decision == False:                         
            chosen_door == chosen_door  
            keepChoice += 1                             # record if decision was to change or to keep the user's decision
        if chosen_door == prize_door:                   
            if decision == True:
                yesWins += 1
            elif decision == False:
                noWins += 1                             # record if decision led to a win or a loss
    print(f'Completed {repetitions} simulations.\nCumulative statistics will be displayed when you quit the game.')
    print()
    main_menu()

# create function that will display the cumulative statistics of results
def end_screen():
    if changeChoice == 0:                               # if/else statements ensure ZeroDivisionError does not occur                      
        switch_W_rate = '0.0%'
    else:
        switch_W_rate = (f'{(yesWins / changeChoice)*100:.1f}%')
    if keepChoice == 0:
        keep_W_rate = '0.0%'
    else:
        keep_W_rate = (f'{(noWins / keepChoice)*100:.1f}%')
    total_games = changeChoice + keepChoice
    total_wins = yesWins + noWins
    if total_games == 0:
        total_rate = '0.0%'
    else:
        total_rate = (f'{(total_wins / total_games)*100:.1f}%')    
     
    print(f"""{'Strategy':>15}{'|':^3}{'Games':^9}{'|':^3}{'Wins':^8}{'|':^3}{'Win Rate':<9}""")
    print('--------------------------------------------------')
    print(f"""{'Change Choice':>15}{'|':^3}{changeChoice:^9}{'|':^3}{yesWins:^8}{'|':^3}{switch_W_rate:<9}""")
    print(f"""{'Keep Choice':>15}{'|':^3}{keepChoice:^9}{'|':^3}{noWins:^8}{'|':^3}{keep_W_rate:<9}""")
    print('--------------------------------------------------')
    print(f"""{'Total':>15}{'|':^3}{total_games:^9}{'|':^3}{total_wins:^8}{'|':^3}{total_rate:<9}""")
    exit

# function that displays all options of program
def main_menu():
    print('Menu:')
    print(' (P) Play a live game')
    print(' (S) Simulate multiple games')
    print(' (Q) Quit')
    options = ['p', 's', 'q']
    menu_choice = input('Selection: ')
    while menu_choice.lower() not in options: 
        print('Menu choice not recognized.')
        print()
        print('Menu:')
        print(' (P) Play a live game')
        print(' (S) Simulate multiple games')
        print(' (Q) Quit')
        menu_choice = input('Selection: ')
    if menu_choice.lower() == 'p':
        play() 
    elif menu_choice.lower() == 's':
        sim()
    elif menu_choice.lower() == 'q':
        end_screen()
# calling the function that will start up game menu
main_menu()