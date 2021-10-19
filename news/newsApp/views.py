from django.shortcuts import render
from .models import *
from random import choice
# Create your views here.
def homeViews(requests):
    son=0
    son1=0
    if requests.POST:
        a=UserModel()
        a.email= requests.POST.get('email')
        a.save()
    ctgall=CategoryModel.objects.all()
    newsall=NewsModel.objects.all().order_by('-id')
    a=choice(ctgall)
    b=NewsModel.objects.all().filter(ctg_id=a.id).order_by('-id')
    b1=NewsModel.objects.all().filter(ctg_id=1).order_by('-id')
    b2=NewsModel.objects.all().filter(ctg_id=2).order_by('-id')
    b3=NewsModel.objects.all().filter(ctg_id=3).order_by('-id')
    b4=NewsModel.objects.all().filter(ctg_id=4).order_by('-id')
    b5=NewsModel.objects.all().filter(ctg_id=5).order_by('-id')
    for i in newsall:
        if son==0:
            d=i.id-5
            son=1
    for i in b3:
        if son1==0:
            d1=i.id-4
            son1=1


    ctx={'ctgall':ctgall , 'newsall':newsall,'a':a , 'b':b , 'b1':b1, 'b2':b2, 'b3':b3, 'b4':b4, 'b4':b4, 'b5':b5 ,'d':d , 'd1':d1}
    return render(requests , 'index.html' , ctx )   
def ctgViews(requests, slug):
    ctgall = CategoryModel.objects.all()
    ctg_one = CategoryModel.objects.get(slug=slug)
    newsctg = NewsModel.objects.all().filter(ctg_id=ctg_one.id)
    last_news = NewsModel.objects.all().filter(ctg_id=ctg_one.id).order_by('-id')
    newsall=NewsModel.objects.all().order_by('-id')
    context = {'ctgall': ctgall , 'newsctg':newsctg, 'ctg_one': ctg_one, 'last_news': last_news ,'newsall':newsall }
    return render(requests, "category.html", context)
def newsViews(requests , pk):
	news=NewsModel.objects.get(pk=pk)
	ctgall=CategoryModel.objects.all()
	newsall=NewsModel.objects.all().order_by('-id')
	ctx={'news':news ,'ctgall':ctgall , 'newsall':newsall}
	return render(requests , 'view.html',ctx)   

def searchViews(requests):
    soz=requests.GET.get('q', '')
    ctgall=CategoryModel.objects.all()
    if soz and soz != '':
        result=NewsModel.objects.filter(title__contains=soz).all()[:5]
    else :
        result=[]   
    last_news = NewsModel.objects.all().order_by('-id')
    l=len(result)
    ctx={'ctgall':ctgall , 'result':result, 'last_news':last_news ,'l':l,'soz':soz}

    return render(requests,'search.html', ctx)    
def contactViews(requests):
    ctgall=CategoryModel.objects.all()
    ctx={'ctgall':ctgall}
    return render(requests , 'contact.html' , ctx )    