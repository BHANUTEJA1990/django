from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Movie
# Create your views here.
def movie(request,action):
    if action =="add":
        mv =Movie(title="bahuballi",director="rajamouli",genre="historic",)
        mv.full_clean()
        mv.save()
        return HttpResponse(f"Movies is added:{mv}")
    elif action =="get":
        template_name='movie_demo.html'
        movies_list=Movie.objects.all()
        print(f"movie_list:{movies_list}")
        context ={"movie_list":movies_list}
        return render(request,template_name,context=context)
       # movie=Movie.objects.all()
      #  movie=Movie.objects.filter(title='avatar').values()
      #  movie=Movie.objects.filter(title='avatar').values_list()
       # movie=Movie.objects.filter(title__startswith="j");

        #print(f"Movie list:{movie}")

       # movie=Movie.objects.exclude (title='avatar')

      #  return HttpResponse(f"Movie will add: {movie} ")

    else:
        return HttpResponse("invalid action.",status=400)


def get_movie(request,id):
       template_name="movie_get.html"
       mv=Movie.objects.get(id=id)
       context={'mv': mv}
       return render(request,template_name,context=context)


def del_movie(request,id):
    mv_inst=Movie.objects.get(pk=id)
    mv_inst.delete()
    return redirect('movie',action='get')


def upd_movie(request, id):
    mv_inst=Movie.objects.get(pk=id)
    mv_inst.title="new title"
    mv_inst.director="new director"
    mv_inst.save()
    return redirect('movie',action='get')