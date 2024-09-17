#aiden clarke
#12/3/23
#create secure passwords

#imports 
import requests
import random
import string
import hashlib
#function to create custom sting of with citeria of lengh and charter upper lower maybee special??
def generate_password(length=12, uppercase=True, digits=True, special_chars=True):
    characters = string.ascii_lowercase
    if uppercase:
        characters += string.ascii_uppercase
    if digits:
        characters += string.digits
    if special_chars:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password
#check in a function for the unieness of a password 
def is_password_unique(password):
    api_url = f'https://api.pwnedpasswords.com/range/{hashlib.sha1(password.encode("utf-8")).hexdigest()[:5]}'
    response = requests.get(api_url)
#use hexdigest to split reponse out iff 200
    if response.status_code == 200:
        hashes = [line.split(':') for line in response.text.splitlines()]
        for h, count in hashes:
            if password.encode("utf-8") == h.encode("utf-8"):
                return False  # Password found in breaches
    else:
        print(f"Error checking password uniqueness: {response.status_code}")
#^parse out the reponse to see if response is uniqe 
    return True  # Password is unique
#main asking for what the cirteria of passwords will be 
def main():
    length = int(input("Enter the desired password length: "))
    uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    digits = input("Include digits? (y/n): ").lower() == 'y'
    special_chars = input("Include special characters? (y/n): ").lower() == 'y'

    while True:
        password = generate_password(length, uppercase, digits, special_chars)
        if is_password_unique(password):
            print(f'Your generated password: {password}')
            break
        else:
            print("Generated password is not unique. Generating a new one.")

if __name__ == "__main__":
    main()
