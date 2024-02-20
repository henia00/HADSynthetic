from django.shortcuts import render
from .forms import QueryHadsForm
from hadsdb.models import Dane
from .utils import make_plot

# Create your views here.

def home(request):
    return render(request, 'pages/home.html', {})

def about(request):
    return render(request, 'pages/about.html', {})

def models(request):
    if request.method == "POST":
        form = QueryHadsForm(request.POST)
        if form.is_valid():
            mass = form.cleaned_data['mass']
            feh = form.cleaned_data['feh']
            fov = form.cleaned_data['fov']
            query_result= Dane.objects.filter(mass=mass, feh=feh, fov=fov)
            x = [x.logt for x in query_result]
            y = [x.logl for x in query_result]
            track_plot = make_plot(x, y)
            return render(request, 'pages/models.html', {'form': form, 'query_result':
                query_result, 'track_plot': track_plot})
    else:
        form = QueryHadsForm()
    return render(request, 'pages/models.html', {'form': form})

def tools(request):
    return render(request, 'pages/tools.html', {})

def papers(request):
    return render(request, 'pages/papers.html', {})

def contact(request):
    return render(request, 'pages/contact.html', {})
