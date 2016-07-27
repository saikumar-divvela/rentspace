from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.template import loader
from django.http import HttpResponseRedirect

from userprofile.models import User
from post.models import Post

# Create your views here.


def getusers(request):
	isemailverified = request.GET.get("isemailverified","")
	isphoneverified = request.GET.get("isphoneverified","")
	isactive = request.GET.get("isactive","")
	print (isactive,isphoneverified,isemailverified)
	userlist = None;
	if (isemailverified =='false'): 
		userlist = User.objects.filter(is_email_verified=False)
	elif (isphoneverified == 'false'):
		userlist = User.objects.filter(is_phone_verified=False)
	elif (isactive == 'false'):
		userlist = User.objects.filter(is_active=False)
	else:
		userlist = User.objects.all()
	for user in userlist:
		print (user)
	context ={}
	context["users"]=userlist
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
