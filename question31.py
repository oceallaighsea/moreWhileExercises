# Using a while Loop to show the following on the
#screen 1+2+3+4+5+6+7+8+9+10=answer
## Date and name
# whileQ3.py

count = 1
answer =0
while count <=10 :
    #print(count)
    if count <10:
        print(count, end = "+")
    else:
        print(count, end = "=")
    answer += count
    count += 1
    
print(answer)

# How can you also do the same thing with only one print statement, there are a number of ways.
