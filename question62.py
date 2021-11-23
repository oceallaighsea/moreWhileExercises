#Password Manager extended Modify question 5 so it will only allow three attempts, on the third attempt, present the message "Max attempts reached, account BLOCKED"

password = ""
count = 0

while count < 3:
  password = input("Enter password")
  if password == "abc123":
    print("Correct password")
    break
  else:
    print("Incorrect PAssword")
  count = count +1 

print("After the loop")