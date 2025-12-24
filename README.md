# Password Checker

A Python based password strength checker that evaluates how secure a password is based 
on common best security practices.

WARNING: This project is a work in progress and under active development.



## Features
  - Checks password length
  - Validates use of uppercase and lowercase letters
  - Detects numbers and special characters
  - Provides security score percentage based on the above checks ^
  - Provides information on how many characters, lowercase letters, uppercase letters,
    numbers, and special characters are within the given password 
  - Simple graphical user interface built with Tkinter



## Upcoming Features
  - Allow users to use super+a to select all characters at character limit
  - Improved UI design
  - Provide password suggestions with security improvements that may have been lacking
  - Make some criteria worth more than others instead of them being all equal weight
    when calculating security score percentage
  - Establish an array of common passwords and if user inputs one of these passwords
    the security score immediately sets to 0%



## How To Run
  1. Clone the repository
  2. Ensure python-tk is installed on your system
  3. Within the downloaded repository directory, execute "python3 passwordChecker.py"
     in terminal
