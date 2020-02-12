from django.shortcuts import render, redirect
from first_app.models import *

def index(request):
    context ={
        "movies": Movie.objects.all()
    }
    return render(request, 'index.html', context)

def create_movie(request):
    Movie.objects.create(title=request.POST['title'],description=request.POST['description'])
    return redirect("/")

def edit_movie(request, id):
    if request.POST:
        movie = Movie.objects.get(id=id)
        movie.title = request.POST['title']
        movie.description = request.POST['description']
        movie.save()
        return redirect("/")
    else:
        context ={
            "movie":Movie.objects.get(id=id)
        }
        return render(request, 'edit.html', context)

def delete_movie(request, id):
    movie = Movie.objects.get(id=id)
    movie.delete()
    return redirect("/")
