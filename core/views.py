from core.models import Publication
from django.shortcuts import render
import feedparser
from .models import Publication



   
  

def home(request):

    feed=feedparser.parse(r'https://www.algerie360.com/feed/')
    
    data={}

    
    #p=Publication(title=i.title,link=i.link,date_published=i.published_parsed,description=i.description,author=i.author)
    #p.save()
    #print(i.keys())
    print(feed.status)

    return render(request,'home.html',feed)