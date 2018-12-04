from django.shortcuts import render
from album.models import Media
# Home page
def home(request):
    medias = Media.objects.all()
    context = {'objects':medias}

    return render(request,'home.html',context)
