
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.db import IntegrityError
from .models import Profile,Post



def signup(request):
    if request.method == 'POST':
        fnm = request.POST.get('fnm')
        emailid = request.POST.get('emailid')
        pwd = request.POST.get('pwd')

        try:
            my_user = User.objects.create_user(
                username=fnm,
                email=emailid,
                password=pwd
            )

            Profile.objects.create(
                user=my_user,
                id_user=my_user.id
            )

            login(request, my_user)
            return redirect('/')

        except IntegrityError:
            invalid = "Username already exists"
            return render(
                request,
                'signup.html',
                {'invalid': invalid}
            )

    return render(request, 'signup.html')



def loginn(request):
    if request.method == 'POST':
        fnm = request.POST.get('fnm')
        pwd = request.POST.get('pwd')

        userr = authenticate(
            request,
            username=fnm,
            password=pwd
        )

        if userr is not None:
            login(request, userr)
            return redirect('/')

        invalid = "Invalid Credentials"
        return render(request, 'loginn.html', {'invalid': invalid})

    return render(request, 'loginn.html')


def logoutt(request):
    logout(request)
    return redirect('/login')

def upload(request):
    if request.method == 'POST':
        user  = request.user.username
        image = request.FILES.get('image-upload')
        caption = request.POST['caption']
        new_post = Post.objects.create(user = user,image = image,caption = caption)
        new_post.save()
        return redirect('/')

    else:
        return redirect ('/')


def home(request):
    post = Post.objects.all().order_by('created_at')
    # profile  = Profile.objects.get(user=request.user)
    context = {
        'post' : post,
        # 'profile':profile
    }
    return render(request,'main.html',context)





