from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Image,Profile,Comment
from django.contrib.auth.models import User
from .forms import NewImageForm,CommentForm,ProfileForm
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
import json

# Create your views here.
@login_required(login_url='accounts/login/')
def index(request):
    if request.user.is_superuser:
        return redirect('http://localhost:8000/admin')
    else:
        images = Image.get_images()
        comments = Comment.objects.all()
        form = CommentForm()
        return render(request,"index.html",{"images":images,"form":form,"comments":comments})

@login_required(login_url='accounts/login/')
def profile(request,username):
    current_user = request.user
    try:
        user = User.objects.get(username = username)
        profile = Profile.objects.get(user = user)
        images = Image.objects.filter(profile = profile)

    except ObjectDoesNotExist:
        return redirect('edit_profile',current_user)

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
    likes = image.likes.all().count()
    return HttpResponse(likes)

def ajax_comment(request):
    comment = request.GET.get('comment')
    image = request.GET.get('image')
    user = request.user

    comment = Comment(comment = comment,image = image,user = user)
    comment.save()

    latest_comment = f"{Comment.objects.all().last().comment}"
    latest_comment_user = f"{Comment.objects.all().last().user}"
    data = {
        'latest_comment': latest_comment,
        'latest_comment_user': latest_comment_user
    }

    return JsonResponse(data)

def search(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        places = User.objects.filter(username__icontains=q)
        results = []
        for pl in places:
            place_json = {}
            place_json = pl.username
            results.append(place_json)
            data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

def search_user(request):
    if 'username' in request.GET and request.GET['username']:
        username = request.GET.get('username')
        searched_user = User.objects.get(username = username)

        return redirect('profile',username = searched_user)

def edit_profile(request,username):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            bio = form.save(commit=False)
            bio.user = current_user
            bio.save()
        return redirect('index')
    form = ProfileForm()
    return render(request,'edit_profile.html',{"form":form})
