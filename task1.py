import random
import string

def generate_password(length, include_uppercase=True, include_digits=True, include_special=True):
    if length <= 0:
        return "Password length must be a positive integer."
    characters = string.ascii_lowercase
    
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_digits:
        characters += string.digits
    if include_special:
        characters += string.punctuation
        
    if not (include_uppercase or include_digits or include_special):
        return "At least one character type must be included."
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("The length must be a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
           
    include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    include_digits = input("Include digits? (y/n): ").lower() == 'y'
    include_special = input("Include special characters? (y/n): ").lower() == 'y'
         
    password = generate_password(length, include_uppercase, include_digits, include_special)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
