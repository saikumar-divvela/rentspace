import sys
import json
import os


from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from django.http import HttpResponse,JsonResponse,HttpResponseRedirect

from post.models import Post,PostPhoto

#TODO  Send SMS/Email of owner details to owner and customer
@login_required(login_url='/signin/')
def contactpostowner(request):
    print ("you hit contact post owner")
    postid = request.GET.get("id")
    print (postid)
    return HttpResponseRedirect("/home")

# TODO bookmark the post
@login_required(login_url='/signin/')
def shortlistpost(request):
    print ("you hit shortlist post")
    postid = request.GET.get("id")
    print (postid)
    return HttpResponseRedirect("/home")

# TODO remove bookmark for the post
@login_required(login_url='/signin/')
def delistpost(request):
    print ("you hit delistpost ")
    postid = request.GET.get("id")
    print (postid)
    return HttpResponseRedirect("/home")

@csrf_exempt
def searchposts(request):
    print ("you hit search posts")
    
    location = request.GET.get("location","")
    housetype = request.GET.get("housetype","")
    bookingtype = request.GET.get("bookingtype","")
    people = request.GET.get("people","")
    
    print (location, housetype,bookingtype,people)
    postlist = Post.objects.all()
    context ={}
    context["posts"]=postlist
    return render(request,'postlist.html',context)

@csrf_exempt
@login_required(login_url='/signin/')
def myposts(request):
    print ("you hit my posts")
    postlist = Post.objects.all()
    for post in postlist:
        print (post)
    context ={}
    context["posts"]=postlist
    return render(request,'myposts.html',context)

#TODO get shortlisted posts
@csrf_exempt
@login_required(login_url='/signin/')
def shortlistedposts(request):
    print ("you hit shortlistedposts")
    postlist = Post.objects.all()
    for post in postlist:
        print (post)
    context ={}
    context["posts"]=postlist
    context["shortlistedposts"] = True
    return render(request,'myposts.html',context)        


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
@login_required(login_url='/signin')
def addpost(request):
    print ("you hit add post")
    if request.method == 'POST':
        print ("got post request")
        title = request.POST.get("title","")
        description = request.POST.get("description","")
        rentperday  = request.POST.get("rentperday","")
        facilities = request.POST.getlist("facilities")
        print (facilities)
        if facilities is not None:
            facilities = ",".join(facilities)
        else:
            facilities = ""

        address = request.POST.get("address","")
        street  = request.POST.get("street","")
        city = request.POST.get("city","")
        pincode = request.POST.get("pincode","")
        state = request.POST.get("state","")
        country = request.POST.get("country","")

        deposit = request.POST.get("deposit","")
        guests  = request.POST.get("guests","")
        house_type = request.POST.get("house_type","")
        accom_type = request.POST.get("accom_type","")
        accom_for =  request.POST.getlist("accom_for")

        if accom_for is not None:
            accom_for = ",".join(accom_for)
        else:
            accom_for = ""

        print (deposit,guests,house_type,accom_type,accom_for)

        p = Post()
        p.description = description
        p.title = title
        p.user = request.user
        p.rentperday = rentperday
        p.facilities = facilities

        p.address = address
        p.street = street
        p.city = city
        p.pincode = pincode
        p.state = state
        p.country = country

        p.deposit = deposit
        p.guests = guests
        p.housetype = house_type
        p.accom_type = accom_type
        p.accom_for = accom_for
        
        p.save()

        if request.FILES.getlist("photos"):
            print (request.FILES.getlist("photos"))
            for f in request.FILES.getlist("photos"):
                print (f)
                image = PostPhoto()
                image.photo = f
                image.post = p
                image.save()
            

        return HttpResponseRedirect("/addpost/?msg=susscessfully added property&id="+str(p.id))
        #return HttpResponseRedirect("/addpost")
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
        title = request.POST.get("title","")
        description = request.POST.get("description","")
        rentperday  = request.POST.get("rentperday","")
        facilities = request.POST.getlist("facilities")
        print (facilities)
        if facilities is not None:
            facilities = ",".join(facilities)
        else:
            facilities = ""

        address = request.POST.get("address","")
        street  = request.POST.get("street","")
        city = request.POST.get("city","")
        pincode = request.POST.get("pincode","")
        state = request.POST.get("state","")
        country = request.POST.get("country","")

        deposit = request.POST.get("deposit","")
        guests  = request.POST.get("guests","")
        house_type = request.POST.get("house_type","")
        accom_type = request.POST.get("accom_type","")
        accom_for =  request.POST.getlist("accom_for")

        if accom_for is not None:
            accom_for = ",".join(accom_for)
        else:
            accom_for = ""


        print (deposit,guests,house_type,accom_type,accom_for)


        print (postid,description)
        p =  Post.objects.get(id=postid)        
        p.description = description
        p.title = title
        #p.user = request.user
        p.rentperday = rentperday
        p.facilities = facilities


        p.address = address
        p.street = street
        p.city = city
        p.pincode = pincode
        p.state = state
        p.country = country


        p.deposit = deposit
        p.guests = guests
        p.house_type = house_type
        p.accom_type = accom_type
        p.accom_for = accom_for

        p.save()

        if request.FILES.getlist("photos"):
            print (request.FILES.getlist("photos"))
            for f in request.FILES.getlist("photos"):
                print (f)
                
                image = PostPhoto()
                image.photo = f
                image.post = p
                image.save()
                
        return HttpResponseRedirect("/updatepost/?msg=susscessfully updated&id="+postid)
    else:
        postid = request.GET.get("id")
        post =  Post.objects.get(id=postid)
        print (post.rentperday)
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

@login_required(login_url='/signin/')
def verifypost(request):
    print ("You hit verify post")
    postid = request.GET.get("postid")
    post = Post.objects.get(pk=postid)
    post["is_verified"] = True
    return HttpResponse("success")