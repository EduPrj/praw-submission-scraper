import praw
import json
import redditAPICredentials as APICreds

reddit = praw.Reddit(client_id=APICreds.credentials['client_id'],
	                 client_secret=APICreds.credentials['client_secret'],
	                 user_agent=APICreds.credentials['user_agent'],
	                 username=APICreds.credentials['username'],
	                 password=APICreds.credentials['password'])
subreddit_names = ['NintendoSwitch']
list_of_items = []
fields = ('id','title','link_flair_text','created_utc','url')

for subreddit_name in subreddit_names:
	print("Looking at the {} subreddit.".format(subreddit_name))
	results = reddit.subreddit(subreddit_name).new(limit = 1000)
	for submission in results:
		to_dict = vars(submission)
		sub_dict = {}
		for field in fields:
			sub_dict[field] = to_dict[field]
		list_of_items.append(sub_dict)
	with open('{0}Data.json'.format(subreddit_name), 'w') as f:
		json.dump(list_of_items,f)