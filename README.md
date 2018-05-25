# praw-submission-scraper
Python 3 implementation of a subreddit submission scraper utilizing the Reddit API and the Python Reddit API Wrapper (PRAW). Requires a Reddit Client ID and Client Secret to use.

### submission-scraper.py
Scrapes 1,000 most recent submissions from a subreddit specified in the subreddit_names script. Outputs data in JSON format to a file named [subreddit_name]Data.json. JSON data fields are specified in the fields list.

### To do
Improve robustness by scraping data from submissions that have been submitted between a range of dates.

Extend functionality by scraping relevant data from individual posts.

### Credits
Logic for field extraction and JSON formatting (line 12; lines 20-24) originate from solution posted in subreddit post at https://www.reddit.com/r/learnpython/comments/5m49wx/how_to_download_praw_data_into_csv_or_json_file/