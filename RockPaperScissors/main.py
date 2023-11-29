import random

options = ['rock', 'paper', 'scissors', 'lizard', 'spock']
name = input('What is your name? ')
print(f"Let's play {name}")

player_score = 0
computer_score = 0


def winner(player1, player2):
    if player1 == player2:
        return f"It's a tie"
    # player1 wins
    elif player1 == "rock" and player2 == "scissors":
        return f'Rock crushes scissors! {name} Wins!'
    elif player1 == "rock" and player2 == "lizard":
        return f'Rock crushes lizard! {name} Wins!'
    elif player1 == "scissors" and player2 == "paper":
        return f'Scissors cuts paper! {name} Wins!'
    elif player1 == "scissors" and player2 == "lizard":
        return f'Scissors decapitates lizard! {name} Wins!'
    elif player1 == "paper" and player2 == "rock":
        return f'Paper overs rock! {name} Wins!'
    elif player1 == "paper" and player2 == "spock":
        return f'Paper disproves Spock! {name} Wins!'
    elif player1 == "spock" and player2 == "rock":
        return f'Spock vaporizes rock! {name} Wins!'
    elif player1 == "spock" and player2 == "scissors":
        return f'Spock smashes scissors! {name} Wins!'
    elif player1 == "lizard" and player2 == "spock":
        return f'Lizard poisons Spock! {name} Wins!'
    elif player1 == "lizard" and player2 == "paper":
        return f'Lizard eats paper! {name} Wins!'

    # player2 wins
    elif player2 == "rock" and player1 == "scissors":
        return f'Rock crushes scissors! Computer Wins!'
    elif player2 == "rock" and player1 == "lizard":
        return f'Rock crushes lizard! Computer Wins!'
    elif player2 == "scissors" and player1 == "paper":
        return f'Scissors cuts paper! Computer Wins!'
    elif player2 == "scissors" and player1 == "lizard":
        return f'Scissors decapitates lizard! Computer Wins!'
    elif player2 == "paper" and player1 == "rock":
        return f'Paper overs rock! Computer Wins!'
    elif player2 == "paper" and player1 == "spock":
        return f'Paper disproves spock! Computer Wins!'
    elif player2 == "spock" and player1 == "rock":
        return f'Spock vaporizes rock! Computer Wins!'
    elif player2 == "spock" and player1 == "scissors":
        return f'Spock smashes scissors! Computer Wins!'
    elif player2 == "lizard" and player1 == "Spock":
        return f'Lizard poisons Spock! Computer Wins!'
    elif player2 == "lizard" and player1 == "paper":
        return f'Lizard eats paper! Computer Wins!'


def score(s):
    global player_score
    global computer_score
    if "Computer Wins!" in s:
        computer_score = computer_score + 1
    elif name in s:
        player_score = player_score + 1


want_to_play = 'y'
player = (input(f'{name}, choose from rock, paper, scissors, lizard, Spock: ')).strip().lower()
while want_to_play == 'y':
    if player in options:
        computer = random.choice(options)
        print(f"Computer's choice is {computer}")
        result = winner(player, computer)
        print(result)
        score(result)
        print(f"{name}: {player_score}")
        print(f"Computer: {computer_score}")
        want_to_play = input("Do you want another round? y/n ").strip()[0].lower()
        if want_to_play == 'y':
            player = (input(f'{name}, choose from rock, paper, scissors, lizard, Spock: ')).strip().lower()
            continue
        else:
            break
    else:
        player = input("Enter one of the options: rock, paper, scissors, lizard, Spock ")
        continue

print("Final score")
print(f"{name}: {player_score}")
print(f"Computer: {computer_score}")
