from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.conf import settings as django_settings
from django.core.mail import send_mail
from django.http import (HttpResponse, HttpResponseBadRequest,
                         HttpResponseForbidden)
from django.template import RequestContext,loader
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.views.generic import CreateView,TemplateView,ListView

from .models import Items


# Redirects to signup/login page

def signUP(request):
   #all_users = signUP().objects.all()

    template = loader.get_template('signup/Register.html')
    context = {

        #'all_users': all_users,

    }

    return HttpResponse(template.render(context,request))


#Redirects to only books based items
@login_required
def books(request):
    all_users = User.objects.all()
    template = loader.get_template('signup/Home.html')
    all_items = Items.objects.filter(item_tag="Books")
    print(all_items)
    context = {
        'all_users': all_users,
        'all_items': all_items
    }
    p = 0
    return render_to_response("signup/Home.html", context)

#Redirects to only cycle based items
@login_required
def cycle(request):
    all_users = User.objects.all()
    template = loader.get_template('signup/Home.html')
    all_items = Items.objects.filter(item_tag="Cycle")
    print(all_items)
    context = {
        'all_users': all_users,
        'all_items': all_items
    }
    p = 0
    return render_to_response("signup/Home.html", context)

#Redirects to only Cooler based items
@login_required
def cooler(request):
    all_users = User.objects.all()
    template = loader.get_template('signup/Home.html')
    all_items = Items.objects.filter(item_tag="Cooler")
    print(all_items)
    context = {
        'all_users': all_users,
        'all_items': all_items
    }
    p = 0
    return render_to_response("signup/Home.html", context)

#Redirects to Upload.Html page
@login_required
def upload(request):
   #all_users = signUP().objects.all()

    template = loader.get_template('signup/upload.html')
    context = {

        #'all_users': all_users,

    }

    return HttpResponse(template.render(context, request))


usernames=""

#Redirects to Home.html
@login_required
def home(request, username=usernames):
   
   all_users = User.objects.all()
   template = loader.get_template('signup/Home.html')
   all_items = Items.objects.all()
   context = {
       'all_users': all_users,
       'all_items': all_items,
       'username' : username
    }
   p = 0
   return render_to_response("signup/Home.html", context)

#Redirects to MNNIT_KART.html
def about(request):
   #all_users = signUP().objects.all()

    template = loader.get_template('signup/MNNIT_KART.html')
    context = {
    }

    return HttpResponse(template.render(context, request))


#Takes All items details and redirects to Home.html
@login_required
def item_detail(request):
    print('ase hi')
    all_items = Items.objects.all()

    context = {
        'all_items': all_items,
    }

    return render_to_response( 'signup/Home.html', context)


#Takes the item Details and redirects to Home.html with the added item
@login_required
@csrf_protect
def add(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        userphone = request.POST.get('phonenumber')
        useremail = request.POST.get('email')
        aboutitem = request.POST.get('aboutitem')
        price = request.POST.get('price')
        tag = request.POST.get('tag')
        image = request.POST.get('image')

        print(image)


        items = Items.objects.all()
        Items.objects.create(user_name=username, user_phone=userphone, user_email=useremail, about_item=aboutitem, item_tag=tag, item_price=price, item_image=image)
        items = Items.objects.all()
        for item in items:
            item.save()
        return redirect('collect')



#Checks if the user logging in is valid or not..If valid looged in successfully, otherwise Remains in the same page
@csrf_protect
def signin(request):
    print('inside authentication.view')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user is not None:
            if user.is_active:
                print('user exists')
                # user = User.objects.filter(username=username)
                all_items = Items.objects.all()
                p = 1
                context = {
                    'user' : user,
                    'all_items' : all_items,
                    'username': username
                }
                login(request, user)
                return render_to_response("signup/Home.html", context)
            else:
                HttpResponse('Inactive user.')
        if not user:
            print("user not exist")
            error_signin = True
            return render(request, 'signup/Register.html', {'error_signin':error_signin})

    else: return render(request, 'signup/Register.html', {})

#Sign up the user
@csrf_protect
def register(request):
    print("matazi ki kripa")

    if request.method == 'POST':
        usernames = request.POST.get('user_name')
        firstname = request.POST.get('first_name')
        lastname = request.POST.get('last_name')
        password = request.POST.get('password')
        email = request.POST.get('email')

        flag = 1

        if usernames:
            if usernames[0].islower():
                flag = 0

            num = 1
            for i in range(len(usernames)):
                if usernames[i].isdigit():
                    num = 0

            if num == 1:
                flag = 0

        if flag == 0:
            print("worng inout dala hai user ne")

            template = loader.get_template('signup/Register.html')
            context = {
                "flag": flag
            }

            return HttpResponse(template.render(context, request))

        else:

            user = User.objects.all().filter(username=usernames,email=email)

            if user:
                error_register = True
                return render(request, 'signup/Register.html', {'error_register': error_register})
            if not user:
                flagp=1
                if password:
                    num = 1
                    for i in range(len(usernames)):
                        if usernames[i].isdigit():
                            num = 0

                    if num == 1:
                        flagp = 0

                if len(password) < 8:
                    flagp = 0

                if flagp == 0:
                    print("worng inout dala hai user ne")

                    template = loader.get_template('signup/Register.html')
                    context = {
                        "flagp": flagp
                    }

                    return HttpResponse(template.render(context, request))
                else:
                    print('No user exists')
                    User.objects.create_user(username=usernames, password=password,
                                             email=email, first_name=firstname,
                                             last_name=lastname)  # removed email at signup to make signup fast
                    user = authenticate(username=usernames, password=password)

                    user.save()
                    login(request,user)
                    return redirect('home')


#logout the user from session
def signout(request):
    logout(request)
    template = loader.get_template('signup/Register.html')
    context = {

        # 'all_users': all_users,

    }

    return HttpResponse(template.render(context, request))


