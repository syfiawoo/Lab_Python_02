number=input("Enter number to send: ")
reverse=0
while number>0:
    reverse=(reverse*10)+(number%10)
    number=number/10
    
print "Encrypted number is",reverse