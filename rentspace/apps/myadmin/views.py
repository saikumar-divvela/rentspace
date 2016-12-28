# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from common import getpagerecords
from userprofile.models import User
from post.models import Post
from myadmin.models import Postbox


def show_admin(request):
    context = {}

    if(request.user.is_authenticated and request.user.is_staff):
        return render(request, 'admin_home.html', context)
    return HttpResponse("This page is accessible to only staff. Either you are not logged in or your are not staff.")


def all_users(request):
    print ("You hit all_users")

    command = request.GET.get("command", "").lower().strip()
    isphonenotverified = request.GET.get("isphonenotverified", "")
    isidproofnotverified = request.GET.get("isidproofnotverified", "")
    searchby = request.GET.get("searchby", "").lower().strip()
    searchdata = request.GET.get("searchdata", "").strip()

    page = request.GET.get('page')
    userlist = []

    if (command == "filter"):
        print ("Filter users by ## Phone not verified:" + isphonenotverified, " and Idproof not verified:" + isidproofnotverified)
        if (isphonenotverified == 'true'):
            userlist = User.objects.filter(is_phone_verified=False)
        elif (isidproofnotverified == 'true'):
            userlist = User.objects.filter(is_id_verified=False)

    elif (command == "search"):
        print ("Search users by ##" + searchby + " and search data:" + searchdata)
        if (searchby == "username"):
            userlist = User.objects.filter(email__icontains=searchdata)
        elif (searchby == "phonenumber"):
            userlist = User.objects.filter(phone_number__icontains=searchdata)
        elif (searchby == "firstname"):
            userlist = User.objects.filter(first_name__icontains=searchdata)
        elif (searchby == "lastname"):
            userlist = User.objects.filter(last_name__icontains=searchdata)
    else:
        print ('executing all')
        userlist = User.objects.all()

    context={}
    context["page_url"]="admin/users/all"
    context["users"]=getpagerecords(userlist, page)

    return render(request, 'admin_users.html', context)


def inactive_users(request):
    print ("You hit inactive_users")
    page = request.GET.get('page')
    userlist = User.objects.filter(is_email_verified=False)

    context={}
    context["page_url"]="admin/users/inactive"
    context["users"]=getpagerecords(userlist, page)

    return render(request, 'admin_users.html', context)


def post_images(request):
    print ("you hit post_images")
    postid = request.GET.get('postid', "")
    print (postid)
    post = Post.objects.get(id=postid)
    context = {}
    context["post"] = post

    return render(request, 'post_images.html', context)

def all_posts(request):
    page = request.GET.get('page')
    postlist = Post.objects.all()

    context = {}
    context["page_url"] = "admin/posts/all"
    context["posts"] = getpagerecords(postlist, page)
    return render(request, 'admin_posts.html', context)


def unverified_posts(request):
    page = request.GET.get('page')
    postlist = Post.objects.filter(is_verified=False)

    context = {}
    context["page_url"] = "admin/posts/unverified"
    context["posts"] = getpagerecords(postlist, page)
    return render(request, 'admin_posts.html', context)

def inactive_posts(request):
    page = request.GET.get('page')
    postlist = Post.objects.filter(is_active=False)

    context = {}
    context["page_url"]= "admin/posts/inactive"
    context["posts"] = getpagerecords(postlist, page)
    return render(request,'admin_posts.html', context)


def verifypost(request):
    print ("You hit verify post")
    postid = request.POST.get("postid")
    print(postid)
    post = Post.objects.get(pk=postid)
    post["is_verified"] = True
    post.save()
    return HttpResponse("success")


def verifyidcard(request):
    print ("You hit verify idcard")
    userid = request.GET.get("userid")
    print(userid)
    user = User.objects.get(pk=userid)
    user["is_id_verified"] = True
    user.save()
    return HttpResponse("success")


def verifyphone(request):
    print ("You hit verify phone")
    userid = request.GET.get("userid")
    print(userid)
    user = User.objects.get(pk=userid)
    user["is_phone_verified"] = True
    user.save()
    return HttpResponse("success")


def get_userqueries(request):
    page = request.GET.get('page')
    postbox = Postbox.objects.all().order_by("-sent_date")
    context = {}
    context["page_url"]= "admin/user/queries"
    context["userqueries"] = getpagerecords(postbox, page)
    return render(request,'admin_userqueries.html', context)

def sendquery(request):
   name = request.POST.get("name", "").strip()
   email = request.POST.get("email", "").strip()
   phone_number = request.POST.get("phone", "").strip()
   subject = request.POST.get("subject", "").strip()
   message = request.POST.get("message", "").strip()
   p = Postbox()
   p.name = name
   p.email = email
   p.phone_number = phone_number
   p.subject = subject
   p.message = message
   p.save()

   output = {}
   output["status"] = "success"
   output["msg"] = "Thanks for getting in touch with us. We will get back to you shortly."
   return JsonResponse(output)
