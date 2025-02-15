
import random

print("INTRUCTIONS:\nMAX POINTS IS 21, EACH PLAYER CAN ROLL AS MANY TIMES THEY WANT \nBUT IF THEY SCORE MORE THAN 21 THEY LOSE :( \nPLAYER WITH 21 or BIGGEST SCORE WINS!")

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

while True: 
    players = input("\nHOW MANY PLAYERS(max. 4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("MUST BE 2 - 4 PLAYERS!")
    else:
        print("MUST BE A NUMBER! TRY AGAIN!\n")

player_scores = [0 for _ in range(players)]
n = 1

while n < players:

    for player_index in range(players):
        current_score = 0

        print("\nTURN OF PLAYER", player_index + 1, ":")
        
        value = roll()
        current_score += value
        print("YOU GOT A ", value)
        print("SCORE: ", current_score)
        player_scores[player_index] += current_score

        while True:
            roll_again = input("WANNA ROLL AGAIN?(Y or N): ")

            if roll_again.lower() == "n":
                break

            elif roll_again.lower() == "y":
                new_roll = roll()
                current_score += new_roll            
                print("YOU GOT A ", new_roll)
                print("SCORE: ", current_score)
                player_scores[player_index] += current_score
            
                if current_score == 21:
                    print("\nPlayer", player_index + 1, "WON!!!!")
                    exit()
                elif current_score > 21:
                    print("\nYOU OVER PASS MAX SCORE, YOU LOST")
                    break
                
                else:
                    continue

            else:
                print("MUST BE Y OR N, TRY AGAIN!!")
                
        n += 1

max_score = max(player_scores)
winner = player_scores.index(max_score)
#if max_score > 21:

    
print("Player", winner + 1, "WON BECUASE HAD THE MOST SCORE!!")
