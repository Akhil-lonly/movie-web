from django.shortcuts import render, redirect

from .forms import movieupdate
from . models import movie

# Create your views here.
def index(request):
    movieobj=movie.objects.all()

    return render(request,'index.html',{'movielist':movieobj})


def detail(request,movieobj_id):
    movieobj = movie.objects.get(id=movieobj_id)
    return render(request,'detail.html',{"movieobj":movieobj})

def add_movie(request):
    if request.method=='POST' :
        Name=request.POST.get('Name')
        desc = request.POST.get('desc')
        year = request.POST.get('year')
        Image =request.FILES['Image']
        movie1=movie(Name=Name,desc=desc,year=year,Image=Image)
        movie1.save()

    return render(request,'add.html')

def update(request,id):
    movie1=movie.objects.get(id=id)
    form=movieupdate(request.POST or None,request.FILES,instance=movie1)
    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request,'update.html',{'form':form,'movie':movie1})

def delete(request,id):
    if request.method=='POST':
        movie1=movie.objects.get(id=id)
        movie1.delete()
        return redirect('/')
    return render(request,'delete.html')

