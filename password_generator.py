import random
import os


def display_menu():
    print("\nWelcome to the Password Generator!")
    print("1. Generate a password")
    print("2. View saved passwords")
    print("3. Quit")
    
def custom_password():
    lowercase_alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    uppercase_alphabets = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    special_characters = ['?','!','#','@','&','/']
    digits = ['0','1','2','3','4','5','6','7','8','9']
    
    total_chars = lowercase_alphabets + uppercase_alphabets + special_characters + digits
    
    try: 
        password_length= int(input("Enter the length of your password: "))
        if password_length <= 3:
            print("Password must be at least 4 characters long for complexity.")
            return None
    
    
        random_password = "".join(random.choices(total_chars, k=password_length))
        print(f"Your password is, {random_password}")
        return random_password
    except ValueError:
        print("Invalid input. Enter a numeric value")

def saved_password(password):
    try:
        with open("passwords.txt", "a") as file:
            file.write(f"{password}\n")
        print("Password has been saved in 'passwords.txt'.")
    except Exception as e:
        print(f"An error occurred while trying to save your password: {e}")

def view_saved_passwords():
    try:
        if os.path.exists("passwords.txt"):
            with open("passwords.txt", "r") as file:
                passwords = file.readlines()
                if passwords:
                    print("\nStored Passwords:")
                    for index, password in enumerate(passwords, start=1):
                        print(f"{index}. {password.strip()}")
                else: 
                    print("\nNo passwords have been saved")
        else:
            print("\nNo passwords have been saved")
    except Exception as e:
        print(f"An error occurred while trying to retrieve your saved  passwords: {e}")
        
def validate_choice(choice):
    return choice in ["1", "2", "3"]
                        
def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()
        
        if validate_choice(choice):
            if choice == "1":
                password = custom_password()
                if password:
                    save = input("Would you like to save your password? (yes/no): ").strip().lower()
                    if save == "yes":
                        saved_password(password)
            elif choice == "2":
                view_saved_passwords()
            elif choice == "3":
                print("Thank you for using the Password Generator!")
                break
        else: 
            print("Wrong choice. Please try again.")
            



if __name__ == "__main__":
    main()
    # display_menu()
    # custom_password()