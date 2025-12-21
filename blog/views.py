from django.shortcuts import render

posts = [
    {
        'author': 'Zin',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2025'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2025'
    }
]

# Create your views here.
def home(request):
    context = {'posts':posts}
    return render(request,'home.html',context)

def about(request):
    return render(request,"about.html",{"title" : "About"})
