from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect

from post.models import Post, PostPhoto, ShortlistedPosts, UserBookings
from common import getpagerecords


#TODO  Send SMS/Email of owner details to owner and customer
@login_required
def contactpostowner(request):
    print ("you hit contact post owner")
    postid = request.GET.get("id")
    print (postid)

    userpost = None
    try:
        userpost = Post.objects.get(id=postid, user_id=request.user.id)
    except:
        print("The  post doesn't belong to user")

    if(not userpost):
        try:
            booking = UserBookings.objects.get(user_id=request.user.id, post_id=postid)
            booking.count = booking.count + 1
            booking.save()
            # TODO send email
            print ("post booked for user")
        except Exception as exp:
            print (exp)
            booking = UserBookings()
            post = Post.objects.get(id=postid)
            booking.post = post
            booking.user = request.user
            booking.count = 1
            booking.save()
            # TODO send email
    else:
        print ("User can not book his own post")

    return HttpResponseRedirect("/home")

@login_required
def shortlistpost(request):
    print ("you hit shortlist post")
    postid = request.GET.get("id")

    userpost = None

    try:
        userpost = Post.objects.get(id=postid, user_id=request.user.id)
    except:
        print(" The  post doesn't belong to user")
    if(not userpost):
        try:  # Updated counter if already shortlisted
            bookmark = ShortlistedPosts.objects.get(user_id=request.user.id, post_id=postid)
            bookmark.count = bookmark.count + 1
            bookmark.save()
        except:  # Add bookmark if not exists
            bookmark = ShortlistedPosts()
            post = Post.objects.get(id=postid)
            bookmark.post = post
            bookmark.user = request.user
            bookmark.count = 1
            bookmark.save()
    else:
        print ("User can not bookmark his own post")
    return HttpResponseRedirect("/shortlistedposts")


# TODO remove bookmark for the post
@login_required
def delistpost(request):
    print ("you hit delistpost ")
    postid = request.GET.get("id")
    print (postid)
    ShortlistedPosts.objects.filter(post_id=postid).delete()
    return HttpResponseRedirect("/shortlistedposts")

def searchposts(request):
    print ("you hit search posts")

    location = request.GET.get("location", "")
    housetype = request.GET.get("housetype", "")
    accomtype = request.GET.get("accomtype", "")
    accomfor = request.GET.get("accomfor", "")
    page = request.GET.get('page')

    print (location, accomtype, housetype, accomfor)
    request.session["accomtype"] = accomtype
    request.session["housetype"] = housetype
    request.session["accomfor"] = accomfor

    postlist = Post.objects.all()
    #postlist = Post.objects.filter(house_type=housetype,accom_type=accomtype,accom_for__contains=accomfor)
    context = {}
    context["posts"] = getpagerecords(postlist, page)
    return render(request, 'postlist.html', context)


@login_required
def myposts(request):
    print ("you hit my posts")
    postlist = Post.objects.filter(user_id=request.user.id)
    context = {}
    context["posts"] = postlist
    return render(request, 'myposts.html', context)


@login_required
def shortlistedposts(request):
    print ("you hit shortlistedposts")
    bookmarks = ShortlistedPosts.objects.filter(user_id=request.user.id)
    print (bookmarks)
    postlist = []
    for bookmark in bookmarks:
        postlist.append(Post.objects.get(id=bookmark.post_id))
    for post in postlist:
        print (post)
    context = {}
    context["posts"] = postlist
    context["shortlistedposts"] = True
    return render(request, 'myposts.html', context)


@login_required
def showpost(request):
    print ("you hit show post")
    postid = request.GET.get("id")
    print (postid)
    post = Post.objects.get(id=postid)
    print (post)
    context = {}
    context["post"] = post
    return render(request, 'showpost.html', context)


@login_required
def addpost(request):
    print ("you hit add post")
    if request.method == 'POST':
        print ("got post request")
        title = request.POST.get("title", "")
        description = request.POST.get("description", "")
        rentperday = request.POST.get("rentperday", "")
        facilities = request.POST.getlist("facilities")
        print (facilities)
        if facilities is not None:
            facilities = ",".join(facilities)
        else:
            facilities = ""

        address = request.POST.get("address", "")
        street = request.POST.get("street", "")
        city = request.POST.get("city", "")
        pincode = request.POST.get("pincode", "")
        state = request.POST.get("state", "")
        country = request.POST.get("country", "")

        deposit = request.POST.get("deposit", "")
        guests = request.POST.get("guests", "")
        house_type = request.POST.get("house_type", "")
        accom_type = request.POST.get("accom_type", "")
        accom_for = request.POST.getlist("accom_for")

        if accom_for is not None:
            accom_for = ",".join(accom_for)
        else:
            accom_for = ""

        print (deposit, guests, house_type, accom_type, accom_for)

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
    else:
        context = {}
        postid = request.GET.get("id", "")
        if postid:
            post = Post.objects.get(id=postid)
            context["post"] = post

        context["msg"] = request.GET.get("msg", "")

        return render(request, 'addpost.html', context)

@login_required
def updatepost(request):
    print ("you hit update post")
    if request.method == 'POST':
        print ("got post request")
        postid = request.POST.get("postid")
        title = request.POST.get("title", "")
        description = request.POST.get("description", "")
        rentperday = request.POST.get("rentperday", "")
        facilities = request.POST.getlist("facilities")
        print (facilities)
        if facilities is not None:
            facilities = ",".join(facilities)
        else:
            facilities = ""

        address = request.POST.get("address", "")
        street = request.POST.get("street", "")
        city = request.POST.get("city", "")
        pincode = request.POST.get("pincode", "")
        state = request.POST.get("state", "")
        country = request.POST.get("country", "")

        deposit = request.POST.get("deposit", "")
        guests = request.POST.get("guests", "")
        house_type = request.POST.get("house_type", "")
        accom_type = request.POST.get("accom_type", "")
        accom_for = request.POST.getlist("accom_for")

        if accom_for is not None:
            accom_for = ",".join(accom_for)
        else:
            accom_for = ""


        print (deposit, guests, house_type, accom_type, accom_for)


        print (postid,description)
        p = Post.objects.get(id=postid)
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
        post = Post.objects.get(id=postid)
        print (post.rentperday)
        context = {}
        context["post"] = post
        context["msg"] = request.GET.get("msg", "")
        return render(request, 'updatepost.html', context)


@login_required
def deletepost(request):
    print ("you hit delete post")

    postid = request.GET.get("id")
    post = Post.objects.get(pk=postid)
    post["is_active"] = False
    post.save()
    return HttpResponseRedirect("/myposts")


@login_required(login_url='/signin/')
def activatepost(request):
    print ("you hit activate post")

    postid = request.GET.get("id")
    post = Post.objects.get(pk=postid)
    post["is_active"] = True
    post.save()
    return HttpResponseRedirect("/myposts")