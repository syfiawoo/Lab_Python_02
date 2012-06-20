number=input("Enter number to send: ")
num_copy=number
new_num=0
i=0
reverse=0
while num_copy>0:
    digit=num_copy%10
    new_num=((digit+7)%10)*(10**i)+ new_num
    num_copy=num_copy/10
    
    reverse=(reverse*10)+new_num/(10**i)
    i=i+1
    
print "Encryption process:",number,"==>",new_num,"==>", reverse