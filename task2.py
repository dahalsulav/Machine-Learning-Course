import json
from operator import itemgetter


def save_dict_to_json(book_string: dict) -> dict:
    """this function takes dictionary as an argument,
    saves the dictionary in json file and returns
    dictionary sorted by published year

    Args:
        book_string (dict): dictionary of 10 books with
        their respective book name, author name and
        published year

    Returns:
        dict: dictionary sorted by published year
    """
    print(type(book_string))
    book_year = sorted(book_string, key=itemgetter('published year'))
    with open("data.json", "w") as outfile:
        json.dump(book_year, outfile)
    return book_year


book_string = [
    {
        "name": "the alchemist",
        "author": "paulo coelho",
        "published year": 1999
    },
    {
        "name": "rich dad poor dad",
        "author": "robert kiyosaki",
        "published year": 1982
    },
    {
        "name": "5 am club",
        "author": "robin sharma",
        "published year": 1990
    },
    {
        "name": "who will cry when you die",
        "author": "robin sharma",
        "published year": 2000
    },
    {
        "name": "start with why",
        "author": "simon senik",
        "published year": 1944
    },
    {
        "name": "steve jobs",
        "author": "walter isaacson",
        "published year": 2014
    },
    {
        "name": "hippie",
        "author": "paulo coelho",
        "published year": 1996
    },
    {
        "name": "revolution 2020",
        "author": "chetan bhagat",
        "published year": 2016
    },
    {
        "name": "think and grow rich",
        "author": "napolean hill",
        "published year": 2002
    },
    {
        "name": "atomic habits",
        "author": "james clear",
        "published year": 2019
    }

]

print(save_dict_to_json(book_string))
