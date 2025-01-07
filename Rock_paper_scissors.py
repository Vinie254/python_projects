import random

def play():
        limit = 10
        tries = 0
        computer_win =0
        player_win =0
        number_of_ties =0
        while tries < limit:
            user1 = input("Rock, paper, scissors?: ")
            print(f"Your choice is {user1}")

            user2 = random.choice(['rock', 'scissors', 'paper'])
            print(f"The computer chose: {user2}")
            tries += 1
            if user1 == user2:
                print("That is a tie")
                number_of_ties +=1
            elif is_win(user1,user2):
                print("You have won")
                player_win +=1
            else:
                print("You have lost")
                computer_win +=1
        if player_win > computer_win:
            print(f"You are the overall winner with {player_win} wins")
        elif player_win == computer_win:
            print("There was a tie")
        else:
            print(f"The computer is the overall winner with {computer_win} wins")
def is_win(player,opponent):
    if(player == 'rock' and opponent == 'scissors') or (player == 'scissors' and opponent == 'paper') or (player == 'paper' and opponent == 'rock'):
        return True

print(play())