class RPS:
    def __init__ (self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2

    def game(self):
        if player_1 == "rock" and player_2 == "scissors":
            print("Player_1 win game")
        elif player_1 == "scissors" and player_2 == "rock":
            print("Player_2 win game")
        elif player_1 == "rock" and player_2 == "paper":
            print("Player_2 win game")
        elif player_1 == "scisccors" and player_2 == "paper":
            print("Player_1 win game")
        elif player_1 == "paper" and player_2 == "rock":
            print("Player_1 win game")
        elif player_1 == "paper" and player_2 == "scissors":
            print("Player_2 win game")
        else:
            print("draw")



if __name__ == "__main__":
    while True:
        player_1 = input('Player1: Choose Rock, paper or scissors')
        if player_1 not in ('rock', 'paper', 'scissors'):
            print('enter valid option')
            continue
        player_2 = input('Player2: Choose Rock, paper or scissors')
        if player_2 not in ('rock', 'paper', 'scissors'):
            print('enter valid option')
            continue
        else:
            break

    game = RPS(player_1,player_2)
    game.game()


