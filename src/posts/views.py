from django.shortcuts import render

from .models import Form, Post

# Create your views here.

import pickle

#CRUD - create retrieve update delete

#List all the posts

def post_list_view(request):
    post_objects=Post.objects.all()
    context={
        'post_objects':post_objects
    }
    return render(request,"posts/index.html",context)

def getPrediction(age,sex,cp,bp,col,fbs,ekg,mhr,ex,stdep,slop,num,thal):
    knnClassifier=pickle.load(open('posts/knnClassifier.pkl', 'rb'))
    ans=knnClassifier.predict([[age,sex,cp,bp,col,fbs,ekg,mhr,ex,stdep,slop,num,thal]])
    if ans==1:
        return "You may have heart disease"
    elif ans==0:
        return "You may not have heart disease"
    else:
        return "Error in prediction"


def form(request):
    form_objects=Form.objects.all()
    # knnClassifier=pickle.load(open('posts/knnClassifier.pkl', 'rb'))
    context={
        'form_objects':form_objects,
        # 'knnClassifier':knnClassifier
    }
    return render(request,"posts/form.html",context)

def result(request):
    try:
        age=int(request.GET['age'])
        sex=int(request.GET['sex'])
        cp=int(request.GET['cp'])
        bp=int(request.GET['bp'])
        col=int(request.GET['col'])
        fbs=int(request.GET['fbs'])
        ekg=int(request.GET['ekg'])
        mhr=int(request.GET['mhr'])
        ex=int(request.GET['ex'])
        stdep=float(request.GET['stdep'])
        slop=int(request.GET['slop'])
        num=int(request.GET['num'])
        thal=int(request.GET['thal'])

        result=getPrediction(age,sex,cp,bp,col,fbs,ekg,mhr,ex,stdep,slop,num,thal)

        return render(request,"posts/result.html",{'result':result})
    except:
        return render(request,"posts/result.html",{'result':'Something went wrong'})

def header(request):
    return render(request,"posts/header.html")