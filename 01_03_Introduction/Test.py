p=10000
n=12
r=0.08
t=input("Number of years? ")
print("n*t: ",n*t)
print("r/n+1: ",(r / n)+1)
A=int(p*(1+(r / n))**(n*t))

print("Result is: ",A)