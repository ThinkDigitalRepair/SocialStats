import argparse
import re

import requests
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser(description="A tool to assist in social media statistic tracking.")
parser.add_argument("username")
args = parser.parse_args()

username = args.username


def get_page(base_url):
    url_string = base_url + username

    page = requests.get(base_url + username)

    if not page.ok:
        page.raise_for_status()
        print("There was no active profile found at {0}. Please check the spelling and try again".format(url_string))
        exit(1)

    return page


def get_soup(page):
    return BeautifulSoup(page.text, "html.parser")


def extract_digits(string):
    return re.findall("(\d+,*\d+)", string)[0]
