from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.template import loader
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from userprofile.models import User
from post.models import Post

# Create your views here.


def getusers(request):
    isemailnotverified = request.GET.get("isemailnotverified","")
    isphonenotverified = request.GET.get("isphonenotverified","")
    isidproofnotverified = request.GET.get("isidproofnotverified","")

    print (isphonenotverified,isidproofnotverified)

    userlist = None;
    
    if (isemailnotverified =='true'): 
        userlist = User.objects.filter(is_email_verified=False)
    
    elif (isphonenotverified == 'true'):
        userlist = User.objects.filter(is_phone_verified=False)
        print ('executing is not phone verified')
    
    elif (isidproofnotverified == 'true'):
        userlist = User.objects.filter(is_id_verified  =False)
    
    else:
        print ('executing all')
        userlist = User.objects.all()

    paginator = Paginator(userlist, 4) # Show 25 contacts per page
    
    page = request.GET.get('page')
    try:
        records = paginator.page(page)
    except PageNotAnInteger:
        records = paginator.page(1)
    except EmptyPage:
        records = paginator.page(paginator.num_pages)    

    context ={} 
    context["users"]=records


    return render(request,'admin_users.html',context)

def getposts(request):
    isverified = request.GET.get("isverified","")
    isactive = request.GET.get("isactive","")

    print (isactive,isverified)
    postlist = None;
    if (isverified =='false'): 
        postlist = Post.objects.filter(is_verified=False)
    elif (isactive == 'false'):
        print ('getting deleted posts') 
        postlist = Post.objects.filter(is_active=False)
    else:
        postlist = Post.objects.all()
    for post in postlist:
        print (post)
    context ={}
    context["posts"]=postlist
    return render(request,'admin_posts.html',context)



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

@login_required(login_url='/signin/')
def verifypost(request):
    print ("You hit verify post")
    postid = request.GET.get("postid")
    print(postid)
    post = Post.objects.get(pk=postid)
    post["is_verified"] = True
    post.save()
    return HttpResponse("success")