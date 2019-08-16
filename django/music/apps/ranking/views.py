from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from apps.index.models import *
# Create your views here.
def rankingView(request):


    search_song = Dynamic.objects.select_related('song').order_by('-dynamic_search').all()[:4]


    All_list = Song.objects.values('song_type').distinct()

    song_type = request.GET.get('type','')

    if song_type:
        song_info = Dynamic.objects.select_related('song').filter(song__song_type=song_type).order_by('-dynamic_plays').all()[:10]
    else:
        song_info = Dynamic.objects.select_related('song').order_by('-dynamic_plays').all()[:10]

        return render(request,'ranking.html',locals())