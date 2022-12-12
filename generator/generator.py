import random

def get_word():
    word = "" 
    for i in range(random.randint(3,7)):
        word += chr(random.randint(ord("a"),ord("z")))
    return word

def password_generator(nb_words=3,separator="_"):
    word = ""
    for n in range(nb_words):
        sep = "" if n == nb_words - 1 else separator
        word += get_word() + sep
    return word

def main():
    print(password_generator())

if __name__ == "__main__":
    main()