from django.shortcuts import render
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Image,Profile
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='accounts/login/')
def index(request):
    images = Image.get_images()
    return render(request,"index.html",{"images":images})

@login_required(login_url='accounts/login/')
def profile(request,username):
    try:
        user = User.objects.get(username = username)
        profile = Profile.objects.get(user = user)
        images = Image.objects.filter(profile = profile)
        print(len(images))
    except DoesNotExist:
        raise Http404()
    return render(request,"profile.html",{"profile":profile, "images":images})
