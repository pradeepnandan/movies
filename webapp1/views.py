from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import movies
from .form import MovieForm

# Create your views here.
def home(request):
    obj=movies.objects.all()
    moviedic={
        'moviekey':obj
    }
    return render(request,'index.html',moviedic)
   # return render(request,'index.html',{'moviekey':obj})
def details(request,movies_id):
    #return HttpResponse("This movie is %s" % movies_id)
    movie=movies.objects.get(id=movies_id)
    return render(request,'details.html', {'movie_key':movie})
def add(request):

    if request.method=='POST':
        mname=request.POST.get('mname')
        desc=request.POST.get('desc')
        img=request.FILES['img']
        new_movie=movies(mname=mname, desc=desc,img=img)
        new_movie.save()
    return render(request,'add.html')
def update(request,id):
    movie=movies.objects.get(id=id)
    form=MovieForm(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form, 'movie':movie})
def delete(request,id):
    if request.method=='POST':
        movie=movies.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')
