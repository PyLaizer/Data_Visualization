from operator import itemgetter

import requests
from plotly.graph_objs import Bar
from plotly import offline

#Make an API call an store the response
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status Code:{r.status_code}")

#Process information about each submission
submission_ids = r.json()
submission_titles = []
submission_comments = []

for submission_id in submission_ids[:30]:
    #Make a seperate API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()
    try:
        title = response_dict['title']
        comment = response_dict['descendants']
    except KeyError:
        print(f"id:{submission_id}, KeyError")
        for key in response_dict:
            print(key)
    else:        
        submission_titles.append(title)
        submission_comments.append(comment)

# print(len(submission_comments))

data = [{
    'type':'bar',
    'x':submission_titles,
    'y':submission_comments,
}]    

my_layout = {
    'title': "Most Commented News on Hacker News",
    'titlefont':{'size':18},
    'xaxis':{
        'title':'News Title',
        'titlefont':{'size':14},
        'tickfont':{'size':12},
    },
    'yaxis':{
        'title':'Comments',
        'titlefont':{'size':14},
        'tickfont':{'size':12},       
    },
}

fig = {'data':data, 'layout':my_layout}
offline.plot(fig, filename='hacker_news.html')
