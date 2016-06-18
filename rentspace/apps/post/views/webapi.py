import sys
import json
import os


from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from django.http import HttpResponse,JsonResponse,HttpResponseRedirect

from post.models import Post


@csrf_exempt
@login_required(login_url='/signin/')
def showallpost(request):
    print ("you hit show post")
    postlist = Post.objects.all()
    for post in postlist:
        print (post)
    context ={}
    context["posts"]=postlist
    return render(request,'postlist.html',context)

@login_required(login_url='/signin/')
def showpost(request):
    print ("you hit show post")
    postid = request.GET.get("id")
    print (postid)
    post =  Post.objects.get(id=postid)
    print (post)
    context ={}
    context["post"] = post
    return render(request,'showpost.html',context)


@csrf_exempt
@login_required(login_url='/signin/')
def addpost(request):
    print ("you hit add post")
    if request.method == 'POST':
        print ("got post request")
        description = request.POST.get("description","")
        rentperday  = request.POST.get("rentperday","")
        avail_start_date = request.POST.get("avail_start_date","")
        avail_end_date   = request.POST.get("avail_end_date","")

        address = request.POST.get("address","")
        street  = request.POST.get("street","")
        city = request.POST.get("city","")
        pincode = request.POST.get("pincode","")
        state = request.POST.get("state","")
        country = request.POST.get("country","")

        p = Post()
        p.description = description
        p.user = request.user
        p.rentperday = rentperday
        p.avail_start_date = avail_start_date
        p.avail_end_date  = avail_end_date

        p.address = address
        p.street = street
        p.city = city
        p.pincode = pincode
        p.state = state
        p.country = country

        p.save()

        return HttpResponseRedirect("/addpost?msg=susscessfully added property&id="+str(p.id))
        #return HttpResponse("POST object created successfully")
    else:
        context ={}
        postid = request.GET.get("id","")
        if postid:
            post =  Post.objects.get(id=postid)
            context["post"] = post

        context["msg"] = request.GET.get("msg","")
        
        return render(request,'addpost.html',context)
    
@csrf_exempt    
@login_required(login_url='/signin/')
def updatepost(request):
    print ("you hit update post")
    if request.method == 'POST':
        print ("got post request")
        postid = request.POST.get("postid")
        description = request.POST.get("description","")
        rentperday  = request.POST.get("rentperday","")
        avail_start_date = request.POST.get("avail_start_date","")
        avail_end_date   = request.POST.get("avail_end_date","")

        address = request.POST.get("address","")
        street  = request.POST.get("street","")
        city = request.POST.get("city","")
        pincode = request.POST.get("pincode","")
        state = request.POST.get("state","")
        country = request.POST.get("country","")


        print (postid,description)
        p =  Post.objects.get(id=postid)        
        p.description = description
        #p.user = request.user
        p.rentperday = rentperday
        p.avail_start_date = avail_start_date
        p.avail_end_date  = avail_end_date

        p.address = address
        p.street = street
        p.city = city
        p.pincode = pincode
        p.state = state
        p.country = country

        p.save()
        return HttpResponseRedirect("/updatepost/?msg=susscessfully updated&id="+postid)
    else:
        postid = request.GET.get("id")
        post =  Post.objects.get(id=postid)
        print (post.rentperday,str(post.avail_start_date),post.avail_end_date)
        context ={}
        context["post"] = post
        context["msg"] = request.GET.get("msg","")
        return render(request,'updatepost.html',context)


@login_required(login_url='/signin/')
def deletepost(request):
    print ("you hit delete post")
    if request.method == 'POST':
        print ("got post request")
        # add post to db
    else:
        context ={}
        #return render(request,'postlist.html',context)
        return HttpResponseRedirect("/posts")

