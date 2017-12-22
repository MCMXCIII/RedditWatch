import praw 
import smtplib

reddit = praw.Reddit(client_id='svuvBEZgEgZhOA',
                     client_secret='nn7D2e6ITDlkKE1PZy6W6VUUKaQ',
                     user_agent='something like firefox',
		     username='Watcher_Bot',
		     password='1234512345') 


#for submission in reddit.subreddit('BaltimoreAndDCr4r').new(limit=10):
    #print(submission.title)


#def get_date(submission):
#   time = submission.created
#  return datetime.datetime.fromtimestamp(time)

#Making a script for a friend who wants to try online dating with reddit


def get_date(submission):
	time = submission.created
	return datetime.datetime.fromtimestamp(time)

#Using this function to  alert me by email
def alert_me(submission):
	for submission in reddit.subreddit('BaltimoreAndDCr4r').new(limit=150):
		if "F4M" in submission.title:
				print("Alerting you by email!")	

def karmaNUpvote(submission):
    upvotes = submission.ups
    score = submission.score
    print('This posts score is' + score)


for submission in reddit.subreddit('BaltimoreAndDCr4r').new(limit=150):
     if "F4M" in submission.title:
		print("Baltimore/DC R4R!")
		print('_________________')
		print(submission.title)
		print("Can't find time.")
		print(submission.url)
		reddit.redditor('Not_A_MadScientist').message('r4r Alert',alert_me )

for submission in reddit.subreddit('r4r').new(limit=250):
    if "F4M" in submission.title:
		print("General R4R")
		print('___________')
		print(submission.title)
		print("Can't find time.")
		print(submission.url)



#Checking for another topic!
#for submission in reddit.subreddit('foxes').new(limit=250):
#    print(submission.title)
#    print(submission.url)


#Checking up on Japanese reddit
#print("250 latest posts on the /r/Japan Subreddit")

#for submission in reddit.subreddit('Japan').new(limit=250):
#    print(submission.title)
#    print('_______________')
#    print(submission.url)


#print('The current 50 most popular posts on /r/Japan')

#for submission in reddit.subreddit('Japan').hot(limit=50):
#    print(submission.title)
#    print('________________')
#    print(submission.url)

#Checking for rising content by Upvote and Karma(Post Score)
#for submission in reddit.subreddit('Japan').hot(limit=50):
#    print('Showing rising content')
#    karmaNUpvote(submission)

reddit.redditor('Not_A_MadScientist').message('TEST', 'test message from PRAW')
