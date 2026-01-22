import re

def check_password_strength(password):
    """
    Evaluate password strength based on security rules.
    Developed by: Renad Alshamrani
    """

    score = 0
    suggestions = []

    # Length check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        suggestions.append("Increase length to at least 8 characters.")

    # Digit check
    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("Add at least one number (0-9).")

    # Upper & lower case check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add lowercase letters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add uppercase letters.")

    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        suggestions.append("Add a special character (e.g., @, #, $).")

    # Final evaluation
    if score >= 6:
        level = "Strong"
    elif score >= 4:
        level = "Medium"
    else:
        level = "Weak"

    return {
        "strength": level,
        "score": f"{score}/7",
        "suggestions": suggestions
    }


if __name__ == "__main__":
    while True:
        print("\n" + "=" * 50)
        print(" Cybersecurity Tool: Password Strength Checker ")
        print("=" * 50)

        user_pwd = input("Enter password (or type 'exit' to quit): ")

        if user_pwd.lower() == "exit":
            print("Exiting... Stay safe! 🔐")
            break

        result = check_password_strength(user_pwd)

        print(f"\nPassword Strength: {result['strength']}")
        print(f"Security Score: {result['score']}")

        if result["suggestions"]:
            print("Suggestions:")
            for tip in result["suggestions"]:
                print(f"- {tip}")
