import praw

reddit = praw.Reddit(client_id='svuvBEZgEgZhOA',
                     client_secret='nn7D2e6ITDlkKE1PZy6W6VUUKaQ',
                     user_agent='something like firefox',
                     username='Watcher_Bot',
                     password='1234512345')

def alert():
     message = "Submission:\n\n"
     for submission in reddit.subreddit('BaltimoreAndDCr4r').new(limit=100):
     	if "F4M" in submission.title:
    		message = message + "[" + submission.title + "](" + submission.url + ")\n\n"
     return message

reddit.redditor('Not_A_MadScientist').message('Alert!', alert())
