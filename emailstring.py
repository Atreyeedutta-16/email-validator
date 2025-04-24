import re
def is_valid_email(email):
    pattern = '^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None
def main():
    emails = input("Enter email addresses seperated by commas: ")
    email_list = [email.strip() for email in emails.split(",")]
    for email in email_list:
        if is_valid_email(email):
            print(f"{email}--> Valid")
        else:
            print(f"{email}--> Invalid")    
if __name__=="__main__":
    main()             