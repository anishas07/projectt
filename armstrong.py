number = int(input("input number goes over here"))
digits = len(str(number))
result=0

temp = number
while temp > 0:
    d = temp %10
    result+=d**digits
    temp //=10

if number== result:
    print(number,"is an armstrong number")
else:
    print(number,"is not an Armstrong number")
    
