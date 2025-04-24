import re #built in module
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None
def main():
    email = input("Enter email address for verification: ")
    if is_valid_email(email):
        print("Valid email address.")
    else:
        print("Invalid email address.")    
if __name__=="__main__":
    main()    
