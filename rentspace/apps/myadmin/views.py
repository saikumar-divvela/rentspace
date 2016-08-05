from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.template import loader
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from django.views.decorators.csrf import csrf_exempt


from common import getpagerecords
from userprofile.models import User
from post.models import Post

# Create your views here.


def all_users(request):
    print ("You hit all_users")
    isphonenotverified = request.GET.get("isphonenotverified","")
    isidproofnotverified = request.GET.get("isidproofnotverified","")
    page = request.GET.get('page')

    userlist = None;
    print ("Phone not verified:"+isphonenotverified,"Idproof not verified:"+isidproofnotverified)

    if (isphonenotverified == 'true'):
        userlist = User.objects.filter(is_phone_verified=False)
        print ('executing is not phone verified')

    elif (isidproofnotverified == 'true'):
        userlist = User.objects.filter(is_id_verified  =False)

    else:
        print ('executing all')
        userlist = User.objects.all()

    context ={}
    context["page_url"]= "admin/users/all"
    context["users"]=getpagerecords(userlist,page)

    return render(request,'admin_users.html',context)

def inactive_users(request):
    print ("You hit inactive_users")
    page = request.GET.get('page')
    userlist = User.objects.filter(is_email_verified=False)

    context ={}
    context["page_url"]= "admin/users/inactive"
    context["users"]=getpagerecords(userlist,page)

    return render(request,'admin_users.html',context)

def post_images(request):
    print ("you hit post_images")
    postid = request.GET.get('postid',"")
    print (postid)
    post = Post.objects.get(id=postid)
    context ={}
    context["post"] = post

    return render(request,'post_images.html',context)

def all_posts(request):
    page = request.GET.get('page')
    postlist = Post.objects.all()

    context = {}
    context["page_url"]= "admin/posts/all"
    context["posts"] = getpagerecords(postlist,page)
    return render(request,'admin_posts.html',context)

def unverified_posts(request):
    page = request.GET.get('page')
    postlist = Post.objects.filter(is_verified=False)

    context = {}
    context["page_url"]= "admin/posts/unverified"
    context["posts"] = getpagerecords(postlist,page)
    return render(request,'admin_posts.html',context)

def inactive_posts(request):
    page = request.GET.get('page')
    postlist = Post.objects.filter(is_active=False)

    context = {}
    context["page_url"]= "admin/posts/inactive"
    context["posts"] = getpagerecords(postlist,page)
    return render(request,'admin_posts.html',context)

#TODO need to fix this
@csrf_exempt
@login_required(login_url='/signin/')
def verifypost(request):
    print ("You hit verify post")
    postid = request.POST.get("postid")
    print(postid)
    post = Post.objects.get(pk=postid)
    post["is_verified"] = True
    post.save()
    return HttpResponse("success")


@login_required(login_url='/signin/')
def verifyidcard(request):
    print ("You hit verify idcard")
    userid = request.GET.get("userid")
    print(userid)
    user = User.objects.get(pk=userid)
    user["is_id_verified"] = True
    user.save()
    return HttpResponse("success")

@login_required(login_url='/signin/')
def verifyphone(request):
    print ("You hit verify phone")
    userid = request.GET.get("userid")
    print(userid)
    user = User.objects.get(pk=userid)
    user["is_phone_verified"] = True
    user.save()
    return HttpResponse("success")

