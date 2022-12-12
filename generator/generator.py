import random

def password_generator():
    return random.randint(1000,9999)

def main():
    print(password_generator())

if __name__ == "__main__":
    main()