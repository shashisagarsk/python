import random
import tkinter
def check(comp,user):
    if comp==user:
        return 0

    if(comp==0 and user==1):
        return -1
    
    if(comp==1 and user==2):
        return -1    
    
    if(comp==2 and user==0):
        return -1
    return 1
comp=random.randint(0,2)
user=int(input("0 for snack,:\n1 for water,:\n2 for gun:\n"))
score=check(comp,user)
print("you", user)
print("computer",comp)
if (score==0):
    print("its a drwa")
elif (score==-1):
    print("you lose")
else:
    print("You won")





