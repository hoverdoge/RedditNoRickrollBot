#imports reddit api stuff
import praw

#link vars 
rickrollLink = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
jebaitedLink = 'https://www.youtube.com/watch?v=d1YBv2mWll0'

reddit = praw.Reddit(user_agent='AGENT',
                     client_id='ID', client_secret="SECRET",
                     username='USERNAME', password='PASSWORD')

#loops through specified number of comments in subreddit
for c in reddit.subreddit('all').comments(limit=1000):
  print(c.body)
  if rickrollLink in c.body:
    print('rickroll detected')
    c.reply("This link goes to Rick Astley's 'Never Gonna Give You Up' on YouTube")
  if jebaitedLink in c.body:
    print('jebait detected')
    c.reply("This link goes to Sordiway's 'Jebaited song' on YouTube")
  
