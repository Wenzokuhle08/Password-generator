import random
# import OS 


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
    
    
    password_length= int(input("Enter the length of your password: "))
    
    if password_length <= 0:
        return password_length
    
    random_password = "".join(random.choices(total_chars, k=password_length))
    print(f"Your password is, {random_password}")
    
   
    
    
    
    
if __name__ == "__main__":
    display_menu()
    custom_password()
    # display_menu()