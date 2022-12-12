import requests
import re

URL = "http://guythomas.free.fr/php/lexique.php?sens=fb&alpha="
ALPHABET = "abcdefghijklmnopqrstuvwxyz"
FILE="./dictionaire_breton.txt"

def scrap():
    liste_brt=[]
    reg = r'"brt">[a-zA-Z]*<'
    for lettre in ALPHABET:
        print("letter ",lettre)
        req = requests.get(URL + lettre).text
        list_brt_scrapped = re.findall(reg,req)
        for word in list_brt_scrapped:
            liste_brt.append(word.replace("\"brt\">","").replace("<",""))

    with open(FILE,'w') as file:
        for word in liste_brt:
            file.write(word+"\n")

def get_words():
    dictionaire_breton = []
    with open("data/"+FILE,"r") as file:
        dictionaire = file.readlines()
    for word in dictionaire:
        dictionaire_breton.append(word.strip("\n"))
    return dictionaire_breton
    
if __name__ == "__main__":
    print(get_words())