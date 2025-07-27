
# Simple Command-Line Login and Registration System

This Python script implements a basic console-based system for user management, allowing a single user to register an account, log in, and reset their password.

-----

## Features

  * **User Registration**: Allows a user to create an account by providing their name, email, address, phone number, and a password. It includes basic validation to ensure the phone number is 10 digits and the password is at least 8 characters long.
  * **User Login**: Authenticates a user based on their registered email and password. Upon successful login, it displays the user's stored personal information.
  * **Password Recovery**: Provides a mechanism to reset the password by verifying the registered email address.
  * **In-Memory Data Storage**: All user information is stored in variables while the script is running.

-----

## Getting Started

Follow these steps to get the system up and running on your local machine.

### Prerequisites

  * Python 3.x installed on your system.

### Installation

1.  **Save the Script**: Copy and paste the provided Python code into a file named, for example, `login_register.py`.

2.  **Run the Script**: Open your terminal or command prompt, navigate to the directory where you saved the file, and execute the script using the Python interpreter:

    ```bash
    python login_register.py
    ```

-----

## How to Use

Once the script starts, you will be presented with the main menu:

```
-----WELCOME TO THE LOGIN PAGE MENU -----

1. REGISTER
2. LOGIN
3. FORGOT PASSWORD / PASSKEY
4. EXIT
ENTER YOUR CHOICE (1 TO 4):
```

### 1\. REGISTER

  * Choose option `1`.
  * You will be prompted to enter your `Name`, `Email`, `Address`, `Phone Number` (must be 10 digits), and `Password` (at least 8 characters).
  * The system will confirm successful registration or prompt for valid input if validation rules are not met.
  * **Note**: This system currently supports registration for only **one user**. If a user is already registered, this option will indicate so.

### 2\. LOGIN

  * Choose option `2`.
  * Enter your registered `Email` and `Password`.
  * If the credentials are correct, you will be logged in, and your stored details will be displayed.
  * If no user is registered or the credentials are incorrect, an appropriate message will be shown.

### 3\. FORGOT PASSWORD / PASSKEY

  * Choose option `3`.
  * Enter your registered `Email`.
  * If the email matches a registered account, you will be prompted to enter a `New Password/Passkey` (minimum 8 characters).
  * The password will be updated if the new input meets the length requirement.

### 4\. EXIT

  * Choose option `4` to terminate the application.

-----
