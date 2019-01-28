import json
import random
import urllib.request

# Python3 type hints
# https://mypy.readthedocs.io/en/latest/cheat_sheet_py3.html
from typing import List, Dict, Any

url = "https://raw.githubusercontent.com/TrumpTracker/trumptracker.github.io/master/_data/data.json"

def download():
    """ This function downloads the json data from the url."""
    return urllib.request.urlopen(url).read() #this is literally going to return the massive string of json data that is retrieved from the url above


def extract_requests(text: str) -> List[Dict[str, Any]]:
    """
        This function turns the json data into a dict object and
        extracts and returns the array of promises.
    """
    return json.loads(text)['promises']


def extract_titles(promises: List[Dict[str, Any]]) -> List[str]:
    """ Make a new array with just the titles. """
    titles = [];
    for promise in promises[:]:
        titles.append(promise['title']);
    return titles


def random_title (titles: List[str]) -> str:
    """ This function takes list of titles and returns one string at random. """
    random.seed(a=1234);
    return titles[random.randint(0,len(titles)-1)]

