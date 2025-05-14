Bnumber = int(input("input number goes over here"))
digits = len(str(Bnumber))
result=0

temp = Bnumber
while temp > 0:
    d = temp %10
    result+=digits * (2 ** result)
    temp //=10

if Bnumber== result:
    print(Bnumber,"is an armstrong number")
else:
    print(Bnumber,"is not an Armstrong number")