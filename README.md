Alexander Sullivan-Wilson

You can run the code by starting python 3.7.  Then importing the code from assignment0.  The main.py file contains the relevant functions.  The example code to retrieve a random title:
from assignment0 import main;
from main import download, extract_requests, extract_titles, random_title;
random_title(extract_titles(extract_requests(download())));

I used https://docs.python.org/2/library/random.html for documentation of the random library and how to use it.

I used https://docs.python.org/2/library/urllib.html for documentation about how to read data from a url.

I used W3schools (https://www.w3schools.com/python/python_json.asp) for help with parsing json files.
