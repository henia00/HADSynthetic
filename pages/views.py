from django.shortcuts import render
from .forms import QueryHadsForm

# Create your views here.

def home(request):
    return render(request, 'pages/home.html', {})

def about(request):
    return render(request, 'pages/about.html', {})

def models(request):
    form = QueryHadsForm()
    return render(request, 'pages/models.html', {'form': form})

def tools(request):
    return render(request, 'pages/tools.html', {})

def papers(request):
    return render(request, 'pages/papers.html', {})

def contact(request):
    return render(request, 'pages/contact.html', {})
