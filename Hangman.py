import random

random_words = ["ATIL","HOCAM","BOĞAZİÇİNDEN","SELAMLAR"]
word = random.choice(random_words)
list_word = list(word)
list_q = ["-" for i in range(len(word))]
try_left = 10

name = input("Name: ")
print(f"Hello {name}. Time to play hangman!")

def findindex(liste,elem):
    index_list = []
    index_num = 0
    while True:
        try:
            index_num = liste.index(elem,index_num)
        except:
            break
        index_list.append(index_num)
        index_num += 1
        if(index_num > len(liste) - 1):
            break
    liste = list(liste)    
    return index_list    

while(try_left>0):      
    for i in range (len(list_q)):
        print(str(list_q[i]))
    if(list_q == list_word):
        break     
    print(f"You have left {try_left} try")
    
    ans = input("Please guess a letter: ").upper()

    if(ans in list_word):
        for a in findindex(list_word,ans):
            list_q[a] = ans
    else:
        try_left -= 1
        
if(list_q == list_word):
    print("Congratulations! You Won!")
    input()
else:        
    print("No try left... You lost!")
    input()                      