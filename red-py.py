import praw

reddit = praw.Reddit(client_id='Your Client ID',
                     client_secret='Your API Secret',
                     user_agent='something like firefox',
                     username='Whatever Username you Have',
                     password='1234512345')

def alert():
     message = "Submission:\n\n"
     for submission in reddit.subreddit('Some_Subreddit').new(limit=100):
     	if "F4M" in submission.title:
    		message = message + "[" + submission.title + "](" + submission.url + ")\n\n"
     return message

reddit.redditor('Not_A_MadScientist').message('Alert!', alert())
