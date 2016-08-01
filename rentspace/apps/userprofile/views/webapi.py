import sys
import json
import os

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from django.template import loader
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

from userprofile.models import User


@csrf_exempt
def create_user(request):
    try: 
        print ("You hit create user")
        username = request.POST.get("username")
        password = request.POST.get("password")
        password_repeat = request.POST.get("password-repeat")
        phone_number =  request.POST.get("phone_number","")
        first_name = request.POST.get("first_name","")
        last_name = request.POST.get("last_name","")
        

        print (username,password,password_repeat,phone_number,first_name,last_name)
        user = User.objects.create_user(email=username,password=password,phone_number=phone_number)  # Only pass the required fields defined in models.py
        print (user,user.password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()  # This doesn't return anything

    except Exception as err:
        print ("Unexpected error:", sys.exc_info()[0])
        print (err)
        context ={}
        context["msg"]= "Some errror occurred while creating user..."
        return render(request,'signup.html',context)

    return HttpResponseRedirect("/register_success")
    
def register_success(request):
    context ={}
    context["msg"]= "User is created successfully"
    return render(request,'register_success.html',context)

# Retun success page if success else show same page with error message
@csrf_exempt
def login_user(request):
    print ('You hit login user')
    if request.method == 'POST':
       username = request.POST.get("username","")
       password = request.POST.get("pwd","")
       print (username,password)

       user = authenticate(username=username, password=password)
       print (user)
       if user is not None:
           login(request, user)
           return HttpResponseRedirect("/")
       else:
            context ={}
            context["msg"]= "Either login name or password is incorrect"
            return render(request,'signin.html',context)        
    else: # Return an 'invalid login' error message.
       return render(request,'signin.html',context)


def login_success(request):
    return render(request,'index.html')
    

# TODO for some unknown reason this is not working
def logout_user(request):
    try:
        print ('logging out...')
        del request.session['userid']
        print (request.user)
        logout(request)
        request.session.flush()
        print (request.user)
    except KeyError:
        pass
  

    context ={}
    context["msg"]= "successfully logged out"
    return render(request,'index.html',context)

@csrf_exempt
@login_required
def change_password(request):
    old_password = request.POST.get("old_password","")
    new_password = request.POST.get("new_password","")
    reset_password = request.POST.get("reset_password","")

    print (old_password,new_password,reset_password)
    output = {}
    output["status"]= "fail"

    if old_password == "":
        output["msg"]= "Current password is empty"
        return JsonResponse(output)
    elif new_password == "":
        output["msg"]= "New password is empty"
        return JsonResponse(output)
    elif reset_password  == "":
        output["msg"]= "Repeated password is empty"
        return JsonResponse(output)

    if not request.user.check_password(old_password):
        output["msg"]= "Incorrect current password"
        return JsonResponse(output)

    if new_password != reset_password:
        output["msg"]= "New password and repeated password doesn't match."
        return JsonResponse(output)

    saveuser = User.objects.get(email=request.user.email)
    saveuser.set_password(reset_password);
    saveuser.save()

    output["status"]= "success"
    output["msg"]= "Password is changed successfully"
    return JsonResponse(output)


def reset_password(request):
    print ("reset password")
    return HttpResponse("you hit reset password change page")

@csrf_exempt
@login_required
def edit_profile(request):
    print ('You hit edit profile')
    print (request.method)
    print (request.POST.get("firstname",""))
    if request.method == 'POST':
        first_name = request.POST.get("firstname","")
        last_name =  request.POST.get("lastname","")   
        phone_number =  request.POST.get("phonenumber","")   
        id_card_type =  request.POST.get("idcardtype","")  
        date_of_birth = request.POST.get("date_of_birth","")
        gender =  request.POST.get("gender","")  

        address = request.POST.get("address","")
        street  = request.POST.get("street","")
        city = request.POST.get("city","")
        pincode = request.POST.get("pincode","")
        state = request.POST.get("state","")
        country = request.POST.get("country","")
        
        print (date_of_birth)
        print (id_card_type)
        saveuser = User.objects.get(email=request.user.email)
        if request.FILES:
            saveuser.idphoto = request.FILES['idphoto']

       
        if saveuser.idphoto:
            print (saveuser.idphoto.url)
            print (saveuser.idphoto.name,saveuser.idphoto.size)
        saveuser.first_name= first_name
        saveuser.last_name= last_name
        saveuser.phone_number= phone_number
        saveuser.id_card_type = id_card_type
        saveuser.gender = gender
        saveuser.date_of_birth = date_of_birth
        saveuser.address = address
        saveuser.street = street
        saveuser.city = city
        saveuser.pincode = pincode
        saveuser.state = state
        saveuser.country = country
        saveuser.save()
    
        output = {}
        output["status"]= "success"
        output["msg"]= "User details are updated successfully"
        return HttpResponseRedirect("/editprofile?msg="+output["msg"])
    else:
        context = {}
        context["status"]= "success"
        context["msg"]= "User details are updated successfully"
        return render(request,'myaccount.html',context)
        
