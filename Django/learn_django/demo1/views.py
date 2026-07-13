from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        "name":"Omraje Vikas Ambure"
    }
    return render(request,"index.html",context)

def about(request):
    return HttpResponse("This is About Page")
