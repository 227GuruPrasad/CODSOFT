import random
import string

def generate_password(length):
    # Define the possible characters in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password using the specified length
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

def main():
    print("Password Generator")
    
    # Prompt the user to specify the desired length of the password
    try:
        length = int(input("Enter the desired length of the password: "))
        
        if length < 1:
            print("Password length should be at least 1.")
            return
        
        # Generate the password
        generated_password = generate_password(length)
        
        # Display the generated password
        print(f"Generated Password: {generated_password}")
        
    except ValueError:
        print("Please enter a valid number for the password length.")

if __name__ == "__main__":
    main()
