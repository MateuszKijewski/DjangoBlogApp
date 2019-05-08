from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .forms import AddPostForm
# Create your views here.
def Home(request):
    context = {
        "title" : 'Blog - Home'
    }
    return render(request, 'posts/home.html', context)

def About(request):
    context = {
        "title" : 'Blog - About',
        "style" : '{% static "posts/home_style.css" %}'
    }
    return render(request, 'posts/about.html', context)

def Contact(request):
    context = {
        "title" : 'Blog - contact'
    }
    return render(request, 'posts/contact.html', context)

def Add_post(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        uploaded_image = request.FILES['image']
        fs = FileSystemStorage()
        name = fs.save(uploaded_image.name, uploaded_image)
        url = fs.url(name)
        return redirect('home')
    else:
        form = AddPostForm()
    
    context = {
            'form': form,
                }
    return render(request, 'posts/add_post.html', context)