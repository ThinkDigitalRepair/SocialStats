import re

import obj

base_url = "https://www.instagram.com/"
obj = obj.Obj(base_url)
username = obj.args.username


def contains_attr(tag):
    return True if "property" in tag.attrs and tag.attrs["property"] == "og:description" else False


soup = obj.get_soup()
result = soup.find_all('meta')
stats = list(filter(contains_attr, result))

# turning stats into a singular variable containing the content of the tag instead of a list
if len(stats) == 1:
    stats = stats[0].attrs['content']

    # break into variables
    # find all instances of numbers that may contain commas.

    stats_list = re.findall("(\d+,*\d+ [A-Za-z]+)", stats)

    # error checking
    if len(stats_list) == 3:
        if ("Followers" in stats_list[0]) and ("Following" in stats_list[1]) and ("Posts" in stats_list[2]):
            # extracting digits
            for i in range(0, len(stats_list)):
                stats_list[i] = obj.extract_digits(stats_list[i])

            # removing any commas that may be in the numbers

    else:
        raise Exception("stats has more or less than 3 variables. Adjust function to include this variation.")
elif len(stats) > 1:
    raise Exception("Found more than 1 \"og:description\" tag.")
else:
    raise Exception("Found no \"og:description\" tag.")
print("Current Instagram stats for {0}: {1} followers, {2} following, and {3} posts.".format(username,
                                                                                             stats_list[0],
                                                                                             stats_list[1],
                                                                                             stats_list[2]))

# TODO: Support multiple account checking.
