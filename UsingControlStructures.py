theInput = raw_input("Enter an integer: ")
#Your code here
theInput=int(theInput)
print theInput
print "--------------------\nQ5."
if theInput%2==0:
    print "even"
else:
    print "odd"
    
print "----------------------\nQ6."
primarySchoolAge=4
legalVotingAge=18
presidentAge=40
retirementAge=60
personsAge=input("Enter an age: ")

if personsAge<primarySchoolAge:
    print "Too young" 
else:
    if personsAge>=legalVotingAge:
        print "Remember to vote"
    if personsAge>=presidentAge:
        print "Vote for me"
    elif personsAge<presidentAge:
        print "You can't be president"
    if personsAge>=retirementAge:
        print "Too old"
        
print "----------------------\nQ7."
i=40
while i>=0:
    if i%3==0:
        print i
    i=i-1
    
print "----------------------\nQ8."
for i in range(6,30):
    if i%2==0 or i%5==0 or i%5==0:
        ""
    else:
        print i
        
        
print "----------------------\nQ9."
n=1
while (79*n)%97!=1:
    n=n+1

print n
    


        
        
