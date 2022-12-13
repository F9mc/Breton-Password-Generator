import random
import data.scrapper as sc
import os
from dotenv import load_dotenv

def password_generator(nb_words=3,separator="_",numbers=True,capitalize=True):
    if type(nb_words) != int:
        raise Exception("Number of words must be int")
    if type(separator) != type("_"):
        raise Exception("Separator must be a string")
    if type(numbers) != bool:
        raise Exception("Number variable must be a boolean")
    if type(capitalize) != bool:
        raise Exception("Capitalize variable must be a boolean")
    
    dictionaire = sc.get_words()
    word = ""
    index_number = None
    if numbers:
        index_number = random.randint(0,nb_words - 1)

    for n in range(nb_words):
        sep = "" if n == nb_words - 1 else separator
        if capitalize:
            word += random.choice(dictionaire).capitalize()
        else:
            word += random.choice(dictionaire).lower()
        if n == index_number:
            word += f"{random.randint(0,9)}"
        word += sep

    return word


if __name__ == "__main__":
    load_dotenv()
    print(os.environ['DICTIONAIRE_FILE_NAME'])
    print(password_generator())