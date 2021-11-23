#Password Manager Use a While loop to ask the user for a password when the password is correct == "abc123" print Correct Password

password = ""
count =0

while password != "abc123":
  if count ==3:
    break
  password = input("Enter password:-")
  count+=1


print("This is after while loop")