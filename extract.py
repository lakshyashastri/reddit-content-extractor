import praw
from credentials import reddit
from pyperclip import copy, paste
from keyboard import press_and_release
import time
from datetime import datetime, timedelta

# probably only works on macOS
def notify(title, text):
    import os

    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))

start=time.time()
ok=[]
subm_count=0
com_count=0
prohibited_chars=['&', 'https', '\\']

SUBREDDIT_NAME = ""
FILE_PATH = r""
print()

for count, submission in enumerate(reddit.subreddit(SUBREDDIT_NAME).top(time_filter='month', limit=None), start=1): # hour day week month year all
    # if count>200:

    # # for getting posts more than a year old
    # if datetime.now().year - (datetime.fromtimestamp(time.time() - submission.created_utc)).year <= 1:
    #     continue
    
    # for submission titles
    with open(FILE_PATH, 'a') as f:
        f.write(submission.title)
        f.write('\n')
    print(submission.id)
    print(submission.title)
    print(f'Total submissions checked: {subm_count}\n')
    subm_count+=1
    # continue

    # for all comments in the submission
    submission.comments.replace_more(limit=None)
    print(submission.id)
    for comment in submission.comments.list():
        if comment.score>=1 and len(comment.body)>69 and len(comment.body.split())>4 and all(char not in comment.body for char in prohibited_chars): # arbitrary restrictions I applied to my dataset to make it to make it easier for my markov code to process the lines, change them as you want, or get rid of them entirely
            # ok.append(comment.body)

            with open(FILE_PATH, 'a') as f:
                f.write(comment.body)
                f.write('\n')
            
            com_count+=1
    subm_count+=1
    print(f'Total comments added: {com_count}\nTotal submissions checked: {subm_count}\n')

    pass

# copy(str(ok))

# print(ok)
print(time.time()-start)

notify('Done','')
