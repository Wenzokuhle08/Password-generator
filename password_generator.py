import random
import os

# This function is responsible for displaying  the menu options to the user
def display_menu():
    print("\nWelcome to the Password Generator!")
    print("1. Generate a password")
    print("2. View saved passwords")
    print("3. Quit")

# This function generates a random password for the user based on the users input  
def custom_password():
    lowercase_alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    uppercase_alphabets = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    special_characters = ['?','!','#','@','&','/']
    digits = ['0','1','2','3','4','5','6','7','8','9']
    
    # This line of code combines all the character sets into a single list
    total_chars = lowercase_alphabets + uppercase_alphabets + special_characters + digits
    
    try: 
        # This line of code prompt the user to enter their desired password length
        password_length= int(input("Enter the length of your password: "))
         # This code ensures the length of the password  meets the complexity requirements
        if password_length <= 3:
            print("Password must be at least 4 characters long for complexity.")
            return None
    
         # This code generates the random password of the specified length, as specified by the user
        random_password = "".join(random.choices(total_chars, k=password_length))
        print(f"Your password is, {random_password}")
        return random_password
    except ValueError:
        # This line if code handles an invalid input where the user happens  not to enter a numeric value
        print("Invalid input. Enter a numeric value")

# This function is responsible for saving the generated password to a file
def saved_password(password):
    try:
        # This code adds/saves  the password to a file named "passwords.txt"
        with open("passwords.txt", "a") as file:
            file.write(f"{password}\n")
        print("Password has been saved in 'passwords.txt'.")
    except Exception as e:
        # This line of code handles any file-related errors
        print(f"An error occurred while trying to save your password: {e}")

# This function is responsible for viewing all tthe previously saved passwords
def view_saved_passwords():
    try:
        if os.path.exists("passwords.txt"):
            # This code checks if the "passwords.txt" file exists
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
        # This line of code handles any file-related errors
        print(f"An error occurred while trying to retrieve your saved  passwords: {e}")
  
# This function is responsible for validating  the user's menu choice      
def validate_choice(choice):
    return choice in ["1", "2", "3"]
 
# Main function for the  the project                   
def main():
    while True:
        # This code displays the menu and prompts for the users input
        display_menu()
        choice = input("Enter your choice: ").strip()
        
        if validate_choice(choice):
            if choice == "1":
                 # This choice generates a password and optionally saves it
                password = custom_password()
                if password:
                    save = input("Would you like to save your password? (yes/no): ").strip().lower()
                    if save == "yes":
                        saved_password(password)
            elif choice == "2":
                 #This choice allows user to view saved passwords
                view_saved_passwords()
            elif choice == "3":
                # This choice allows user to exit the program
                print("Thank you for using the Password Generator!")
                break
        else: 
            # This code handles an invalid menu choice
            print("Wrong choice. Please try again.")
            



if __name__ == "__main__":
    main()
    # display_menu()
    # custom_password()