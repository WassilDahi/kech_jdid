from django.shortcuts import render
import feedparser
   
  

def home(request):

    feed=feedparser.parse(r'https://www.algerie360.com/feed/')
  
    for i in  feed.entries:
        print(i.title)

    return render(request,'home.html',feed)