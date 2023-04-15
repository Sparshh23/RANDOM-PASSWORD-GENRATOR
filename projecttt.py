import string
import random

def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
     
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password


while True:
    try:
        length = int(input("Enter the length of the password: "))
        break
    except ValueError:
        print("Please enter a valid integer.")
        

password = generate_password(length)
print("Random password: ", password)
