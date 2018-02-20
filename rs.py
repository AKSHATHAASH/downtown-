#r.p.s
import random
l=["rock","paper","cessor"]
computer=random.choice(l)
print("rock","paper","cessor")
user=input("enter your choice")
if computer==user:
    print("tie")
elif computer=="rock" and user=="paper":
    print("user wins")
elif computer=="paper" and user=="rock":
    print("computer wins")
elif computer=="paper" and user=="sessors":
    print("user wins")
elif computer=="sessors" and user=="paper":
    print("computer wins")
elif computer=="sessors" and user=="rock":
    print("user wins")
else:
    print("you lost")
