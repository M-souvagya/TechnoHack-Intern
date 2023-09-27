#   Rock, paper, scissors game
import random

def game(ui,ci):
    if ui==ci:
        print("It's a tie !!" )
        print(f'As you choosed {ui} and computer choosed {ci}')
    elif ui=='rock' and ci=='paper':
        print("computer wins !!")
        print(f'As computer choosed {ci} and you choosed {ui}')
    elif ui=='rock' and ci=='scissor':
        print('You won !!')
        print(f'As you choosed {ui} and computer choosed {ci}')
    elif ui=='paper' and ci=='scissor':
        print("computer wins !!")
        print(f'As computer choosed {ci} and you choosed {ui}')
    elif ui=='paper' and ci=='rock':
        print('You won !!')
        print(f'As you choosed {ui} and computer choosed {ci}')
    elif ui=='scissor' and ci=='rock':
        print("computer wins !!")
        print(f'As computer choosed {ci} and you choosed {ui}')
    elif ui=='scissor' and ci=='paper':
        print('You won !!')
        print(f'As you choosed {ui} and computer choosed {ci}')

def user_input():
    ui=input("Enter your choice(rock/paper/scissor):") #ui= user input
    inputs=['rock','paper','scissor']
    ci=random.choice(inputs)                        #ci= computer input
    game(ui,ci)
    
x=True
while x==True:
    user_input() 
    y=input('Do you want to play again? ')
    y=y.upper()
    if y=='YES' or y=='Y':
        x=True
    else :
        print("\n\n--- Thank You ---\n\n")
        break

        
