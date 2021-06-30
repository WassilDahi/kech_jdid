from core.models import Publication
from django.shortcuts import render
import feedparser
from .models import Publication



   
  

def home(request):

    feed=feedparser.parse(r'https://www.algerie360.com/feed/')
    
    data={}

    for i in  feed.entries:
        p=Publication(title=i.title)
        p.save()
        print(i.title)

    return render(request,'home.html',feed)