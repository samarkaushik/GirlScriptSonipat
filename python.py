#a is total balance
#b is amount to be withdrawn
a,b=input("enter the values").split( )
a=int( a)
b=int (b)
if a<b :
    print("your balance is",a)
else :
    c=a-b-0.5 
    print("your transaction is successful ,current balance is",c)
    
    
    
    
    


