import re

import obj

if __name__ == '__main__':
    username = obj.args.username
    base_url = "https://www.instagram.com/"
    url_string = url_string = base_url + username


    def contains_attr(tag):
        return True if "property" in tag.attrs and tag.attrs["property"] == "og:description" else False


    soup = obj.get_soup(obj.get_page(base_url))
    result = soup.find_all('meta')
    stats = list(filter(contains_attr, result))

    # turning stats into a singular variable containing the content of the tag instead of a list
    if len(stats) == 1:
        stats = stats[0].attrs['content']

        # break into variables
        # find all instances of numbers that may contain commas.

        stats_temp = re.findall("(\d+,*\d+ [A-Za-z]+)", stats)

        # error checking
        if len(stats_temp) == 3:
            if ("Followers" in stats_temp[0]) and ("Following" in stats_temp[1]) and ("Posts" in stats_temp[2]):
                # extracting digits
                for i in range(0, len(stats_temp)):
                    stats_temp[i] = obj.extract_digits(stats_temp[i])

                # removing any commas that may be in the numbers
                stats = dict(followers=stats_temp[0].replace(",", ""),
                             following=stats_temp[1].replace(",", ""),
                             posts=stats_temp[2].replace(",", ""))
        else:
            raise Exception("stats has more or less than 3 variables. Adjust function to include this variation.")
    elif len(stats) > 1:
        raise Exception("Found more than 1 \"og:description\" tag.")
    else:
        raise Exception("Found no \"og:description\" tag.")
    print("Current Instagram stats for {0}: {1} followers, {2} following, and {3} posts.".format(username,
                                                                                                 stats['followers'],
                                                                                                 stats['following'],
                                                                                                 stats['posts']))

# TODO: Support multiple account checking.
