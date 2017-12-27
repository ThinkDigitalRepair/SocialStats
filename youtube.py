from obj import Obj

base_url_user = "https://www.youtube.com/"
base_url_search = "https://www.youtube.com/results?search_query="
obj = Obj(base_url_user)
username = obj.args.username
subscriber_count = obj.extract_digits(obj.find_text("subscribers\">(\d+,?\d+)")[0])
print("Current YouTube stats for {0}: {1} subscribers".format(username, subscriber_count))
pass
