import praw 

reddit = praw.Reddit(client_id='your-client-ID',
                     client_secret='your-secret',
                     user_agent='something like firefox',
		     username='Username for the account ',
		     password='1234512345') 



for submission in reddit.subreddit('aww').new(limit=150):
     if "F4M" in submission.title:
		print("cute stuff!")
		print('_________________')
		print(submission.title)
		print(submission.url)


#Checking for another topic!
#for submission in reddit.subreddit('foxes').new(limit=250):
#    print(submission.title)
#    print(submission.url)


