from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts

# Create your views here.
# posts = [
#     {
#         'author': 'Anna',
#         'title': 'Blog post 1',
#         'content': 'First post content',
#         'date': 'August 10, 2020'
#     },
#     {
#         'author': 'Frank',
#         'title': 'Blog post 2',
#         'content': 'First post content',
#         'date': 'August 1, 2020'
#     }
# ]

def home(request):
    context = {'posts':Posts.objects.all()}
    return render (request,'home.html',context)
