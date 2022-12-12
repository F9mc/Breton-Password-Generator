import random
import data.scrapper as sc

def password_generator(nb_words=3,separator="_"):
    dictionaire = sc.get_words()
    word = ""
    for n in range(nb_words):
        sep = "" if n == nb_words - 1 else separator
        word += random.choice(dictionaire) + sep
    return word

def main():
    print(password_generator())

if __name__ == "__main__":
    main()