import re

def check_password_strength(password):
    """
    Function to evaluate the strength of a password based on common security standards.
    Developed by: Renad Alshamrani
    """
    strength = 0
    feedback = []
    
    # 1. Check length (Minimum 8 characters)
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password is too short (minimum 8 characters).")
    
    # 2. Check for numbers
    if re.search(r"\d", password):
        strength += 1
    else:
        feedback.append("Add at least one digit (0-9).")
    
    # 3. Check for uppercase and lowercase letters
    if re.search(r"[a-z]", password) and re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Mix both uppercase and lowercase letters.")
    
    # 4. Check for special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        feedback.append("Add at least one special character (e.g., @, #, $, %).")

    # Final Result Logic
    print("-" * 30)
    if strength == 4:
        return "Result: Strong Password (Excellent Security)"
    elif strength == 3:
        return f"Result: Medium Password. \nSuggestions: {' '.join(feedback)}"
    else:
        return f"Result: Weak Password! \nRequirements: {' '.join(feedback)}"

# Interactive User Input
# --- This is the Loop section ---
if __name__ == "__main__":
    while True: # This starts the continuous loop
        print("\n" + "="*45)
        print("   Cybersecurity Tool: Password Strength Checker")
        print("="*45)
        
        # Ask user for input
        user_pwd = input("Enter a password to evaluate (or type 'exit' to quit): ")
        
        # Check if the user wants to close the program
        if user_pwd.lower() == 'exit':
            print("Exiting... Stay safe!")
            break
            
        # Run the strength checker function
        result = check_password_strength(user_pwd)
        print(result)