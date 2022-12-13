import sys
import os
from dotenv import load_dotenv

load_dotenv()

PATH = os.path.dirname(os.path.abspath(__file__)) + "/"
DICTIONAIRE = os.environ['DICTIONAIRE_FILE_NAME']

sys.path.insert(0,PATH + "../")
from data import scrapper as sc

# Test if the function / file exists
def test_sc_exist():
    assert sc.scrap

def test_get_words_exist():
    assert sc.get_words

def test_file_exist():
    assert os.path.isfile(PATH + "../data/" + DICTIONAIRE)

# test return variables
def test_non_empty_words():
    assert sc.get_words != []

def test_type_get_words():
    assert type(sc.get_words()) == list