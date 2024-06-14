def f(money,interest,month):
    ans=0
    for i in range(month):
        ans=ans+money*(1+interest/100)**(month-i)
    return ans
print(f(100,10,3))