#this is a simple rock paper scissors


rps1 = 'rock'
rps2 = 'paper'
rps3 = 'scissor'

player1_score = 0
player2_score = 0

#The beginning of the grampro
print(f'Welcome to the Rock, Paper Scissors game.')
print("")
print("")
player1_name = input(f'Please enter the name of player 1. ')
print("")
print("")
player2_name = input(f'Please enter the name of player 2. ')
print("")
print("")
print("""If you are unfamiliar with the Rock, Paper, Scissors game,
 the rules are simple:
 Rock Beats Scissors
 Scissors Beats Paper
 Paper Beats Rock
 Your objective is to choose the winning hand.""")
print("")
print("")
begin = input(f"Are both players ready to begin? (Y/N)").lower()
if begin == 'y':
    print(f"Let's get started then shall we!")
else:
    print("Thank you for considering playing!")

print("")
print("")
print(f"let's get into the first game!")
print("")
print("")
print("Your options are Rock, Paper or Scissors")
#player 1 input
while True:
    player1_play = input(f'{player1_name} What would you like to throw? ').lower()
    if player1_play == 'rock':
        player1_play = rps1
        break
    elif player1_play == 'paper':
        player1_play = rps2
        break
    elif player1_play == 'scissors':
        player1_play = rps3
        break
    else:
            print("I didn't understand that input. Please select again.")
print("""



""")
#player 2 input
player2_play = input(f"{player2_name} What would you like to throw? ").lower()
while True:
    player2_play = input(f'{player2_name} What would you like to throw? ').lower()
    if player2_play == 'rock':
        player2_play = rps1
        break
    elif player2_play == 'paper':
        player2_play = rps2
        break
    elif player2_play == 'scissors':
        player2_play = rps3
        break
    else:
        print("I didn't understand that input. Please select again.")

#the brains of the game
#win conditions
if player1_play == player2_play:
    print("A draw!")
    print("No one wins this game!")
elif player1_play == rps1 and player2_play == rps2:
    print(f"""The score sits at:
    {player1_name} with {player1_score} points, and
    {player2_name} with {player2_score} points.""")
    print(f"{player2_name} wins! ")
    player2_score += 1
elif player1_play == rps2 and player2_play == rps3:
    print(f"""The score sits at:
    {player1_name} with {player1_score} points, and
    {player2_name} with {player2_score} points.""")
    print(f"{player2_name} wins! ")
    player2_score += 1
    print("")
    print("")

elif player1_play == rps3 and player2_play == rps1:
    print(f"""The score sits at:
    {player1_name} with {player1_score} points, and
    {player2_name} with {player2_score} points.""")
    print(f"{player2_name} wins! ")
    player2_score += 1
elif player1_play == rps1 and player2_play == rps3:
    print(f"""The score sits at:
    {player1_name} with {player1_score} points, and
    {player2_name} with {player2_score} points.""")
    print(f"{player1_name} wins! ")
    player1_score += 1
elif player1_play == rps2 and player2_play == rps1:
    print(f"""The score sits at:
    {player1_name} with {player1_score} points, and
    {player2_name} with {player2_score} points.""")
    print(f"{player1_name} wins! ")
    player1_score += 1
elif player1_play == rps3 and player2_play == rps2:
    print(f"""The score sits at:
    {player1_name} with {player1_score} points, and
    {player2_name} with {player2_score} points.""")
    print(f"{player1_name} wins! ")
    player1_score += 1
else:
    print(f"{player1_name}, {player2_name} Did y'all choose something?")

end_game = input("Do you want to play again? (Y/N)").lower()
if end_game == 'y':
    print("Great! Let's keep going.")
elif end_game == 'n':
    print("Thank you for playing!")
else:
    print(f"I did not understand that input. Please select again.")













