from obj import Obj

# this is the class name for the div that contains the values we need.
class_name = '_4bl9'
base_url = "https://www.facebook.com/"
obj = Obj(base_url)

likes = 0
followers = 0
found = [False, False]
soup = obj.get_soup()
tags = soup.find_all('div', {'class': class_name})

for tag in tags:
    # find tags that have likes and follows in them.
    for item in tag.contents:
        if 'people like this' in item.get_text():
            likes = obj.extract_digits(item.get_text())
            found[0] = True
        if 'people follow this' in item.get_text():
            followers = obj.extract_digits(item.get_text())
            found[1] = True
if found[0] and found[1]:
    print("Current Facebook stats for {0}: {1} likes and {2} followers.".format(obj.username, likes, followers))

pass
