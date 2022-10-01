import random

def judge(player,ai):
    if player==ai:
        return "Draw"
    elif (player=="rock" and ai=="scissors") or (player=="paper" and ai=="rock") or (player=="scissors" and ai=="paper"):
        return True
    else:
        return False
print("You don't have any friends to play rock paper scissors? Then you are in the right place!\nLet's play!")        
while True:
    move = input("You first, I've closed my eyes ;)\n").lower()
    moves = ["rock","scissors","paper"]
    ai_move = random.choice(moves)
    if judge(move,ai_move) == True:
        print("You: ", move.upper()," AI: ",ai_move.upper(),"\nYOU WIN!\n")
    elif judge(move,ai_move) == "Draw":
        print("You: ", move.upper()," AI: ",ai_move.upper(),"\nDRAW\n")
    else:
        print("You: ", move.upper()," AI: ",ai_move.upper(),"\nYOU HAVE LOST\n")
    