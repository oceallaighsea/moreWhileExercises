# Date and name
# whileQ2.py
# Using a while loop - Ask the user for 10 numbers,
# add the numbers together, print out the final answer.

count = 0
answer =0
while count <10 :
    #print(count)
    # Get a number from the user and put it in variable
    aNumber = int(input("Enter a number"))
    answer += aNumber
    count += 1
    
print("The sum of the numbers are", answer)
