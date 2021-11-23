#Password Manager extended Modify question 5 so it will only allow three attempts, on the third attempt, present the message "Max attempts reached, account BLOCKED"

password = ""
count = 0

while (password != "abc123") and (count <3):
  password = input("Enter password:-")
  count+=1
  print("you have tried ",count,"times")
  if count ==3:
    print("ACCOUNT BLOCKED")

print("This is after while loop")

