import requests
import re
import os
from dotenv import load_dotenv
load_dotenv()

ALPHABET = "abcdefghijklmnopqrstuvwxyz"
PATH = os.path.dirname(os.path.abspath(__file__)) + "/"
FILE = os.environ['DICTIONAIRE_FILE_NAME']
URL = os.environ['URL_SCRAPPER']

def scrap():
    liste_brt=[]
    reg = r'"brt">[a-z\'ñù-]*<'
    for lettre in ALPHABET:
        print("letter ",lettre)
        req = requests.get(URL + lettre).text
        list_brt_scrapped = re.findall(reg,req)
        for word in list_brt_scrapped:
            liste_brt.append(word.strip("\"brt\">").strip("<"))

    with open(PATH + FILE,'w') as file:
        for word in liste_brt:
            file.write(word+"\n")

def get_words():
    dictionaire_breton = []
    with open(PATH + FILE,"r") as file:
        dictionaire = file.readlines()
    for word in dictionaire:
        dictionaire_breton.append(word.strip("\n"))
    return dictionaire_breton
    
if __name__ == "__main__":
    scrap()
    print("Words: ",get_words())