n = int(input("Enter the nummber : "))

for i in range (2,n):
    if(n%2)==0:
        print("Number is not prime number")
        break
    else:
        print("Number is prime number")