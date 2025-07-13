email = input("Enter your email")
confirm_email = input("Confirm Your Email:")
has_lower = False
has_digit = False
has_at = "@" in email
has_dot = "." in email
no_space = "" in email
has_gmail = "gmail.com" in email
start_fine = not(email.startswith("@") or email.startswith("."))

for char in email:
    if char.islower():
        has_lower = True
    elif char.isdigit(): 
        has_digit = True
        
       
        
        
        
if email !=confirm_email:
    print("Emails Do not match ")

# elif all([has_lower, has_digit, has_at, has_dot, no_space, start_fine , has_gmail]):
    
#     print("✅ Valid email")
elif email.isupper():
       print("Your Email is in upper case. Consider it in lowecase")
        
    
else:
    print("❌ Invalid email.")
