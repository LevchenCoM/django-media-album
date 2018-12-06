from django.shortcuts import render, redirect
from album.models import Media
from .forms import MediaAddForm, MediaEditForm, MediaLinkForm
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
import requests
from django.conf import settings
import datetime
import json

def home(request):
    medias = Media.objects.all()
    context = {'objects':medias}

    return render(request,'home.html',context)

def media_page(request, media_id):
    media = Media.objects.get(id=media_id)
    context = {'media':media}

    return render(request,'media_page.html',context)

@login_required
def media_edit(request, media_id):
    media = Media.objects.get(id=media_id)
    form = MediaEditForm(model_to_dict(media))
    context = {'form':form, 'media':media}
    if request.method == 'POST':
        form = MediaEditForm(request.POST, request.FILES)
        if 'file' in request.FILES:
            media.file=request.FILES['file']
        media.title= request.POST['title']
        media.description=request.POST['description']
        media.file_type=request.POST['file_type']
        media.save()
        return redirect(media.get_absolute_url())
    return render(request,'media_edit_page.html',context)

@login_required
def media_add(request):
    form = MediaAddForm()
    context = {'form':form}
    if request.method == 'POST':
        form = MediaAddForm(request.POST, request.FILES)
        if 'file' in request.FILES:
            new_media = Media(file=request.FILES['file'],\
                              title= request.POST['title'],\
                              description=request.POST['description'],\
                              file_type=request.POST['file_type'],\
                              author=request.user)
            new_media.save()
            return redirect(new_media.get_absolute_url())
    return render(request,'media_add_page.html',context)

@login_required
def media_add_insta(request):
    form = MediaLinkForm()
    context = {'form':form}
    if request.method == 'POST':
        json_text = requests.get(request.POST['link'] + '?__a=1').text
        parsed_json = json.loads(json_text)
        shortcode_media = parsed_json['graphql']['shortcode_media']
        date = datetime.datetime.utcfromtimestamp(shortcode_media['taken_at_timestamp'])
        file_name = shortcode_media['id']
        title = shortcode_media['owner']['full_name']
        description = shortcode_media['edge_media_to_caption']['edges'][0]['node']['text']

        file_name = '/media_content/{}.png'.format(file_name + str(shortcode_media['taken_at_timestamp']))

        with open(settings.MEDIA_ROOT + file_name,'wb') as image:
            a = requests.get((request.POST['link']) + 'media/')
            image.write(a.content)

        new_media = Media(title= title,\
                          file= file_name,\
                          description=description[:128],\
                          file_type="0",\
                          link=request.POST['link'],\
                          created=date,\
                          author=request.user)
        new_media.save()

        return redirect(new_media.get_edit_url())
    return render(request,'media_add_by_insta_page.html',context)

@login_required
def media_mine(request):
    medias = Media.objects.filter(author=request.user)
    context = {'objects':medias}

    return render(request,'media_mine_page.html',context)
