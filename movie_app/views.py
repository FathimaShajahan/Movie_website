from django.http import HttpResponse
from django.shortcuts import redirect, render
from . form import MovieForm
from . models import Movie1

# Create your views here.

def index(request):
    movie=Movie1.objects.all()
    context={
        'movie_list': movie
    }
    # return HttpResponse("HELLO I AM NEW ")
    return render(request,'index.html',context)

def detail(request,movie_id):
    movie=Movie1.objects.get(id=movie_id)
    return render(request,"details.html",{'movie':movie})

def add_movie(request):
    if request.method=="POST":
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        year = request.POST.get('year')
        img = request.FILES['img']
        movie=Movie1(name=name,desc=desc,year=year,img=img)
        movie.save()
    return render(request,'add.html')


def update(request,id):
    movie=Movie1.objects.get(id=id)
    form = MovieForm(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,"update.html",{'form':form,'movie':movie})


def delete(request,id):
    if request.method=='POST':
        movie=Movie1.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')