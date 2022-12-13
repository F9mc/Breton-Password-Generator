import random

from numpy import number
import data.scrapper as sc

def password_generator(nb_words=3,separator="_",numbers=True,campitalize=True):
    dictionaire = sc.get_words()
    word = ""
    index_number = None
    if numbers:
        index_number = random.randint(0,nb_words - 1)

    for n in range(nb_words):
        sep = "" if n == nb_words - 1 else separator
        if campitalize:
            word += random.choice(dictionaire).capitalize()
        else:
            word += random.choice(dictionaire)
        if n == index_number:
            word += f"{random.randint(0,9)}"
        word += sep

    return word


if __name__ == "__main__":
    print(password_generator())