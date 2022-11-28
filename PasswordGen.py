import random
import string

passlen = int(input("Enter the length of your password:"))

letters_upper = string.ascii_uppercase
letters_lower = string.ascii_lowercase
numbers = string.digits
exc = "!"
pw = letters_lower + letters_upper + numbers

password = "Your new password is: " + "".join(random.sample(pw, passlen - 1)) + "!"
print(password)
