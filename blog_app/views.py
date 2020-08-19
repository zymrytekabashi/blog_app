from .models import Post, PostManager, Comment, CommentManager
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.contrib import messages

#### main page displayed
def index(request):
    context = {
        'all_posts': Post.objects.all(),
    }
    return render(request, 'index.html', context)


### route to display the form for adding a new post
def new_post(request):
    return render(request, 'new_post.html')


### method to create a new post
def add_post(request):
    errors = Post.objects.post_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/new_post')
    else:
        post = Post.objects.create(title=request.POST['title'], desc=request.POST['desc'])
        if 'cover_image' in request.FILES != None:
            pic = request.FILES['cover_image']
            fs = FileSystemStorage()
            fs.save(pic.name, pic)
            post.cover_image = pic
            post.save()
        return redirect('/')
    
    
### display one post 
def one_post(request, post_id):
    context = {
        'post': Post.objects.get(id=post_id),
        'all_comments': Comment.objects.filter(post = post_id),
        
    }
    return render(request, 'one_post.html', context)

### creating a comment
def add_comment(request, post_id):
    str_id = str(post_id)
    comm = Comment.objects.create(name = request.POST['name'], comment = request.POST['comment'], post = Post.objects.get(id = post_id))
    return redirect(f'/posts/{str_id}')


### search bar in homepage
def search(request):
    if "q" in request.GET:
        context = {
            "all_posts": Post.objects.filter(title__contains=request.GET["q"]),
             
        }
        return render(request, "index.html", context)
    else:
        return redirect('/')