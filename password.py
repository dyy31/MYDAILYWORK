import random
import string

def generate_password(length, use_uppercase=True, use_lowercase=True, use_digits=True, use_punctuation=True):
    # Initialize the possible characters to include in the password
    characters = ""
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_punctuation:
        characters += string.punctuation
    
    # Ensure that at least one character set is selected
    if not characters:
        raise ValueError("At least one character type must be selected!")
    
    # Generate the password
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

def main():
    # Get the desired password length from the user
    length = int(input("Enter the desired length of the password: "))
    
    # Get user preferences for complexity
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_punctuation = input("Include punctuation? (y/n): ").lower() == 'y'
    
    # Generate the password based on user preferences
    try:
        password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_punctuation)
        # Display the generated password
        print(f"Generated Password: {password}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
