from project import near_match
from project import misspell_match
from project import abbreviate_match

def test_near_match():
    list = ["Japan", "United States", "Poland", "Spain"]
    assert near_match("Japan", list) == "Japan"
    assert near_match("japan", list) == "Japan"
    assert near_match("japa", list) == "Japan"
    assert near_match("apan", list) == "Japan"
    assert near_match("my country is japan", list) == "Japan"
    assert near_match("my country japan is", list) == "Japan"
    assert near_match("japant", list) == ""
    assert near_match("London", list) == ""
    assert near_match("spai", list) == "Spain"
    assert near_match("unitEd StaTes", list) == "United States"
    assert near_match("Nited states", list) == "United States"


def test_mispell_match():
    list = ["Japan", "United States", "Poland", "Spain"]
    #5-9 letter words can have 1 letter mispelled
    assert misspell_match("Japn", list) == "Japan"
    assert misspell_match("Jappn", list) == "Japan"
    assert misspell_match("Japaf", list) == "Japan"
    assert misspell_match("Jopan", list) == "Japan"
    assert misspell_match("JaRAn", list) == "Japan"
    assert misspell_match("Jan", list) == ""
    assert misspell_match("Jpn", list) == ""
    #10-14 letter words can have 2 letter mispelled
    assert misspell_match("Uned States", list) == "United States"
    assert misspell_match("Unitd Staes", list) == "United States"
    assert misspell_match("Uned States", list) == "United States"
    assert misspell_match("Ued States", list) == ""
    assert misspell_match("Unite Saes", list) == ""


def test_abbreviate_match():
    list = ["Japan", "United States", "United Arab Emirates", "Heard Island and McDonald Islands"]
    assert abbreviate_match("Japan", list) == ""
    assert abbreviate_match("J", list) == ""
    assert abbreviate_match("us", list) == "United States"
    assert abbreviate_match("Us", list) == "United States"
    assert abbreviate_match("uS", list) == "United States"
    assert abbreviate_match("US", list) == "United States"
    assert abbreviate_match("uae", list) == "United Arab Emirates"
    assert abbreviate_match("himi", list) == "Heard Island and McDonald Islands"
    #algorithm ignores "and" (see below result)
    assert abbreviate_match("hiami", list) == ""


def test_recommend_options():
    list = ["Japan", "", "United States", "Poland", "Spain"]
