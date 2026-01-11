# Password Strength Checker (Python) 🛡️

## Description
A Python-based tool designed to evaluate the strength of passwords based on security best practices. It provides real-time feedback on password complexity and security levels.

## Key Features
* **Length Validation:** Checks if the password meets the minimum length requirements.
* **Character Diversity:** Verifies the presence of Uppercase, Lowercase, Numbers, and Special characters.
* **Security Rating:** Categorizes passwords into (Weak, Medium, Strong, or Very Strong).
* **Feedback System:** Provides specific tips to improve the password.

## Technologies Used
* **Language:** Python
* **Modules:** `re` (Regular Expressions for pattern matching)

## How It Works
The tool uses **Regular Expressions (Regex)** to scan the input string for:
1. At least 8 characters.
2. At least one digit (0-9).
3. At least one uppercase letter (A-Z).
4. At least one lowercase letter (a-z).
5. At least one special character (!@#$%^&*).
