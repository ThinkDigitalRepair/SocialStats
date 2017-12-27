import argparse

import regex
import requests
from bs4 import BeautifulSoup


class Obj:

    def __init__(self, url):
        """
        Doesn't set username until after url is sent to init.

        :param url: base_url. Adds username to url after.
        """

        parser = argparse.ArgumentParser(description="A tool to assist in social media statistic tracking.")
        parser.add_argument("username")
        parser.add_argument("--searchrank")
        self.args = parser.parse_args()

        self.username = self.args.username
        self.page = self.get_page(url)
        self.soup = self.get_soup()

    def get_page(self, base_url):
        """

        :type base_url: string
        """
        url_string = base_url + self.username

        page = requests.get(base_url + self.username)

        if not page.ok:
            page.raise_for_status()
            print(
                "There was no active profile found at {0}. Please check the spelling and try again".format(url_string))
            exit(1)

        return page

    def get_soup(self):
        return BeautifulSoup(self.page.text, "html.parser")

    @staticmethod
    def extract_digits(string):
        return int(regex.findall("(\d+,*\d+)", string)[0].replace(',', ''))

    def find_text(self, query):
        return regex.findall(query, self.page.text)

    def parseargs(self):
        return
