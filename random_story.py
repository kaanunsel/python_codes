import random

subjects = {"Racoons" : "p", "Grandma" : "s", "Ahmet" : "s"}
s_verbs = ["is","will","was"]
p_verbs = ["are","were","are going to"]
verbs = ["kill","peel","love"]
objs = ["tree","desk","books"]

def get_subject(dic):
    s = random.choice(list(dic.keys()))
    return s
    
def get_averb(sub,sverb,pverb):
    sub_type = subjects[sub]
    if sub_type == "p":
        v = random.choice(p_verbs)
    else:
        v = random.choice(s_verbs)
    return v        

while True:
    subject = get_subject(subjects)
    averb = get_averb(subject,s_verbs,p_verbs)
    verb = random.choice(verbs)
    obj = random.choice(objs)
    print(subject,"",averb,"",verb,"",obj)
    i = input("Please type N for a new story. Type E to exit the program.")
    
    if i == "N":
        continue
    else:
        break
            