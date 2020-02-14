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

def add_actor(request, id):
    if request.POST:
        actors_list = Actor.objects.filter(name=request.POST['name'])
        if (len(actors_list)>0):
            actor = actors_list[0]
        else:
            actor = Actor(name=request.POST['name'])
            actor.save()
        actor.movies.add(Movie.objects.get(id=id))
        actor.save()
        print(actor.movies)
        return redirect("/")
    else:    
        return render(request, 'add_actor.html' )

def show_actor(request, id):
    context = {
        "actor" : Actor.objects.get(id=id) 
    }
    return render(request, 'show_actor.html', context)

def delete_movie(request, id):
    movie = Movie.objects.get(id=id)
    movie.delete()
    return redirect("/")
