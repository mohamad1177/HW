import sympy  as sp

n=int(input("Enter number of partial summation  "))
x=sp.Symbol("x")

denominator=0
Sum=0
j=0
for i in range(1,n+1):
    j+=1
    denominator=0
    while i>0:
        denominator=denominator+(i*(x**i))
        i=i-1
        
    print(denominator)
    if j%2==0:
        denominator=-denominator
        
    Sum= Sum +(1/(denominator))
    #denominator=0
    

print("partial summation of series equal to",Sum)
print("simplify summationequal to",sp.simplify(Sum))
