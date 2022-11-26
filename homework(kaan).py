prompt_1 = "Please enter the board size\n"
prompt_2 = "Please enter how many squares you want to place\n"
prompt_3 = "Please enter the coordinates of a square you want to place\n"
prompt_4 = "Please enter a target square coordinate, or enter exit to exit\n"
prompt_5 = "Congratulations, you won!"
prompt_6 = "Thanks for playing."
error_message_1 = "Improper board size"
error_message_2 = "Improper amount of squares"
error_message_3 = "Incorrect input format for square coordinates"
error_message_4 = "Improper square coordinates"
error_message_5 = "Sign already placed to square"


# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

def isInt(inp):
    inp.strip()
    for i in inp.split():
        try:
            int(i)
        except:
            return False
    return True       

def isCoor(coords,n):
    for i in coords[0:2]:
        if i<1 or i>n:
            return False
    return True    


board_number = int(input(prompt_1))
n = board_number
all_cors = []

for i in range(1,n+1):
    for j in range(1,n+1):
        all_cors.append([i,j])
        all_cors.append(0)

while(board_number<5 or board_number>9):
    print(error_message_1)
    board_number=int(input(prompt_1))

square = int(input(prompt_2))

while(square<1 or square>(board_number**2)):
    print(error_message_2)
    square = int(input(prompt_2))

coord = []
cor_list = []

for _ in range(square):
    inp = input(prompt_3)

    while isInt(inp) == False:
        print(error_message_3)
        inp = input(prompt_3)
        
    coord = [int(i) for i in inp.split()[0:2]]

    while isCoor(coord,board_number) == False:
        print(error_message_4)
        inp = input(prompt_3)
        coord = [int(i) for i in inp.split()[0:2]]

    if coord in cor_list:
        print(error_message_5)    
        continue
    
    cor_list.append(coord)

    print("  ",end="")
    for i in range(1,n+1):
        print(i,end=" ")    
    print()
    for i in range(1,n+1):
        print(i,end=" ")
        for j in range(1,n+1):
            if [i,j] in cor_list:
                a = all_cors.index([i,j])
                all_cors[a+1] = 1
                print("+",end=" ")
            else:
                print("-",end=" ")
        print()

while True:
    target_squares = []
    target_s = input(prompt_4)
    if target_s.strip().lower() == "exit":
        print(prompt_6)
        break
    target = [int(i) for i in target_s.strip().split()]
    for i in range(-1,2):
        target_squares.append([(target[0]+i),(target[1]+i)])
    for i in range(-1,2):
        target_squares.append([(target[0]+(i*-1)),(target[1]+(i))])
    target_squares.remove(target)
    for b in all_cors:
        if b in target_squares:
            a = all_cors.index(b)
            all_cors[a+1] = 0 if all_cors[a+1] == 1 else 1

    print("  ",end="")
    for i in range(1,n+1):
        print(i,end=" ")    
    print()
    for i in range(1,n+1):
        print(i,end=" ")
        for j in range(1,n+1):
            x = all_cors.index([i,j])
            if all_cors[x+1] == 1:
                print("+",end=" ")
            else:
                print("-",end=" ")
        print()

    for i in range(1,(2*(board_number**2))+1,2):
        if all_cors[i] == 1:
            break
    else:
        print(prompt_5)
        print(prompt_6)
        break        


# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
