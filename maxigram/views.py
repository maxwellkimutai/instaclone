from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Image,Profile,ImageLikes
from django.contrib.auth.models import User
from .forms import NewImageForm
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
@login_required(login_url='accounts/login/')
def index(request):
    if request.user.is_superuser:
        return redirect('http://localhost:8000/admin')
    else:
        images = Image.get_images()
        return render(request,"index.html",{"images":images})

@login_required(login_url='accounts/login/')
def profile(request,username):
    current_user = request.user
    try:
        user = User.objects.get(username = username)
        profile = Profile.objects.get(user = user)
        images = Image.objects.filter(profile = profile)

    except ObjectDoesNotExist:
        raise Http404()

    if request.method == 'POST':
        form = NewImageForm(request.POST,request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.profile = profile
            image.save()
    else:
        form = NewImageForm()
    return render(request,"profile.html",{"profile":profile, "images":images, "form":form})

def ajaxlikephoto(request):
    img_id = None
    current_user = request.user

    if request.method == 'GET':
        img_id = request.GET['image_id']

    if not Image.objects.filter(id = img_id,likes = request.user ).exists():
        image = Image.objects.get(id = img_id)
        image.likes.add(current_user)
        image.save()

    image = Image.objects.get(id = img_id)
    print(image.likes.count())
    return HttpResponse(img_id)
