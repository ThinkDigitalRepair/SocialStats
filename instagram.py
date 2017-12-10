from bs4 import BeautifulSoup
import requests
import re
import argparse


parser = argparse.ArgumentParser(description="A tool to assist in social media statistic tracking.")
parser.add_argument("username")
args = parser.parse_args()

if __name__ == '__main__':
    username = args.username
    base_url = "https://www.instagram.com/"
    url_string = url_string = base_url + username

    try:
        igpage = requests.get(base_url + username)
        if not igpage.ok:
            igpage.raise_for_status()
    except requests.HTTPError:
        print("There was no active profile found at {0}. Please check the spelling and try again".format(url_string))
        exit(1)
    soup = BeautifulSoup(igpage.text, "html.parser")
    result = soup.find_all('meta')

    def contains_attr(tag):
        if "property" in tag.attrs and tag.attrs["property"] == "og:description":
            return True
        else:
            return False


    stats = list(filter(contains_attr, result))

    # turning stats into a singular variable containing the content of the tag instead of a list
    if len(stats) == 1:
        stats = stats[0].attrs['content']

        """def exclusions(x):
            filtering function to remove extraneous information from the stats variable
            if x == ', ' or "See Instagram photos and videos from" in x:
                return False
            else:
                return True"""

        # break into variables
        # find all instances of numbers that may contain commas.

        stats_temp = re.findall("(\d+,*\d+ [A-Za-z]+)", stats)

        # error checking
        if (len(stats_temp) == 3):
            if ("Followers" in stats_temp[0]) and ("Following" in stats_temp[1]) and ("Posts" in stats_temp[2]):
                stats = re.findall("(\d+,*\d+)", stats)

            # removing any commas that may be in the numbers
            stats = dict(followers=stats[0].replace(",", ""),
                         following=stats[1].replace(",", ""),
                         posts=stats[2].replace(",", ""))
        else:
            raise Exception("stats has more or less than 3 variables. Adjust function to include this variation.")
    elif len(stats) > 1:
        raise Exception("Found more than 1 \"og:description\" tag.")
    else:
        raise Exception("Found no \"og:description\" tag.")
    print("Current stats for {0}: {1} followers, {2} following, and {3} posts.".format(username, stats['followers'], stats['following'], stats['posts']))

