import sys
import os
import re
import pytest
from dotenv import load_dotenv

load_dotenv()

PATH = os.path.dirname(os.path.abspath(__file__)) + "/"
NB_TEST = 50

sys.path.insert(0,PATH + "../")
import generator as gen

# test si les fonctions existent
def tes_generator_exist():
    assert gen.password_generator

# test sur le return generator
def test_generator_return():
    assert gen.password_generator()

def test_generator_return_is_string():
    assert type(gen.password_generator()) == str

## test regex format
def test_generator_return_base():
    for i in range(NB_TEST):
        assert re.match(r"[a-zA-Z0-9\'ñùêéèà\-]*_[a-zA-Z0-9\'ñùêéèà\-]*_[a-zA-Z0-9\'ñùêéèà\-]*",gen.password_generator())

def test_generator_return_separator():
    for i in range(NB_TEST):
        assert re.match(r"[a-zA-Z0-9\'ñùêéèà\-]*-[a-zA-Z0-9\'ñùêéèà\-]*-[a-zA-Z0-9\'ñùêéèà\-]*",gen.password_generator(separator="-"))


def test_generator_return_nb_words():
    for i in range(NB_TEST):
        assert re.match(r"[a-zA-Z0-9\'ñùêéèà\-]*_[a-zA-Z0-9\'ñùêéèà\-]*_[a-zA-Z0-9\'ñùêéèà\-]*_[a-zA-Z0-9\'ñùêéèà\-]*",gen.password_generator(nb_words=4))

def test_generator_return_number():
    for i in range(NB_TEST):
        assert re.match(r"[a-zA-Z\'ñùêéèà\-]*_[a-zA-Z\'ñùêéèà\-]*_[a-zA-Z\'ñùêéèà\-]*",gen.password_generator(numbers=False))

def test_generator_return_capitalize():
    for i in range(NB_TEST):
        assert re.match(r"[a-z\'ñùêéèà\-0-9]*_[a-z\'ñùêéèà\-0-9]*_[a-z\'ñùêéèà\-0-9]*",gen.password_generator(capitalize=False))
    
# Test input type
def test_input_nm_words():
    with pytest.raises(Exception):
        gen.password_generator(nb_words="3")

def test_input_separator():
    with pytest.raises(Exception):
        gen.password_generator(separator=0)
    
def test_input_numbers():
    with pytest.raises(Exception):
        gen.password_generator(numbers=[True])

def test_input_capitalize():
    with pytest.raises(Exception):
        gen.password_generator(capitalize="true")