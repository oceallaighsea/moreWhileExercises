#Password Manager Use a While loop to ask the user for a password when the password is correct == "abc123" print Correct Password

password = ""
#passValue = "abc123"
passValue = input("Enter password to sotre")

while password != passValue:
  password = input("Confirm password:-")
  if password == passValue:
    print("Correct Password")
print("This is after while loop")