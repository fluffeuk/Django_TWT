from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item

# Create your views here.
def index(response, id):
    ls = ToDoList.objects.get(id = id)
    item = ls.item_set.get(id = 1)
    return HttpResponse("<h1>%s</h1><br></br><p>%s</p>" %(ls.name, str(item.text)))

def home(response):
    pass
'''
what goes between the brackets is html code. we can add tags on either side. if we don't it will be the same as 
    preformatted (plain) text. we could achieve this in a .html doc by putting text between body tags:
    <body> koalahhh! </body>
    or using the pre tag:
    <pre> koalahhh! </pre>
'''